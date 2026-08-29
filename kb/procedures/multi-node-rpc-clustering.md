---
id: LLM-KB-PROCEDURES-MULTI-NODE-RPC
title: "Multi-node distributed inference with llama.cpp RPC and vLLM"
category: procedures
tags: [rpc, clustering, multi_node, llamacpp, vllm, tensor_split]
status: active
created: 2026-08-25
updated: 2026-08-29
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

This procedure describes a possible multi-node deployment pattern. The hardware capacities and performance figures below are reported or illustrative values, not universal guarantees. See the [multi-node RPC research receipt](../receipts/multi-node-rpc-receipt.md) and the originating [Issue #86](https://github.com/ozand/localllm-kb/issues/86) for provenance and limitations.

Running a model across multiple independent physical machines may pool available device memory, but actual feasibility and performance depend on the model, artifact, runtime version, backend, topology, interconnect, context, workload, and placement. Values such as `16GB + 12GB = 28GB` are illustrative only; exact usable memory and throughput are `unknown` unless measured for the stated configuration.

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

The table below retains the existing reported values with evidence status `reported_community_partial` / illustrative guidance. They are not measurements from a single controlled comparison. Hardware, protocol overhead, message sizes, runtime version, model, context, workload, and measurement method are `unknown` unless explicitly stated in the linked receipt.

| Network Interface | Raw Bandwidth | Generation Latency Impact | Optimal Use Case |
|---|---|---|---|
| **1 Gbps Ethernet** | ~110 MB/s | Reported high impact; the cited 4–8s prompt-evaluation and 40–60% tok/s reduction are unverified here | Reported emergency-offload scenario |
| **2.5 Gbps Ethernet** | ~280 MB/s | Reported moderate impact; the cited ~15–22 tok/s on 27B–32B dense models is unverified here | Reported home-lab baseline, not a guarantee |
| **10 Gbps SFP+ / Thunderbolt** | ~1.1 GB/s | Reported low impact; the cited <5% PCIe Gen4 penalty is unverified here | Reported near-native scenario, not a guarantee |

### Layer Sharding vs Tensor Parallel: bounded guidance
- **Layer-wise pipeline sharding** can send activations between nodes at layer boundaries. The statement that it “works smoothly over 2.5GbE” is reported guidance, not a universal result; validate it for the specific topology and workload.
- **Tensor Parallel (TP)** commonly requires frequent collective communication, including all-reduce operations. The statement that it “requires minimum 10GbE / Thunderbolt” is a reported rule of thumb, not a validated threshold for every model or runtime. Treat the required interconnect and resulting penalty as `unknown` until measured.

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
2. Measure latency with `ping`; the earlier `<0.5ms` value is a reported target, not a universal requirement. Record the actual topology and measurement conditions before using it as a gate.
3. Ensure GGUF model files exist only on the master node when using the documented RPC workflow; the receipt records this as a reported behavior and runtime/version-specific details remain `unknown`.
