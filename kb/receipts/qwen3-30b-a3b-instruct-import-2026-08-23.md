---
id: receipt-qwen3-30b-a3b-instruct-import-2026-08-23
title: Qwen3-30B-A3B Instruct external import receipt
category: receipt
status: partial-upstream-metadata
date: 2026-08-23
tags: [receipt, model, qwen3, moe, import, external-contract]
---

# Qwen3-30B-A3B Instruct import receipt

## Scope

This receipt covers Issue [#37](https://github.com/ozand/localllm-kb/issues/37) and the provenance-preserving external import record:

`kb/raw/research/qwen3-30b-a3b-instruct-2026-08.json`

The record is a partial upstream-metadata result. It does not claim local runtime measurements. Producer canonical identity is preserved separately from downstream consumer mapping.

## Upstream evidence

- Base model: `Qwen/Qwen3-30B-A3B`.
- Base revision: `ad44e777bcd18fa416d9da3bd8f70d33ebb85d39`.
- GGUF repository: `unsloth/Qwen3-30B-A3B-GGUF`.
- GGUF revision: `d5b1d57bd0b504ac62ae6c725904e96ef228dc74`.
- Exact artifact filename: `Qwen3-30B-A3B-Q4_K_S.gguf`.
- Reported artifact size: `17,456,009,792` bytes.
- Reported artifact SHA-256/LFS OID: `fa0c96bed61759800bcab82a8a44a8effcd92cdd8bced06b8195232237390b4a`.
- Original safetensors total: `61,589,265,392` bytes across 16 files.

The artifact hash is explicitly marked as reported upstream metadata and was not independently recomputed from a local download. No model artifact was downloaded or stored in this repository.

## Architecture and context

The upstream config and model card report a sparse MoE Qwen3 model with 30.5B total parameters and 3.3B activated parameters, 48 layers, 32 attention heads, 4 KV heads, head dimension 128, 128 experts, and 8 experts selected per token. The model card reports 32,768 native context and 131,072 tokens with YaRN; the config sets `max_position_embeddings` to 40,960. These values are retained separately.

Qwen3 supports switchable thinking/non-thinking behavior in one checkpoint. The Artificial Analysis slugs `qwen3-30b-a3b-instruct` and `qwen3-30b-a3b-instruct-reasoning` are identity/join aliases only, not evidence of separate local artifacts or measurements.

## Consumer identity mapping

The producer canonical ID is `qwen/qwen3-30b-a3b`. For `ai-dashboards-kb`, `alibaba/qwen3-30b-a3b-instruct` is recorded only as a candidate consumer canonical ID. Join keys are:

- `artificial-analysis/qwen3-30b-a3b-instruct`;
- `artificial-analysis/qwen3-30b-a3b-instruct-reasoning`.

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
- The export preserves producer identity separately from consumer candidate mapping.

## Limitations

This is a partial import receipt, not a complete local benchmark receipt. A follow-up measurement increment is required before claiming support or performance for the requested 98,304-token Q8 KV configuration.
