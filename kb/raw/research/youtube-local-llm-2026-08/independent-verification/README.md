---
id: LLM-KB-RESEARCH-YOUTUBE-INDEPENDENT-VERIFICATION
category: research
status: active
created: 2026-08-28
updated: 2026-08-28
error_signatures: []
---

# Bounded independent verification of YouTube local-inference claims

This artifact reviews selected high-value claims from the existing 30-transcript corpus under [Issue #90](https://github.com/ozand/localllm-kb/issues/90). The prior selection manifest records 29 sources because the 30th transcript was added later; this increment uses only claims already present in the finalized 30-transcript corpus.

The review covers runtime comparisons, speculative decoding, VRAM/KV-cache behavior, Apple/AMD hardware, and distributed inference. Official documentation is used only to corroborate runtime capability or semantics. Creator-reported TPS, VRAM, TTFT, speedup, and OOM results remain `reported_community_partial` unless all benchmark conditions and an independent measurement are available.

The machine-readable claim set is in [`verification-artifact.json`](verification-artifact.json).
