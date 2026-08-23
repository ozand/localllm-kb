---
id: receipt-qwen2.5-32b-instruct-import-2026-08-23
title: Qwen2.5-32B Instruct external import receipt
category: receipt
status: partial-upstream-metadata
date: 2026-08-23
tags: [receipt, model, qwen2.5, import, external-contract]
---

# Qwen2.5-32B Instruct import receipt

## Scope

This receipt covers Issue [#39](https://github.com/ozand/localllm-kb/issues/39) and the provenance-preserving external import record:

`kb/raw/research/qwen2.5-32b-instruct-2026-08.json`

The record is a partial upstream-metadata result. It does not claim local runtime measurements. Producer canonical identity is preserved separately from downstream consumer mapping.

## Upstream evidence

- Base model: `Qwen/Qwen2.5-32B-Instruct`.
- Base revision: `5ede1c97bbab6ce5cda5812749b4c0bdf79b18dd`.
- GGUF repository: `bartowski/Qwen2.5-32B-Instruct-GGUF`.
- GGUF revision: `2116cbb385b8ce3a4d28cf3bf1cd2039a55821a6`.
- Exact artifact filename: `Qwen2.5-32B-Instruct-Q4_K_S.gguf`.
- Reported artifact size: `18,784,410,496` bytes.
- Reported artifact SHA-256/LFS OID: `97b51ba6fd524e09b15d36f726725445710aec0b10fb2584604b5f6803e6cd08`.
- Original safetensors total: `65,527,841,856` bytes across 17 files.

The artifact hash is explicitly marked as reported upstream metadata and was not independently recomputed from a local download. No model artifact was downloaded or stored in this repository.

## Architecture and context

The upstream config and model card report a dense Qwen2 architecture with 32.5B parameters, 64 layers, 40 attention heads, 8 KV heads, hidden size 5120, intermediate size 27648, and config `max_position_embeddings` of 32,768. The model card documents full context of 131,072 tokens and 8,192 generation tokens. These values are retained separately and are not silently merged into one context claim.

This is a Qwen2.5 Instruct record. It is kept separate from Qwen3 general, Qwen3 Coder, and other cohort identities; no Qwen3 or coder benchmark/local properties are inherited.

## Consumer identity mapping

The producer canonical ID is `qwen/qwen2.5-32b-instruct`. For `ai-dashboards-kb`, `alibaba/qwen2.5-32b-instruct` is recorded only as a candidate consumer canonical ID. The join key is `artificial-analysis/qwen2.5-32b-instruct`.

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
- Producer identity is separate from consumer candidate mapping and from all Qwen3/coder variants.

## Limitations

This is a partial import receipt, not a complete local benchmark receipt. A follow-up measurement increment is required before claiming support or performance for the requested 98,304-token Q8 KV configuration.
