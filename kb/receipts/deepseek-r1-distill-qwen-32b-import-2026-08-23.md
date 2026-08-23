---
id: receipt-deepseek-r1-distill-qwen-32b-import-2026-08-23
title: DeepSeek R1 Distill Qwen 32B external import receipt
category: receipt
status: partial-upstream-metadata
date: 2026-08-23
tags: [receipt, model, deepseek, reasoning, import, external-contract]
---

# DeepSeek R1 Distill Qwen 32B import receipt

## Scope

This receipt covers Issue [#42](https://github.com/ozand/localllm-kb/issues/42) and the provenance-preserving external import record:

`kb/raw/research/deepseek-r1-distill-qwen-32b-2026-08.json`

The record is a partial upstream-metadata result. It does not claim local runtime measurements. Producer canonical identity is preserved separately from downstream consumer mapping.

## Upstream evidence

- Base model: `deepseek-ai/DeepSeek-R1-Distill-Qwen-32B`.
- Base revision: `711ad2ea6aa40cfca18895e8aca02ab92df1a746`.
- GGUF repository: `bartowski/DeepSeek-R1-Distill-Qwen-32B-GGUF`.
- GGUF revision: `1dc8cf9ffa5dd333057ea1b09ccf4772d8726dec`.
- Exact artifact filename: `DeepSeek-R1-Distill-Qwen-32B-Q4_K_S.gguf`.
- Reported artifact size: `18,784,409,760` bytes.
- Reported artifact SHA-256/LFS OID: `ae5f7e5570239257d554fa1a38ffb8ad634da9dd7e9661e624d1b3bbb6a7b5e8`.
- Original safetensors total: `65,527,841,532` bytes across 8 files.

The artifact hash is explicitly marked as reported upstream metadata and was not independently recomputed from a local download. No model artifact was downloaded or stored in this repository.

## Architecture and reasoning identity

The distilled model uses a dense Qwen2 architecture with 32.5B parameters, 64 layers, 40 attention heads, 8 KV heads, hidden size 5120, intermediate size 27648, and a reported 131,072-token context. `head_dimension` remains `null`; it is not inferred from other fields.

This is a distilled reasoning model, distinct from base Qwen and from Qwen2.5/Qwen3 instruct variants. The record makes no multimodal or projector claim. Any text-only GGUF inference support must be validated separately from runtime-specific capabilities.

## Consumer identity mapping

The producer canonical ID is `deepseek-ai/deepseek-r1-distill-qwen-32b`. For `ai-dashboards-kb`, the same string is recorded only as a candidate consumer canonical ID. The join key is `artificial-analysis/deepseek-r1-distill-qwen-32b`.

Final canonical resolution belongs to `ai-dashboards-kb`, may differ from the producer canonical ID, and must not silently substitute one identity for another.

## Local evidence status

The following requested local fields remain explicit `null` with `unknown` status:

- 98,304-token context with Q8 KV support/result;
- runtime and runtime version;
- hardware profile and placement/offload;
- VRAM/KV allocation;
- OOM result;
- prompt evaluation TPS;
- generation/eval TPS;
- TTFT;
- system power.

No local benchmark was run in this increment, and no unidentified environment evidence was imported.

## Validation notes

- JSON parses successfully.
- Unknown numeric and status values are represented as `null` rather than fabricated values.
- Provenance URLs, immutable revisions, artifact filename, byte size, and reported hash are retained.
- Nested `model_identity.consumer_mapping` follows the downstream contract.
- Text-only GGUF evidence is not expanded into multimodal/projector support.

## Limitations

This is a partial import receipt, not a complete local benchmark receipt. A follow-up measurement increment is required before claiming support or performance for the requested 98,304-token Q8 KV configuration.
