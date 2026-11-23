---
title: "Should I Get Gas?"
summary: "Tells you whether to fill up now or wait, based on where regional gas prices are heading."
group: personal
weight: 50
oldAnchor: "should-i-get-gas"
---

{{< alert "github" >}}
[shouldigetgas](https://github.com/tahmidul612/shouldigetgas) || [Live site](https://shouldigetgas.vercel.app/)
{{< /alert >}}

A web app that answers one question: should you fill up now, or wait a couple of days? Most gas apps tell you where prices are lowest. This one looks at where regional prices are heading and gives a verdict (fill up, top off, or wait) with a short explanation.

A Python backend pulls prices from the US EIA, NRCAN, and Ontario datasets plus fuel news, runs part of the analysis through Claude Haiku, and writes a fresh snapshot for 62 regions every six hours. The updater has been paused since late September 2026, so the prices on the site are from then until I get it running again. The frontend is React with no build step, works as a PWA, and is hosted on Vercel. I vibe-coded the whole thing with Claude and say so on the site, so treat the verdicts as a hint and not financial advice.

{{< columns >}}

**Tech Used**

- Python
- React
- Claude API

<--->

**&nbsp;**

- Vercel
- EIA and NRCAN open data

{{< /columns >}}
