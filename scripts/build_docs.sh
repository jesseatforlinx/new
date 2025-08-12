#!/usr/bin/env bash
set -e
for dir in platform/*/*; do
  if [ -f "$dir/conf.py" ]; then
    echo "Building $dir"
    outdir="docs_build/${dir#platform/}"
    sphinx-build -b html -c "$dir" "$dir" "$outdir"
  fi
done
