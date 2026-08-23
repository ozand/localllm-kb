---
id: receipt-qwen3.8-27b-xhigh-import-2026-08-23
title: Qwen3.8 27B xhigh external import receipt
category: receipt
status: partial-upstream-metadata
date: 2026-08-23
tags: [receipt, model, qwen3.8, xhigh, multimodal, import, external-contract]
---

# Qwen3.8 27B xhigh import receipt

## Scope

This receipt covers Issue [#45](https://github.com/ozand/locallm-kb/issues/45) and the provenance-preserving external import record:

`kb/raw/research/qwen3.8-27b-xhigh-2026-08.json`

The record is a partial upstream-metadata result. It does not claim local runtime measurements. Producer canonical identity is preserved separately from downstream consumer mapping.

## Identity evidence

- Producer model: `Qwen/Qwen3.8-27B`.
- Producer revision: `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`.
- Artificial Analysis alias: `qwen3-8-27b`.
- Artificial Analysis source ID: `b01dee41-c62b-48ed-8d16-984adc405e5c`.
- Artificial Analysis URL: `https://artificialanalysis.ai/models/qwen3-8-27b`.

AA fields are retained as identity/join metadata only. They are not evidence for local artifacts, runtime, VRAM, OOM, throughput, TTFT, or power.

## Upstream evidence

- GGUF repository: `unsloth/Qwen3.8-27B-GGUF`.
- GGUF revision: `4ca720788d1e01f1bff70c033e0d0028fd02e502`.
- Available exact artifact: `Qwen3.8-27B-UD-Q4_K_S.gguf`.
- Reported artifact size: `15,358,213,024` bytes.
- Reported artifact SHA-256/LFS OID: `75bc9c8adba2842e72f0ab5201aaa07133c5010b566305c09187fcbdcd364017`.
- Original safetensors total: `55,563,006,776` bytes across 18 files.

The requested standard `Q4_K_S` filename was not found in the selected upstream GGUF repository. The available `UD-Q4_K_S` artifact is retained explicitly and is not silently renamed to standard `Q4_K_S`. The hash is reported upstream metadata and was not independently recomputed from a local download. No model artifact was downloaded or stored.

## Architecture and xhigh identity

Qwen3.8 is reported as a multimodal Qwen3.5 architecture with 27B parameters, 64 text layers, 24 attention heads, 4 KV heads, text head dimension 256, mixed linear/full attention every fourth layer, 262,144 text context, 27 vision layers, one MTP layer, and optional video/image tokens.

The upstream card documents `reasoning_effort` levels `xhigh`, `medium`, and `low`, with xhigh as the default. No effort-specific local performance or hosted benchmark value is transferred into this local record.

## Consumer identity mapping

The producer canonical ID is `qwen/qwen3.8-27b`. For `ai-dashboards-kb`, the same string is recorded only as a candidate consumer canonical ID. The join key is `artificial-analysis/qwen3-8-27b`.

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
- Provenance URLs, immutable revisions, AA identity metadata, exact available artifact identity, size, and reported hash are retained.
- Nested `model_identity.consumer_mapping` follows the downstream contract.
- xhigh is retained as a reasoning-effort variant; no effort-specific local result is claimed.
- UD-Q4_K_S is kept distinct from standard Q4_K_S.

## Limitations

This is a partial import receipt, not a complete local benchmark receipt. A follow-up measurement increment is required before claiming support or performance for the requested 98,304-token Q8 KV configuration, xhigh local performance, or multimodal local runtime support.
