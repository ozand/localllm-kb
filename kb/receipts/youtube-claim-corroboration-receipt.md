---
id: LLM-KB-RECEIPT-YOUTUBE-CLAIM-CORROBORATION
category: receipts
title: "Receipt: official-source corroboration pass for YouTube inference claims"
status: active
created: 2026-08-28
updated: 2026-08-28
environment:
  os: Windows
  shell: bash
  tools: [qmd, kb-bootstrap]
error_signatures: []
---

# YouTube Claim Corroboration Receipt

## Scope
A conservative corroboration pass compared the 99 candidate claims from 30 YouTube
transcripts with public official runtime documentation and source repositories.

## Results
- Candidate claims reviewed: 99.
- Claims with a related official runtime surface/reference: 13.
- Claims upgraded to measured: 0.
- Claims upgraded to official performance facts: 0.
- All video-specific numbers remain `reported_community_partial` until exact conditions
  and independent measurements are available.

## References used
- [vLLM Automatic Prefix Caching](https://docs.vllm.ai/en/stable/features/automatic_prefix_caching.html)
- [llama.cpp RPC tools](https://github.com/ggml-org/llama.cpp/tree/master/tools/rpc)
- [Ollama API](https://docs.ollama.com/api)
- [MLX](https://github.com/ml-explore/mlx)
- [llama-cpp-python server](https://llama-cpp-python.readthedocs.io/en/latest/server/)
- [SGLang documentation](https://docs.sglang.ai/)

## Interpretation rule
Documentation can corroborate that a runtime feature exists or describe its semantics.
It does not validate a creator's TPS, VRAM, TTFT, speedup, or OOM result without matching
model, artifact, runtime version, hardware, context, batch, and workload conditions.
