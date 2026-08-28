---
id: LLM-KB-RECEIPT-YOUTUBE-BOUNDED-VERIFICATION
category: receipts
title: "Receipt: bounded independent verification of YouTube local-inference claims"
status: active
created: 2026-08-28
updated: 2026-08-28
issue: https://github.com/ozand/localllm-kb/issues/98
source_issue: https://github.com/ozand/localllm-kb/issues/90
environment:
  os: Windows
  shell: bash
  tools: [kb-bootstrap, qmd]
error_signatures: []
---

# Bounded independent-verification receipt

## Scope

This receipt canonicalizes the bounded review of 11 selected claims from the finalized 30-transcript local-inference corpus. The machine-readable source artifact is [`../raw/research/youtube-local-llm-2026-08/independent-verification/verification-artifact.json`](../raw/research/youtube-local-llm-2026-08/independent-verification/verification-artifact.json).

The review covers runtime comparisons, speculative decoding, VRAM/KV-cache behavior, Apple/AMD hardware, and distributed inference. It does not perform new benchmarking, downloads, runtime changes, or corpus expansion.

## Provenance

| Evidence source | Identity / stable reference | Access date | Use in review |
|---|---|---:|---|
| vLLM speculative decoding | `vllm-project/vllm`, `docs/features/speculative_decoding/README.md`, stable documentation URL | 2026-08-28 | Runtime capability and limitations for MTP, EAGLE, draft-model, and n-gram methods |
| vLLM parallelism | `vllm-project/vllm`, `docs/serving/parallelism_scaling.md`, stable documentation URL | 2026-08-28 | Tensor/pipeline parallelism and multi-node deployment semantics |
| llama.cpp RPC | `ggml-org/llama.cpp`, `tools/rpc/README.md`, repository `master` reference | 2026-08-28 | Remote-device/RPC capability and proof-of-concept security limitation |
| Ollama API | `ollama/ollama`, `docs/api.md`, repository `main` reference | 2026-08-28 | Runtime options and reported timing-counter semantics |
| MLX unified memory | `ml-explore/mlx`, `usage/unified_memory.html`, documentation version 0.32.2 | 2026-08-28 | Apple unified-memory semantics |
| MLX-LM | `ml-explore/mlx-lm`, `README.md`, repository `main` reference | 2026-08-28 | Apple Silicon generation and distributed-inference capability |

Where an upstream immutable commit or release was not captured in the source review, the stable repository path is recorded and the revision is explicitly described as `unknown`; no revision is inferred.

## Results

- Selected claims: **11**.
- Dimensions covered: runtime comparison; DFlash/MTP speculative decoding; VRAM/KV-cache/context; Apple/AMD/CPU hardware; distributed inference.
- Partially corroborated at runtime/capability level: **3**.
- Unresolved: **8**.
- Promoted to measured performance: **0**.
- Promoted to official performance facts: **0**.
- Promoted to community-reproducible measurements: **0**.

All video-specific numerical claims remain `reported_community_partial`. Official documentation confirms feature existence or semantics only; it does not validate creator-reported TPS, VRAM, TTFT, speedup, or OOM values without matched model, artifact, runtime version, hardware, context, batch, workload, and measurement method.

## Scoped QMD validation record

- **Collection scope:** local project collection `localllm-kb-wiki`; canonical `kb/` paths only, with `kb/raw/**` excluded by `qmd/collections/wiki.yaml`.
- **Validation date:** 2026-08-28.
- **Check:** targeted search for `bounded independent verification`, `DFlash MTP speculative decoding`, and `VRAM KV cache distributed inference`.
- **Result:** canonical receipt and linked research artifact are addressable within the project KB scope; no raw-corpus leakage was intentionally introduced. The configured global `qmd update` remains avoided because workstation-wide updates are known to time out.
- **Repository graph validation:** `kb-bootstrap validate --dir kb` reported 69 nodes, 124 edges, one connected component, and zero dead links.

## Limitations and next step

This receipt is a provenance and canonicalization record, not a benchmark receipt. Claims requiring measured confirmation remain deferred to a separately governed benchmark increment.
