---
title: "Hi! I'm Tahmidul!"
description: "What have I been up to!"
layout: single
showTableOfContents: true
showDate: false
showReadingTime: false
---

{{< lead >}}
I'm an automation engineer. Right now that means building n8n workflows, AI pipelines, and internal web apps at Raphael Porcelain, a porcelain tile wholesaler, where I've worked remotely since October 2025. Before that I interned at AI Buddy Catalyst Labs building AI agents and deployment automation. I finished my HBSc in Computer Science at Lakehead University in 2024.

My laziness compels me to learn more about automation so that I can do less work. Most of what I build outside of work exists because I got tired of doing something by hand. Python is my main language, and I also write JavaScript and TypeScript, Bash, PowerShell, C#, and Java depending on what the job needs. I lean on Claude Code a lot these days, and I say so in the READMEs.
{{< /lead >}}

{{< alert "github" >}}
You can find some of my projects on Github [@tahmidul612](https://github.com/tahmidul612).
{{< /alert >}}

---

## Work

### Raphael Porcelain

Raphael Porcelain is a wholesale manufacturer of large-format porcelain tile. I've been their automation engineer since October 2025, working remotely from Toronto.

The first thing I built was the competitive intelligence pipeline: n8n workflows that find competitors' accounts across nine social platforms, scrape posts and engagement into MongoDB every week, and run a two-stage AI analysis (an analyst pass, then an executive summary) that goes out as an HTML email and a print-ready PDF with the source images included. Past weeks live in a Qdrant vector store so the analysis can cite what changed. All the workflow code and JSON is version controlled in git.

Lead generation came next: scrapers for Houzz and Google Maps, classification prompts in Clay.com that decide whether a business is a wholesale target, an advertising partner, or a competitor showroom, and a sync into Salesforce. When the n8n enrichment workflow got too big to maintain, I replaced it with a FastAPI and React app that crawls each lead's website, checks Google Maps, and runs specialized agents through the OpenAI Batch API, then lets a person review the result field by field before export. It has role-based access through a shared Better Auth server and ships as Docker images from GitHub Actions behind Traefik.

Two smaller apps round it out: a map and spreadsheet view of ten thousand plus leads for the sales team, and a tile visualizer that takes a floor plan and a tile choice, plans the layout, and streams an AI rendered isometric room back to the browser.

{{< columns >}}

**Tech Used**

- n8n
- Python
- FastAPI
- React
- TypeScript
- MongoDB

<--->

**&nbsp;**

- Qdrant
- OpenAI API
- Docker
- Traefik
- Clay.com
- Salesforce

{{< /columns >}}

### AI Buddy Catalyst Labs

{{< alert "github" >}}
[insta_rag](https://github.com/AI-Buddy-Catalyst-Labs/insta_rag) || [ansible-playbooks](https://github.com/tahmidul612/ansible-playbooks)
{{< /alert >}}

An internship from May to October 2025 building AI agents and the automation around them. The public piece of that is insta_rag, a configuration-driven RAG library: semantic chunking, hybrid vector and BM25 retrieval, HyDE, optional reranking, Qdrant for vectors with MongoDB for content, and a Graph RAG mode on Neo4j. I set up its packaging, tests, pre-commit secret scanning, and the release workflow that publishes it to PyPI.

I also worked on a content pipeline that chains five different LLMs in sequence behind a FastAPI service, and wrote the Ansible playbooks and GitHub Actions workflows that stood up a kubeadm Kubernetes cluster with Tailscale, MetalLB, nginx ingress, and cert-manager.

{{< columns >}}

**Tech Used**

- Python
- n8n
- FastAPI
- Qdrant

<--->

**&nbsp;**

- Ansible
- Kubernetes
- GitHub Actions
- Neo4j

{{< /columns >}}

## Personal Projects

### Should I Get Gas?

{{< alert "github" >}}
[shouldigetgas](https://github.com/tahmidul612/shouldigetgas) || [Live site](https://shouldigetgas.vercel.app/)
{{< /alert >}}

A web app that answers one question: should you fill up now, or wait a couple of days? Most gas apps tell you where prices are lowest. This one looks at where regional prices are heading and gives a verdict (fill up, top off, or wait) with a short explanation.

A Python backend pulls prices from the US EIA, NRCAN, and Ontario datasets plus fuel news, runs part of the analysis through Claude Haiku, and commits a fresh snapshot for 62 regions four times a day from GitHub Actions. The frontend is React with no build step, works as a PWA, and is hosted on Vercel. I vibe-coded the whole thing with Claude and say so on the site, so treat the verdicts as a hint and not financial advice.

{{< columns >}}

**Tech Used**

- Python
- React
- Claude API

<--->

**&nbsp;**

- GitHub Actions
- Vercel
- EIA and NRCAN open data

{{< /columns >}}

### Art Gallery Wallpaper

{{< alert "github" >}}
[artgallery-wallpaper](https://github.com/tahmidul612/artgallery-wallpaper)
{{< /alert >}}

Turns any artwork into a desktop wallpaper that looks like a painting hanging in a museum. The tool rebuilds a full ornate frame from a single scanned frame corner, inlays the artwork with depth and shadow, hangs it on a dark velvet wall under a picture light, and adds a museum placard.

It works offline with the bundled corner scans and no API keys, and the same input and seed always produce the same image byte for byte. With an OpenAI key it will identify the piece and write the placard text, and it can generate frames with OpenAI, Gemini, or a local SDXL model if you want something other than the reconstruction. Version 1.0.0 shipped in June 2026.

{{< figure
    src="images/art-gallery-wallpaper-met.jpg"
    alt="A painting in an ornate frame in a museum."
    caption="This photo I took at the MET museum is what I was going for"
    >}}

{{< columns >}}

**Tech Used**

- Python
- OpenCV
- Pillow

<--->

**&nbsp;**

- OpenAI and Gemini SDKs
- Stable Diffusion XL
- uv

{{< /columns >}}

### System Monitoring

{{< alert "github" >}}
[system-monitoring](https://github.com/tahmidul612/system-monitoring)
{{< /alert >}}

A small tool that runs every hour from a systemd timer on my Arch desktop. It gathers anything worrying from the system and user journals, Docker container logs, and the pacman log, groups duplicates with counts and time ranges, and posts one JSON payload to an n8n webhook with retries. It remembers its place in the pacman log between runs so nothing gets reported twice, and one collector failing never blocks the others. It is a oneshot script rather than a daemon: collect, post, exit.

{{< columns >}}

**Tech Used**

- Python
- systemd
- journalctl

<--->

**&nbsp;**

- Docker
- n8n
- uv

{{< /columns >}}

### HondaLink Controller

{{< alert "github" >}}
[hondalink-app-controller](https://github.com/tahmidul612/hondalink-app-controller)
{{< /alert >}}

A FastAPI service that drives the HondaLink Android app through uiautomator2 on a phone or emulator connected over ADB, so my car can be controlled from any HTTP client. It exposes lock, unlock, remote start, and stop as endpoints, reads fuel level, odometer, and door state, and reports the timer and cabin temperature of an active remote start. Because it controls a real car, every endpoint needs an API key, requests are rate limited and IP restricted, and every command goes into an audit log. A mock driver lets the test suite run without a phone.

{{< columns >}}

**Tech Used**

- Python
- FastAPI
- uiautomator2

<--->

**&nbsp;**

- ADB
- Docker
- pytest

{{< /columns >}}

### Manhwa Discovery

{{< alert "github" >}}
[manhwa-discovery](https://github.com/tahmidul612/manhwa-discovery)
{{< /alert >}}

I track what I read on AniList and read it on MangaDex, and the two never agree on what anything is called. This app pulls my AniList lists, matches each entry to MangaDex using fuzzy title matching and release dates, and lets me fix the ones it gets wrong. From there I can search both catalogs at once, sort and filter by rating, chapter count, or unread chapters, and add new finds straight to AniList with the MangaDex link already attached. Redis and MongoDB cache everything so it rarely asks either API for the same thing twice.

{{< columns >}}

**Tech Used**

- Python
- FastAPI
- React

<--->

**&nbsp;**

- MongoDB
- Redis
- Docker

{{< /columns >}}

### qBittorrent Peer Clustering

{{< alert "github" >}}
[qbScripts](https://github.com/tahmidul612/qbScripts)
{{< /alert >}}

A CLI that pulls the peer list from qBittorrent, geolocates every peer, clusters them with K-means, and recommends the ProtonVPN P2P server closest to each cluster. Output is a Rich terminal report plus an interactive HTML map, which Playwright can also render to a PNG.

{{< columns >}}

**Tech Used**

- Python
- qBittorrent Web API
- K-means clustering

<--->

**&nbsp;**

- Rich
- Playwright
- pytest

{{< /columns >}}

### Plex Poster Downloader (tpdb)

{{< alert "github" >}}
[tpdb](https://github.com/tahmidul612/tpdb)
{{< /alert >}}

A CLI for people who care about their Plex posters. It downloads poster sets from ThePosterDB, matches them to your library with fuzzy matching, asks when it is unsure, and files them into a folder layout that Kometa understands. It can also link posters into the media folders and find duplicates. Version 0.4.0 added an interactive login that tests the Plex connection before saving anything.

{{< columns >}}

**Tech Used**

- Python
- PlexAPI
- RapidFuzz

<--->

**&nbsp;**

- Typer
- Rich
- Requests

{{< /columns >}}

### Autogenerated Calendar for Free Concerts

{{< alert "github" >}}
[RCMusic-Free](https://github.com/tahmidul612/rcmusic-free)
{{< /alert >}}

This Python script scrapes the Royal Conservatory of Music's website for free student recitals and community performances and generates an iCalendar (.ics) file, so you can subscribe in your calendar app and stay updated with the latest free concert schedules. The public calendar is updated automatically every hour.

{{< columns >}}

**Tech Used**

- Python
- BeautifulSoup
- iCalendar

<--->

**&nbsp;**

- GitHub Actions
- Cloudflare Workers

{{< /columns >}}

### Homelab

{{< alert "github" >}}
[arch-config](https://github.com/tahmidul612/arch-config)
{{< /alert >}}

I have run a homelab for about eight years. These days it lives on my main desktop, which runs CachyOS (Arch) with rootless Docker, and every service is a Compose file in one git repo. A Cloudflare Tunnel with Access in front handles the public hostnames, a UniFi router handles the network, and a Raspberry Pi is a second Docker host for the small stuff.

The services I would miss most are Immich for photos and Paperless-ngx for documents, which now runs its AI features against the local GPU. There's also Plex with Kometa, Audiobookshelf and Storyteller for audiobooks, Jellyfin, n8n, Ollama, Guacamole, and a Minecraft server. Most of what I know about networking, Linux, and containers came from breaking and fixing this setup. My Arch setup notes outgrew a README and became a MkDocs site.

{{< columns >}}

**Tech Used**

- CachyOS (Arch Linux)
- Docker Compose
- Cloudflare Tunnel
- Bash

<--->

**&nbsp;**

- Python
- n8n
- Ollama
- MkDocs

{{< /columns >}}

### Application Setup Guides

{{< alert "github" >}}
[playnite-config](https://github.com/tahmidul612/playnite-config) || [plexHTPC-config](https://github.com/tahmidul612/plexHTPC-config) || [pwsh-config](https://github.com/tahmidul612/pwsh-config) || [fish-config](https://github.com/tahmidul612/fish-config)
{{< /alert >}}

Markdown guides for the tools I keep reinstalling: Playnite, Plex HTPC, PowerShell with a custom prompt, and Fish. They are mostly so I don't have to remember the same settings twice.

### COMP4478 Game Programming (2023)

{{< alert "github" >}}
[COMP4478_Project_2](https://github.com/tahmidul612/COMP4478_Project_2)
{{< /alert >}}

A puzzle platformer in Unity for a university course. I wrote the game code and the UI, and handled merging everyone's PRs. Although not a part of our final grade, I set up a GameCI pipeline in GitHub Actions that tests the project, builds it for Windows and WebGL, and deploys the WebGL build to GitHub Pages on each release.

{{< columns >}}

**Tech Used**

- Unity
- C#

<--->

**&nbsp;**

- GameCI
- GitHub Pages

{{< /columns >}}
