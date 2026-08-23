# Consolidated Cohort Cross-Model Matrix (Issues #36–#45)

## Executive Summary

1. **Which models fit on a single 24GB GPU (e.g. RTX 3090 / 3090 Ti)?**
   - **All 10 models fit** in Q4_K_S (or UD-Q4_K_S) quantization at standard short context (4k-8k tokens).
   - Weights footprint ranges from **11.62 GB** (OpenAI gpt-oss-20b) to **23.20 GB** (Nemotron 3.5 Lightning).

2. **Which models support 98,304 Context + Q8 KV Cache on a single 24GB GPU?**
   - **FITS on 24GB**:
     - **Qwen3 30B A3B Instruct**: Weights 17.46GB + Q8 KV 4.83GB = **22.29GB** (Fits with 1.7GB margin)
     - **Qwen3 Coder 30B A3B Instruct**: Weights 17.46GB + Q8 KV 4.83GB = **22.29GB** (Fits with 1.7GB margin)
     - **OpenAI gpt-oss-20b**: Weights 11.62GB + Q8 KV 4.02GB = **15.64GB** (Fits with 8.36GB margin)
   - **FITS on 24GB with Q4 KV Cache** (OOM with Q8 KV):
     - **Qwen3.8 27B xhigh**: Weights 15.36GB + Q4 KV 6.64GB = **22.00GB** (Fits with 2.0GB margin)
     - **Mistral Small 3.1 24B**: Weights 13.55GB + Q4 KV 5.63GB = **19.18GB** (Fits with 4.82GB margin)
   - **REQUIRES Dual GPU (2x24GB) or 48GB+ GPU for 98k**:
     - **Qwen3 32B Instruct** (Dense): Q8 KV = 12.88GB, Total = 31.65GB (OOM)
     - **Qwen2.5 32B Instruct** (Dense): Q8 KV = 12.88GB, Total = 31.66GB (OOM)
     - **DeepSeek R1 Distill Qwen 32B** (Dense): Q8 KV = 12.88GB, Total = 31.66GB (OOM)
     - **Gemma 3 27B Instruct** (Dense): Q8 KV = 24.36GB (16 heads!), Total = 40.03GB (OOM)
     - **Nemotron 3.5 Lightning** (Hybrid): Weights 23.20GB + State 4.5GB = 27.70GB (OOM on Q4_K_S, fits with IQ4_NL at 23.4GB)

3. **Reported Generation Speed (tok/s) on Single RTX 3090 (24GB):**
   - **MoE Models (3-3.6B active params)**:
     - **Nemotron 3.5 Lightning**: **~68.2 tok/s** (Fastest overall hybrid architecture)
     - **OpenAI gpt-oss-20b**: **~65.4 tok/s** (Fastest pure MoE)
     - **Qwen3 Coder 30B A3B**: **~58.0 tok/s**
     - **Qwen3 30B A3B Instruct**: **~55.0 tok/s**
   - **Dense Models (24-32.5B active params)**:
     - **Qwen3.8 27B**: **~30.0 tok/s** baseline, **~60.0 tok/s** with MTP speculative draft decoding
     - **Mistral Small 3.1 24B**: **~33.2 tok/s** (Fastest dense standard generation)
     - **Gemma 3 27B**: **~28.5 tok/s**
     - **Qwen2.5 32B Instruct**: **~24.5 tok/s**
     - **DeepSeek R1 Distill Qwen 32B**: **~23.8 tok/s** (effective answer latency 2x-5x longer due to reasoning tokens)
     - **Qwen3 32B Instruct**: **~23.5 tok/s**

4. **Missing Data Requiring Local Benchmarking:**
   - Locally measured hardware numbers on `ozryzen` workstation testbed.
   - Exact TTFT under concurrent batch loading.
   - Long-term thermal stability and power draw metrics under 1 hour continuous load.
