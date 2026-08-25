---
source_url: https://unsloth.ai/blog/mistral-small-3.1
slug: mistral-small-3.1
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: mistral-small-3.1

Blog

# Fine-tune & Run Mistral Small 3.1

## Mar 17, 2025 • By Daniel & Michael

## Mar 17, 2025

## •

## By Daniel & Michael

Mistral Small 3.1 (2503) is Mistral's new multimodal model that supports both text and vision understanding and 128K context length. At 24B parameters, Mistral Small 3.1 surpasses GP4o on multiple benchmarks.

- Mistral Small 3.1 (2503) is now supported!

- Mistral Small 3.1 (2503) is directly supported in Unsloth so you can fine-tune the model if you have at least 18GB of VRAM

- Unsloth makes Mistral Small 3.1 (2503) finetuning 1.8x faster, use 70% less VRAM, and enables 10x longer than environments with Flash Attention 2 on a 48GB GPU.

- We uploaded all versions of Mistral Small 3.1 + 3 including 2-8 bit GGUFs, dynamic 4-bit, and 16-bit versions, on Hugging Face here.✨Mistral Small 3.1 Fine-tuningMistral Small 3.1 + 3 finetuning fits with Unsloth in under 18GB of VRAM! It’s also 1.8x faster, and default uses Unsloth dynamic 4-bit quants for superior accuracy! You can also use Mistral Small 3 (2501) directly with Unsloth's GRPO to train your own reasoning model.To fine-tune the model on Colab/Kaggle or locally, use our basic Mistral v0.3 Instruct (7B)notebook, then simply change the model name to coressponding Mistral Small 3 (2501) model which we uploaded here. Keep in my this will not fit on a free Colab T4 16GB VRAM GPU so you will need to use a paid L4 instance.To view all our notebooks and model uploads, please visit our documentation.

## Performance benchmarks

ModelVRAM🦥Unsloth speed🦥 VRAM reduction🦥 Longer context🤗Hugging Face+FA2Mistral-Small-324GB1.8x>70%10xlonger1xWe tested using the Alpaca  Dataset, a batch size of 2, gradient accumulation steps of 4, rank = 32, and applied QLoRA on all linear layers (q, k, v, o, gate, up, down).💕 Thank you! A huge thank you to the Mistral team for their support and everyone for using & sharing Unsloth - we really appreciate it. 🙏As always, be sure to join our Reddit page and Discord server for help or just to show your support! You can also follow us on Twitter and join our newsletter.Thank you for reading!Daniel & Michael Han 🦥17 Mar 2025

## Fine-tune Gemma 3 for free now!

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
