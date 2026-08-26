---
id: LLM-KB-RECEIPT-YOUTUBE-TRANSCRIPT-EXPANSION
category: receipts
title: "Receipt: stratified YouTube transcript extraction expansion"
status: active
created: 2026-08-26
updated: 2026-08-26
environment:
  os: Windows
  shell: bash
  tools: [yt-dlp, youtube-deep-research]
error_signatures: []
---

# YouTube Transcript Expansion Receipt

## Scope
A stratified sample was selected from the 82-source discovery corpus across runtime,
hardware, quantization, distributed inference, speculative decoding, reasoning, and
coding-agent queries.

## Results
- Selected sources: 29.
- Transcript captures: 29.
- Unavailable transcripts: 0.
- Extracted text: approximately 79,000 words.
- Run record: `../raw/research/youtube-local-llm-2026-08/transcript-runs/extraction-results.json`.
- Selection record: `../raw/research/youtube-local-llm-2026-08/transcript-runs/selection-manifest.json`.

## Error boundary
23 yt-dlp processes returned non-zero status because fallback language requests received
HTTP 429 responses; the requested transcript files were nevertheless produced. These are
recorded as non-fatal extraction issues, not silently treated as clean runs. The retained
transcript content requires normal source-level review before claims are promoted.
