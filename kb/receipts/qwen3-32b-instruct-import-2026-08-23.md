---
id: receipt-qwen3-32b-instruct-import-2026-08-23
title: Qwen3-32B Instruct external import receipt
category: receipt
status: partial-upstream-metadata
date: 2026-08-23
tags: [receipt, model, qwen3, import, external-contract]
---

# Qwen3-32B Instruct import receipt

## Scope

This receipt covers Issue [#36](https://github.com/ozand/localllm-kb/issues/36) and the provenance-preserving external import record:

`kb/raw/research/qwen3-32b-instruct-2026-08.json`

The record is suitable for downstream import as a partial upstream-metadata result. It does not claim local runtime measurements.

## Upstream evidence

- Base model: `Qwen/Qwen3-32B`.
- Base revision: `9216db5781bf21249d130ec9da846c4624c16137`.
- GGUF repository: `unsloth/Qwen3-32B-GGUF`.
- GGUF revision: `931c84066f88693a02ab8de820cfcd066d913241`.
- Exact artifact filename: `Qwen3-32B-Q4_K_S.gguf`.
- Reported artifact size: `18,771,245,728` bytes.
- Reported artifact SHA-256/LFS OID: `359efe7aba13c3ad81311b47c101c62a0419eb21ccda7bea553c3fae045232ac`.
- Original safetensors total: `65,524,328,560` bytes across 17 files.

The artifact hash is explicitly marked as reported upstream metadata and was not independently recomputed from a local download. No model artifact was downloaded or stored in this repository.

## Architecture and context

The upstream config reports a dense Qwen3 causal language model with 64 layers, 64 attention heads, 8 KV heads, and head dimension 128. The model card reports 32.8B parameters, 32,768 native context, and 131,072 tokens with YaRN. The config sets `max_position_embeddings` to 40,960; these values are retained separately and are not silently merged.

Qwen3 supports switchable thinking/non-thinking behavior in one checkpoint. The Artificial Analysis slugs `qwen3-32b-instruct` and `qwen3-32b-instruct-reasoning` are retained only as identity/join aliases from Issue #36, not as evidence of separate local artifacts or measurements.

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
- The export preserves the distinction between upstream reported facts and local unknowns.
- The `ai-dashboards-kb` external contract was reviewed from its public `docs/external-local-benchmark-import.md` and schema files. Downstream schema validation remains the responsibility of the consumer repository.

## Limitations

This is a partial import receipt, not a complete local benchmark receipt. A follow-up measurement increment is required before claiming support or performance for the requested 98,304-token Q8 KV configuration.
