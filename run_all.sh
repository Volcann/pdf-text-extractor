#!/bin/bash

# Loop through all PDFs in examples/
for pdf in examples/*.pdf; do
  echo "Processing: $pdf"
  python scripts/run_extractor.py "$pdf"
done
