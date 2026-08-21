# Raw Capture: Reddit r/LocalLLaMA Community Benchmarks & VRAM Tuning for 27B-32B Models

- Source: Reddit r/LocalLLaMA (`/r/LocalLLaMA/comments/1kfvba4/`, `/r/LocalLLaMA/comments/1jgdb4a/`, `/r/LocalLLaMA/comments/1j5kdcm/`)
- Date Captured: 2026-04-18
- Topic: VRAM requirements, KV cache quantization, offloading strategies, and LiteLLM/Aider integration on 24GB GPUs (RTX 3090 / 3090 Ti)

## Key Takeaways from Community Experience

### 1. VRAM Budgets on Single 24GB GPU
- **Model Weights**: A 27B-32B model at `UD-Q4_K_S` / `Q4_K_M` takes ~16.5–18.2 GB of VRAM.
- **Headroom on 24GB GPU**: Leaves ~5.8–7.5 GB for KV cache and CUDA runtime overhead.
- **KV Cache Impact**:
  - FP16 KV Cache: Consumes ~1.5–2.0 GB per 8k context on 32B models. At 32k context, FP16 KV alone consumes ~6–8 GB $\to$ triggers CUDA OOM on 24GB VRAM.
  - `q8_0` KV Cache: Halves memory requirement to ~0.8 GB per 8k context, enabling up to 64k-98k context fully in 24GB VRAM.
  - `q4_0` KV Cache: Reduces memory to ~0.4 GB per 8k context with minimal perplexity degradation, allowing >128k context without CPU offloading.

### 2. Offloading with High System RAM (128GB DDR4 + Ryzen 5950X)
- When expanding to full 262k context, KV cache and additional model layers can be partially offloaded to system RAM (`--numa`, `--threads 16`).
- CPU offloading on Ryzen 9 5950X handles prefill efficiently over PCIe Gen 4, while generation speed drops if compute layers are split across PCIe, but remains stable if only excess KV context spills into system RAM.

### 3. LiteLLM & Agent Tool Calling Pitfalls
- **Endpoint differences**: Aider / Pi agent tools interact via `/v1/chat/completions`. When using LiteLLM proxy with local models, passing raw OpenAI formatting without mapping `thinking` tags can cause tool calls to fail if thinking tokens are placed in content rather than parsed.
- **Server-side default locking**: Launching llama.cpp / unsloth server with locked sampling parameters (temp 1.0 / top_p 0.95 for thinking, temp 0.7 for non-thinking) provides the most consistent agent behavior across diverse clients.
