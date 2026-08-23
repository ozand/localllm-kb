---
id: receipt-cohort-merged-inventory-2026-08-23
title: Consolidated inventory of merged local-model metadata increments
category: receipt
status: read-only-inventory
date: 2026-08-23
tags: [receipt, cohort, inventory, provenance, local-measurements]
---

# Consolidated cohort inventory

This read-only inventory covers merged Issues #36–#45 in `ozand/localllm-kb`. The machine-readable inventory is:

`kb/raw/research/cohort-merged-inventory-2026-08.json`

Each entry records the merged PR commit, export path, receipt path, and unresolved local fields. All ten increments are upstream-metadata inputs; none claims a local runtime benchmark.

## Common unresolved local fields

Across the cohort, the following remain unresolved and explicit `null`/`unknown`:

- runtime and runtime version;
- hardware class;
- 98,304-token context with Q8 KV result;
- VRAM/KV allocation;
- GPU/CPU placement and offload;
- OOM outcome;
- `prompt_eval_tps`;
- `eval_tps`;
- TTFT;
- system power.

Additional variant-specific unresolved fields:

- Issues #40 and #41: local multimodal projector/runtime support;
- Issue #43: effort-specific local variants;
- Issue #45: xhigh local performance and multimodal runtime support.

## Qwen3.8 correction boundary

The existing Qwen3.8 export uses producer canonical `qwen/qwen3.8-27b`, while the downstream consumer currently requires candidate `alibaba/qwen3-8-27b` for AA alias joining. The standard `Q4_K_S` target remains unavailable. The available `UD-Q4_K_S` artifact must remain a distinct alternative and must not be represented as the standard target.

This inventory is read-only and does not replace the required immutable correction commit/PR for the Qwen3.8 export.
