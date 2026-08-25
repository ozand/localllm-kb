---
source_url: https://unsloth.ai/blog/qwen3
slug: qwen3
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: qwen3

Blog

# Fine-tune & Run Qwen3

## May 2, 2025 • By Daniel & Michael

## May 2, 2025

## •

## By Daniel & Michael

Qwen's new Qwen3 models delivery advancements in reasoning, instruction-following, agent capabilities, and multilingual support. Fine-tuning is now supported in Unsloth.All Qwen3 uploads use our new Unsloth Dynamic 2.0 methodology, delivering the best performance on 5-shot MMLU and KL Divergence benchmarks. This means, you can run and fine-tune quantized Qwen3 LLMs with minimal accuracy loss!We also uploaded Qwen3 with native 128K context length. Qwen achieves this by using YaRN to extend its original 40K window to 128K.

- Qwen3 (14B) Fine-tuning notebook out now! Colab notebook

- Unsloth makes Qwen3 (8B) finetuning 2x faster, use 70% less VRAM, and enables 8x longer than all environments with Flash Attention 2. Qwen3-30B-A3B comfortably fits on 17.5GB of VRAM with Unsloth.

- We uploaded all versions of Qwen3, including Dynamic 2.0 GGUFs, dynamic 4-bit and more on Hugging Face here.

- Read our guide on How to correctly Run Qwen3 here.Unsloth supports EVERYTHING* including: full fine-tuning, 8-bit, pretraining, ALL transformer-style models (Phi-4 reasoning, Mixtral, MOE, Cohere etc.) and ANY training algorithms like GRPO with VLMs.Also big thanks to the Qwen team for collabing and supporting us!✨Qwen3 Fine-tuningSupport for Qwen3 MOE models including 30B-A3B and 235B-A22B also work.View our Qwen3 Alpaca notebook.Ensure you use the latest pip version of Unsloth. To update use:`pip install --upgrade --force-reinstall --no-cache-dir unsloth unsloth_zoo`

## Performance benchmarks

ModelVRAM🦥Unsloth speed🦥 VRAM reduction🦥 Longer context🤗Hugging Face+FA2Qwen3-30B24GB2x>70%8xlonger1xWe tested using the Alpaca  Dataset, a batch size of 2, gradient accumulation steps of 4, rank = 32, and applied QLoRA on all linear layers (q, k, v, o, gate, up, down).💕 Thank you! A huge thank you to the Qwen team for their support, Datta for helping us with Qwen3 implementation. And of course everyone for using & sharing Unsloth - we really appreciate it. 🙏As always, be sure to join our Reddit page and Discord server for help or just to show your support! You can also follow us on Twitter and join our newsletter.Thank you for reading!Daniel & Michael Han 🦥2 May 2025

## Fine-tune Qwen for free now!

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
