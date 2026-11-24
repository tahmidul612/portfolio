"""Build the public Edwin demo (static/demos/edwin) from simulated calls.

Reuses the private call reel's pipeline (reel.py) but reads a demo-only reel config
and writes into the portfolio, with costs removed.

    python3 build_demo.py <ai-phone-assistant repo> <demo reel.json> <out dir>
"""
import importlib.util
import json
import pathlib
import subprocess
import sys

repo, reel_path, out = (pathlib.Path(a).resolve() for a in sys.argv[1:4])
spec = importlib.util.spec_from_file_location("reel", repo / "private/call-reel/reel.py")
reel = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reel)

cfg = json.loads(reel_path.read_text())
(out / "audio").mkdir(parents=True, exist_ok=True)
calls = []
for k in cfg["order"]:
    m, d = cfg["calls"][k], reel.CALLS / k
    call = json.loads((d / "call.json").read_text())
    events, seen = [], set()
    for msg in reel.messages(call):
        for tc in msg.get("toolCalls") or []:
            key = (round(msg.get("secondsFromStart", 0), 1), tc["function"]["name"])
            if key not in seen:
                seen.add(key)
                events.append({"t": key[0], "label": reel.EVENT.get(key[1], key[1]).replace("Aryan", "Sam")})
    mp3 = out / "audio" / f"{k}.mp3"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(d / "stereo.wav"), "-ac", "1", "-ar", "22050",
                    "-c:a", "libmp3lame", "-b:a", "48k", "-map_metadata", "-1", str(mp3)], check=True)
    audio_dur, lane = reel.lanes(d / "stereo.wav")
    vv = (call.get("assistantOverrides") or {}).get("variableValues") or {}
    calls.append({
        "short": k, "date": m.get("date", call["createdAt"][:10]), "duration": reel.seconds(call), "cost": 0,
        "endedReason": call.get("endedReason"), "task": m.get("task") or vv.get("task_short"),
        "title": m["title"], "who": m["who"], "kind": m["kind"], "outcome": m["outcome"],
        "moments": [{"t": t, "label": l} for t, l in m.get("moments", [])],
        "issues": [{"t": t, "label": l} for t, l in m.get("issues", [])],
        "source": m.get("source", "Soniox per-speaker transcript, cleaned up by hand"),
        "turns": json.loads((d / "transcript-clean.json").read_text()),
        "events": events, "audio": f"audio/{k}.mp3", "audioDuration": audio_dur, "lanes": lane,
    })
    print(k, m["title"], f"{reel.seconds(call)}s", f"{len(events)} events")
(out / "calls.json").write_text(json.dumps({"people": cfg.get("people", {}), "calls": calls}, ensure_ascii=False, separators=(",", ":")))
print("wrote", out / "calls.json")
