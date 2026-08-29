---
id: LLM-KB-RECEIPT-SPECULATIVE-DECODING-CLAIM-VERIFICATION
category: receipts
title: "Receipt: DFlash, MTP, and DSpark claim verification"
status: active
created: 2026-08-29
updated: 2026-08-29
issue: https://github.com/ozand/localllm-kb/issues/100
source_issues:
  - https://github.com/ozand/localllm-kb/issues/90
  - https://github.com/ozand/localllm-kb/issues/98
environment:
  os: Windows
  shell: bash
  tools: [gh, qmd, kb-bootstrap]
error_signatures: []
---

# Speculative-decoding claim verification receipt

## Scope and method

This receipt verifies three high-value claims from the finalized 30-transcript corpus: one DFlash throughput claim, one MTP metric claim, and one DSpark speedup claim. The review uses public upstream documentation/repositories and published benchmark material available online. It does not download models or media, run local benchmarks, change installed runtimes, or expand the corpus.

The originating claims remain in [`claim-verification.json`](../raw/research/youtube-local-llm-2026-08/transcript-runs/claim-verification.json). All transcript locators below are the extracted line location; timestamps were not available and remain `unknown`.

## Evidence policy

- `documented_capability`: an upstream project documents the technique, integration, or supported model.
- `published_benchmark_unmatched`: a project publishes benchmark material, but the source does not match all conditions required to verify the transcript claim.
- `reported_community_partial`: the creator claim is retained as reported community evidence.
- `unresolved`: the numeric or comparative result cannot be independently established from the available evidence.

A capability match is not a performance match. No claim is promoted to `measured_by_external_project` or `reported_community_reproducible` unless model, artifact, runtime version, hardware, context, workload, baseline, and measurement method match.

## Claim review

### 1. DFlash: Qwen 3 8B 38 tok/s to 97 tok/s

- **Claim ID:** `YT90-x9MuyVOtX78-C3`
- **Origin:** [DFlash Just Made AI 6x Faster](https://www.youtube.com/watch?v=x9MuyVOtX78), uploader Kai.
- **Transcript evidence:** “D flash is a speculative decoding method, now merged straight into llama.cpp, aimed at the Qwen 3.6 family. On the Qwen 3 8 billion build, plain auto-regressive decoding runs at 38 tokens per second. Block diffusion pushes that to 97.”
- **Locator:** extracted transcript line 14; timestamp `unknown`.
- **Published conditions:** model `Qwen 3 8B` as transcribed; baseline `38 tok/s`; DFlash/block-diffusion result `97 tok/s`; hardware `unknown`; quantization `unknown`; runtime version `unknown`; context `unknown`; workload and measurement method `unknown`.
- **Upstream evidence:** vLLM Speculators README — `https://raw.githubusercontent.com/vllm-project/speculators/main/README.md`; repository `vllm-project/speculators`, revision `7a58fc56217632d8d179b665734fa2269e8d9ffa`, accessed 2026-08-29. It documents DFlash training/integration and lists a DFlash speculator for Qwen3-8B (`https://huggingface.co/RedHatAI/Qwen3-8B-speculator.dflash`) with vLLM deployment support.
- **Additional evidence:** llama.cpp speculative examples — `https://github.com/ggml-org/llama.cpp/tree/master/examples/speculative`; repository `ggml-org/llama.cpp`, default branch reference `master`, revision `unknown`, accessed 2026-08-29. The examples document speculative decoding generally; they do not establish this DFlash result.
- **Result:** `partially_corroborated_capability_only`.
- **Evidence status:** `reported_community_partial`.
- **Reason:** Upstream evidence supports DFlash as an available speculative-decoding integration for Qwen3-8B in vLLM, but does not verify the llama.cpp merge claim, the 38-to-97 tok/s values, or the missing benchmark conditions.

### 2. MTP: mean value around 4.54 across named datasets

- **Claim ID:** `YT90-RBlRTUwJMI4-C4`
- **Origin:** [Fastest Qwen 3.8 27B in Llama.cpp?](https://www.youtube.com/watch?v=RBlRTUwJMI4), uploader Lukasz Gawenda.
- **Transcript evidence:** “So here we have various data sets GSM 8K, MAF 500, human evil, MVP, MTB badge and we can see here mean. So the MTP was the beginning of the speculative decoding with Eagle 3 and so on. The mean was around 4.54.”
- **Locator:** extracted transcript line 14; timestamp `unknown`.
- **Published conditions:** model `unknown`; runtime `unknown`; hardware `unknown`; datasets as transcribed; metric definition `unknown`; baseline `unknown`; measurement method `unknown`.
- **Upstream evidence:** vLLM speculative decoding documentation — `https://docs.vllm.ai/en/stable/features/speculative_decoding/`; repository `vllm-project/vllm`, revision `9662ab0835e9eac28ac7d95d4b25ecb7140b7bf3`, accessed 2026-08-29. It documents MTP as a supported method, notes that real gains depend on model family, traffic pattern, hardware, and sampling settings, and points to reproducible benchmark examples.
- **Additional evidence:** vLLM Speculators README — `https://raw.githubusercontent.com/vllm-project/speculators/main/README.md`; repository `vllm-project/speculators`, revision `7a58fc56217632d8d179b665734fa2269e8d9ffa`, accessed 2026-08-29. It documents speculator deployment and GuideLLM-based sample benchmarking, but does not define the transcript’s `4.54` metric or conditions.
- **Result:** `documented_capability_and_benchmark_method_only`.
- **Evidence status:** `reported_community_partial`.
- **Reason:** MTP and benchmark tooling are independently documented, but the metric, dataset protocol, model, and runtime conditions are absent, so the reported mean is unresolved.

### 3. DSpark: “50% faster” MLX on Mac

- **Claim ID:** `YT90-S0qHmLjy6gs-C4`
- **Origin:** [Run MLX LLMs 50% Faster on a Mac with DSpark](https://www.youtube.com/watch?v=S0qHmLjy6gs), uploader Joe Maddalone.
- **Transcript evidence:** title/extracted text: “Run MLX LLMs 50% Faster on a Mac with DSpark (Speculative Decoding)”.
- **Locator:** extracted transcript line 12; timestamp `unknown`.
- **Published conditions:** hardware `Mac`, exact model `unknown`; runtime `MLX`, exact version `unknown`; model `unknown`; baseline and improved throughput `unknown`; workload, context, sampling, and measurement method `unknown`.
- **Upstream evidence:** MLX-LM README — `https://raw.githubusercontent.com/ml-explore/mlx-lm/main/README.md`; repository `ml-explore/mlx-lm`, revision `unknown`, accessed 2026-08-29. It documents text generation on Apple silicon and `mx.distributed`, but not DSpark or the claimed speedup.
- **Additional evidence:** vLLM Speculators README — `https://raw.githubusercontent.com/vllm-project/speculators/main/README.md`; repository `vllm-project/speculators`, revision `7a58fc56217632d8d179b665734fa2269e8d9ffa`, accessed 2026-08-29. It documents DSpark as an algorithm extending DFlash with Markov and confidence heads; this is a vLLM/speculators capability reference, not an MLX benchmark.
- **Result:** `unresolved`.
- **Evidence status:** `reported_community_partial`.
- **Reason:** The upstream references establish related Apple/MLX and DSpark capabilities separately, but no public matched evidence verifies a 50% MLX speedup on the Mac configuration used in the video.

## Cross-claim findings

- DFlash: capability partially corroborated; numeric throughput claim unresolved.
- MTP: method and benchmark procedure documented; reported metric unresolved.
- DSpark: algorithm documented in the vLLM Speculators project; MLX-specific speedup unresolved.
- Claims upgraded to `measured_by_external_project`: **0**.
- Claims upgraded to `reported_community_reproducible`: **0**.
- Claims contradicted: **0**.

The existing speculative-decoding procedure contains illustrative speedup figures, but those figures are not treated as independent verification here because the procedure does not provide a matching public artifact, revision, or complete benchmark conditions for these three transcript claims.

## Scoped QMD validation record

- **Collection:** `localllm-wiki` (canonical project KB scope; `kb/raw/**` excluded by `qmd/collections/wiki.yaml`).
- **Date:** 2026-08-29.
- **Checks:** inspected the configured collection list and ran a targeted, CPU/no-rerank search for `bounded independent verification YouTube local inference`.
- **Result:** the collection is registered and the search command completed without a private or unsanitized payload. A scoped `qmd update -c localllm-wiki` was attempted but exceeded the 300-second tool timeout; no global update was run. The new receipt is therefore validated by repository graph checks and direct file review, while QMD re-indexing remains a documented environment limitation.

## Repository validation

- `kb-bootstrap validate --dir kb`: passed; 70 nodes, 126 edges, one connected component, zero dead links (before this receipt was added; the post-change result is recorded in the PR).
- `python -m pytest -q`: passed; 44 tests.
- `git diff --check`: passed.

## Limitations and next step

This is a bounded evidence review, not a benchmark campaign. Independent local or reproducible external measurements are still required before any of the three numerical claims can support canonical performance guidance.
