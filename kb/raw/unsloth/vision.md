---
source_url: https://unsloth.ai/blog/vision
slug: vision
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: vision

Blog

# Llama 3.2 Vision fine-tuning

## Nov 21, 2024 • By Daniel & Michael

## Nov 21, 2024

## •

## By Daniel & Michael

Vision/multimodal models are now supported in Unsloth including Meta's Llama 3.2 (11B + 90B) models. Unsloth makes Vision finetuning 1.5-2x faster and use up to 70% less memory than Flash Attention 2 (FA2) + Hugging Face (HF), and can do 4-8x longer context lengths.We uploaded Google Colab notebooks to finetune on a free Tesla T4 with different use cases (just change the model name to your desired one):

- Llama 3.2 Vision (11B)  - Radiography use case: Colab • Kaggle

- Qwen 2 VL (7B)  - Maths OCR to LaTeX: Colab • Kaggle

- Mistral - Pixtral (12B) 2409 - General QA datasets: ColabWe also uploaded all Vision models including Llama 3.2 Vision, Llava, Pixtral and Qwen2 VL in original 16bit and pre-quantized 4bit (for 4x faster downloading) to Hugging Face. Don't forget to follow us on Hugging Face to stay updated whenever we upload new models! Currently only Instruct versions of VLMs work but we are working on supporting base versions as well.Dec 24 Update: QvQ (72B), Qwen's new o1-like vision model is now supported. See the QvQ collection.See here for all our model uploads. Step by step tutorials coming soon on our documentation site!👁️ Fixing Vision BugsBefore releasing support for any models, we prioritize ensuring everything is accurate and functions the way it is supposed to. During the process, we identified and resolved numerous issues, such as bugs in chat templates, memory usage issues and more.For example, we found issues in Pixtral's Hugging Face chat template and SDPA support for Pixtral to reduce VRAM usage. Pixtral finetuning also fits in a 16GB GPU, but it took some tweaks to make it work. We also patched other models with full gradient checkpointing support, reducing VRAM usage from >20GB to just 5GB. And there are many other bug fixes! Use Unsloth to achieve optimal results with vision fine-tuning.💡 Vision fine-tuning detailsFine-tuning vision models has numerous use cases across various industries, enabling models to adapt to specific tasks and datasets. We provided 3 examples for vision finetuning.1. Llama 3.2 Vision finetuning for radiography -  how can we assist medical professionals in analyzing Xrays, CT Scans & ultrasounds faster.2. Qwen 2 VL finetuning for converting handwriting to LaTeX - this allows complex maths formulas to be easily transcribed as LaTeX without manually writing it.3. Pixtral 12B vision finetuning for general Q&A - one can concatenate general Q&A datasets with more niche datasets to make the finetune not forget base model skills.To finetune vision models, we now allow you to select which parts of the mode to finetune. You can select to only finetune the vision layers, or the language layers, or the attention / MLP layers! We set them all on by default!🌟 Qwen 2.5 + CoderQwen 2.5 and Qwen 2.5 Coder models are now supported. We also found and fixed some bugs. We uploaded  Google Colab notebooks to finetune on a free Tesla T4:

- Qwen 2.5 Coder (14B)

- Qwen 2.5 (7B)Original models only have 32K context lengths. Qwen uses YaRN to extend it to 128K from 32B. We uploaded native 128K GGUFs and made an entire collection of the Qwen 2.5 models to Hugging Face.💕 Thank you! As usual, a huge thank you to everyone for using & sharing Unsloth - we really appreciate it. Also a huge shout out to: Jeffrey, kaeru39 and Uday who are new supporters! 🙏Be sure to join our Reddit page and our Discord server for help or just to show your support! You can also follow us on Twitter and join our newsletter.Thank you for reading!Daniel & Michael Han 🦥21 Nov 2024

## Multimodal fine-tuning

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
