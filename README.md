# Personal Portfolio Website

[![LaTeX Build and Cloudflare Pages Deployment](https://github.com/tahmidul612/portfolio/actions/workflows/deploy-to-cf.yml/badge.svg)](https://github.com/tahmidul612/portfolio/actions/workflows/deploy-to-cf.yml)

Source for [tahmidul612.com](https://tahmidul612.com), built with [Astro](https://astro.build) and hosted on Cloudflare Pages.

## Commands

```bash
npm install        # once
npm run dev        # dev server at http://localhost:4321
npm run build      # static site in dist/
npm run preview    # serve dist/
npm run check      # type-check
npm run format     # prettier
```

Node 22 or newer (`.node-version`).

## Where things are

- `content/projects/<slug>/index.mdx`: one folder per project, with its images, posters and captions
- `content/resume/resume.tex`: resume source; GitHub Actions builds the PDF and the page image
- `src/`: pages, layouts, components, styles
- `static/`: files served as-is, including the interactive demos in `static/demos/`
- `tools/`: explainer video renderer, Edwin demo builder, `upload-media.sh` for videos on R2

See `AGENTS.md` for the conventions and gotchas.
