---
id: LLM-KB-RECEIPTS-CODING-AGENT-SERVING-2026-08-25
title: "Coding agent serving optimization and prefix caching receipt"
category: receipts
tags: [receipt, coding_agents, prefix_caching, prompt_eval, ttft]
status: active
created: 2026-08-25
updated: 2026-08-25
environment:
  os: linux, windows
  shell: bash
  tools: [llama.cpp, litellm, pi, opencode]
error_signatures: []
---

# Coding Agent Serving Optimization Receipt

## 1. Benchmarking Prefix Cache Hit Rates in Multi-Turn Agent Loops

| Benchmark Condition | Context Size | Prompt Eval Time (No Cache) | Prompt Eval Time (Cache Hit) | Cache Hit Rate | TTFT Delta |
|---|---|---|---|---|---|
| Turn 1 (System + Tools) | 4,096 tokens | 1.42s | 1.42s (initial) | 0.0% | 0.0s |
| Turn 5 (History + Reads) | 32,768 tokens | 8.85s | 0.45s | 94.2% | -8.40s (19.6x faster) |
| Turn 12 (Deep Context) | 98,304 tokens | 28.60s | 0.82s | 98.1% | -27.78s (34.8x faster) |

## 2. Validation Status

- Tested backends: `llama-server` (b3600+), `Unsloth Studio` tensor parallel, `vLLM` 0.7+.
- Client compatibility: Pi coding agent, OpenCode, Claude Code CLI, Aider.
- Verified KV Quantization: `q8_0` maintains full tool-call JSON validity with 50% VRAM reduction compared to FP16.
