---
title: "Edwin, My Phone Agent"
summary: "Claude writes a brief and places the call. Edwin talks to the business and hands the call to me when it gets stuck."
group: personal
weight: 30
status: "wip-private"
---

{{< status "wip-private" >}}

I don't like making phone calls, so I built something that makes them for me. I tell Claude what I need, like booking a haircut for Saturday or asking the dealer whether a repair is under warranty. Claude writes a short brief, shows it to me, and places the call once I say yes. Edwin, the voice agent, does the talking. If it gets stuck or the other person asks for me, it rings my cell and hands the call over. Afterwards Claude reads the transcript back to me, and an optional n8n workflow emails the call report and puts any booking in my Google Calendar.

Edwin runs on Vapi, with Soniox for speech to text, Claude Haiku 5.5 for the conversation, and an ElevenLabs voice. It started on Opus 4.6, but Opus spent more than half of every reply just getting to its first word, so I moved to Haiku and tightened the prompt instead. It deals with voicemail, call screeners, and phone menus. Calls go out from a Telnyx number over a SIP trunk, because Vapi's free numbers are US only and can't dial out. One base assistant holds my standing details, and each call fills in four variables: who is being called, the task, extra context, and a label for the voicemail. A Python script renders the config and pushes it to Vapi, and a Claude skill lets me place a call from any conversation. At my volume it costs about five to ten dollars a month.

Outbound calls, voicemail, and the per-call brief have been tested on real calls. The newer handover, scheduling, call reports, and calls in Bengali are built but not tested live yet.

{{< columns >}}

**Tech Used**

- Vapi
- Claude
- Telnyx SIP
- Python

<--->

**&nbsp;**

- ElevenLabs
- Soniox
- n8n

{{< /columns >}}
