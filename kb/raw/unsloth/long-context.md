---
source_url: https://unsloth.ai/blog/long-context
slug: long-context
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: long-context

Unsloth Gradient Checkpointing - 4x longer context windows

unsloth

ModelsBlogUnsloth Desktop✨Docs

Download

☰

ModelsBlogUnsloth DesktopDocumentation

Download

Blog

# Unsloth Gradient Checkpointing - 4x longer context windows

## Apr 9, 2024 •  By Daniel & Michael

## Apr 9, 2024

## •

## By Daniel & Mike

We are excited to introduce 'Unsloth Gradient Checkpointing', a new algorithm that enables fine-tuning LLMs with exceptionally long context windows. On NVIDIA H100 80GB GPUs, it supports context lengths of up to 228K tokens - 4x longer than 48K for Hugging Face (HF) + Flash Attention 2 (FA2). On RTX 4090 24GB GPUs, Unsloth enables context lengths of 56K tokens, 4x more HF+FA2 (14K tokens).Unsloth Gradient Checkpointing reduces memory usage by a further 30% at the cost of +1.9% extra time overhead, making fine-tuning of LLMs with transformers on long contexts much more efficient.

- Unsloth Gradient Checkpointing works on all model architectures which use gradient checkpointing (ie stable diffusion, Mamba etc)

- We have a Colab notebook for Tesla T4 training on 16K sequence lengths using Mistral 7b v2 (new Mistral 7b model trained on long sequence lengths) + ChatML here!

- Below shows our maximum context calculation of Mistral 7b on each popular GPU variant using a batch size of 1 and with 4bit QLoRA. We used a lora rank of 32 with adamw_8bit.Numbers are extrapolated based on experiments, so set the context window 10% less due to VRAM fragmentation. Also you can 1.7x your batch size now as well as another benefit!

- PS Don't forget to ⭐Star us on Github and join our Discord server ❤️

## Maximum context window benchmarks

GPUVRAMUnsloth(New)Unsloth(Old)Hugging Face+FA2RTX 40608 GB7,3403,7161,696RTX 407012 GB19,61011,0554,797RTX 408016 GB31,88018,3947,898RTX 409024 GB56,42033,07314,099A10040 GB105,50062,43126,502A600048 GB130,04077,11032,704H10080 GB228,199135,82657,510💡 The DetailsHow did we do it? We asynchronously offload activations to system RAM using our own gradient checkpointing in pure Pytorch code (only 20 lines of code). We were very surprised it incurred a +1.9% ish extra overhead, primarily since we smartly hide the communication from GPU to CPU with non blocking calls during the forward and backward passes.The expectation was that offloading would make things grind to a halt, but our experiments show otherwise. Native Hugging Face without Flash Attention 2 makes VRAM usage scale quadratically, being only able to do 5K context windows on Mistral 7b on a L4 GPU. With FA2, around 14K is possible (2.8x).Also now linear VRAM scaling is seen since FA2 never forms the full attention matrix. Unsloth's previous version allowed 33K context windows (2.4x), and our new version allows 56K context windows (1.7x). This means for Mistral 7b, Unsloth fits 4x longer context windows than HF+FA2, and a whopping 11.2x than native HF.To enable long context window finetuning, first set the maximum sequence length. You can use our table for Mistral 7b above, and try to reduce it by 10% or so. Don’t forget to update Unsloth if you’re on a local machine. On Colab / Kaggle, no need to update!🖥️ 2.4x faster CodeGemma 7b + 71% less memoryGoogle released their new CodeGemma models today! CodeGemma is built on top of Gemma 2b and 7b, but finetuning an extra 500B of code data on top of Gemma 7b’s 6 trillion token dataset.We uploaded 4bit pre-quantized models for CodeGemma, allowing you to download them 4x faster and save 1GB of VRAM due to reduced GPU fragmentation. We uploaded them on our HF page. You can also use our CodeGemma 7b + the ChatML template Colab notebook.Gemma 7b1x A100243%fasterGemma 7b1x A100-71%VRAMGemma 2b1xA100200%fasterGemma 2b1xA100-68%VRAM❤️‍🩹Self Healing TokenizersWe managed to smartly and on the fly convert a slow HF tokenizer to a fast one. We also automatically now load the tokenizer, and fix some dangling incorrect tokens. What can this be useful for?

- 1. Broken tokenizers like Starling or CodeLlama can be “self healed” to work. Not healing them can cause unlucky out of bounds memory accesses.

- 2. No need to manually edit the tokenizer files to support the ChatML format. Sloth automatically edits the sentencepiece tokenizer.model and other files.

- 3. Sometimes model uploaders require you to use the slow tokenizer, due to the fast tokenizer (HF’s Rust version) giving wrong results. We try to convert it to a fast variant, and confirm if it tokenizes correctly.Reminder we also support all Chat Templates seamlessly with Unsloth (Vicuna, ChatML, Zephyr etc). You can see here for more details or use our ChatML notebook. 🧶28% Faster RoPE EmbeddingsHuyNguyen-hust managed to make Unsloth RoPE Embeddings around 28% faster! This primarily is useful for long context windows. Via torch profiler, Unsloth's original kernel made RoPE use up less than 2% of total runtime, so you will see maybe 0.5 to 1% speedups especially for large training runs. Any speedup is vastly welcome!⚡More 4x faster downloading 4bit pre-quantized modelsWe uploaded more 4 bit models (4x faster downloading + 1GB less VRAM use). If you have any other requests, ask about it on our Discord or file a Github issue!

- CodeGemma 2b and 7b

- The newly released Gemma 1.1 instruct for 2b and 7b

- Mistral’s new retrained 7b v2 for long contexts

- Teknium’s Open Hermes 2.5

- Starling Beta

- Nous Research’s Hermes Pro🐛Notable bug fixes

- Gemma would not convert to GGUF correctly due to tied weights. Now fixed.

- Merging to 16bit on Kaggle breaks since Kaggle only supports 20GB of disk space - we smartly delete the 4GB model.safetensors file, allowing you to merge to 16bit.

- Inference is finally fixed on batched generation. We did not accidentally account for the attention mask and position ids. Reminder inference is 2x faster natively!

- Fine-tuning on lm_head and embed_tokens now works correctly! Remember to set modules_to_save.🔮Future updates

- We’re working on an automatic model optimizer. Large requests from the community include Mixtral, Command R, DBRX, and more, and the goal is to automatically optimize models using our kernels. It’ll be like torch.compile, except using our kernels.

- We’re working on a Colab enhanced 1 click finetuning system, hopefully making it simpler for people to use Unsloth.💕Support us! Feel free to support us via our Ko-fi donation page. Huge shout out to: Roman, Henrik, Rajesh, 007ok, Netrve, Goblin, pacozaa,  Datta Nimmaturi, Hamel Husain, Ratish, Chris, Steffen, Remek, Anthony, Richard, Chrismcmaster, Trelis Research, preemware and Nam who are new supporters! 🙏As always, be sure to join our Discord server for help or just to show your support! You can also follow us on Twitter and Substack.Thank you for reading!Daniel & Michael Han 🦥9 April 2024

## Unsloth Studio loading...

Start for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
