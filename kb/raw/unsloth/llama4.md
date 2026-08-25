---
source_url: https://unsloth.ai/blog/llama4
slug: llama4
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: llama4

Blog

# Fine-tune & Run Llama 4

## Apr 7, 2025 • By Daniel & Michael

## Apr 7, 2025

## •

## By Daniel & Michael

Meta's new Llama 4 models can now be fine-tuned & run with using Unsloth.Llama 4 Scout (17B, 16 experts) is the best model for its size with a 10M context window.Llama 4 Maverick (17B, 128 experts) surpasses GPT-4o % rivals DeepSeek v3 in reasoning and coding.

- Read our Guide on How To Run Llama 4 here

- Unsloth makes Llama-4-Scout (109B) training work with 71GB VRAM. Unsloth is the only framework that supports QLoRA 4-bit training of Llama 4. Scout will fit on a single H100 80GB VRAM GPU.

- Unsloth makes Llama 4 finetuning 1.5x faster, use 50% less VRAM, and enables 8x longer context lengths than environments with Flash Attention 2.

- We uploaded Llama 4 including dynamic GGUF, dynamic 4-bit & 16-bit versions, on Hugging Face here. The 16-bit & FP8 versions run anywhere (e.g., vLLM), but 4-bit & 8-bit only work on Unsloth for training and inference.Unsloth now also supports EVERYTHING* including: full fine-tuning, 8-bit, pretraining, ALL transformer-style models (Mixtral, MOE, Cohere etc.) and ANY training algorithms like GRPO with VLMs.

## Performance benchmarks

ModelVRAM🦥Unsloth speed🦥 VRAM reduction🦥 Longer context🤗Hugging Face+FA2Llama 4 Scout80GB1.5x>50%8xlongerOOMWe tested Llama-4-Scout-Instruct on a 80GB A100 and did 4bit QLoRA on all linear layers (Q, K, V, O, gate, up and down) with rank = 32 with a batch size of 1. We padded all sequences to a certain maximum sequence length to mimic long context finetuning workloads.QLoRA fine-tuning for Llama 4 Scout in 4-bit precision is currently only supported by 🦥Unsloth. All other frameworks, do not yet support 4-bit finetuning for Llama 4, resulting in significantly higher VRAM usage (300GB+), often causing out-of-memory (OOM) errors.To ensure a fair comparison, we benchmarked Llama 4 Scout with LoRA instead of QLoRA across all platforms. Otherwise, Unsloth would appear to use up to 400% less VRAM due to proper QLoRA support.💕 Thank you! A huge thank you to everyone for using & sharing Unsloth - we really appreciate it. And of course thank you to Meta who built the models.🙏As always, be sure to join our Reddit page and Discord server for help or just to show your support! You can also follow us on Twitter and join our newsletter.Thank you for reading!Daniel & Michael Han 🦥7 Apr 2025

## Fine-tune Llama 4 for free now!

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
