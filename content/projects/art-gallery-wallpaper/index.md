---
title: "Art Gallery Wallpaper"
summary: "Turns any artwork into a wallpaper of a framed painting hanging in a museum."
group: personal
weight: 60
oldAnchor: "art-gallery-wallpaper"
feature: "art-gallery-wallpaper-met.jpg"
featureAlt: "A painting in an ornate frame in a museum."
---

{{< alert "github" >}}
[artgallery-wallpaper](https://github.com/tahmidul612/artgallery-wallpaper)
{{< /alert >}}

Turns any artwork into a desktop wallpaper that looks like a painting hanging in a museum. The tool rebuilds a full ornate frame from a single scanned frame corner, inlays the artwork with depth and shadow, hangs it on a dark velvet wall under a picture light, and adds a museum placard.

It works offline with the bundled corner scans and no API keys, and the same input and seed always produce the same image byte for byte. With an OpenAI key it will identify the piece and write the placard text, and it can generate frames with OpenAI, Gemini, or a local SDXL model if you want something other than the reconstruction. Version 1.0.0 shipped in June 2026.

{{< figure
    src="art-gallery-wallpaper-met.jpg"
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
