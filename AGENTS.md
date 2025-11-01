# AGENTS.md

This file provides guidance to AI coding agents like Claude Code (claude.ai/code), Cursor AI, Codex, Gemini CLI, GitHub Copilot, and other AI coding assistants when working with code in this repository.

## Project Overview

Personal portfolio website at <https://tahmidul612.com> built with Hugo static site generator. Dual-theme Hugo setup with Congo (primary) + hugo-embed-pdf-shortcode (secondary). Deployed to Cloudflare Pages with automated LaTeX PDF compilation.

## Essential Commands

### Development

```bash
hugo server                    # Start dev server with live reload (http://localhost:1313)
hugo                           # Build static files to public/ directory
npx prettier --write .         # Format files (Go template support via prettier-plugin-go-template)
```

### VS Code Shortcuts

- `F5` - Launch dev server with browser auto-open
- `Ctrl+Shift+B` - Build static files

### Theme Management (Git Submodules)

```bash
git submodule update --init --recursive           # Initialize themes after clone
git submodule update --remote themes/congo        # Update Congo to latest stable branch
```

### Resume PDF Build

LaTeX files in `content/resume/` are automatically compiled to PDF via GitHub Actions when `.tex` files change. The workflow:

1. Detects `.tex` file changes
2. Compiles with `pdflatex` to `build/` subdirectory
3. Commits generated PDFs back to repo
4. Triggers Cloudflare deployment webhook

## Architecture

### Dual-Theme System

Theme order in `config/_default/config.toml` defines precedence: `["hugo-embed-pdf-shortcode", "congo"]`

- **congo** (Git submodule, `stable` branch) - Main styling, layout, and shortcodes
- **hugo-embed-pdf-shortcode** (Git submodule) - Enables `{{< embed-pdf >}}` shortcode

CRITICAL: Both are Git submodules. Never modify theme files directly. Override via `layouts/` directory in project root.

### Configuration Split Pattern

Hugo config is modularized in `config/_default/`:

- `config.toml` - Core settings, theme order, output formats `["HTML", "RSS", "JSON"]`
- `params.toml` - Congo theme parameters (colorScheme: "ocean", layout: "profile")
- `menus.en.toml` - Navigation structure
- `languages.en.toml` - Language/locale settings
- `markup.toml` - Markdown processing

Changing theme appearance or features? Edit `params.toml`. Never edit theme files.

### Content Structure & Shortcodes

All content uses Hugo front matter + Congo-specific shortcodes:

```markdown
{{< lead >}}Highlighted intro text{{< /lead >}}
{{< alert "github" >}}Styled callout with icon{{< /alert >}}
{{< columns >}}
Left column content
<--->
Right column content
{{< /columns >}}
{{< embed-pdf url="./file.pdf" >}}
```

**Content locations:**

- `content/projects/_index.md` - Main portfolio page with all project descriptions
- `content/resume/` - Resume content + LaTeX source (`resume.tex`) + compiled PDF in `build/`

### Custom Layouts Override

`layouts/shortcodes/columns.html` - Custom implementation of columns shortcode using `<--->` separator. Splits inner content and renders side-by-side with flexbox. Sourced from hugo-geekdoc theme.

### Build & Deploy Pipeline

1. Push to `main` branch
2. GitHub Actions detects `.tex` changes
3. Compiles LaTeX → PDF in `content/resume/build/`
4. Commits PDFs back to repo
5. Triggers Cloudflare Pages webhook for deployment

Deployment workflow: `.github/workflows/deploy-to-cf.yml`

## Critical Patterns

### When Editing Content

- Projects are in single file: `content/projects/_index.md` with multiple headings
- Use `{{< columns >}}` with `<--->` separator for tech stack listings
- Images in `content/projects/images/` referenced relatively
- Never break existing shortcode syntax

### When Modifying Theme Behavior

1. Check if parameter exists in `config/_default/params.toml`
2. If layout change needed, override in `layouts/` directory (not theme files)
3. Theme files are Git submodules - changes will be lost on updates

### When Working with Resume

- Edit `content/resume/resume.tex` for LaTeX source
- GitHub Actions auto-compiles to `content/resume/build/resume.pdf`
- Resume page uses `layout: simple` and `{{< embed-pdf >}}` shortcode

### Prettier Configuration

`.prettierrc` specifies `prettier-plugin-go-template` for Hugo template syntax. Run formatting before commits to avoid template syntax breaking.

## Output Formats

Site generates multiple formats defined in `config.toml`: `["HTML", "RSS", "JSON"]`

- HTML for browsing
- RSS for feed readers  
- JSON for API consumption

## VS Code Integration

Configuration in `.vscode/`:

- `launch.json` - F5 launches `hugo server` with browser
- `tasks.json` - Ctrl+Shift+B runs `hugo` build with custom problem matcher
- `extensions.json` - Recommended Hugo/Prettier extensions

Problem matcher detects Hugo errors and displays in VS Code Problems panel.
