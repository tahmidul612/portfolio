#!/usr/bin/env bash
# Upload every explainer MP4 in content/projects/ to the R2 bucket that serves
# them (see mediaBase in config/_default/params.toml). Run after re-rendering.
set -euo pipefail
cd "$(dirname "$0")/.."
for f in content/projects/*/*.mp4; do
  key="${f#content/}"
  npx -y wrangler@4 r2 object put "portfolio-media/$key" --file "$f" \
    --content-type video/mp4 --cache-control "public, max-age=86400" --remote
done
