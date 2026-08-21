---
id: runtime-llamacpp-qwen3.8-optimization
title: "llama.cpp & Llama-Server Optimization Guide for Qwen 3.8 / 27B-32B"
type: runtime
status: verified
revision: "b4500+"
evidence:
  - "../raw/research/reddit-50-threads-corpus.md"
  - "../raw/research/reddit-qwen3.8-deepdive-synthesis.md"
  - "../raw/research/reddit-longcontext-pflash-sglang.md"
scope: "Local execution on NVIDIA RTX 3090 Ti (24GB VRAM) + AMD Ryzen 9 5950X (32 Threads) + 128GB RAM"
---

# llama.cpp & Llama-Server Optimization Guide: Qwen 3.8 27B

## Overview

This guide establishes the validated operating configuration for hosting Qwen 3.8 27B (and related 27B–32B architectures) using `llama-server.exe` on a 24GB VRAM / 128GB RAM workstation.

---

## 1. Production Launch Configuration

```bash
llama-server.exe \
  -m "models/Qwen3.8-27B-UD-Q4_K_S.gguf" \
  --mmproj "models/mmproj-BF16.gguf" \
  --jinja \
  --chat-template-kwargs "{\"reasoning_effort\":\"medium\"}" \
  --reasoning on \
  --reasoning-preserve \
  -c 98304 \
  --flash-attn on \
  --cache-type-k q8_0 \
  --cache-type-v q8_0 \
  --spec-type draft-mtp,ngram-mod \
  --spec-draft-n-max 2 \
  --spec-ngram-mod-n-match 24 \
  --spec-ngram-mod-n-min 24 \
  --spec-ngram-mod-n-max 86 \
  -t 16 \
  --batch-size 1024 \
  --ubatch-size 512 \
  --port 8000
```

---

## 2. Parameter Justification & Breakdown

### Multi-Token Prediction (Draft-MTP) + N-gram Speculative Decoding
- `--spec-type draft-mtp,ngram-mod`: Combines model-native multi-token prediction heads with n-gram pattern matching.
- `--spec-draft-n-max 2`: Evaluates up to 2 predicted tokens simultaneously.
- **Observed Throughput**: Increases token generation from ~42 t/s to **65–70 t/s** without requiring an external draft model binary.

### Agentic Loop & Reasoning Preservation
- `--reasoning on` & `--reasoning-preserve`: Instructs the server to preserve thinking tags in the context cache. Crucial for coding agents (Pi, OpenCode) to prevent "Memento" loops and tool hallucinations.
- `--jinja`: Enables native Jinja template parsing for complex system and tool signatures.

### Memory & Thread Allocation
- `-c 98304`: Baseline context window. Requires ~7.2 GB VRAM when quantized to `q8_0` KV. Total VRAM allocation: ~23.1 GB / 24.5 GB.
- `-t 16`: Locks 16 worker threads to match the 16 physical cores of the AMD Ryzen 9 5950X, preventing thread contention with CUDA scheduling.
- `--batch-size 1024` / `--ubatch-size 512`: Smooths VRAM allocation during prompt prefill spikes.

---

## 3. High-Context Extension Protocols (>100k Tokens)

When extending context to **262k** tokens on a 24GB VRAM system, apply the following stepped degradation scheme:

| Context Span | Weight Quant | KV-Cache Type | VRAM Usage | Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **0 – 98k** | `UD-Q4_K_S` | `q8_0` | ~23.1 GB | Full GPU inference |
| **98k – 180k** | `UD-Q4_K_S` | `q4_0` | ~22.8 GB | KV Quantization |
| **180k – 262k** | `UD-Q3_K_XL` | `q4_0` | ~23.4 GB | Stepped Quantization Drop |

---

## Related Documents
- [Qwen 3.8 27B Canonical Model Record](../models/qwen3.8-27b.md)
- [LiteLLM Gateway Integration](../clients/litellm.md)
- [Pi Coding Agent Configuration](../clients/pi.md)
