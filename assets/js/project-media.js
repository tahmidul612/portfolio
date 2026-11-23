// Behaviour for the demo and video shortcodes (layouts/_shortcodes/).

// Demo facade: swap the poster for the iframe on click.
document.querySelectorAll(".pdemo__frame").forEach((frame) => {
  frame.querySelector(".pdemo__play").addEventListener("click", () => {
    const iframe = document.createElement("iframe");
    iframe.src = frame.dataset.src;
    iframe.title = frame.dataset.title;
    iframe.allow = "fullscreen; autoplay";
    iframe.setAttribute(
      "sandbox",
      "allow-scripts allow-same-origin allow-popups allow-forms",
    );
    frame.replaceChildren(iframe);
    iframe.focus();
  });
});

// Explainer videos play while at least half on screen, unless the visitor
// prefers reduced motion or has paused that video themselves.
const calm = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const videos = document.querySelectorAll("video[data-autoplay]");
if (!calm && videos.length && "IntersectionObserver" in window) {
  const autoPaused = new WeakSet();
  const userPaused = new WeakSet();
  const watcher = new IntersectionObserver(
    (entries) => {
      for (const { target: v, isIntersecting } of entries) {
        if (userPaused.has(v)) continue;
        if (isIntersecting) {
          v.play().catch(() => {});
        } else if (!v.paused) {
          autoPaused.add(v);
          v.pause();
        }
      }
    },
    { threshold: 0.5 },
  );
  for (const v of videos) {
    v.addEventListener("pause", () => {
      if (autoPaused.has(v)) autoPaused.delete(v);
      else userPaused.add(v);
    });
    v.addEventListener("play", () => userPaused.delete(v));
    watcher.observe(v);
  }
}
