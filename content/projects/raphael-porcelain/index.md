---
title: "Raphael Porcelain"
summary: "Automation engineer since October 2025: n8n pipelines, lead tools, and internal web apps for a porcelain tile wholesaler."
group: work
weight: 10
oldAnchor: "raphael-porcelain"
---

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
