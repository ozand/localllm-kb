---
id: LLM-KB-PROCEDURES-MULTI-NODE-RPC
title: "Multi-node distributed inference with llama.cpp RPC and vLLM"
category: procedures
tags: [rpc, clustering, multi_node, llamacpp, vllm, tensor_split]
status: active
created: 2026-08-25
updated: 2026-08-25
environment:
  os: linux, macos, windows
  shell: bash
  tools: [llama.cpp, rpc-server, vllm, ray]
error_signatures:
  - "rpc-server connection refused"
  - "network bandwidth bottleneck on 1GbE"
  - "CUDA / Metal tensor parallel mismatch"
---

# Multi-Node Distributed Inference with llama.cpp RPC & vLLM

Running large frontier models (such as Qwen 3.8 27B, Qwen3 32B, Llama 70B, or MiniMax-M2) across multiple independent physical machines allows pooling VRAM (e.g. 16GB Mac Metal + 12GB Nvidia PC = 28GB total pool) without buying high-end datacenter GPUs.

## 1. llama.cpp RPC Architecture

llama.cpp provides a lightweight Remote Procedure Call (`rpc-server`) daemon that exposes local GPU/VRAM to a central master node over TCP/IP:

```
[ Worker 1 (Mac Metal 16GB) ] <--- TCP:50052 --- [ Master Node (Nvidia 12GB) ]
[ Worker 2 (AMD / Strix Halo) ] <-- TCP:50053 ---/
```

### Worker Daemon Setup (RPC Server)
On each remote worker node, launch the `rpc-server` bound to local GPU memory:
```bash
# On Worker (IP: 192.168.1.50)
./rpc-server -p 50052 -H 0.0.0.0 --device 0
```

### Master Inference Command
On the primary master node, specify remote RPC servers and the VRAM memory split across nodes:
```bash
llama-server   -m models/qwen3.8-27b-ud-q4_k_s.gguf   --rpc 192.168.1.50:50052,192.168.1.51:50053   --tensor-split 12,16   -c 32768   -ngl 99   --port 8080
```

## 2. Bandwidth & Network Latency Constraints

| Network Interface | Raw Bandwidth | Generation Latency Impact | Optimal Use Case |
|---|---|---|---|
| **1 Gbps Ethernet** | ~110 MB/s | High (Prompt eval takes 4-8s; tok/s drops 40-60%) | Emergency offload only |
| **2.5 Gbps Ethernet** | ~280 MB/s | Moderate (~15-22 tok/s on 27B-32B dense models) | Recommended baseline for home lab |
| **10 Gbps SFP+ / Thunderbolt** | ~1.1 GB/s | Minimal (<5% penalty vs PCIe Gen4) | Near-native multi-GPU performance |

### Key Rule for Layer Sharding vs Tensor Parallel:
- **Layer-wise pipeline sharding** sends activations between nodes only once per layer boundary $	o$ Works smoothly over 2.5GbE.
- **Tensor Parallel (TP)** requires all-reduce communication on *every attention layer* $	o$ Requires minimum 10GbE / Thunderbolt or Ray/vLLM with high-bandwidth interconnects.

## 3. vLLM Multi-Node (Ray-based Distributed Serving)

For high-throughput concurrent agent traffic, vLLM supports multi-node Ray clusters:

```bash
# On Head Node
ray start --head --port=6379

# On Worker Node
ray start --address='192.168.1.100:6379'

# Launch vLLM Master
vllm serve Qwen/Qwen2.5-32B-Instruct --tensor-parallel-size 2 --pipeline-parallel-size 2
```

## 4. Operational Checklist & Verification

1. Verify worker firewalls allow incoming TCP connections on RPC ports (default 50052).
2. Measure latency with `ping` (<0.5ms on local switched LAN is required).
3. Ensure GGUF model files exist only on the master node (RPC transfers layer weights dynamically to worker VRAM on startup).
