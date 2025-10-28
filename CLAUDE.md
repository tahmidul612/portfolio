# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal portfolio website built with Hugo static site generator using the Congo theme. The site is deployed at <https://tahmidul612.com> and contains projects and resume content.

## Development Commands

### Setup

```bash
npm install  # Install prettier and prettier-plugin-go-template
```

### Development Server

```bash
hugo server  # Start development server with live reload
```

Or use VS Code:

- Press `F5` to launch with browser auto-open
- Or run "hugo: Serve site" debug configuration

### Build

```bash
hugo  # Build static files to public/ directory
```

Or use VS Code:

- Press `Ctrl + Shift + B` to build
- Or run "hugo: Build site" task

### Code Quality

```bash
npx prettier --write .  # Format files with Go template support
```

## Architecture

### Directory Structure

- `content/` - Markdown content files
  - `projects/` - Project portfolio entries
  - `resume/` - Resume content and generated PDFs
- `config/_default/` - Hugo configuration split into multiple TOML files
  - `config.toml` - Main site configuration
  - `params.toml` - Theme-specific parameters
  - `menus.en.toml` - Navigation menus
  - `languages.en.toml` - Language settings
  - `markup.toml` - Markdown processing configuration
- `themes/` - Git submodules for Hugo themes
  - `congo/` - Main Congo theme (stable branch)
  - `hugo-embed-pdf-shortcode/` - PDF embedding functionality
- `layouts/` - Custom Hugo template overrides
- `static/` - Static assets (images, files, etc.)
- `assets/` - Hugo Pipes assets for processing

### Theme Configuration

The site uses a dual-theme setup:

- Primary: Congo theme for main styling and layout
- Secondary: hugo-embed-pdf-shortcode for PDF embedding capabilities

Both themes are managed as Git submodules and should be updated using Git submodule commands.

### Content Management

- Resume content includes an automated PDF build system
- Projects are managed as individual markdown files in `content/projects/`
- The site supports both HTML and JSON output formats for API consumption

### VS Code Integration

- Launch configuration automatically opens browser when serving
- Build task configured for Ctrl+Shift+B shortcut
- Problem matcher configured for Hugo error reporting
