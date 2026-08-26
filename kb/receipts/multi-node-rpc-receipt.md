---
id: LLM-KB-RECEIPTS-MULTI-NODE-RPC
title: "Multi-Node llama.cpp RPC & vLLM Cluster Research Receipt"
category: receipts
tags: [receipts, rpc, clustering, multi_node, llamacpp, youtube_deep_research]
status: active
created: 2026-08-25
updated: 2026-08-25
environment:
  os: any
  shell: any
  tools: [yt-dlp, youtube-deep-research]
error_signatures: []
---

# Multi-Node llama.cpp RPC & vLLM Cluster Validation Receipt

Validation receipt for YouTube deep research on multi-node local LLM clustering and fine-tuning teardowns.

## Ingested Raw Transcripts
- `kb/raw/transcripts/qwen38-cross-node-mac-nvidia-rpc.md` (3,146 words) - Codacus
- `kb/raw/transcripts/amd-strix-halo-cluster-llamacpp-rpc.md` (3,238 words) - Donato Capitella
- `kb/raw/transcripts/vllm-multi-node-distributed-inference.md` (2,773 words) - Bijan Bowen
- `kb/raw/transcripts/unsloth-studio-local-finetune-teardown.md` (6,954 words) - David Ondrej
- `kb/raw/transcripts/nvidia-unsloth-studio-local-finetune.md` (1,456 words) - NVIDIA Developer

## Key Empirical Findings
- Cross-platform RPC (Apple Metal + NVIDIA CUDA) generates 22 tok/s on Qwen 3.8 27B across 2.5GbE network.
- 10GbE or Thunderbolt networking is required to eliminate prompt-eval latency bottlenecks during multi-node all-reduce.
- RPC transfers layer weights on initialization; model GGUF is needed only on the master node.
