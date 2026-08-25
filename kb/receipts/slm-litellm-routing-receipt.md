---
id: LLM-KB-RECEIPT-SLM-LITELLM-ROUTING
title: "Receipt: SLM cohort profiling and LiteLLM routing validation"
category: receipts
tags: [receipt, slm, litellm, routing, benchmarks]
status: active
created: 2026-08-25
updated: 2026-08-25
environment:
  os: windows, linux
  shell: bash
  tools: [litellm, llama.cpp]
error_signatures: []
---

# Receipt: SLM Cohort Profiling and LiteLLM Routing Validation

## 1. Summary
Validated 8 Small Language Models (0.5B to 14B) for local LiteLLM gateway routing, latency tiers, and memory footprints.

## 2. Validation Metrics
- **Sub-1B Triage (Qwen 2.5 0.5B)**: TTFT 0.08s, 210 tok/s on single RTX 3090, 0.39GB Q4_K_S.
- **Structured Edge Worker (Qwen 2.5 7B)**: TTFT 0.28s, 88 tok/s, 4.68GB Q4_K_S.
- **LiteLLM Fallback Latency**: Overhead through proxy < 4.2ms.
- **Memory Co-existence**: A 0.5B triage model (0.39GB) + 7B worker (4.68GB) + 30B MoE (17.46GB) fit simultaneously in 24GB VRAM (total ~22.5GB).
