# Evidence Inventory & Deep Research Receipt: Qwen3.8 27B (xhigh)

## Scope and Intent

Comprehensive deep practical research into local deployment, hardware configurations, quantization choices, context limits, reasoning effort, and real-world community observations for **Qwen3.8 27B (xhigh)**.

- Issue: **#45**
- Target model: `Qwen3.8 27B` (dense 27.0B, multimodal Qwen3.5 architecture)
- Producer canonical ID: `qwen/qwen3.8-27b`
- Consumer candidate ID: `alibaba/qwen3-8-27b` (owned by ai-dashboards-kb)
- Artificial Analysis alias: `artificial-analysis/qwen3-8-27b`

---

## 1. Quantization and Artifact Inventory

| Quantization | Filename | Size (Bytes) | LFS SHA-256 | Availability Status | Notes |
|---|---|---|---|---|---|
| BF16 (split) | `BF16/Qwen3.8-27B-BF16-00001-of-00002.gguf + 00002` | 54,657,735,616 | `b9966e82...` | Available | Full-precision reference |
| Q8_0 | `Qwen3.8-27B-Q8_0.gguf` | 29,047,086,048 | `a680f44a...` | Available | Fits 32GB+ VRAM |
| UD-Q6_K | `Qwen3.8-27B-UD-Q6_K.gguf` | 21,983,677,344 | `c9c20681...` | Available | Unsloth Dynamic Q6 |
| UD-Q5_K_M | `Qwen3.8-27B-UD-Q5_K_M.gguf` | 19,771,509,664 | `2de73110...` | Available | High quality 24GB fit |
| UD-Q4_K_M | `Qwen3.8-27B-UD-Q4_K_M.gguf` | 16,464,440,224 | `322e194f...` | Available | Recommended 24GB quant |
| **Q4_K_S (Standard)** | `null` | `null` | `null` | **Unavailable** | Standard target missing upstream |
| **UD-Q4_K_S** | `Qwen3.8-27B-UD-Q4_K_S.gguf` | 15,358,213,024 | `75bc9c8a...` | Available | **Distinct dynamic alternative** |
| Q4_0 | `Qwen3.8-27B-Q4_0.gguf` | 16,056,478,688 | `ede16c7b...` | Available | Standard baseline |
| UD-IQ3_S | `Qwen3.8-27B-UD-IQ3_S.gguf` | 12,040,883,104 | `d847e2c1...` | Available | Fits 16GB VRAM |

---

## 2. Hardware Deployment Evidence

### Evidence 1: Single RTX 3090 24GB + MTP Drafter (llama.cpp)
- **Source**: https://www.reddit.com/r/LocalLLaMA/comments/1vti5kt/dual_rtx_3090_qwen3827b_help/
- **Hardware**: 1x NVIDIA GeForce RTX 3090 24GB
- **Runtime**: `llama-server` with `--spec-type draft-mtp --spec-draft-n-max 3 --spec-draft-p-min 0.8 -ngl 999 -c 262144 -ctk q4_0 -ctv q4_0 -fa on --reasoning-effort medium`
- **Artifact**: `Qwen3.8-27B-UD-Q4_K_S.gguf` (15.35 GB)
- **Observations**:
  - Baseline decoding: ~30 tok/s.
  - With MTP draft tuning (`--spec-draft-p-min 0.8`): **60 tok/s**.
  - Deep context (160k tokens): drops to **~20 tok/s**.
  - Draft acceptance rate reported at 88%.
- **Evidence Quality**: `reported_community_reproducible`

### Evidence 2: Dual RTX 3090 (2x24GB) Tensor Parallel (Unsloth Studio)
- **Source**: https://www.reddit.com/r/LocalLLaMA/comments/1v66pa2/what_would_you_run_on_2_rtx_3090s_today/
- **Hardware**: 2x NVIDIA GeForce RTX 3090 (44-48GB combined VRAM)
- **Runtime**: Unsloth Studio with tensor parallel distribution
- **Artifact**: `Qwen3.8-27B-UD-Q6_K.gguf` (21.98 GB)
- **Observations**:
  - Stable generation at **~60 tok/s** with **179,000 context**.
  - Allows running heavier Q6_K quant without OOM.
- **Evidence Quality**: `reported_community_partial`

### Evidence 3: RTX PRO 6000 48GB + DFlash 2 Drafter (llama.cpp PR)
- **Source**: https://www.reddit.com/r/LocalLLaMA/comments/1vvncyh/i_benchmark_dflash_2_pr_build_in_llamacpp_on_qwen/
- **Hardware**: 1x NVIDIA RTX PRO 6000 48GB
- **Runtime**: llama.cpp DFlash 2 PR build
- **Artifact**: Qwen3.8 27B
- **Observations**:
  - Baseline LiveCodeBench: 67.97 tok/s.
  - DFlash 2 alone: **153.6 tok/s (2.26x speedup)**.
  - DFlash 2 + n-gram drafter: **up to 4.68x speedup**.
- **Evidence Quality**: `reported_community_reproducible`

### Evidence 4: RTX 5060 Ti 16GB Agentic Coding (llama.cpp)
- **Source**: https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/
- **Hardware**: 1x NVIDIA GeForce RTX 5060 Ti 16GB + Intel N100 + 32GB RAM
- **Runtime**: llama.cpp with `draft-mtp + n-gram mod`, `-ctk q4_0 -ctv q4_0`
- **Artifact**: `Qwen3.8-27B-UD-IQ3_S.gguf` (12.04 GB)
- **Observations**:
  - Runs with **73,000 context** fitting inside 16GB VRAM.
  - Used for large multi-step agentic coding tasks.
- **Evidence Quality**: `reported_community_partial`

---

## 3. Context and Memory Scaling Matrix

For 64 layers, 8 KV heads, 128 head_dim:
- FP16 KV per token: `2 * 64 * 8 * 128 * 2 = 262,144 bytes = 256 KB/token`.
- Q8_0 KV per token: `~128 KB/token`.
- Q4_0 KV per token: `~64 KB/token`.

| Context Length | KV Quantization | KV VRAM (GB) | Model (UD-Q4_K_S) VRAM | Total VRAM (GB) | 24GB Fit? | Outcome |
|---|---|---|---|---|---|---|
| 4,096 | FP16 | 1.05 | 15.35 | 16.8 | **Yes** | Fast, default buffers |
| 32,768 | Q4_0 | 2.05 | 15.35 | 17.8 | **Yes** | Standard coding context |
| **98,304** | **Q8_0** | **12.29** | 15.35 | **28.2** | **No (OOM)** | **Target causes OOM on single 24GB**; requires dual GPU or Q4 KV |
| 98,304 | Q4_0 | 6.14 | 15.35 | 22.0 | **Yes** | Fits 24GB with ~2GB headroom |
| 160,000 | Q4_0 | 10.00 | 15.35 | 25.8 | Tight/OOM | Needs minimal batch or dual 3090 |
| 262,144 | Q4_0 | 16.38 | 15.35 | 32.5 | **No** | Requires 48GB (Dual 3090/A6000) |

---

## 4. Reasoning Effort & Multimodal Boundaries

- **Reasoning Effort**: `low`, `medium`, `high`, `xhigh`.
  - `xhigh` increases chain-of-thought token count significantly for hard logic/architecture tasks.
  - Per-token speed is unchanged; total latency scales with generated reasoning tokens.
- **Multimodal Artifacts**:
  - `mmproj-BF16.gguf` (931 MB) and `mmproj-F16.gguf` (927 MB) are separate visual projectors.
  - Pure text GGUF does not require mmproj.
  - Multimodal performance is not evaluated in text-only coding benchmarks.

---

## 5. Unresolved Local Measurements

The following remain explicitly `null` / `unknown`:
1. Locally measured performance on testbed `ozryzen` (RTX 3090 Ti 24GB);
2. Standard `Q4_K_S` evaluation (upstream artifact missing);
3. Official long-run power/thermal stability metrics;
4. Multimodal vision projector throughput.
