---
source_url: https://unsloth.ai/blog/dynamic-v2
slug: dynamic-v2
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: dynamic-v2

Unsloth Dynamic v2.0 GGUFs

unsloth

ModelsBlogUnsloth Desktop✨Docs

Download

☰

ModelsBlogUnsloth DesktopDocumentation

Download

Blog

# Unsloth Dynamic 2.0 GGUFs

## Apr 24, 2025 • By Daniel & Michael

## Apr 24, 2025

## •

## By Daniel & Michael

We're excited to introduce our Dynamic v2.0 quantization method - a major upgrade to our previous quants. This new method outperforms leading quantization methods and sets new benchmarks for 5-shot MMLU and KL Divergence.This means you can now run + fine-tune quantized LLMs while preserving as much accuracy as possible! You can run the v2.0 GGUFs on any inference engine like llama.cpp, Ollama, Open WebUI etc.View our Dynamic v2.0 GGUFs here.

## 🦥 What's New in Dynamic 2.0?

- Revamped Layer Selection for GGUFs + safe tensors: Unsloth Dynamic 2.0 now selectively quantizes layers much more intelligently and extensively. Rather than modifying only select layers, we now dynamically adjust the quantization type of every possible layer, and the combinations will differ for each layer and model.

- Current selected and all future GGUF uploads will utilize Dynamic 2.0 and our new calibration dataset. The dataset ranges from 300K to 1.5M tokens (depending on model) and comprise of high-quality, hand-curated and cleaned data - to greatly enhance conversational chat performance.

- Previously, our Dynamic quantization (DeepSeek-R1 1.58-bit GGUF) was effective only for MoE architectures. Dynamic 2.0 quantization now works on all models (including MoEs).

- Model-Specific Quants:  Each model now uses a custom-tailored quantization scheme. E.g. the layers quantized in Gemma 3 differ significantly from those in Llama 4.To ensure accurate benchmarking, we built an internal evaluation framework to match official reported 5-shot MMLU scores of Llama 4 and Gemma 3. This allowed apples-to-apples comparisons between full-precision vs. Dynamic v2.0, QAT and standard imatrix GGUF quants.Our Dynamic 2.0 GGUF models are now live on Hugging Face here. Updated quantized versions are available for: DeepSeek-R1 + DeepSeek-V3-0324 + Gemma 3 (12B & 27B) + Llama 4 (Scout).📊 Benchmarking and EvaluationThis is a high-level summary; analysis further below or you can read our detailed analysis in our docs.We benchmarked Dynamic 2.0 against our earlier Dynamic method, and other popular quantization methods like standard imatrix using 5-shot MMLU tests on models like Google's new Gemma 3 QAT quants (12B & 27B) and Llama 4 (Scout).Before testing quantized models, we first evaluated unquantized versions of Gemma 3 and Llama 4 using many open-source frameworks. All failed to reproduce the reported MMLU scores (78.6 for Gemma 3, 79.6 for Llama 4), so we needed to build our own evaluation framework. After building our own evaluation framework for more reliable and standardized testing, we were able to match the reported scores within 0.1 points.With the validated evaluation framework, we were then allowed to conduct correct 5-shot MMLU benchmarks which is a time intensive but effective LLM accuracy/performance metric. While metrics like KL Divergence and Perplexity are useful, they’re not ideal at all for accuracy testing.Our results show Dynamic 2.0 consistently outperforms other quantization methods in accuracy, efficiency, and consistency.

## ⚖️ Calibration Dataset Overfitting

Most frameworks report perplexity and KL Divergence using a test set of Wikipedia articles. However, we noticed using the calibration dataset which is also Wikipedia related causes quants to overfit, and attain lower perplexity scores. We utilize Calibration_v3 and Calibration_v5 datasets for fair testing which includes some wikitext data amongst other data. Also instruct models have unique chat templates, and using text only calibration datasets is not effective for instruct models (base models yes). In fact most imatrix GGUFs are typically calibrated with these issues. As a result, they naturally perform better on KL Divergence benchmarks that also use Wikipedia data, since the model is essentially optimized for that domain.To ensure a fair and controlled evaluation, we do not to use our own calibration dataset (which is optimized for chat performance) when benchmarking KL Divergence. Instead, we conducted tests using the same standard Wikipedia datasets, allowing us to directly compare the performance of our Dynamic 2.0 method against the baseline imatrix approach.🔢MMLU Replication AdventureReplicating MMLU 5 shot was extremely nightmarish. We could not replicate MMLU results for many models including Llama 3.1 8B Instruct, Gemma 3 12B and others due to subtle implementation issues. Llama 3.1 8B for example should be getting ~68.2%, whilst using incorrect implementations can attain 35% accuracy.Llama 3.1 8B Instruct has a MMLU 5 shot accuracy of 67.8% using a naive MMLU implementation. We find however Llama tokenizes "A" and "_A" (A with a space in front) as different token ids. If we consider both spaced and non spaced tokens, we get 68.2%(+0.4%)Interestingly Llama 3 as per Eleuther AI's LLM Harness also appends "The best answer is" to the question, following Llama 3's original MMLU benchmarks.There are many other subtle issues, and so to benchmark everything in a controlled environment, we designed our own MMLU implementation from scratch by investigating github.com/hendrycks/test directly, and verified our results across multiple models and comparing to reported numbers.✨Gemma 3 QAT Replication, BenchmarksThe Gemma team released two QAT (quantization aware training) versions of Gemma 3:

- Q4_0 GGUF - Quantizes all layers to Q4_0 via the formula w = q * block_scale with each block having 32 weights. See llama.cpp wiki for more details.

- int4 version - presumably TorchAO int4 style?We benchmarked all Q4_0 GGUF versions, and did extensive experiments on the 12B model. We see the 12B Q4_0 QAT model gets 67.07% whilst the full bfloat16 12B version gets 67.15% on 5 shot MMLU. That's very impressive!

| Metric

| 1B

| 4B

| 12B

| 27B

| MMLU 5 shot

| 26.12%

| 55.13%

67.07%

(67.15% BF16)

| 70.64%  (71.5% BF16)

| Disk Space

| 0.93 GB

| 2.94 GB

| 7.52 GB

| 16.05 GB

| Efficiency*

| 1.20

| 10.26

| 5.59

| 2.84

We designed a new Efficiency metric which calculates the usefulness of the model whilst also taking into account its disk size and MMLU 5 shot score:

Efficiency =

MMLU 5 shot score

−

25

Disk Space GB

We have to minus 25 since MMLU has 4 multiple choices - A, B, C or D. Assume we make a model that simply randomly chooses answers - it'll get 25% accuracy, and have a disk space of a few bytes. But clearly this is not a useful model.On KL Divergence vs the base model, below is a table showcasing the improvements. Reminder the closer the KL Divergence is to 0, the better (ie 0 means identical to the full precision model)

| Quant

| Baseline KLD

| Baseline GB

| New KLD

| New GB

| IQ1_S

| 1.035688

| 5.83

| 0.972932

| 6.06

| IQ1_M

| 0.832252

| 6.33

| 0.800049

| 6.51

| IQ2_XXS

| 0.535764

| 7.16

| 0.521039

| 7.31

| IQ2_M

| 0.265540

| 8.84

| 0.258192

| 8.96

| Q2_K_XL

| 0.229671

| 9.78

| 0.220937

| 9.95

| Q3_K_XL

| 0.087845

| 12.51

| 0.080617

| 12.76

| Q4_K_XL

| 0.024916

| 15.41

| 0.023701

| 15.64

If we plot the ratio of the disk space increase and the KL Divergence ratio change, we can see a much clearer benefit! Our dynamic 2bit Q2_K_XL reduces KLD quite a bit (around 7.5%).🦙 Llama 4 Bug FixesFor Llama’s largest vision model, we see some spikes, but not that much. The cross attention phenomena from the 11B model seems to be much less pronounced.

- Llama 4 Scout changed the RoPE Scaling configuration in their official repo. We helped resolve issues in llama.cpp to enable this change

- Llama 4's QK Norm's epsilon for both Scout and Maverick should be from the config file - this means using 1e-05 and not 1e-06. We helped resolve these in llama.cpp and transformers

- The Llama 4 team and vLLM also independently fixed an issue with QK Norm being shared across all heads (should not be so) here. MMLU Pro increased from 68.58% to 71.53% accuracy.

- Wolfram Ravenwolf showcased how our GGUFs via llama.cpp attain much higher accuracy than third party inference providers - this was most likely a combination of the issues explained above, and also probably due to quantization issues.💕 Thank you for reading!As usual, a huge thank you to everyone for using & sharing Unsloth - we really appreciate it. 🙏Be sure to join our Reddit page and our Discord server for help or just to show your support! You can also follow us on Twitter and join our newsletter.Daniel & Michael Han 🦥24 Apr 2025

## Multimodal fine-tuning

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
