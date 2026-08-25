---
source_url: https://unsloth.ai/blog/qwen-coder
slug: qwen-coder
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: qwen-coder

Blog

# Qwen 2.5 Coder Fine-tuning

## Nov 13, 2024 • By Daniel & Michael

## Nov 13, 2024

## •

## By Daniel & Michael

Qwen 2.5 and Qwen 2.5 Coder models are now supported. Unsloth makes Qwen 2.5 finetuning 2x faster and use 60% less memory than Flash Attention 2 (FA2) + Hugging Face (HF).We uploaded  Google Colab notebooks to finetune on a free Tesla T4:

- Qwen 2.5 Coder (14B)

- Qwen 2.5 (7B)Original models only have 32K context lengths. Qwen uses YaRN to extend it to 128K from 32B. We uploaded native 128K GGUFs and made an entire collection of the Qwen 2.5 models to Hugging Face. UPDATE: 13th Nov 2024 - Fixed GGUF YaRNs - should all now work!See here for all our model uploads.✍️ Qwen 2.5 AnalysisWe also found and some bugs for the Qwen 2.5 models. You can see our tweet for more details:

- `Pad_token` for should NOT be `<|endoftext|>` You will get infinite generations when finetuning. We uploaded fixes to Hugging Face

-  Base model `<|im_start|> <|im_end|>` tokens are untrained. Do NOT use them for the chat template if finetuning or doing inference on the base model.If you do a PCA on the embeddings between the Base (left) and Instruct (right) versions, you first see the BPE hierarchy, but also how the <|im_start|> and <|im_end|> tokens are untrained in the base model, but move apart in the instruct model.💕 Thank you! As usual, a huge thank you to everyone for using & sharing Unsloth - we really appreciate it.As always, be sure to join our Discord server for help or just to show your support! You can also follow us on Twitter and Substack.Thank you for reading!Daniel & Michael Han 🦥13 Nov 2024

## Multimodal fine-tuning

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
