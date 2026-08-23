# NVIDIA Nemotron 3.5 Lightning 30B A3B — Deep Practical Local Research Receipt

- Date: 2026-08-23
- Model: NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16
- Scope: Hybrid Mamba-2/MoE/Attention architecture (30B total / 3B active), dual artifact paths (Bartowski Q4_K_S vs Unsloth UD-Q4_K_S), 98K hybrid context scaling, and multi-GPU memory fit

## 1. Architecture & MoE Parameters
- **Architecture**: Hybrid State-Space (Mamba-2) + Sparse Mixture-of-Experts + Periodic Attention.
- **Parameters**: 30B total parameters, only **3.0B active parameters** per token.
- **Layers & Heads**: 48 layers, 32 attention heads, 8 KV heads, 128 experts (8 active per token).
- **Context Window**: 262,144 config tokens (up to 1,048,576 documented in specialized deployments).

## 2. Quantization Matrix
- Original safetensors: 65.83 GB
- **Primary GGUF Artifact (Bartowski)**:
  * `NVIDIA-Nemotron-3.5-Lightning-30B-A3B-Q4_K_S.gguf`: **23.20 GB** (SHA LFS: `82d6eb30ee69...`)
  * `Q8_0`: 35.00 GB
  * `Q6_K`: 34.31 GB
  * `Q5_K_M`: 26.96 GB
  * `Q4_K_M`: 25.48 GB
  * `IQ4_NL`: 18.92 GB
  * `Q3_K_M`: 19.82 GB
  * `Q2_K`: 18.91 GB
- **Alternative GGUF Artifact (Unsloth)**:
  * `NVIDIA-Nemotron-3.5-Lightning-30B-A3B-UD-Q4_K_S.gguf`: **24.47 GB** (retained as distinct alternative)

## 3. Hardware Deployments & 98K Memory Limit
- **Single RTX 3090 / 3090 Ti 24GB**:
  * Standard Q4_K_S weights require **23.20 GB**, leaving almost no room on a single 24GB card for long contexts.
  * `IQ4_NL` (18.92 GB) runs smoothly on single 24GB cards at **~68.2 tok/s** (exceptionally high throughput due to only 3B active params).
  * **98,304 tokens scaling**: Because Mamba-2 layers maintain a fixed-size recurrent state, memory does not explode quadratically. Total state + sparse KV cache at 98k is **~4.5 GB** -> **27.7 GB total VRAM with Q4_K_S (OOM on 1x 24GB, FITS with IQ4_NL at 23.4 GB total or Dual 3090)**.
- **Dual RTX 3090 (2x24GB = 48GB)**:
  * Runs Q5_K_M or Q8_0 at **~75.0 tok/s** with support for deep 262k contexts.

## 4. Evidence Classification
- Architecture and weights: `reported_official` / Hugging Face model tree.
- Hardware measurements: `reported_community_reproducible` (llama.cpp community benchmarks).
- 98K context scaling: `estimated` based on hybrid Mamba-2 state space + sparse attention formula.
