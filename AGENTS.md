# AGENTS.md

Personal portfolio at <https://tahmidul612.com>, built with Astro (static output) and hosted on Cloudflare Pages. Scripts are in `package.json`; run `npm run format` and `npm run check` before committing.

## Layout

- `content/projects/<slug>/index.mdx`: one bundle per project, with its images, posters and captions beside it. The folder name is the URL. Front matter is validated by `src/content.config.ts`. `group: smaller` renders inline at the bottom of `/projects/` instead of getting a page.
- `src/`: pages, layouts, components and `styles/global.css`, which holds the design tokens.
- `static/`: served as-is (Astro's `publicDir`): favicons, `_headers`, `_redirects`, `vcard.vcf`, and the self-contained demos under `static/demos/<slug>/`, which use fake data and no backend.
- `tools/explainers/<slug>/`: GSAP compositions. `uv run tools/explainers/render.py <slug>` renders `explainer.mp4`, the poster and the `.vtt` into the project bundle.

## Gotchas

- **Video lives on R2.** Pages ignores Range requests, and iOS Safari won't play video without them. `<Video>` loads the MP4 from `media.tahmidul612.com` (R2 bucket `portfolio-media`, same path as the bundle). After rendering a video, run `tools/upload-media.sh`. The MP4 in the bundle is the source copy and drives the card's Video badge; it is not part of the build.
- **Resume:** edit `content/resume/resume.tex`. GitHub Actions compiles it to `content/resume/build/resume.pdf`, renders `resume.png` for the page, and commits both. Locally: `pdftoppm -png -r 200 -singlefile -hide-annotations` on the PDF.
- **Old URLs keep working:** `/resume/build/resume.pdf` is a static endpoint, `/projects/#<oldAnchor>` redirects to the project's page, and `/vcard` and `/ssh` live in `static/_redirects`.
- **MDX:** comments are `{/* */}`, and a bare `<` or `{` in prose needs escaping.
- **Work content (Raphael Porcelain) is public:** use invented data only, with no client names, internal domains, hosts or internal figures.

## Design

Read `PRODUCT.md` (audience, voice, principles) before any visual or copy change. The look is "deep sea": dark blue with cyan light that follows the pointer, and "sunlit shallows" in light mode. Unbounded is the display face and Onest the body face, both loaded through Astro's Fonts API. Colours are OKLCH tokens using `light-dark()`, so a new colour needs both values.
