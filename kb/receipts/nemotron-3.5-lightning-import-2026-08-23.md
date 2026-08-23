---
id: receipt-nemotron-3.5-lightning-import-2026-08-23
title: NVIDIA Nemotron 3.5 Lightning external import receipt
category: receipt
status: partial-upstream-metadata
date: 2026-08-23
tags: [receipt, model, nvidia, nemotron, hybrid, moe, import, external-contract]
---

# NVIDIA Nemotron 3.5 Lightning import receipt

## Scope

This receipt covers Issue [#44](https://github.com/ozand/localllm-kb/issues/44) and the provenance-preserving external import record:

`kb/raw/research/nemotron-3.5-lightning-30b-a3b-2026-08.json`

The record is a partial upstream-metadata result. It does not claim local runtime measurements. Producer canonical identity is preserved separately from downstream consumer mapping.

## Upstream evidence

- Reference model: `nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16`.
- Reference revision: `d468880b6ad3c6e0d21377ce7242adaea4cc884d`.
- Primary standard GGUF: `bartowski/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF` revision `f0eec2267ae843d9eb21ea3926ab0046da0a8628`.
- Exact primary artifact: `NVIDIA-Nemotron-3.5-Lightning-30B-A3B-Q4_K_S.gguf`.
- Reported primary size: `23,199,183,840` bytes.
- Reported primary SHA-256/LFS OID: `82d6eb30ee69073b2e37311da4b5e65c0040e894aed4a4b2cb95ff990869c752`.
- Original safetensors total: `65,827,374,264` bytes across 14 files.
- Separate alternative: Unsloth `UD-Q4_K_S`, `24,468,027,456` bytes, retained as an alternative and not substituted for standard Q4_K_S.

Artifact hashes are explicitly marked as reported upstream metadata and were not independently recomputed from local downloads. No model artifact was downloaded or stored in this repository.

## Architecture and context

Nemotron 3.5 Lightning is reported as a hybrid Mamba-2/MoE/Attention model with MTP. Config metadata reports 52 layers, 32 attention heads, 2 KV heads, head dimension 128, 128 routed experts, 6 experts per token, Mamba head count 64, and Mamba state size 128. The config specifies 262,144 context; the model card documents up to 1M context in supported deployments and describes 256K as a single-H100 validated context. These are upstream deployment claims, not local fit results.

Reasoning is configurable on/off through the chat template. No hosted or Artificial Analysis reasoning/effort behavior is transferred to the local configuration.

## Consumer identity mapping

The producer canonical ID is `nvidia/nvidia-nemotron-3.5-lightning-30b-a3b-bf16`. For `ai-dashboards-kb`, `nvidia/nemotron-3-5-lightning` is recorded only as a candidate consumer canonical ID. The join key is `artificial-analysis/nemotron-3-5-lightning`.

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
- Provenance URLs, immutable revisions, primary/alternative artifact identities, sizes, and reported hashes are retained.
- Nested `model_identity.consumer_mapping` follows the downstream contract.
- Standard Q4_K_S and Unsloth UD-Q4_K_S remain distinct artifacts.

## Limitations

This is a partial import receipt, not a complete local benchmark receipt. A follow-up measurement increment is required before claiming support or performance for the requested 98,304-token Q8 KV configuration or local runtime behavior.
