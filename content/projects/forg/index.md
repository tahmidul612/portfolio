---
title: "forg File Organizer"
summary: "A Rust tool that catalogues my drives, proposes where every file should go, and only moves things after I approve. Every move can be undone."
group: personal
weight: 40
status: "wip-private"
---

{{< status "wip-private" >}}

My drives are full of duplicate photos, half-renamed folders, and downloads I forgot about. forg audits them. It catalogues every file with its hash in SQLite, proposes where each one should go and what it should be called, and moves nothing until I approve the plan. Every move is hash checked and written to a journal, so any run can be undone.

It never deletes anything during a run. Duplicates, empty files, and whatever I mark for removal go to a quarantine folder on the same drive, and they are only deleted when I sign off. A drive I only add to can be marked receive only, so forg will move files onto it but never touch what is already there. When a folder moves and an editing project points into it, forg leaves a link at the old path so the project still opens. It can also benchmark drives, pull metadata with exiftool, ffmpeg, and ImageMagick, and ask Claude to describe files through the Message Batches API.

It is one binary built from six crates. It builds and passes its tests on Linux, but the Windows code still needs a run on real hardware, so the repo stays private for now.

{{< columns >}}

**Tech Used**

- Rust
- SQLite
- Claude Message Batches API

<--->

**&nbsp;**

- exiftool
- ffmpeg
- ImageMagick

{{< /columns >}}
