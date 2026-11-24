# /// script
# requires-python = ">=3.11"
# dependencies = ["playwright>=1.48"]
# ///
"""Render an explainer composition to MP4, a WebP poster and a WebVTT captions file.

Usage (from the repo root):
    uv run tools/explainers/render.py forg
    uv run tools/explainers/render.py forg --fps 30 --out content/projects/forg

A composition is tools/explainers/<slug>/index.html. It must define:
    window.EXPLAINER = {
        duration: 52,          # seconds
        poster: 24.5,          # time of the poster frame
        captions: [{start, end, text}, ...],
    }
    window.seek(t)             # render the paused timeline at t seconds

Frames are rendered by seeking, not by recording in real time, so every frame
is exact and the output is the same on every run.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent.parent
WIDTH, HEIGHT = 1920, 1080


def vtt_time(t: float) -> str:
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}"


def find_chromium() -> str | None:
    for name in ("chromium", "chromium-browser", "google-chrome-stable"):
        if path := shutil.which(name):
            return path
    return None  # fall back to Playwright's own browser


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--crf", type=int, default=28, help="x264 quality, higher is smaller")
    ap.add_argument("--out", type=Path, help="default: content/projects/<slug>")
    ap.add_argument("--name", default="explainer", help="output base name")
    ap.add_argument("--preview", metavar="T1,T2", help="only save PNG frames at these times, then exit")
    args = ap.parse_args()

    comp = ROOT / args.slug / "index.html"
    if not comp.exists():
        sys.exit(f"no composition at {comp}")
    out = (args.out or REPO / "content/projects" / args.slug).resolve()
    out.mkdir(parents=True, exist_ok=True)
    mp4, poster, vtt = (out / f"{args.name}{ext}" for ext in (".mp4", "-poster.webp", ".vtt"))

    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=find_chromium())
        page = browser.new_page(viewport={"width": WIDTH, "height": HEIGHT}, device_scale_factor=1)
        page.goto(comp.as_uri())
        page.evaluate("document.fonts.ready.then(() => true)")
        meta = page.evaluate("window.EXPLAINER")
        frames = round(meta["duration"] * args.fps)

        if args.preview:
            pdir = ROOT / args.slug / "preview"
            pdir.mkdir(exist_ok=True)
            for t in (float(x) for x in args.preview.split(",")):
                page.evaluate("t => { window.seek(t); }", t)
                page.screenshot(path=pdir / f"t{t:05.1f}.png")
            print(f"frames in {pdir.relative_to(REPO)}")
            browser.close()
            return 0

        ffmpeg = subprocess.Popen(
            [
                "ffmpeg", "-y", "-loglevel", "error",
                "-f", "image2pipe", "-framerate", str(args.fps), "-c:v", "mjpeg", "-i", "-",
                "-c:v", "libx264", "-preset", "slow", "-crf", str(args.crf),
                "-vf", "scale=out_range=tv,format=yuv420p", "-color_range", "tv", "-movflags", "+faststart", str(mp4),
            ],
            stdin=subprocess.PIPE,
        )
        for i in range(frames):
            page.evaluate("t => { window.seek(t); }", i / args.fps)
            ffmpeg.stdin.write(page.screenshot(type="jpeg", quality=92))
            if i % args.fps == 0:
                print(f"\r{i / args.fps:5.1f}s / {meta['duration']}s", end="", flush=True)
        ffmpeg.stdin.close()
        if ffmpeg.wait() != 0:
            sys.exit("ffmpeg failed")
        print()

        page.evaluate("t => { window.seek(t); }", meta["poster"])
        png = page.screenshot(type="png")
        browser.close()

    subprocess.run(["magick", "png:-", "-quality", "82", str(poster)], input=png, check=True)

    lines = ["WEBVTT", ""]
    for i, c in enumerate(meta["captions"], 1):
        lines += [str(i), f"{vtt_time(c['start'])} --> {vtt_time(c['end'])}", c["text"], ""]
    vtt.write_text("\n".join(lines))

    for f in (mp4, poster, vtt):
        print(f"{f.relative_to(REPO)}  {f.stat().st_size / 1_048_576:.2f} MiB")
    if mp4.stat().st_size > 20 * 1_048_576:
        print("warning: over 20 MiB, Cloudflare Pages refuses files over 25 MiB", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
