---
id: procedure-multimodal-workflows
title: "Multimodal (Vision & Video) Operating Procedure for Qwen 3.8 / Qwen-VL"
type: procedure
status: active
revision: "v1.1"
evidence:
  - "../raw/research/reddit-50-threads-corpus.md"
  - "../raw/research/qwen3.8-27b-card.md"
scope: "Local vision & video processing on 24GB VRAM using llama.cpp mmproj"
evidence_status: reported_community_partial
limitations: "Numeric capacity, sampling, and token figures below are bounded guidance from the cited captures, not universal runtime guarantees."
---

# Multimodal Operating Procedure: Vision & Video

## Overview

Qwen 3.8 is described in the cited model-card capture as supporting interleaved text, image, and video understanding when paired with a compatible multimodal projector (`mmproj`). This capability statement is separate from runtime/client compatibility and does not establish the numeric limits below.

---

## 1. Projector Artifact & VRAM Allocation

- **Artifact:** `mmproj-BF16.gguf` or `mmproj-F16.gguf` (reported size: ~1.2 GB; exact filename, revision, and byte size are `unknown`).
- **VRAM impact:** reported ~1.3 GB static VRAM at initialization; exact projector, runtime, backend, hardware, and measurement method are `unknown`.
- **Combined footprint with 27B UD-Q4_K_S:** reported ~16.2 GB weights plus projector, leaving a reported ~8.3 GB for KV-cache in the cited setup. The claim that 64k–98k multimodal context “comfortably fits” is not independently established; usable headroom depends on KV datatype, image/video tokenization, runtime overhead, and workload.

**Evidence status:** `reported_community_partial` / estimate from the cited captures. Do not treat these figures as artifact specifications or a capacity guarantee.
---

## 2. Video Frame Sampling Best Practices

When analyzing local video files:
1. **Sampling rate:** The cited guidance recommends **1.0 to 2.0 FPS** or one keyframe every 2–5 seconds for long-form tutorials. This is conditional guidance, not a universal best practice; motion, media duration, scene changes, model processor, and workload are `unknown`.
2. **Resolution downscaling:** Pre-scale frames to `448 × 448` or `672 × 672` px when supported by the selected processor. The cited ~256–576 tokens per frame is a reported estimate; exact tokenization depends on processor, image dimensions, model/runtime version, and preprocessing.
3. **Budget control:** The cited 60-second clip at 1 FPS and ~15,000–30,000 tokens is an estimate under unstated preprocessing assumptions. Treat frame count, patch count, and token budget as `unknown` until measured for the selected artifact and runtime.

**Evidence status:** `reported_community_partial` / illustrative processing guidance. Do not use the figures as deterministic VRAM or context-budget calculations.
---

## 3. Launching Llama-Server with Multimodal Support

```bash
llama-server.exe \
  -m "models/Qwen3.8-27B-UD-Q4_K_S.gguf" \
  --mmproj "models/mmproj-BF16.gguf" \
  -c 65536 \
  --cache-type-k q8_0 \
  --cache-type-v q8_0 \
  --flash-attn on \
  -t 16
```

---

## Related Documents
- [Model Specification](../models/qwen3.8-27b.md)
- [Runtime Optimization](../runtimes/llamacpp-qwen3.8.md)
