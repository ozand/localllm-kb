---
id: procedure-multimodal-workflows
title: "Multimodal (Vision & Video) Operating Procedure for Qwen 3.8 / Qwen-VL"
type: procedure
status: verified
revision: "v1.0"
evidence:
  - "../raw/research/reddit-50-threads-corpus.md"
  - "../raw/research/qwen3.8-27b-card.md"
scope: "Local vision & video processing on 24GB VRAM using llama.cpp mmproj"
---

# Multimodal Operating Procedure: Vision & Video

## Overview

Qwen 3.8 natively supports interleaved text, image, and video understanding when paired with a compatible multimodal projector (`mmproj`).

---

## 1. Projector Artifact & VRAM Allocation

- **Artifact**: `mmproj-BF16.gguf` or `mmproj-F16.gguf` (Size: ~1.2 GB).
- **VRAM Impact**: Consumes ~1.3 GB static VRAM upon initialization.
- **Combined Footprint with 27B UD-Q4_K_S**: ~16.2 GB weights + projector. Remaining VRAM for KV-cache: ~8.3 GB (comfortably fits 64k–98k multimodal context).

---

## 2. Video Frame Sampling Best Practices

When analyzing local video files:
1. **Sampling Rate**: Extract frames at **1.0 to 2.0 FPS** (or 1 keyframe every 2–5 seconds for long-form tutorials).
2. **Resolution Downscaling**: Pre-scale frames to $448 	imes 448$ or $672 	imes 672$ px before encoding. Each frame consumes ~256–576 tokens.
3. **Budget Control**: A 60-second clip at 1 FPS produces ~60 image patches ($approx 15,000	ext{–}30,000$ tokens).

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
