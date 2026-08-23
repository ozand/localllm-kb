---
id: receipt-gemma3-27b-instruct-import-2026-08-23
title: Gemma 3 27B Instruct external import receipt
category: receipt
status: partial-upstream-metadata
date: 2026-08-23
tags: [receipt, model, gemma3, multimodal, import, external-contract]
---

# Gemma 3 27B Instruct import receipt

## Scope

This receipt covers Issue [#40](https://github.com/ozand/localllm-kb/issues/40) and the provenance-preserving external import record:

`kb/raw/research/gemma3-27b-instruct-2026-08.json`

The record is a partial upstream-metadata result. It does not claim local runtime measurements. Producer canonical identity is preserved separately from downstream consumer mapping.

## Upstream evidence

- Base model: `google/gemma-3-27b-it`.
- Base revision: `005ad3404e59d6023443cb575daa05336842228a`.
- GGUF repository: `unsloth/gemma-3-27b-it-GGUF`.
- GGUF revision: `7cd0121f2530b00e42c4df952d4cad4418c0b3c1`.
- Exact artifact filename: `gemma-3-27b-it-Q4_K_S.gguf`.
- Reported artifact size: `15,674,056,416` bytes.
- Reported artifact SHA-256/LFS OID: `27e963b83243c886e64aff611428d7c8abebe53383b0049af0cc928af9c47b7c`.
- Original safetensors total: `54,864,980,440` bytes across 12 files.

The artifact hash is explicitly marked as reported upstream metadata and was not independently recomputed from a local download. No model artifact was downloaded or stored in this repository.

## Architecture and context

Gemma 3 27B Instruct is reported as a multimodal dense model supporting text and image input. The GGUF config reports a `Gemma3ForConditionalGeneration` architecture, 62 text layers, 32 text attention heads, 16 KV heads, head dimension 128, text hidden size 5376, text intermediate size 21504, 131,072 text context, 896 image size, and 256 multimodal tokens per image. The model card describes a 128K context window and multimodal operation.

The reported architecture/config facts do not establish local projector availability or multimodal runtime support.

## Consumer identity mapping

The producer canonical ID is `google/gemma-3-27b-it`. For `ai-dashboards-kb`, `google/gemma-3-27b` is recorded only as a candidate consumer canonical ID. The join key is `artificial-analysis/gemma-3-27b`.

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
- Multimodal claims are kept separate from verified runtime/projector support.

## Limitations

This is a partial import receipt, not a complete local benchmark receipt. A follow-up measurement increment is required before claiming support or performance for the requested 98,304-token Q8 KV configuration or local multimodal inference.
