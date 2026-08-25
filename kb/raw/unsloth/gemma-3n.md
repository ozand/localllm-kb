---
source_url: https://unsloth.ai/blog/gemma-3n
slug: gemma-3n
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: gemma-3n

Blog

# Fine-tune & Run Gemma 3n

## Jul 1, 2025 • By Daniel & Michael

## Jul 1, 2025

## •

## By Daniel & Michael

Gemma 3n are Google's new multimodal (text, vision & audio) models. Available in 2B and 4B sizes, Gemma 3n has a 32K context window, multilingual support and is now supported in Unsloth.

- Fine-tune Gemma-3n-E2B for free using our Colab notebook.

- Unsloth is the only framework that supports inference and training for Gemma 3n on f16 GPUs.

- We uploaded all versions of Gemma 3n, including Dynamic GGUFs, 4-bit, and 16-bit versions, on Hugging Face here. Currently GGUFs only support text.

- Read our detailed guide on How to Run & Fine-tune Gemma 3n here.A big thank you to the Gemma team for their support! It was also wonderful meeting you all at our Gemma Developer Meetup with Google!✨Gemma 3n Fixes

## ♾️Infinities and NaN gradients and activations

Gemma 3n, like Gemma 3, has issues running on FP16 GPUs (e.g., Tesla T4s in Colab). For Gemma 3, we found that activations exceed float16's maximum range of 65504. Gemma 3N removed the activation issue, but instead we still encountered infinities!We instead plotted the absolute maximum weight entries for Gemma 3N, and we see the below:We note that the green crosses are convolutional weights. You can see the magnitude is much larger than other weights. And if we inspect the activations, they go to infinity!Below is a table for Conv2D weights which have large magnitudes. Essentially during a Conv2D operation, large weights multiply and sum together, and unluckily exceed float16's maximum range of 65504. Bfloat16 is fine, since it's maximum range is 10^38.

| Name

| Value

| msfa.ffn.pw_proj.conv.weight

| 98.000000

| blocks.2.21.attn.key.down_conv.weight

| 37.000000

| blocks.2.32.pw_exp.conv.weight

| 34.750000

| blocks.2.30.pw_exp.conv.weight

| 33.750000

| blocks.2.34.pw_exp.conv.weight

| 33.750000

The solution is to upcast all Conv2D weights to float32 on float16 machines! But this uses more VRAM, so instead we use autocasting to on the fly upcast weights and input matrices to float32, and do accumulations in float32.Unsloth is the only framework that enables Gemma 3n inference and training on float16 GPUs, so Colab Notebooks with free Tesla T4s work!

## 🏁Gradient Checkpointing issues

We found Gemma 3N's vision encoder is unique since it re-uses hidden states. This unfortunately limits the usage of gradient checkpointing, so memory usage is a bit more than usual.However, we still managed to leverage Unsloth's automatic compiler to optimize Gemma 3N!

## 🦙 GGUF issues + fixes:

Thanks to discussions from from the Ollama team and also Nguyen from Hugging Face, there were 2 issues specifically for GGUFs:1. The add_shared_kv_layers was accidentally encoded in float32 which is fine, but is slightly complicated to decode from Ollama's side - a simple change to uint32 solves the issue.2. The per_layer_token_embd should be Q8_0 in precision. Anything lower seems to not function properly and errors out in the Ollama engine - to reduce issues for our community, we made this all Q8_0 in all quants - unfortunately this does use more space.As an update, Matt mentioned we can also use Q4_0, Q4_1, Q5_0, Q5_1 for the embeddings - and we confirmed it can also work in Ollama! This means once again the smaller 2, 3 and 4bit quants are smaller in size, and don't need Q8_0!

## 🌵 Large losses during finetuning:

We also found losses are interestingly very large during finetuning - in the range of 6 to 7, but they do shrink over time quickly. We theorize this is either because of 2 possibiltiies:1. There might be some implementation issue, but this is unlikely since inference seems to work well.2. Multimodal models always seem to exhibit this behivour - we found Llama 3.2 Vision's loss starts at 3 or 4, Pixtral at 8 or so, and Qwen 2.5 VL also 4 ish. Because Gemma 3N includes audio as well, it might amplify the starting loss. But this is just a hypothesis. We also found quantizing Qwen 2.5 VL 72B Instruct to have extremely high perpelxity scores of around 30 or so, but the model seems to work fine.✨Gemma 3n Fine-tuningGemma 3n, like Gemma 3, had issues running on F16 GPUs such as Tesla T4s in Colab. Essentially you will get NaNs and infinities if you did not patch it for inference or finetuning.We found a simple workaround was to upcast all convolutional layers in the vision encoder to float32, which increased VRAM usage. To reduce memory usage, we simply used autocasting, which left the Conv layers in float16, and only upcasted to float32 during the matrix multiply itself.Because Gemma 3n's unique architecture reuses hidden states in the vision encoder, Unsloth's Gradient Checkpointing algorithm (which drastically reduces VRAM use) can't be applied to the vision encoder, however we still applied our automatic compiler optimizations.Unsloth is the only framework which works in float16 machines for Gemma 3n inference and training. This means Colab Notebooks with free Tesla T4 GPUs also work!Gemma 3n-E4B  finetuning fits with Unsloth in under 12GB of VRAM! It’s also 1.6x faster, and default uses Unsloth dynamic 4-bit quants for superior accuracy! Technically you can We also heard a lot of you asking for a Gemma 3 (4B) Vision notebooks so you can try it now in our free Google Colab Notebook here.

## Performance benchmarks

ModelVRAM🦥Unsloth speed🦥 VRAM reduction🦥 Longer context🤗Hugging Face+FA2Gemma-3n-E4B24GB1.5x>50%5xlonger1xWe tested using the Alpaca  Dataset, a batch size of 2, gradient accumulation steps of 4, rank = 32, and applied QLoRA on all linear layers (q, k, v, o, gate, up, down).🔮 Gemma 3n Analysis

Here's an in depth analysis for Gemma 3n's MatFormer architecture:So what is so special about Gemma 3n you ask? It is based on Matryoshka Transformer or MatFormer architecture meaning that each transformer layer/block embeds/nests FFNs of progressively smaller sizes. Think of it like progressively smaller cups put inside one another. The training is done so that at inference time you can choose the size you want and get the most of the performance of the bigger models.There is also Per Layer Embedding which can be cached to reduce memory usage at inference time. So the 2B model (E2B) is a sub-network inside the 4B (aka 5.44B) model that is achieved by both Per Layer Embedding caching and skipping audio and vision components focusing solely on text.The MatFormer architecture, typically is trained with exponentially spaced sub-models aka of sizes S, S/2, S/4, S/8 etc in each of the layers. So at training time, inputs are randomly forwarded through one of the said sub blocks giving every sub block equal chance to learn. Now the advantage is, at inference time, if you want the model to be 1/4th of the original size, you can pick S/4 sized sub blocks in each layer.You can also choose to Mix and Match where you pick say, S/4 sized sub block of one layer, S/2 sized sub block of another layer and S/8 sized sub block of another layer. In fact, you can change the sub models you pick based on the input itself if you fancy so. Basically its like choose your own kind of structure at every layer. So by just training a model of one particular size, you are creating exponentially many models of smaller sizes. No learning goes waste. Pretty neat huh.

💕 Thank you! A huge thank you to the Google Gemma team for enabling us to have Day 0 support. Also thanks to everyone for using & sharing Unsloth - we really appreciate it. 🙏As always, be sure to join our Reddit page and Discord server for help or just to show your support! You can also follow us on Twitter and join our newsletter.Thank you for reading!Daniel & Michael Han 🦥1 Jul 2025

## Fine-tune Gemma 3n now!

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
