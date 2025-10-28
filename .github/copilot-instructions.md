# GitHub Copilot Instructions

This is a personal portfolio website built with Hugo static site generator, using the Congo theme and deployed to Cloudflare Pages.

## Architecture Overview

### Dual Theme Setup
- Primary: `congo` theme (Git submodule on `stable` branch) - main styling and layout
- Secondary: `hugo-embed-pdf-shortcode` theme - enables PDF embedding via shortcodes
- Theme order in `config.toml`: `["hugo-embed-pdf-shortcode", "congo"]` - precedence matters

### Configuration Split Pattern
Configuration is modularized across `config/_default/`:
- `config.toml` - Core Hugo settings, theme order, output formats
- `params.toml` - Congo theme-specific parameters (colorScheme, layout options)
- `menus.en.toml` - Navigation structure
- `languages.en.toml` - Language/locale settings
- `markup.toml` - Markdown processing configuration

### Content Structure
- `content/projects/` - Portfolio entries using custom layouts and Congo shortcodes
- `content/resume/` - Resume content with LaTeX source files for PDF generation
- Content uses Hugo's front matter + Congo-specific shortcodes (`{{< lead >}}`, `{{< alert >}}`, `{{< columns >}}`)

## Development Workflow

### VS Code Integration
- **F5**: Launch dev server with browser auto-open (via `launch.json`)
- **Ctrl+Shift+B**: Build static files (via `tasks.json` with Hugo problem matcher)
- Extensions: Hugo language support, syntax highlighting, Prettier with Go template plugin

### Build & Deploy Pipeline
1. **Local Development**: `hugo server` for live reload
2. **PDF Generation**: LaTeX files in `content/resume/` auto-compile to PDF via GitHub Actions
3. **Deployment**: Cloudflare Pages webhook triggered on main branch push
4. **Code Formatting**: Prettier with `prettier-plugin-go-template` for Hugo template formatting

### Git Submodule Management
```bash
git submodule update --init --recursive  # Initialize themes
git submodule update --remote themes/congo  # Update Congo to latest stable
```

## Key Patterns & Conventions

### Custom Shortcode Usage
- `{{< columns >}}` with `<--->` separator for side-by-side content
- `{{< alert "github" >}}` for styled callouts with icons
- `{{< lead >}}` for highlighted intro text (Congo theme)

### Content Organization
- Projects use descriptive sections with consistent tech stack listings
- Image assets in `content/projects/images/` and referenced relatively
- Resume PDF build system maintains source `.tex` files alongside generated output

### Output Formats
Site generates multiple formats: `["HTML", "RSS", "JSON"]` for API consumption and feeds.

## Critical Files for Changes
- `config/_default/params.toml` - Theme appearance and feature toggles
- `content/projects/_index.md` - Main portfolio content with project descriptions
- `layouts/shortcodes/columns.html` - Custom layout for side-by-side content
- `.github/workflows/deploy-to-cf.yml` - LaTeX PDF build and deployment automation

## Development Notes
- No package.json at root - dependencies managed through Hugo modules and themes
- Prettier configuration specifically includes Go template plugin for Hugo syntax
- Site uses Congo's "profile" homepage layout with custom content structure
- PDF embedding capability through secondary theme integration