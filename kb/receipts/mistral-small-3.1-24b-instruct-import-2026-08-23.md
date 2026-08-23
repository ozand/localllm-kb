---
id: receipt-mistral-small-3.1-24b-instruct-import-2026-08-23
title: Mistral Small 3.1 24B Instruct external import receipt
category: receipt
status: partial-upstream-metadata
date: 2026-08-23
tags: [receipt, model, mistral, multimodal, import, external-contract]
---

# Mistral Small 3.1 24B Instruct import receipt

## Scope

This receipt covers Issue [#41](https://github.com/ozand/localllm-kb/issues/41) and the provenance-preserving external import record:

`kb/raw/research/mistral-small-3.1-24b-instruct-2026-08.json`

The record is a partial upstream-metadata result. It does not claim local runtime measurements. Producer canonical identity is preserved separately from downstream consumer mapping.

## Upstream evidence

- Base model: `mistralai/Mistral-Small-3.1-24B-Instruct-2503`.
- Base revision: `68faf511d618ef198fef186659617cfd2eb8e33a`.
- GGUF repository: `unsloth/Mistral-Small-3.1-24B-Instruct-2503-GGUF`.
- GGUF revision: `d63ca9416f5db4f54a78145fb9a025317a57289f`.
- Exact artifact filename: `Mistral-Small-3.1-24B-Instruct-2503-Q4_K_S.gguf`.
- Reported artifact size: `13,549,280,832` bytes.
- Reported artifact SHA-256/LFS OID: `57fac5dcc4a6909444f5cf67550c61331bcab42e36736d021d1aabb45195fd24`.
- Original consolidated safetensors size: `48,022,792,280` bytes.

The artifact hash is explicitly marked as reported upstream metadata and was not independently recomputed from a local download. No model artifact was downloaded or stored in this repository.

## Architecture and context

Mistral Small 3.1 24B Instruct is reported as a multimodal dense text-and-image model. The GGUF configuration reports a `Mistral3ForConditionalGeneration` wrapper with a 24B text model: 40 text layers, 32 attention heads, 8 KV heads, head dimension 128, hidden size 5120, intermediate size 32768, and 131,072 text context. The vision configuration reports 24 vision layers, 16 vision heads, head dimension 64, hidden size 1024, and 1540 image size.

These configuration facts do not establish local projector availability or multimodal runtime support.

## Consumer identity mapping

The producer canonical ID is `mistralai/mistral-small-3.1-24b-instruct-2503`. For `ai-dashboards-kb`, the same string is recorded only as a candidate consumer canonical ID. The join key is `artificial-analysis/mistral-small-3-1`.

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
- Multimodal claims are kept separate from verified local projector/runtime support.

## Limitations

This is a partial import receipt, not a complete local benchmark receipt. A follow-up measurement increment is required before claiming support or performance for the requested 98,304-token Q8 KV configuration or local multimodal inference.
