---
source_url: https://unsloth.ai/blog/dynamic-4bit
slug: dynamic-4bit
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: dynamic-4bit

Unsloth - Dynamic 4-bit Quantization

unsloth

ModelsBlogUnsloth Desktop✨Docs

Download

☰

ModelsBlogUnsloth DesktopDocumentation

Download

Blog

# Unsloth - Dynamic 4-bit Quantization

## Dec 4, 2024 • By Daniel & Michael

## Dec 4, 2024

## •

## By Daniel & Michael

Can we shrink a 20GB language model to just 5GB without sacrificing accuracy? Enter quantization! Popular algorithms like AWQ, Bitsandbytes, GPTQ, and HQQ aim to compress models, but naive quantization often hurts accuracy, making models unusable.We’re excited to introduce Unsloth - Dynamic 4-bit Quantization, which involves dynamically opting not to quantize certain parameters and this builds on top of BitsandBytes 4-bit. This approach delivers significant accuracy gains while only using <10% more VRAM than BnB 4-bit.January, 2025 Update: A great example of our dynamic quants' effectiveness is our recent dynamic quants for Microsoft's Phi-4. We fixed bugs in Phi-4 and submitted our dynamic 4-bit quants to Hugging Face's OpenLLM Leaderboard. Our dynamic 4-bit model scored nearly as high as our 16-bit version—and well above standard Bnb 4-bit and Microsoft's official 16-bit model, especially for MMLU.We’ve uploaded vision models on Hugging Face, including Llama 3.2 Vision, quantized with our new method under the names 'unsloth-bnb-4bit' here. Text based models like Llama 3.1 (8B) are also uploaded  We also have a Colab notebook fine-tuning Llama 3.2 (11B) Vision with our new dynamic quantization method here.Our tests below show that standard 4-bit quantization performed worse than original 16-bit, while Unsloth’s dynamic 4-bit quantization provided very accurate and reliable results.💔 Quantizing can break modelsUnsloth by default utilizes the gold standard Bitsandbytes for all linear layers. For example, Llama 3.2 Vision (11B) uses 20GB in full precision but just 6.5GB with nf4—a 68% reduction.For example, quantizing Qwen2 Vision (2B) down to 4bits breaks the model entirely. Anecdotal evidence suggests smaller models to only use 6 to 8 bit quantization, and larger models like 8B and larger to use 4 bit quantization.

| Qwen2-VL-2B-Instruct

| Description

| Size

| Result

| 16bit

| The image shows a train traveling on tracks.

| 4.11GB

| ✅

| Default 4bit all layers

| The image depicts a vibrant and colorful scene of a coastal area.

| 1.36GB

| ❌

| Unsloth quant

| The image shows a train traveling on tracks.

| 1.81GB

| ✅

For example, quantizing all layers to 4bit will make the model describe the image above as “a vibrant and colorful scene of a coastal area” which is wrong. By carefully selecting not to quantize some parameters, the model recovers its accuracy and performs similarly to its full precision format with an extra 450MB in memory usage. Full precision uses 4.11GB.Most vision models have a linear projection, so if we also turn off quantizing all intermediate linear projections, we see the model is still broken.

| Qwen2 VL (2B) Instruct

| Description

| Size

| Result

| Except linear layers

| The image depicts a vibrant and colorful scene of a coastal area during a sunny day.

| 4.11GB

| ❌

| Unsloth quant

| The image shows a train traveling on tracks.

| 1.81GB

| ✅

On error analysis, we see Qwen2 VL 2B Instruct has large activation quantization errors (left plot) in the first few layers. There is also a large spike, and a gradual decrease in activation errors. We also see 1 parameter having a large weight quantization error.We uploaded our dynamically 4bit quantized model for Qwen2 VL:

- Qwen 2.5 VL (2B) Instruct)

- Qwen 2.5 VL (7B) Instruct🦙 Llama 3.2 Vision subtletiesLlama 3.2 11B Vision is much less sensitive to quantization. So the goal is to match 16 bit precision as much as possible.

| Llama-3.2-Vision-11B-Instruct

| Description

| Size

| Result

| 16bit

| The image depicts a serene scene of a wooden bench situated near a body of water, with a group of birds perched on the backrest. The purpose of the image appears to be capturing a peaceful moment in nature.

| 19.87GB

| ✅

| Default 4bit all layers

| The image depicts a serene scene featuring a wooden bench with a row of small birds perched on its backrest, set against the backdrop of a body of water. The bench, made of light-colored wood, has a horizontal slat design and is positioned at an angle, facing the water.

| 6.54GB

| 🆗 No mention of the purpose of the image

| Unsloth quant

| The image depicts a serene scene featuring a wooden bench with a row of small birds perched on its backrest, set against the backdrop of a body of water. The purpose of the image appears to be capturing a peaceful moment in nature.

| 7.23GB

| ✅Purpose of image returns

Interestingly 4bit quantization removes the sentence describing the image’s purpose. Unsloth's dynamic quantization uses a bit more memory, but again returns the image’s purpose back!Llama’s error plots looks quite interesting! The vision encoder does not seem to have extremely large errors, except for 1 large spike. The weight quantization errors seem quite interesting! We find the cross attention’s output projection on all layers except the first should all not be quantized.Our dynamically 4bit quantized models for Llama 3.2 (11B) Vision:

- Llama 3.2 (11B) Vision Instruct

- Llama 3.2 (11B) Vision BasePixtral (12B) VisionPixtral was the most interesting to analyse! The weight quantization errors took relatively tame, albeit with 1 large spike. The activation errors are very interesting! We see the entire vision encoder should not be quantized to 4bit, since it’ll cause large differences.The most interesting thing is if we use our dynamic quantization approach, it does make the model much better, but it still weirdly does not match 16bit full precision. If we loosen the constraint and capture all “bad” modules, we then recover the full capability of the model!Below you can see the 4bit version does OK, but the 16bit version analyses the X-ray much more. Our dynamic quantization uses 400MB more, but actually starts analysing the X-ray unlike a full 4bit model. If we use 3.5GB more (that’s quite a lot), we then fully mimic full 16bits of precision!We also compare 8bit which uses 1GB more, and it interestingly looks similar to 4bit, so 8bit does not seem to do well. This does require more investigation though!

| Pixtral-12B

| Description

| Size

| Result

| 16bit

The image is a dental X-ray (radiograph) of a child's mouth, showing the arrangement of teeth and jaw structure. The X-ray highlights several key features:

1. **Upper Arrows**: These arrows point to the upper jaw area, likely indicating the presence of unerupted or impacted teeth, which are teeth that have not erupted through the gums but are trapped beneath the surface.

| 26.32GB

| ✅

| Default 4bit all layers

This is a dental X-ray image of a child's mouth, highlighting several teeth with arrows. The image shows the positions of different types of teeth: primary (baby teeth), secondary (adult teeth), and tertiary (permanent teeth). The primary teeth are already fallen, the secondary teeth are coming out, and the tertiary teeth have not yet come out.

| 7.83GB

| 🆗 No mention of arrows’ purpose. No detailed analysis.

| Unsloth quant

| This is an X-ray image of a child's mouth, highlighting several teeth with arrows. The image shows the arrangement and presence of primary (baby) teeth and permanent teeth. The arrows are pointing to specific teeth that may require attention, possibly for removal or other dental treatment.

| 8.42GB

| 🆗 Much better - analyses the X-ray more.

| 8bit quant

| The image is a dental X-ray of a child's mouth, highlighting specific areas with arrows. The X-ray shows the arrangement and development of the child's teeth and jaw structure. The arrows likely indicate areas of concern or interest, such as potential issues with tooth alignment, decay, or other dental problems.

| 13.1GB

| 🆗Also better than full 4bit - analysis the X-ray.

🦙 Llama 3.2 (90B) Vision InstructFor Llama’s largest vision model, we see some spikes, but not that much. The cross attention phenomena from the 11B model seems to be much less pronounced.💕 Thank you for reading!As usual, a huge thank you to everyone for using & sharing Unsloth - we really appreciate it. And thank you so much David for the support! 🙏Be sure to join our Reddit page and our Discord server for help or just to show your support! You can also follow us on Twitter and join our newsletter.Daniel & Michael Han 🦥4 Dec 2024

## Multimodal fine-tuning

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
