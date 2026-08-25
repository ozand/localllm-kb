---
source_url: https://unsloth.ai/blog/deepseekr1-dynamic
slug: deepseekr1-dynamic
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: deepseekr1-dynamic

Blog

# Run DeepSeek R1Dynamic 1.58-bit

## Jan 27, 2025 • By Daniel & Michael

## Jan 27, 2025

## •

## By Daniel & Michael

DeepSeek-R1 has been making waves recently by rivaling OpenAI's O1 reasoning model while being fully open-source. We explored how to enable more local users to run it & managed to quantize DeepSeek’s R1 671B parameter model to 131GB in size, a 80% reduction in size from the original 720GB, whilst being very functional.By studying DeepSeek R1’s architecture, we managed to selectively quantize certain layers to higher bits (like 4bit) & leave most MoE layers (like those used in GPT-4) to 1.5bit. Naively quantizing all layers breaks the model entirely, causing endless loops & gibberish outputs. Our dynamic quants solves this - see our dynamic quants' impact and benchmarks on models like Phi-4 and Llama Vision here.For instructions on how to run the model see: Guide to Run R1.The 1.58bit quantization should fit in 160GB of VRAM for fast inference (2x H100 80GB), with it attaining around 140 tokens per second for throughput and 14 tokens/s for single user inference. You don't need VRAM (GPU) to run 1.58bit R1, just 20GB of RAM (CPU) will work however it will be very slow. For optimal performance, we recommend the sum of VRAM + RAM to be at least 80GB+.Feb 6, 2025 update: You can now train your own reasoning model like R1 using: GRPO + UnslothWe uploaded dynamic quantized versions ranging from 131GB to 212GB in size to: huggingface.co/unsloth/DeepSeek-R1-GGUFP.S. if you liked our work, feel free to ⭐Star us: github.com/unslothai/unsloth or follow us @UnslothAi 💖🦥 1. Dynamic Quantized versionsWe provide 4 dynamic quantized versions. The first 3 uses an importance matrix to calibrate the quantization process (imatrix via llama.cpp) to allow lower bit representations. The last 212GB version is a general 2bit quant with no calibration done.MoE BitsDisk SizeTypeQualityLinkDown_proj1.58-bit131GBIQ1_SFairLink2.06/1.56bit1.73-bit158GBIQ1_MGoodLink2.06bit2.22-bit183GBIQ2_XXSBetterLink2.5/2.06bit2.51-bit212GBQ2_K_XLBestLink3.5/2.5bitYou can view our full R1 collection of GGUF's including 4-bit, distilled versions & more: huggingface.co/collections/unsloth/deepseek-r1📊 2. Benchmarks and ablationsTo test all quantized models, instead of relying on general benchmarks, we instead ask DeepSeek r1 to create a Flappy Bird game with 3 tries (pass@3), and we score it on 10 criteria (like using random colors, random shapes, whether it can run in an Python interpreter). We used seed 3407, 3408 and 3409, and the suggested temperature of 0.6.On the left, we have an example of what chat.deepseek.com generated. On the right is the 1.58bit version.

## DeepSeek Original

## 1.58-bit Version

We see surprisingly that our dynamic 1.58bit version can still produce valid output even after reducing the model's size by 80%!However, if you DO NOT use our dynamic 1.58bit version and instead naively quantize all layers, you will get infinite repetitions like in seed 3407: “Colours with dark Colours with dark Colours with dark Colours with dark Colours with dark” or in seed 3408: “Set up the Pygame's Pygame display with a Pygame's Pygame's Pygame's Pygame's Pygame's Pygame's Pygame's Pygame's Pygame's”.Similarly, if you do not use our dynamic version, and instead quantize all layers to 1.75bits (149GB), infinite repetitions stop, but the result is totally incorrect. All output produces fully black screens. If you quantize all layers to even 2.06bits (175GB), the result is even worse than the 1.58bit (131GB) dynamic quant. You would rather use the 2.22bit (183GB) version which is superior in performance.The 1.58bit dynamic quants do sometimes rarely produce 1 incorrect token per 8000 tokens, which we need to comment out. Using min_p = 0.1  or 0.05 should mitigate the 1.58bit quant from generating singular incorrect tokens.For a summary for a score out of 10 and Pass@3, we find the 1.58bit 131GB version correctly scores 69.2% on our Flappy Bird benchmark, and the 2bit 183GB version scores 91.7%.The non dynamic quants on the other hand do terribly. Quantizing all layers to 1.58bits gets 0% on our benchmark, and even at 175Gb we get 61.7%, which is even lower than our dynamic quant (and is smaller!)

| Model Size

| Dynamic Quant

| Model Size

| Basic Quant

| 131GB

| 6.92

| 133GB

| 0

| 158GB

| 9.08

| 149GB

| 1.67

| 183GB

| 9.17

| 175GB

| 6.17

We provide more detailed results at the end of the blog post.🐋 3. Exploiting DeepSeek R1’s architectureIn our previous analysis of the DeepSeek V3 model, which used DeepSeek r1 for synthetic data generation, we noted that the first 3 layers of DeepSeek are fully dense, and not MoE. As a refresher, MoE (mixture of experts) layers allow us to increase the number of parameters in a model, without increasing the number of FLOPs used, since we dynamically mask most entries as 0, and so we essentially skip doing matrix multiples on the zeroed out entries.The goal of MoEs is to "trick" the scaling laws, since we increase the number of parameters without changing the compute cost. For more notes on MoEs and a new method called Memory Layers, which aims to do better than MoEs, see this tweet: x.com/danielhanchen/status/1868748998783517093By combining 4 ideas, including:

- Our 4-bit Dynamic Quantization method

- The 1.58-bit LLMs paper

- Llama.cpp’s 1.5-bit quantization

- The Super Weights paperWe managed to employ these insights:

- The first 3 dense layers use 0.5% of all weights. We’ll leave these as 4 or 6bit.

- MoE layers use shared experts, using 1.5% of weights. We’ll use 6bit.

- We can leave all MLA attention modules as 4 or 6bit, using <5% of weights. We should quantize the attention output (3%), but it’s best to leave it in higher precision.The down_proj is the most sensitive to quantization, especially in the first few layers. We corroborated our findings with the Super Weights paper, our dynamic quantization method and llama.cpp’s GGUF quantization methods. So, we shall leave the first 3 to 6 MoE down_proj matrices in higher precision. For example in the Super Weights paper, we see nearly all weights which should NOT be quantized are in the down_proj:The main insight on why all the "super weights" or the most important weights are in the down_proj is because of SwiGLU which does:

[

f

⁡

(

X

⁢

W

g

⁢

a

⁢

t

⁢

e

)

∗

(

X

⁢

W

u

⁢

p

)

]

⁢

W

d

⁢

o

⁢

w

⁢

n

This means the up and gate projection essentially multiply to form larger numbers, and the down_proj has to scale them down - this means quantizing the down_proj might not be a good idea, especially in the early layers of the transformer.

- We should leave the embedding and lm_head as 4bit and 6bit respectively. The MoE router and all layer norms are left in 32bit.

- This leaves ~88% of the weights as the MoE weights! By quantizing them to 1.58bit, we can massively shrink the model!

- We provided our dynamic quantization code as a fork to llama.cpp: github.com/unslothai/llama.cpp

- We leveraged Bartowski’s importance matrix for the lower quants.💬 Chat Template IssuesAll distilled versions and the main 671B R1 model use the same chat template:`<｜begin▁of▁sentence｜><｜User｜>What is 1+1?<｜Assistant｜>It's 2.<｜end▁of▁sentence｜><｜User｜>Explain more!<｜Assistant｜>`A BOS is forcibly added, and an EOS separates each interaction. To counteract double BOS tokens during inference, you should only call tokenizer.encode(..., add_special_tokens = False) since the chat template auto adds a BOS token as well.For llama.cpp / GGUF inference, you should skip the BOS since it’ll auto add it.`<｜User｜>What is 1+1?<｜Assistant｜>`The <think> and </think> tokens get their own designated tokens. For the distilled versions for Qwen and Llama, some tokens are re-mapped, whilst Qwen for example did not have a BOS token, so <|object_ref_start|> had to be used instead.Tokenizer ID Mappings:

| Token

| R1

| Distill Qwen

| Distill Llama

| <think>

| 128798

| 151648

| 128013

| </think>

| 128799

| 151649

| 128014

| <|begin_of_sentence|>

| 0

| 151646

| 128000

| <|end_of_sentence|>

| 1

| 151643

| 128001

| <|User|>

| 128803

| 151644

| 128011

| <|Assistant|>

| 128804

| 151645

| 128012

| Padding token

| 2

| 151654

| 128004

Original tokens in models:

| Token

| Qwen 2.5 32B Base

| Llama 3.3 70B Instruct

| <think>

| <|box_start|>

| <|reserved_special_token_5|>

| </think>

| <|box_end|>

| <|reserved_special_token_6|>

| <｜begin▁of▁sentence｜>

| <|object_ref_start|>

| <|begin_of_text|>

| <｜end▁of▁sentence｜>

| <|endoftext|>

| <|end_of_text|>

| <｜User｜>

| <|im_start|>

| <|reserved_special_token_3|>

| <｜Assistant｜>

| <|im_end|>

| <|reserved_special_token_4|>

| Padding token

| <|vision_pad|>

| <|finetune_right_pad_id|>

All Distilled and the original R1 versions seem to have accidentally assigned the padding token to <｜end▁of▁sentence｜>, which is mostly not a good idea, especially if you want to further finetune on top of these reasoning models. This will cause endless infinite generations, since most frameworks will mask the EOS token out as -100.We fixed all distilled and the original R1 versions with the correct padding token (Qwen uses <|vision_pad|>, Llama uses <|finetune_right_pad_id|>, and R1 uses <｜▁pad▁｜> or our own added <｜PAD▁TOKEN｜>.🖥️ Running Dynamic R1 QuantsYou do NOT need to use a new llama.cpp version - any system (like Ollama, OpenWebUI, Transformers) which can run GGUFs should be able to run dynamic quants. It might be slow if you do not have enough VRAM or RAM, but it works.If you want to use llama.cpp directly, follow the build instructions for llama.cpp here - don’t forget to enable GPU support! I normally use the below:apt-get update

apt-get install build-essential cmake curl libcurl4-openssl-dev -y

git clone https://github.com/ggerganov/llama.cpp

cmake llama.cpp -B llama.cpp/build \

-DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON

cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split

cp llama.cpp/build/bin/llama-* llama.cpp

Then download the model through huggingface.co/unsloth/DeepSeek-R1-GGUF You can use Hugging Face for this. To download the 1.58bit version, run the following code snippet below. If you want faster downloads, also use hf_transfer by un-commenting out the first few lines below.# pip install huggingface_hub hf_transfer

# import os # Optional for faster downloading

# os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

from huggingface_hub import snapshot_download

snapshot_download(

repo_id = "unsloth/DeepSeek-R1-GGUF",

local_dir = "DeepSeek-R1-GGUF",

allow_patterns = ["*UD-IQ1_S*"],

)

This will download 3 GGUF files to DeepSeek-R1-GGUF/DeepSeek-R1-UD-IQ1_S. Then, use this formula to decide how many layers you can offload to the GPU. If you do not have a GPU, set offloading to 0:

n

offload

=

VRAM

⁡

(

G

⁢

B

)

Filesize

⁡

(

G

⁢

B

)

×

n

layers

−

4

DeepSeek R1 has 61 layers. For example with a 24GB GPU or 80GB GPU, you can expect to offload after rounding down (reduce by 1 if it goes out of memory):

| Quant

| File Size

| 24GB GPU

| 80GB GPU

| 2x80GB GPU

| 1.58bit

| 131GB

| 7

| 33

| All layers 61

| 1.73bit

| 158GB

| 5

| 26

| 57

| 2.22bit

| 183GB

| 4

| 22

| 49

| 2.51bit

| 212GB

| 2

| 19

| 32

To run the model, we quantize the K cache to 4bit. Quantizing the V cache requires flash attention kernels to be compiled for llama.cpp. We use all threads on the machine and use the recommended temperature by DeepSeek of 0.6. The context size is how many tokens you want the model to generate.Go to the main directory - you should see a llama.cpp folder and a DeepSeek-R1-GGUF folder.--threads == how many CPU cores you have--ctx-size == context length of output--n-gpu-layers == the number of layers to offload to your GPU (get this from the table above)For example, on an RTX 4090 GPU with 24GB VRAM / memory, we do:./llama.cpp/llama-cli \

--model DeepSeek-R1-GGUF/DeepSeek-R1-UD-IQ1_S/DeepSeek-R1-UD-IQ1_S-00001-of-00003.gguf \

--cache-type-k q4_0 \

--threads 16 \

--prio 2 \

--temp 0.6 \

--ctx-size 8192 \

--seed 3407 \

--n-gpu-layers 7 \

-no-cnv \

--prompt "<｜User｜>Create a Flappy Bird game in Python.<｜Assistant｜>"

## 🍎 Running on Mac / Apple devices

For Apple Metal devices, be careful of --n-gpu-layers. If you find the machine going out of memory, reduce it. For a 128GB unified memory machine, you should be able to offload 59 layers or so../llama.cpp/llama-cli \

--model DeepSeek-R1-GGUF/DeepSeek-R1-UD-IQ1_S/DeepSeek-R1-UD-IQ1_S-00001-of-00003.gguf \

--cache-type-k q4_0 \

--threads 16 \

--prio 2 \

--temp 0.6 \

--ctx-size 8192 \

--seed 3407 \

--n-gpu-layers 59 \

-no-cnv \

--prompt "<｜User｜>Create a Flappy Bird game in Python.<｜Assistant｜>"

## 🦙 Run in Ollama/Open WebUI

Open WebUI has made an official step-by-step tutorial on how to run R1 here: docs.openwebui.com/tutorials/integrations/deepseekr1-dynamic/If you want to use Ollama for inference on GGUFs, you need to first merge the 3 GGUF split files into 1 like the code below. Then you will need to run the model locally../llama.cpp/llama-gguf-split --merge \

DeepSeek-R1-GGUF/DeepSeek-R1-UD-IQ1_S/DeepSeek-R1-UD-IQ1_S-00001-of-00003.gguf \

merged_file.gguf

💡 Prompt and resultsThe full prompt used is below:Create a Flappy Bird game in Python. You must include these things:

- You must use pygame.

- The background color should be randomly chosen and is a light shade. Start with a light blue color.

- Pressing SPACE multiple times will accelerate the bird.

- The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.

- Place on the bottom some land colored as dark brown or yellow chosen randomly.

- Make a score shown on the top right side. Increment if you pass pipes and don't hit them.

- Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.

- When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.The final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.Full tables and results at: docs.unsloth.ai/basics/deepseek-r1-dynamic-1.58-bitAll 18 outputs and Python generated code are also uploaded there!💕 Thank you! As usual, a huge thank you to everyone for using & sharing Unsloth - we really appreciate it. 🙏As always, be sure to join our Reddit page and Discord server for help or just to show your support! You can also follow us on Twitter and newsletter.Thank you for reading!Daniel & Michael Han 🦥27 Jan 2025

## Fine-tune your own model now!

Learn more  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
