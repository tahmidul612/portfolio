---
title: "System Monitoring"
summary: "An hourly systemd job that collects anything worrying from my Arch desktop's logs and posts it to n8n."
group: personal
weight: 80
oldAnchor: "system-monitoring"
---

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
