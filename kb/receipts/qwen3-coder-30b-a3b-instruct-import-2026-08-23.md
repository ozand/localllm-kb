---
id: receipt-qwen3-coder-30b-a3b-instruct-import-2026-08-23
title: Qwen3 Coder 30B A3B Instruct external import receipt
category: receipt
status: partial-upstream-metadata
date: 2026-08-23
tags: [receipt, model, qwen3, coder, moe, import, external-contract]
---

# Qwen3 Coder 30B A3B Instruct import receipt

## Scope

This receipt covers Issue [#38](https://github.com/ozand/localllm-kb/issues/38) and the provenance-preserving external import record:

`kb/raw/research/qwen3-coder-30b-a3b-instruct-2026-08.json`

The record is a partial upstream-metadata result. It does not claim local runtime measurements. Producer canonical identity is preserved separately from downstream consumer mapping.

## Upstream evidence

- Base model: `Qwen/Qwen3-Coder-30B-A3B-Instruct`.
- Base revision: `b2cff646eb4bb1d68355c01b18ae02e7cf42d120`.
- GGUF repository: `unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF`.
- GGUF revision: `b17cb02dd882d5b6ab62fc777ad2995f19668350`.
- Exact artifact filename: `Qwen3-Coder-30B-A3B-Instruct-Q4_K_S.gguf`.
- Reported artifact size: `17,456,012,448` bytes.
- Reported artifact SHA-256/LFS OID: `56a7d00783419bcb0ae566253c371bcb3678261bb79881a553539f5679864db4`.
- Original safetensors total: `61,066,575,656` bytes across 16 files.

The artifact hash is explicitly marked as reported upstream metadata and was not independently recomputed from a local download. No model artifact was downloaded or stored in this repository.

## Architecture and context

The upstream config and model card report a sparse MoE model with 30.5B total parameters and 3.3B activated parameters, 48 layers, 32 attention heads, 4 KV heads, head dimension 128, 128 experts, and 8 experts selected per token. The coder model documents 262,144 native context and warns that OOM may require reducing context, including to 32,768 tokens. These facts are reported metadata, not local fit measurements.

The coder checkpoint is non-thinking only and does not generate `<think>` blocks. It must not be merged with the general Qwen3 30B A3B model or assigned a reasoning alias.

## Consumer identity mapping

The producer canonical ID is `qwen/qwen3-coder-30b-a3b-instruct`. For `ai-dashboards-kb`, `alibaba/qwen3-coder-30b-a3b-instruct` is recorded only as a candidate consumer canonical ID. The join key is `artificial-analysis/qwen3-coder-30b-a3b-instruct`.

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
- Total and active parameter counts are retained as separate fields; active parameters are not used as a memory-footprint estimate.

## Limitations

This is a partial import receipt, not a complete local benchmark receipt. A follow-up measurement increment is required before claiming support or performance for the requested 98,304-token Q8 KV configuration.
