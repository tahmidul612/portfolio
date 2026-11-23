---
title: "HondaLink Controller"
summary: "A FastAPI service that drives the HondaLink Android app so my car can be controlled over HTTP."
group: personal
weight: 90
oldAnchor: "hondalink-controller"
---

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
