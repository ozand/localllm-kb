---
source_url: https://unsloth.ai/blog/llama3-1
slug: llama3-1
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: llama3-1

Blog

# Finetune & Run Llama 3.1 with Unsloth

## Jul 23, 2024 • By Daniel & Michael

## Jul 23, 2024

## •

## By Daniel & Michael

Llama 3.1 (8B)1xL4 24GB210%fasterLlama 3.1 (8B)1xL4 24GB-60%VRAMLlama 3.1 (70B)1xA100 80GB190%fasterLlama 3.1 (70B)1xA100 80GB-65%VRAMMeta's update to their Llama 3 models makes them the most advanced models to date. Llama 3.1 was trained on 15.6T tokens, expands context lengths to 128K and now supports new languages. Unsloth makes Llama 3.1 (8B) finetuning 2.1x faster and use 60% less memory than Flash Attention 2 (FA2) + Hugging Face (HF). Llama 3.1 (70B) is 1.9x faster and uses 65% less VRAM.We uploaded a Google Colab notebook to finetune Llama 3.1 (8B) on a free Tesla T4: Llama 3.1 (8B) Notebook. We also have a new UI on Google Colab for chatting with your Llama 3.1 Instruct models which uses our own 2x faster inference engine. Unsloth provides 6x longer context length for Llama 3.1 training. On 1xA100 80GB GPU, Llama 3.1 (70B) with Unsloth can fit 48K total tokens (8192 * bsz of 5) vs 7K tokens without Unsloth.We also uploaded pre-quantized 4bit models for 4x faster downloading to our Hugging Face page which includes Llama 3.1 Instruct (8B, 70B and 405B) and Base (8B, 70B and 405B) in 4bit bnb form.💎Introducing Unsloth Run UIWe created a new chat UI using Gradio where users can upload and chat with their Llama 3.1 Instruct models online for free on Google Colab. The chat UI is a work in progress and we will add support for all models later. It's entirely powered by our own inference engine which provides 2x faster inference than Hugging Face.This release will just be a taste of what's to expect for Unsloth Studio (Beta), our upcoming fine-tuning UI.🦙 Llama 3.1 BenchmarksModelVRAM🦥Unsloth speed🦥 VRAM reduction🦥 Longer context🤗Hugging Face+FA2Llama 3.1 (8B)24GB2.1x60%3x longer1xLlama 3.1 (70B)80GB1.9x65%6x longer1xWe tested using the Alpaca  Dataset, a batch size of 2, gradient accumulation steps of 4, rank = 32, and applied QLoRA on all linear layers (q, k, v, o, gate, up, down).🧶 6x longer context lengthsUnsloth significantly enhances long context support for Llama 3.1 (70B), fitting it on a 48GB GPU and enabling fine-tuning on ~7K context lengths. In comparison, HF + FA2 can only handle lengths of 2 or even out-of-memory (OOM) errors. Meta’s update increases context lengths to 128K but requires more VRAM.With 80GB VRAM, Unsloth supports 6x longer context lengths with just a +1.9% overhead, allowing fine-tuning on 48K sequence lengths versus 7.5K lengths. Experimental data shows Unsloth’s clear advantage over HF + FA2 for long context fine-tuning.

## Llama 3.1 (70B) max. context length

GPU VRAMUnslothHugging Face+FA248 GB7,698OOM80 GB48,0537,433In all our experiments, we used QLoRA with a rank of 32 and applied LoRA adapters to all linear linears (q, k, v, o, gate, up, down). We used a batch size of 1, and repeated data to make it fit to the maximum context window.🦙 Llama 3.1 (8B) finetuning fits in 8GBUsing a batch size of 1 and a LoRA rank of 32 on all linear layers, HF + FA2 fails or runs out of memory (OOM) on 8GB GPU cards, needing around 9GB of memory. In contrast, Unsloth comfortably supports 2K context lengths on the same 8GB cards. On a 24GB consumer card, Unsloth allows for 20K context lengths, which is 3.5 times longer than HF + FA2.Below shows the VRAM consumption vs context lengths tested on a L4 GPU via Colab:

## Llama 3.1 (8B) max. context length

GPU VRAMUnslothHugging Face+FA28 GB1,983OOM12 GB6,6381,04416 GB11,2922,66324 GB20,6015,90140 GB39,21912,37748 GB48,52815,61580 GB85,76528,567🔎 Llama 3.1 AnalysisThough the architecture from Llama 3 mostly remains the same, there are some key differences. All 3.1 model outputs can now be used to train other models, not just Llama and the 3.1 models now use fp8 precision. Here is our tweet and a list of our findings:

- New RoPE extension methodUses an interesting low and high scaling factor, and scales the inv_freq vector - can be computed in 1 go, so no need for dynamic re computation. Used a 6 stage ramping up approach from 8K tokens to 128K tokens with 800B tokens.

- Training bfloat1638% to 43% MFU using bfloat16. Pipeline parallelism used + FSDP. Model averaging for RM, SFT & DPO stages.

-  Data mixture50% general knowledge25% maths & reasoning17% code data and tasks8% multilingual data

-

- Preprocessing stepsUses Roberta, DistilRoberta, fasttext to filter out good quality data. Lots of de-duplication and heuristics to remove bad data.

-  Float8 quantizationQuantizes weights to fp8 and input to fp8, then multiplies by scaling factors. fp8 x fp8 then output is bf16. Faster for inference & less VRAM use.

-

- Vision & Speech ExperimentsThe Llama 3.1 team also trained vision & speech adapters - not released though, but very cool!💕 Thank you! Meta released an article by Mark Zuckerberg addressing the importance of open-source: "We need to train, fine-tune, and distill our own models. Every organization has different needs that are best met with models of different sizes that are trained or fine-tuned with their specific data. On-device tasks and classification tasks require small models, while more complicated tasks require larger models. Now you’ll be able to take the most advanced Llama models, continue training them with your own data and then distill them down to a model of your optimal size – without us or anyone else seeing your data." So a big thank you to the Meta team as always for supporting open-source!Feel free to support us via our Ko-fi donation page. Huge shout out to: Marshall from NASA, Anthony, John, Pichet & Steven who are new supporters! 🙏As always, be sure to join our Discord server for help or just to show your support! You can also follow us on Twitter and Substack.Thank you for reading!Daniel & Michael Han 🦥23 July 2024

## Unsloth Studio next

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
