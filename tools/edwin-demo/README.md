# Edwin demo data

Builds `static/demos/edwin/calls.json` and `audio/*.mp3` from simulated calls, using the call reel pipeline in the private ai-phone-assistant repo.

1. In ai-phone-assistant: `uv run python private/call-reel/reel.py fetch <call id>`, then `transcribe <id8> --who <Name> --setting "..."`, then tidy `calls/<id8>/transcript-clean.json` by hand.
2. Add the call to `demo-reel.json` (title, outcome, moments, issues, avatar), using only made-up people.
3. From the portfolio root: `python3 tools/edwin-demo/build_demo.py ~/Documents/repos/ai-phone-assistant tools/edwin-demo/demo-reel.json static/demos/edwin`

The calls are Vapi simulations against the assistant "Edwin demo (portfolio)", which has a made-up owner ("Sam") and no transfer tool.
