---
id: receipt-gpt-oss-20b-import-2026-08-23
title: OpenAI gpt-oss-20b external import receipt
category: receipt
status: partial-upstream-metadata
date: 2026-08-23
tags: [receipt, model, openai, gpt-oss, moe, import, external-contract]
---

# OpenAI gpt-oss-20b import receipt

## Scope

This receipt covers Issue [#43](https://github.com/ozand/localllm-kb/issues/43) and the provenance-preserving external import record:

`kb/raw/research/gpt-oss-20b-2026-08.json`

The record is a partial upstream-metadata result. It does not claim local runtime measurements. Producer canonical identity is preserved separately from downstream consumer mapping.

## Upstream evidence

- Base model: `openai/gpt-oss-20b`.
- Base revision: `6cee5e81ee83917806bbde320786a8fb61efebee`.
- GGUF repository: `unsloth/gpt-oss-20b-GGUF`.
- GGUF revision: `d449b42d93e1c2c7bda5312f5c25c8fb91dfa9b4`.
- Exact artifact filename: `gpt-oss-20b-Q4_K_S.gguf`.
- Reported artifact size: `11,618,492,608` bytes.
- Reported artifact SHA-256/LFS OID: `3c5483e8749f4865f1aae2c36b796e7b8c43ec02c5a74d663a82a5fe916b2298`.
- Original safetensors total: `27,522,617,888` bytes across 3 files.

The artifact hash is explicitly marked as reported upstream metadata and was not independently recomputed from a local download. No model artifact was downloaded or stored in this repository.

## Architecture and variant identity

gpt-oss-20b is reported as a sparse MoE model with 21B total parameters and 3.6B active parameters, 24 layers, 64 attention heads, 8 KV heads, head dimension 64, 32 local experts, and 4 experts per token. The model config reports 131,072 maximum context with a 4,096 initial context and YaRN scaling. The model uses native MXFP4 quantization for MoE weights.

The model supports configurable reasoning effort levels: low, medium, and high. No effort-specific local benchmark is claimed; these modes must not be merged into one performance result.

## Consumer identity mapping

The producer canonical ID is `openai/gpt-oss-20b`. For `ai-dashboards-kb`, the same string is recorded only as a candidate consumer canonical ID. The join key is `artificial-analysis/gpt-oss-20b`.

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
- Low/medium/high reasoning levels are retained as a variant distinction without effort-specific measurements.

## Limitations

This is a partial import receipt, not a complete local benchmark receipt. A follow-up measurement increment is required before claiming support or performance for the requested 98,304-token Q8 KV configuration or any specific reasoning-effort level.
