---
id: LLM-KB-RESEARCH-YOUTUBE-DISTILLATION-2026-08
category: research-synthesis
title: "Distillation of 30 YouTube transcripts: local LLM inference research"
capture_date: 2026-08-27
source_count: 30
evidence_status: "reported_community_partial"
tags: [youtube, local-llm, inference, hardware, quantization, runtimes]
---

# Distillation of 30 YouTube Transcripts

## Method

Thirty raw transcripts from the 82-source discovery corpus were scanned for candidate
claims and technical terms. The regex extraction artifact is a triage aid, not an
independent benchmark. Numeric claims remain `reported_community_partial` until the
video context, model artifact, runtime version, hardware, context, and workload are
verified.

## Observed themes

- Runtime comparisons frequently mix different models, quantizations, context lengths,
and batch settings; direct rankings are not portable without normalization.
- DFlash/MTP claims require acceptance rate, draft/target pair, baseline throughput,
and generation workload; headline speedup alone is insufficient.
- Apple unified memory, AMD Strix Halo, discrete NVIDIA GPUs, and CPU offload form
separate hardware classes and should not share one TPS leaderboard.
- VRAM claims often omit KV-cache precision and context length. Future records must
separate weights, KV cache, activations, and total peak memory.
- Coding-agent videos use informal task claims. A reproducible agent comparison needs
harness version, tools, task set, prompt, reasoning budget, completion rate, and latency.
- Distributed inference requires network topology and communication mode: layer
sharding, tensor parallel, RPC, Ethernet, Thunderbolt, or NVLink.

## New search hypotheses

1. Re-run the top runtime comparisons with the same GGUF, prompt, context, and batch size.
2. Extract every DFlash/MTP numerical claim into a claim table and verify acceptance rate.
3. Search for CPU-only and AMD/Apple measurements with explicit memory bandwidth.
4. Compare KV-cache quantization (`q8_0`, `q4_0`, FP16) at fixed contexts.
5. Search coding-agent videos for tool-call failure rates rather than marketing claims.
6. Cross-check claims against official llama.cpp, vLLM, SGLang, MLX, and model docs.

## Source artifacts

- Discovery manifest: `../source-manifest.json`.
- Selection manifest: `transcript-runs/selection-manifest.json`.
- Extraction results: `transcript-runs/extraction-results.json`.
- Candidate extraction: `transcript-runs/claim-extraction.json`.


## Corroboration pass

- [Official-source corroboration receipt](../../../receipts/youtube-claim-corroboration-receipt.md)
