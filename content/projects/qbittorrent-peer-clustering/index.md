---
title: "qBittorrent Peer Clustering"
summary: "Clusters torrent peers on a map and picks the closest VPN server for each cluster."
group: personal
weight: 110
oldAnchor: "qbittorrent-peer-clustering"
---

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
