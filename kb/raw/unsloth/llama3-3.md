---
source_url: https://unsloth.ai/blog/llama3-3
slug: llama3-3
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: llama3-3

Blog

# Fine-tune Llama 3.3 with Unsloth

## Dec 10, 2024 • By Daniel & Michael

## Dec 10, 2024

## •

## By Daniel & Michael

Llama 3.3 (70B)1xA100 80GB13xlonger contextLlama 3.3 (70B)1xA100 80GB2xfasterLlama 3.3 (70B)1xA100 80GB>75%less VRAMMeta's new Llama 3.3 (70B) model delivers similar performance to Llama 3.1 (405B) and Unsloth makes Llama 3.3 (70B) fine-tuning 2x faster and use 70% less memory than Flash Attention 2 (FA2) + Hugging Face (HF). New: Unsloth can now fine-tune Llama 3.3 (70B) up to 89,000 context lengths, which is 13x longer than what HF + FA2 supports at 6,900 on a 80GB GPU. Unsloth's new ultra long context support is 1.85x longer than previous versions of Unsloth. It is powered by our gradient checkpointing algorithm and we collaborated with Apple to add their new Cut Cross Entropy (CCE) algorithm.Please note this new update works for all models, not just Llama. We also uploaded GGUFs + pre-quantized 4bit models for 4x faster downloading to our Hugging Face page.

- GGUF - Llama 3.3 (70B) Instruct

- BnB 4bit - Llama 3.3 (70B) Instruct

- Original 16bit - Llama 3.3 (70B) Instruct🦙 Llama 3.3 BenchmarksFor Llama 3.1 (8B), Unsloth can now do a whopping 342,000 context length, which exceeds the 128K context lengths Llama 3.1 supports. Hugging Face + FA2 can only do 28,000 on a 80GB GPU, so Unsloth supports 12x context lengths. HF+FA2 goes out of memory for 8GB GPUs, whilst Unsloth now supports up to 2,900 context lengths, up from 1,500.ModelVRAM🦥Unsloth speed🦥 VRAM reduction🦥 Longer context🤗Hugging Face+FA2Llama 3.3 (70B)80GB2x>75%13x longer1xLlama 3.1 (8B)80GB2x>70%12x longer1xWe tested using the Alpaca  Dataset, a batch size of 2, gradient accumulation steps of 4, rank = 32, and applied QLoRA on all linear layers (q, k, v, o, gate, up, down).🦙 Llama 3.3 (70B) finetuning fits in 41GB

## Llama 3.3 (70B) max. context length

GPU VRAMUnsloth(+ Apple CCE)Unsloth(Old)Hugging Face+FA248 GB12,1067,385OOM80 GB89,38948,4476,916We tested Llama 3.3 (70B) Instruct on a 80GB A100 and did 4bit QLoRA on all linear layers (Q, K, V, O, gate, up and down) with rank = 32 with a batch size of 1. We padded all sequences to a certain maximum sequence length to mimic long context finetuning workloads. Apple Cut Cross EntropyWe collabed with the author's of Apple’s Cut Cross Entropy including Erik to bring a memory efficient cross entropy kernel written in Triton into Unsloth. We also made it work for older GPUs like Tesla T4 and the RTX 20 series. You can read their paper here. By not materializing the logits, but rather doing the matrix multiplications on the fly (like in Flash Attention), memory usage is vastly reduced. By also smartly ignoring extremely small numbers during the gradient calculation without affecting accuracy, performance can also be improved.CCE further increases long context support by another 3.6x for Llama 3.1 (8B) and 1.85x for Llama 3.3 (70B) Instruct. So in total, by multiplying the benefits of Unsloth Gradient Checkpointing and also Cut Cross Entropy, we have Unsloth’s new version to have 12-13x longer context length support than HF+FA2!To leverage long context finetuning for Llama 3.3 70B, you can download our 4bit pre-quantized bitsandbytes versions to reduce VRAM fragmentation and allow 4x faster downloads here.🦥 Unsloth Gradient Checkpointing In April 2024, we introduced our smart Unsloth Gradient Checkpointing algorithm which smartly offloads activations to system RAM with a tiny performance overhead. You can read our past blog post here about it here.Our method allows context lengths to be 7x longer than HF+FA2 for Llama 3.3 (70B) Instruct, and 3.3x longer for Llama 3.1 (8B). We continue leveraging this for extreme long context finetuning.💾 System RAM usageJust a reminder you will need a bit more system RAM since Unsloth smartly offloads activations to system RAM!For Llama 3.3 (70B) Instruct, we see it has 80 hidden layers and a hidden size of 8192. This means 89,000 sequence lengths will need at least 89,000 x 80 x 8192 x 2 bytes = 109GB of system RAM.For Llama 3.1 (8B), it has 32 hidden layers and a hidden size of 4096. 128K context lengths will need 32GB of system RAM. The maximum context length of 342,000 with Unsloth will need 84GB of system RAM.🦙 Llama 3.1 (8B) benchmarks We tested Llama 3.1 (8B) Instruct and did 4bit QLoRA on all linear layers (Q, K, V, O, gate, up and down) with rank = 32 with a batch size of 1. We padded all sequences to a certain maximum sequence length to mimic long context finetuning workloads.

## Llama 3.1 (8B) max. context length

GPU VRAMUnsloth(+ Apple CCE)Unsloth(Old)Hugging Face+FA28 GB2,9721,586OOM12 GB21,8486,74493216 GB40,72411,9032,55124 GB78,47522,2205,78940 GB153,97742,85512,26448 GB191,72853,17315,50280 GB342,73394,44228,454💕 Thank you! As usual, a huge thank you to everyone for using & sharing Unsloth - we really appreciate it. 🙏 We would like to thank Apple's team including: Erik Wijmans, Brody Huval, Alexander Hertzberg, Vladlen Koltun, and Philipp Kr. for their research and Erik for their help.As always, be sure to join our Reddit page and Discord server for help or just to show your support! You can also follow us on Twitter and Substack.Thank you for reading!Daniel & Michael Han 🦥10 Dec 2024

## Fine-tune Vision models now!

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
