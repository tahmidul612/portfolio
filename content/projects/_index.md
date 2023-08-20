---
title: "Hi! I'm Tahmidul!"
description: "What have I been up to!"
layout: single
showTableOfContents: true
showDate: false
showReadingTime: false
---

{{< lead >}}
I am currently studying Computer Science at Lakehead University, and hoping to graduate in April 2024. My laziness compels me to learn more about automation so that I can do less work. So my current field of interest is automation.
{{< /lead >}}
{{< alert "github" >}}
You can find some of my projects on Github [@tahmidul612](https://github.com/tahmidul612).
{{< /alert >}}

---

## Personal Projects

### Media Server

I use a Ubuntu Server to store and host my Anime collection, using multiple softwares to make the process automated. Github and Docker are a major part of my entire system. I store my docker compose files in Github and deploy my containers to multiple nodes in a Docker swarm through Portainer.

{{< columns >}}

**Tech Used**

- Ubuntu Server
- Bash
- Python

<--->

 **&nbsp;**

- Docker
- Portainer
- Multiple Open Source Projects

{{< /columns >}}

### Game Server

One of my best buddies lives in a different city, and we wanted to play games together. Since NVIDIA GPUs have GPU-P support, I decided that was a great opportunity for me to learn more and let my friend play games.
I used Hyper-V in Windows to setup a guest Windows system and shared my GPU partition with it. My friend can now remotely access the guest system with Parsec and play games, while I have full access to my PC.

## University Projects

### COMP4478 - Game Programming

{{< alert "github" >}}
[COMP4478_Project_2](https://github.com/tahmidul612/COMP4478_Project_2)
{{< /alert >}}

Our second project for the course was to develop a game using Unity. We chose to make a simple puzzle platformer. My responsibility was to write the code and use unity editor to implement the user interface for the game.

I also played a part in overseeing the collaboration on Github, to merge the PRs and fix any conflicts. Although not a part of our final grade, I implemented a simplified DevOps pipeline using Github Actions and GameCI, with continuous integration and deployment. When we release a new version of the game, I setup a workflow using GameCI to test the project before building the package for Windows and WebGL. The same workflow is used to deploy the WebGL package to Github Pages.

{{< columns >}}

**Tech Used**

- Unity
- C#
- Github

<--->

 **&nbsp;**

- GameCI
- Github Pages

{{< /columns >}}
