---
source_url: https://unsloth.ai/blog/deepseek-v3.1
slug: deepseek-v3.1
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: deepseek-v3.1

Blog

# Run DeepSeek-V3.1 Dynamic 1-bit GGUFs

## Aug 21, 2025 • By Daniel & Michael

## Aug 21, 2025

## •

## By Daniel & Michael

DeepSeek-V3,1 is DeepSeek's new update to their V3 models. V3.1 is a hybrid reasoning model, rivalling OpenAI's GPT-4.5, o3 and Google's Gemini 2.5 Pro.You can run the model using Unsloth's 1-bit Dynamic 2.0 GGUFs on your favorite inference frameworks. We quantized DeepSeek-V3.1, a 671B parameter model from 720GB down to 170GB - a 80% size reduction. We also fixed the chat template for llama.cpp supported tools.Recommended: Read our Complete Guide for a walkthrough on how to run DeepSeek-V3.1 locally.To ensure the best tradeoff between accuracy and size, we do not to quantize all layers, but selectively quantize e.g. the MoE layers to lower bit, and leave attention and other layers in 4 or 6bit.And see our DeepSeek-V3.1 GGUFs here🐋How to Run DeepSeek-V3.1DeepSeek’s V3.1 update introduces hybrid reasoning inference, combining 'think' and 'non-think' into one model. The full 671B parameter model requires 715GB of disk space. The quantized dynamic 1-bit version uses 170GB (-80% reduction in size).According to DeepSeek, these are the recommended settings for V3.1 inference:- Set the temperature 0.6 to reduce repetition and incoherence.- Set top_p to 0.95 (recommended)- 128K context length

## 🦙 How to V3.1 in Ollama:

- Install ollama if you haven't already!apt-get update

apt-get install pciutils -y

curl -fsSL https://ollama.com/install.sh | sh

- Run the model! Note you can call ollama servein another terminal if it fails! We include all our fixes and suggested parameters (temperature etc) in params in our Hugging Face upload!(NEW) To run the full R1-0528 model in Ollama, you can use our TQ1_0 (170GB quant):OLLAMA_MODELS=unsloth ollama serve &

OLLAMA_MODELS=unsloth ollama run hf.co/unsloth/DeepSeek-V3.1-GGUF:TQ1_0

- To run other bigger quants, you need to first merge the GGUF split files into 1 like the code below. Then you will need to run the model locally../llama.cpp/llama-gguf-split --merge \

DeepSeek-V3.1-GGUF/DeepSeek-V3.1-UD-Q2_K_XL/DeepSeek-V3.1-UD-Q2_K_XL-00001-of-00006.gguf \

merged_file.ggufOLLAMA_MODELS=unsloth ollama serve &

OLLAMA_MODELS=unsloth ollama run merged_file.gguf

## ✨ How to Run V3.1 in llama.cpp:

- Obtain the latest llama.cpp on GitHub here. You can follow the build instructions below as well. Change -DGGML_CUDA=ON to -DGGML_CUDA=OFF if you don't have a GPU or just want CPU inference.apt-get update

apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y

git clone https://github.com/ggml-org/llama.cpp

cmake llama.cpp -B llama.cpp/build \

-DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON

cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split

cp llama.cpp/build/bin/llama-* llama.cpp

- If you want to use llama.cpp directly to load models, you can do the below: (:Q2_K_XL) is the quantization type. You can also download via Hugging Face (point 3). This is similar to ollama run . Use export LLAMA_CACHE="folder" to force llama.cpp to save to a specific location.export LLAMA_CACHE="unsloth/DeepSeek-V3.1-GGUF"

./llama.cpp/llama-cli \

-hf unsloth/DeepSeek-V3.1-GGUF:Q2_K_XL \

--cache-type-k q4_0 \

--threads -1 \

--n-gpu-layers 99 \

--prio 3 \

--temp 0.6 \

--top_p 0.95 \

--min_p 0.01 \

--ctx-size 16384 \

--seed 3407 \

-ot ".ffn_.*_exps.=CPU"Download the model via (after installing pip install huggingface_hub hf_transfer ). You can choose UD-Q2_K_XL (dynamic 2-bit quant) or other quantized versions like Q4_K_M . I recommend using our 2.7bit dynamic quant UD-Q2_K_XL to balance size and accuracy.# !pip install huggingface_hub hf_transfer

import os

os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0" # Can sometimes rate limit, so set to 0 to disable

from huggingface_hub import snapshot_download

snapshot_download(

repo_id = "unsloth/DeepSeek-V3.1-GGUF",

local_dir = "unsloth/DeepSeek-V3.1-GGUF",

allow_patterns = ["*UD-Q2_K_XL*"], # Dynamic 1bit (168GB) Use "*UD-Q2_K_XL*" for Dynamic 2bit (251GB)

)

- Run the model by prompting it.You can edit --threads 32 for the number of CPU threads, --ctx-size 16384 for context length, --n-gpu-layers 2 for GPU offloading on how many layers. Try adjusting it if your GPU goes out of memory. Also remove it if you have CPU only inference../llama.cpp/llama-cli \

--model unsloth/DeepSeek-V3.1-GGUF/UD-Q2_K_XL/DeepSeek-V3.1-UD-Q2_K_XL-00001-of-00006.gguf \

--cache-type-k q4_0 \

--jinja \

--threads -1 \

--n-gpu-layers 99 \

--temp 0.6 \

--top_p 0.95 \

--min_p 0.01 \

--ctx-size 16384 \

--seed 3407 \

-ot ".ffn_.*_exps.=CPU"

- Get the 1bit version (170GB) if you don't have enough combined RAM and VRAM:from huggingface_hub import snapshot_download

snapshot_download(

repo_id = "unsloth/DeepSeek-V3.1-GGUF",

local_dir = "unsloth/DeepSeek-V3.1-GGUF",

allow_patterns = ["*UD-TQ1_0*"], # Use "*UD-Q2_K_XL*" for Dynamic 2bit

)🦋Chat template bug fixesWe fixed a few issues with DeepSeek V3.1's chat template since they did not function correctly in llama.cpp and other engines:1. DeepSeek V3.1 is a hybrid reasoning model, meaning you can change the chat template to enable reasoning. The chat template introduced thinking = True , but other models use enable_thinking = True . We added the option to use enable_thinking as a keyword instead.2. llama.cpp's jinja renderer via minja does not allow the use of extra arguments in the .split() command, so using .split(text, 1) works in Python, but not in minja. We had to change this to make llama.cpp function correctly without erroring out. We fixed it in all our quants and you will get the following error when using other quants:`terminate called after throwing an instance of 'std::runtime_error' what(): split method must have between 1 and 1 positional arguments and between 0 and 0 keyword arguments at row 3, column 1908`💕 Thank you! Thank you for the constant support. 🙏As always, be sure to join our Reddit page and Discord server for help or just to show your support! You can also follow us on Twitter and newsletter.Thank you for reading!Daniel & Michael Han 🦥21 Aug 2025

## Run DeepSeek-V3.1 now!

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
