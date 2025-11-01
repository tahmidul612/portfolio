# Personal Portfolio Website

[![LaTeX Build and Cloudflare Pages Deployment](https://github.com/tahmidul612/portfolio/actions/workflows/deploy-to-cf.yml/badge.svg)](https://github.com/tahmidul612/portfolio/actions/workflows/deploy-to-cf.yml)
[![Hugo](https://img.shields.io/badge/Hugo-0.125.4-blue?style=flat&logo=hugo)](https://gohugo.io/)

Source code for my personal portfolio at [tahmidul612.com](https://tahmidul612.com). This README is a personal guide for setting up and managing the project.

## Essential Commands

- **Run dev server**: `hugo server`
- **Build static files**: `hugo`
- **Format code**: `npx prettier --write .`
- **Initialize themes**: `git submodule update --init --recursive`
- **Update themes**: `git submodule update --remote themes/congo`

## Getting Started

1.  **Prerequisites**:
    - [Hugo (Extended version)](https://gohugo.io/installation/)
    - [Node.js](https://nodejs.org/en/download/) (for formatting)

2.  **Clone the repository**:
    ```bash
    git clone https://github.com/tahmidul612/portfolio.git
    cd portfolio
    ```

3.  **Initialize themes (Git Submodules)**:
    ```bash
    git submodule update --init --recursive
    ```

4.  **Install dependencies**:
    ```bash
    npm install
    ```
    This installs Prettier and the Go template plugin for code formatting.

5.  **Run the dev server**:
    ```bash
    hugo server
    ```
    The site will be available at `http://localhost:1313`.

### VS Code Integration

This project is configured for a seamless VS Code experience:
- Press `F5` to launch the dev server.
- Press `Ctrl+Shift+B` to build the static files.
- The editor will recommend extensions for Hugo and Prettier.

## Architecture Overview

This project has a few key architectural patterns to be aware of:

-   **Dual-Theme System**: The site uses two themes as Git submodules:
    -   `congo`: The primary theme for styling and layout.
    -   `hugo-embed-pdf-shortcode`: Adds the `{{< embed-pdf >}}` shortcode.
    Theme files should not be modified directly. Use the root `layouts/` directory for overrides.

-   **Modular Configuration**: The Hugo configuration is split into multiple files in the `config/_default/` directory. The main theme parameters are in `params.toml`.

-   **Content Structure**:
    -   The main portfolio content is in a single file: `content/projects/_index.md`.
    -   The resume's LaTeX source is at `content/resume/resume.tex`.

-   **Custom Shortcodes**: The project includes a custom `columns` shortcode, implemented in `layouts/shortcodes/columns.html`.

## Automation

This project uses GitHub Actions for CI/CD:

-   **LaTeX to PDF**: Any changes to `.tex` files in `content/resume/` will automatically trigger a GitHub Action that compiles them into PDFs and commits them back to the repository.

-   **Cloudflare Pages Deployment**: After the PDF build, a webhook is called to trigger a new deployment on Cloudflare Pages.

The full workflow is defined in `.github/workflows/deploy-to-cf.yml`.
