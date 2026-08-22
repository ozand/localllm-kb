# Reddit Deep Research Synthesis: RTX 3090 & RTX 3090 Ti 24GB Hardware Tuning & LLM Optimization Guide (50+ Sources)

**Date:** 2026-08-22  
**Corpus:** 47 In-Depth Reddit r/LocalLLaMA Threads & Benchmarks (Scraped via Authenticated Native Surf Session)  
**Status:** Canonical Hardware & Runtime Field Knowledge (Raw Community Data & Engineering Synthesis)  

---

## 1. Executive Hardware & Deployment Synthesis

### A. The 24GB VRAM Gold Standard & Sweet-Spot Models
1. **Model Capacity on Single 3090 Ti (24GB):**
   - **27B Class (e.g. Qwen 3.8 / Qwen 2.5 / Gemma 27B):** `UD-Q4_K_S` / `Q4_K_M` occupies ~15.3–16.2 GB VRAM. Leaves **7.5–8.5 GB free VRAM**, which accommodates **Q8_0 KV Cache up to 73k–98k context** or FP16 KV Cache up to 32k context entirely on-chip.
   - **32B Class (e.g. Qwen 2.5 32B / DeepSeek R1 32B distills):** `Q4_K_M` occupies ~19.8 GB VRAM. Leaves ~3.8–4.0 GB free VRAM $\to$ requires `Q4_0` / `Q8_0` KV cache with context capped at 32k–48k.
   - **70B Class (e.g. Llama 3 70B / Qwen 72B):** Cannot run fully on 1x 24GB. Requires `IQ2_XXS` / `IQ2_XS` (~22GB, degraded quality) or splitting across 2x–4x 3090s via Tensor Parallelism (vLLM) / Pipeline Parallelism (llama.cpp).

### B. Power Management, Undervolting & Thermal Throttling
1. **Power Limit (TDP) vs Inference Speed Trade-off:**
   - **Stock 3090 Ti:** 450W TDP. Stock 3090: 350W TDP.
   - **Community Benchmark Consensus:** LLM autoregressive token generation is **memory bandwidth bound (VRAM memory controller load)**, NOT compute/core bound!
   - **Optimal Power Target:** Setting power limit to **280W–300W on 3090 Ti (or 250W–270W on 3090)** drops power consumption by **35–40%** and temperature by **12–15°C**, while losing **less than 1.5% to 3% token generation speed (t/s)**!
   - *Command:* `nvidia-smi -pl 300` (Linux) / MSI Afterburner voltage curve lock at 825mV–850mV.
2. **GDDR6X Memory Junction Temperatures (VRAM Hotspot):**
   - Unlike the base RTX 3090 (which has VRAM chips on the backplate reaching 105°C+ without copper shims/active cooling), the **RTX 3090 Ti has all 24GB on the front side under the main heatsink (16Gb / 2GB single-sided modules)**.
   - 3090 Ti memory junction temps stay much healthier (~72–82°C under full AI load), making it far more durable and thermally stable for 24/7 server workloads.

### C. Memory Bandwidth, PCIe Gen 4 vs Gen 3, and KV Cache Offloading
1. **Raw Memory Bandwidth:**
   - RTX 3090 Ti features **1,008 GB/s** (21 Gbps GDDR6X) vs RTX 3090's **936 GB/s** (19.5 Gbps).
   - This delivers a direct **7–10% speed advantage in pure token generation** (e.g., 48–52 t/s on 27B Q4 vs 44–46 t/s).
2. **PCIe Bandwidth (Gen 4.0 x16 vs Gen 3.0 x16 vs Gen 4.0 x8):**
   - **Generation Phase (Token-by-Token):** Zero impact (0% difference) between PCIe 3.0 and 4.0 because the model weights and active KV cache live entirely inside VRAM.
   - **Prompt Processing (Prefill Phase / TTFT):** PCIe 4.0 x16 yields 20–30% faster time-to-first-token on huge prompts (32k+ tokens) when uploading prompt embeddings/data.
   - **CPU/RAM Offloading Penalty:** If layers or KV cache spill into system RAM, speed drops from 50 t/s down to 3–8 t/s (bottlenecked by system DDR4/DDR5 RAM bandwidth ~50–80 GB/s).

### D. llama.cpp / vLLM / Unsloth Runtime Best Practices on 3090 Ti
1. **FlashAttention-2 (`-fa` / `--flash-attn`):**
   - Mandatory on Ampere (sm_86). Cuts KV cache memory footprint by 40–50% during long context sequences and prevents quadratic VRAM spikes.
2. **KV Cache Quantization (`-ctk q8_0 -ctv q8_0`):**
   - `q8_0` KV cache has zero measurable perplexity loss compared to FP16, while halving the KV memory footprint.
   - Allows expanding context from 48k to **98,304 tokens** within the remaining 8GB VRAM buffer on a 27B model.

---

## 2. Synthesized Thread Digest (Key Evidence Points)

### [RTX 3090 EBay Pricing is Crazy!!](https://www.reddit.com/r/LocalLLaMA/comments/1tysbyj/rtx_3090_ebay_pricing_is_crazy/)

**Post Summary:**
Couple of years ago, before Local LLMs were in vogue, I bought 8 RTX 3090 @ $700 each to build a AI rig, it been working great and I was looking to build another to increase my capacity but looking at EBay those are now selling for 1,300 -1,500 range!
That price seems totally crazy because on my main machine I have 3090 Ti that I bought new 5 years ago for about 1,400.
Needless to say, I was in shock and started looking for other GPUs. Then I went to Amazon and can buy a brand spanking new 3090 for 1,550!
Please tell me if you can buy a new GPU with great thermals why are people buying 5 years old used GPUs with degraded thermals for 1,400+ and keeping the EBay prices so high. What am I missing here?
Couple of years ago, before Local LLMs were in vogue, I bought 8 RTX 3090 @ $700 each to build a AI rig, it been working great and I was looking to build another to increase my capacity but looking at EBay those are now selling for 1,300 -1,500 range!
That price seems totally crazy bec

**Key Community Comments:**
- **vick2djax** (Score: 105): vick2djax • 3mo ago OP just woke up from a 6 month coma. TrifleHopeful5418 • 3mo ago Haha kind of true :) 8 more replies...
- **TrifleHopeful5418** (Score: 14): TrifleHopeful5418 • 3mo ago Haha kind of true :)...
- **Icaruszin** (Score: 114): Icaruszin • 3mo ago It's still the cheapest single NVIDIA card with 24gb if you don't want to go the dual route. But yeah, $1400 for one is crazy. No-Refrigerator-1672 • 3mo ago 3090 is the cheapest 24 gb sure; buy if you're willing to give up just a few GBs, then Alibaba has 3080 20GB at roughly $450, and 2080  22GB at roughly $350, excluding shipping and import tax. Those two options are the act...
- **No-Refrigerator-1672** (Score: 23): No-Refrigerator-1672 • 3mo ago 3090 is the cheapest 24 gb sure; buy if you're willing to give up just a few GBs, then Alibaba has 3080 20GB at roughly $450, and 2080  22GB at roughly $350, excluding shipping and import tax. Those two options are the actual kings of budget builds right now. ScrapEngineer_ • 3mo ago Do you got a link or search terms? No-Refrigerator-1672 • 3mo ago I can give you a l...
- **ScrapEngineer_** (Score: 2): ScrapEngineer_ • 3mo ago Do you got a link or search terms? No-Refrigerator-1672 • 3mo ago I can give you a link to this product. I have personally purchased 2x 3080 20gb, and 2x Mi50 32gb from this exact seller, half a year and a year ago. I have also published a review of my pair of 3080 here. 1 more reply...

### [5070 Ti —> 3090 move. Worth it?](https://www.reddit.com/r/LocalLLaMA/comments/1t1peq7/5070_ti_3090_move_worth_it/)

**Post Summary:**
I got into LLMs late 2024, and local in Jan 2025. since then, I’ve upgraded my mini PC then added eGPU with 5070 Ti back when it was retailing for $750-$800. At 16GB VRAM and DDR5 @ 8500 Mt/s I can’t complain much with 50t/s for Qwen3.6-35B-A3B, and 16t/s for Qwen3.6-27B when offloading some layers to iGPU (max context 70k). I don’t make money off my coding hobby or gaming, so I don’t mind the slow performance. Sometimes though I wish there was a bit more VRAM for more context.
Watching 3090 on hardware swap I can get something for $800-$850 shipped, and sell my 5070 Ti for around the same or slightly more. I game on my PC sometimes and use the 2x DLSS frame gen, and very happy with performance. From benchmarks, 3090 is capable as well and will likely be fine for my needs for a couple more years.
what do you think about this move? is it worth it?
I got into LLMs late 2024, and local in Jan 2025. since then, I’ve upgraded my mini PC then added eGPU with 5070 Ti back when it was retail

**Key Community Comments:**
- **snowieslilpikachu69** (Score: 7): snowieslilpikachu69 • 4mo ago i would just add a 5060 ti 16gb simracerman • 4mo ago I could, but that means another eGPU Dock + Power supply, and bandwidth losses between Oculink and USB4 means slower inference..? lemondrops9 • 4mo ago The slower inference will come from the card and not the connection. I have a 3090 running from a wifi socket quite well  simracerman • 4mo ago Well then.! For the ...
- **simracerman** (Score: 2): simracerman • 4mo ago I could, but that means another eGPU Dock + Power supply, and bandwidth losses between Oculink and USB4 means slower inference..? lemondrops9 • 4mo ago The slower inference will come from the card and not the connection. I have a 3090 running from a wifi socket quite well  simracerman • 4mo ago Well then.! For the price of one 3090, I can have a used 5060Ti, eGPU dock and pow...
- **lemondrops9** (Score: 1): lemondrops9 • 4mo ago The slower inference will come from the card and not the connection. I have a 3090 running from a wifi socket quite well  simracerman • 4mo ago Well then.! For the price of one 3090, I can have a used 5060Ti, eGPU dock and power supply and save some money too. lemondrops9 • 4mo ago I have a mix of 3090s and 5060tis on my main and the 5060ti do quite well at 1/3 the power usag...
- **simracerman** (Score: 4): simracerman • 4mo ago Well then.! For the price of one 3090, I can have a used 5060Ti, eGPU dock and power supply and save some money too. lemondrops9 • 4mo ago I have a mix of 3090s and 5060tis on my main and the 5060ti do quite well at 1/3 the power usage of a 3090. Part of me wishes I went all 5060ti's. simracerman • 4mo ago Now’s the best time to part ways with that 5090 and maybe get two 5060...
- **lemondrops9** (Score: 1): lemondrops9 • 4mo ago I have a mix of 3090s and 5060tis on my main and the 5060ti do quite well at 1/3 the power usage of a 3090. Part of me wishes I went all 5060ti's. simracerman • 4mo ago Now’s the best time to part ways with that 5090 and maybe get two 5060 Ti’s with that price...

### [What should I build my local LLM machine around? RTX 3090s or Arc Pro B60s?](https://www.reddit.com/r/LocalLLaMA/comments/1ucx2xj/what_should_i_build_my_local_llm_machine_around/)

**Post Summary:**
Hi, so pretty much as the title says. I am thinking about building a rig for running local models. Is Intel Arc Pro B60 worth itt these days? How's the hardware speeds compared to a 3090? Anyone using them, can you provide any benchmarks/stats with some common models to reference?
Also, how is software support with Arc cards and is there anything I should be aware of if I decide to go that route?
Currently, out of the box I can find new B60s for about the same price pretty much on demand with next day shipping, as a used 3090 if I spent a few days hawking the auction sites - is it worth it over immediate b60 buy?
Obviously getting multiple 3090s for a decent price could turn into a month-long, or multiple months-long project if I'm unlucky.
I appreciate any feedback, thanks!
Hi, so pretty much as the title says. I am thinking about building a rig for running local models. Is Intel Arc Pro B60 worth itt these days? How's the hardware speeds compared to a 3090? Anyone using them, can

**Key Community Comments:**
- **sooki10** (Score: 5): sooki10 • 2mo ago 3090s if you want speed, better software support and way more online peer knowledge. Dont get 3090s if one or both cards living a short life will bug you. Majority have been used and abused. But they were still worth the risk, their recent prices make the gamble more costly. R9700 if you are okay with slower, but want more lonevity. Software and guides have improved. Downside is ...
- **jstormes** (Score: 2): jstormes • 2mo ago I have two ASRock R9700s and I don't really notice they are that loud. Just basic case with basic cooling. sooki10 • 2mo ago Interesting, well I do live in a hot climate, so probably why my two are noisy. mr_zerolith • 2mo ago They're still loud in a cold area :/...
- **sooki10** (Score: 1): sooki10 • 2mo ago Interesting, well I do live in a hot climate, so probably why my two are noisy. mr_zerolith • 2mo ago They're still loud in a cold area :/...
- **mr_zerolith** (Score: 1): mr_zerolith • 2mo ago They're still loud in a cold area :/...
- **DocMadCow** (Score: 13): DocMadCow • 2mo ago Definitely 3090s. I have a B70 and have buyers remorse. nail_nail • 2mo ago Uh why? Sycl needs to improve... DocMadCow • 2mo ago It needs a lot of improvement especially if you are trying to run software like llama.cpp on Windows. The PP and TG are absolutely abysmal. A pair of RTX 5060 Ti will blow it out of the water. lemondrops9 • 2mo ago what does Llama.cpp run like in Linu...

### [Which GPU for local LLM inference? 3090 or 5070 Ti](https://www.reddit.com/r/LocalLLaMA/comments/1s916kt/which_gpu_for_local_llm_inference_3090_or_5070_ti/)

**Post Summary:**
I want to get a new GPU for local LLM inference.
The 3090 is the best 24GB VRAM option, but is 2 generations old.
Second hand, its prices are at the same level of a new 5070 Ti.
Which card would be the best purchase?
Comparing specs:
Card	RTX 3090	RTX 5070 Ti
CUDA cores	10,496	8,960
Tensor cores	328 @ gen3 (FP16/bfloat16/TF32)	280 @ gen5
Memory	24 GB @ 936.2 GB/s GDDR6X	16 GB @ GDDR7
Tensor compute	71 TFLOPS @ FP16	175.76 TFLOPS @ FP16
		351.52 TFLOPS @ FP8
		703.04 TFLOPS @ FP4
CUDA compute	35.58 TFLOPS BF16/FP32/TF32	43.94 TFLOPS FP16/FP32
Raw compute
I haven't been able to find actual benchmarks of the 3rd vs 5th gen Nvidia consumer cards.
But from the specs, I would expect that with the new tensor cores, you should get huge gains.
Not sure if the inference software (using llama-cpp probably) manages to use the FP4/8 compute for quantized models, that would be a game changer, as it would boost the 44 CUDA TFLOPS to 703 for FP4.
I do expect in practice that the party is limited

**Key Community Comments:**
- **fragment_me** (Score: 7): fragment_me • 5mo ago  Top 1% Commenter 50% more VRAM on the 3090 that’s an easy decision....
- **_twrecks_** (Score: 2): _twrecks_ • 5mo ago Vram is king. 12gb is not enough, 16gb 5070ti are hard to find. I found the speed improvement for llms on the 5070ti to be small....
- **aeonbringer** (Score: 2): aeonbringer • 5mo ago The thing with 3090 is that it’s the last generation of consumer card nvidia kept nvlink on. So you can effectively pool multiple cards. With new consumer cards, they have to go through the slow pcie lanes so you can’t easily pool vram. Nvidia gate kept this functionality to their server cards h100+ now that’s 20k+.  [deleted] • 5mo ago...
- **jacek2023** (Score: 1): jacek2023 • 5mo ago llama.cpp  Top 1% Commenter I replaced 3090 on my desktop with 5070. I use 5070 for desktop apps like Lightroom, Photoshop, Davinci Resolve or Steam games. It's not great for LLM because it has only 12GB of VRAM. My 3090 went to another computer where I have 72+ GB of VRAM, I use it for LLMs. So ask yourself what is your primary use, LLMs or games. robkered • 5mo ago Please rea...
- **robkered** (Score: 1): robkered • 5mo ago Please read my question properly. I am asking about 50xx cards with 16 GB VRAM, and the 5070 Ti is in a sweet spot. Quite a bit cheaper than the 5080 at a marginal drop in performance, same memory size. jacek2023 • 5mo ago llama.cpp  Top 1% Commenter I shared my personal experiences, I have 12GB version....

### [Poor man's guide to servicing a used RTX 3090 for local LLM inference](https://www.reddit.com/r/LocalLLaMA/comments/1t0jd95/poor_mans_guide_to_servicing_a_used_rtx_3090_for/)

**Post Summary:**
Writeup documenting replacing thermal paste on RTX 3090 with thermal issues. Wrote up the whole process with disassembly photos and HWiNFO before/after data. Hope it saves someone some headaches.
https://github.com/cubebecu/writeups/tree/main/gpu-service
Writeup documenting replacing thermal paste on RTX 3090 with thermal issues. Wrote up the whole process with disassembly photos and HWiNFO before/after data. Hope it saves someone some headaches.
https://github.com/cubebecu/writeups/tree/main/gpu-service
This keeps getting reported for self-promotion, but I'm leaving it up because OP has an account history of interacting conversationally with the community (and not with bot-slop).
The rules against self-promotion are partly to prevent outsiders from simply dropping a link on the sub and neglecting meaningful interaction, but I'm not seeing that with canred, so am happy to leave this post up.
Kryonaut is a terrible paste for longevity. It's meant for overclocking. It tends to tank in

**Key Community Comments:**
- **ttkciar** (Score: 1): ttkciar • 4mo ago llama.cpp  Top 1% Commenter This keeps getting reported for self-promotion, but I'm leaving it up because OP has an account history of interacting conversationally with the community (and not with bot-slop). The rules against self-promotion are partly to prevent outsiders from simply dropping a link on the sub and neglecting meaningful interaction, but I'm not seeing that with ca...
- **seamonn** (Score: 13): seamonn • 4mo ago  Top 1% Commenter Kryonaut is a terrible paste for longevity. It's meant for overclocking. It tends to tank in performance a couple weeks into the repaste. Duronaut is what you should be using. patricious • 4mo ago llama.cpp Even better, PTM 7950. canred • 4mo ago I used thermal kryonaut before on my ryzens and radeon, used it because I know it but thanks for this info, I'll try ...
- **patricious** (Score: 6): patricious • 4mo ago llama.cpp Even better, PTM 7950....
- **canred** (Score: 2): canred • 4mo ago I used thermal kryonaut before on my ryzens and radeon, used it because I know it but thanks for this info, I'll try to remember...
- **McSendo** (Score: 7): McSendo • 4mo ago • Edited 4mo ago You should look into the honeywell PTM 7950 . Every thermal paste I used suffered fro the pump out effect, and I would've to replace it every half a year or so. Not with the PTM 7950. canred • 4mo ago You're another person telling me I may have issues with kryonaut, I'll definitely keep an eye on temps over time, thanks!...

### [Is a $699 RTX 3090 (24GB) a good entry point for running strong local LLMs?](https://www.reddit.com/r/LocalLLaMA/comments/1ronpwd/is_a_699_rtx_3090_24gb_a_good_entry_point_for/)

**Post Summary:**
I found a used RTX 3090 with 24 GB of VRAM for $699, and I'm considering buying it to run an LLM locally instead of relying entirely on commercial chatbots and agents (ChatGPT, Gemini, Claude, etc.).
I'm a programmer, but I'm new to the local LLM ecosystem and not very familiar with the practical capabilities and limitations of running open-source models on a single GPU like this. So far I've only run models on CPU/RAM, and while they were decent, performance and speed were awful compared to commercial services.
Would a 3090 be a reasonable purchase if my goal is to run a strong local model — something like a “pseudo-Claude” setup (for example, Qwen-class 9B models) — while being realistic about its limitations?
This would be purely a personal project. I enjoy using Claude, but I also like the idea of managing my own local system and experimenting with open-source models.
Here's my full server setup:
- ASRock B450M Pro4
- Ryzen 5 3600
- 24 GB of DDR4 RAM
- 500 GB NVMe M.2 SSD
- No 

**Key Community Comments:**
- **Signal_Ad657** (Score: 27): Signal_Ad657 • 6mo ago 24GB for $700 is no joke. undevmas • 6mo ago • Edited 6mo ago I've seen that it's a very low price, which actually worries me. Is it worth the risk of it being a scam? For context, I'm from Latin America, so prices here are usually much higher due to import taxes, VAT, and limited availability. Because of that, $699 is actually a pretty good price — but it's still low enough...
- **undevmas** (Score: 3): undevmas • 6mo ago • Edited 6mo ago I've seen that it's a very low price, which actually worries me. Is it worth the risk of it being a scam? For context, I'm from Latin America, so prices here are usually much higher due to import taxes, VAT, and limited availability. Because of that, $699 is actually a pretty good price — but it's still low enough that it makes me a bit suspicious. mustafar0111 ...
- **mustafar0111** (Score: 11): mustafar0111 • 6mo ago If this is off eBay check how much feedback the seller has. But yes unusually low prices can be a warning sign. If this is a local used card, test it before you pay....
- **kidflashonnikes** (Score: 7): kidflashonnikes • 6mo ago I usually buy "for parts" RTX 3090s and end up fixing more than 70% of them. It's usually an easy fix, since most people dont have the hardware background. Repadding ect, these are common, a cheap way to get compute, if you learn how to do it. I make around 10k every 2 months repairing and selling the cards. At this rate, my kids know how to do it, and I jsut tell them to...
- **micnaches** (Score: 1): micnaches • 4mo ago that is cool! where can someone learn is this something you can find out on youtube?...

### [Finally finished my LLM server: EPYC 9575F, 4× RTX 3090 (96GB VRAM), 768GB ECC RAM](https://www.reddit.com/r/LocalLLaMA/comments/1tx9tf2/finally_finished_my_llm_server_epyc_9575f_4_rtx/)

**Post Summary:**
Took a while, but Nalthis is finally up and assembled.
Specs:
Supermicro H13SSL-N
AMD EPYC 9575F (64C/128T Zen 5)
768GB DDR5-5600 ECC RDIMM
4× RTX 3090 (96GB VRAM total)
1× 2TB NVMe OS
2× 3.94TB NVMe data
2050W ATX 3.1 PSU
Corsair 9000D
Planned use:
vLLM - high throughput small models
llamacpp - larger reasoning models
I have been making a space simulation and finally ready to integrate AI into how the NPCs doing planning, hoping to get decent throughput on smaller models with lots of requests
The original plan involved a lot more MCIO risers and custom mounting, but I was able to fit two of the 3090s directly on the motherboard and front-mount the other two.
Planning to run all four cards power-limited to 250W since this box is primarily for LLM inference.
The 9000D has been surprisingly good for a 4×3090 build. I also used these fan mounts for additional airflow:
https://www.thingiverse.com/thing:2804306
Still need to finish thermal testing, but the hardware side is

**Key Community Comments:**
- **MotokoAGI** (Score: 56): MotokoAGI • 3mo ago Run a large model like KimiK2.6, GLM5.1 MiniMax2.7 etc and give us the numbers. I want to know what $25k+ gets us today val_in_tech • 3mo ago ~7-8 tps, 200-500 prefil on larger ones. Unfortunate reality of that build - won't run anything fast except 27b moderately-extremist • 3mo ago Yeah, I recently priced out almost this exact build with the intention of having something that...
- **val_in_tech** (Score: 14): val_in_tech • 3mo ago ~7-8 tps, 200-500 prefil on larger ones. Unfortunate reality of that build - won't run anything fast except 27b moderately-extremist • 3mo ago Yeah, I recently priced out almost this exact build with the intention of having something that can run GLM5.1 Q6. But it wouldn't be a nearly fast enough for an interactive chat experience. This would be reasonable numbers for setting...
- **moderately-extremist** (Score: 7): moderately-extremist • 3mo ago Yeah, I recently priced out almost this exact build with the intention of having something that can run GLM5.1 Q6. But it wouldn't be a nearly fast enough for an interactive chat experience. This would be reasonable numbers for setting it on a task and then coming back later to see the product though. And could run Qwen3.6-27B when you need more of a realtime interac...
- **DeepOrangeSky** (Score: 3): DeepOrangeSky • 3mo ago What if, instead of bothering with VRAM, you got some dual-socket setup with like 24 channels of memory, with 24 sticks of DDR5 32GB sticks, instead of a single socket 12-channel setup with 12 sticks of 64GB DDR5 + 96GB of VRAM the way OP has? Would that get higher speeds than the OP-style setup? With this amount of offloading, having more channels of fast DDR5 on dual, goo...
- **FullstackSensei** (Score: 6): FullstackSensei • 3mo ago llama.cpp  Top 1% Commenter NUMA is still largely unsupported, at least in llama.cpp and derivatives. Generally, you can't lump the channels of dual or more CPUs together. It doesn't work that way. The bandwidth between NUMA nodes is 1/U3 - 1/6th the memory bandwidth depending on platforms, with SP5 Epyc being closer to 1/4 - 1/5th. Even with proper NUMA support, don't ex...

### [Qwen3.8-27B on 2x 3090 + vLLM + DFlash2: 218 tok/s single request](https://www.reddit.com/r/LocalLLaMA/comments/1vsccit/qwen3827b_on_2x_3090_vllm_dflash2_218_toks_single/)

**Post Summary:**
I hacked this together so there's probably more on the table in terms of performance.
Measured with the Club-3090 canonical bench suite (bench.sh, 3 warmups + 5 measured runs, temp 0.6 / top_p 0.95 / top_k 20).
Prefill: 1342 tok/s @ 10k, 628 tok/s @ 90k
Spec-decode: 7 draft tokens, acceptance length 3.35, 47.8% acceptance
Peak VRAM: 22.3 GB/card
Context ceiling: 131k (DFlash2 drafter eats ~13.5 GB)
Used Kimi K3 for all the VLLM fixes
Metric	Narrative	Code
Decode TPS	120.1	218.3
Wall TPS	117.7	204.8
TTFT	168 ms	178 ms
Stack
2× RTX 3090 (PCIe Gen4 x16/x16, no NVLink, patched P2P)
Power capped 220/250 W
Bare-metal vLLM v0.26.1rc1 + AutoRound INT4 (group 128) + DFlash2 draft model
Custom vLLM changes that made it boot cleanly: https://github.com/oceanplexian/vllm/pull/1
I hacked this together so there's probably more on the table in terms of performance.
Measured with the Club-3090 canonical bench suite (bench.sh, 3 warmups + 5 measured runs, temp 0.6 / top_p 0.95 / top_k 20)

**Key Community Comments:**
- **tinny66666** (Score: 40): tinny66666 • 3d ago I may be blind, but what model and quant are you using? AdamTReineke • 3d ago Autoround int4, according to the PR  starkruzr • 3d ago in other words, like most of these benchmarks, a bench of something effectively useless. SmartCustard9944 • 3d ago Please substantiate. Why useless? From several posts and even personal use, 4-5 bpw performs extremely well across the board. The m...
- **AdamTReineke** (Score: 26): AdamTReineke • 3d ago Autoround int4, according to the PR  starkruzr • 3d ago in other words, like most of these benchmarks, a bench of something effectively useless. SmartCustard9944 • 3d ago Please substantiate. Why useless? From several posts and even personal use, 4-5 bpw performs extremely well across the board. The model appears to be very robust to quantization, so I am curious to understan...
- **starkruzr** (Score: 61): starkruzr • 3d ago in other words, like most of these benchmarks, a bench of something effectively useless. SmartCustard9944 • 3d ago Please substantiate. Why useless? From several posts and even personal use, 4-5 bpw performs extremely well across the board. The model appears to be very robust to quantization, so I am curious to understand why you disagree. starkruzr • 3d ago very robust to quant...
- **SmartCustard9944** (Score: 15): SmartCustard9944 • 3d ago Please substantiate. Why useless? From several posts and even personal use, 4-5 bpw performs extremely well across the board. The model appears to be very robust to quantization, so I am curious to understand why you disagree. starkruzr • 3d ago very robust to quantization I have not found this to be the case at long context for sufficiently complex tasks with 3.6, and si...
- **starkruzr** (Score: 10): starkruzr • 3d ago very robust to quantization I have not found this to be the case at long context for sufficiently complex tasks with 3.6, and since 3.8 is architecturally the same I doubt that will have changed. SmartCustard9944 • 3d ago I suggest to try that, 3.8 and 3.6 behave differently. vienna_city_skater • 3d ago 3.8 is much better, 3.6 was barely useful for me, 3.8 works great, same quan...

### [vLLM MAXIMUM performance on multi-3090](https://www.reddit.com/r/LocalLLaMA/comments/1r66jyp/vllm_maximum_performance_on_multi3090/)

**Post Summary:**
TLDR: install patched p2p driver, patch vllm platform and skip p2p check. You'll get +50% performance on 4x3090 with Qwen3 Coder Next FP8. Free performance, free tokens, very nice :)
So, YOU (yes, YOU) managed to setup vLLM on your multi gpu platform with consumer cards. It's nice, running fast and doesn't lose a lot of performance on long contexts. But there are HIDDEN and FREE performance laying here just for you.
Let's go into the deep.
Prerequisite
I assume you have something like cheap RTX 3090 and running vLLM with tensor parallelism on linux without docker. Otherwise I cannot guarantee results. As if I could guarantee anything otherwise, lol.
Resizable bar
You need to enable resizable bar. Check it with sudo lspci -vvv | grep -i -A40 'VGA compatible controller', look for Region 1: Memory at 17800000000 (64-bit, prefetchable) [size=32G]. If it's 32M, then you need to flash new BIOS.
https://www.techpowerup.com/download/nvidia-nvflash/ - nvflash
https://www.techpowerup.com

**Key Community Comments:**
- **zipperlein** (Score: 6): zipperlein • 6mo ago I wouldn't patch the function of vllm in the env. Just use a monkey-patch. Nepherpitu • 6mo ago What do you mean? zipperlein • 6mo ago U can actually change any python method at runtime. U can just do that and run the serve from a python script below that. For example: from vllm.platforms.cuda import CudaPlatformBase def is_fully_connected(cls, physical_device_ids: list[int]) ...
- **Nepherpitu** (Score: 2): Nepherpitu • 6mo ago What do you mean? zipperlein • 6mo ago U can actually change any python method at runtime. U can just do that and run the serve from a python script below that. For example: from vllm.platforms.cuda import CudaPlatformBase def is_fully_connected(cls, physical_device_ids: list[int]) -> bool:     return True CudaPlatformBase.is_fully_connected = classmethod(is_fully_connected) #...
- **zipperlein** (Score: 11): zipperlein • 6mo ago U can actually change any python method at runtime. U can just do that and run the serve from a python script below that. For example: from vllm.platforms.cuda import CudaPlatformBase def is_fully_connected(cls, physical_device_ids: list[int]) -> bool:     return True CudaPlatformBase.is_fully_connected = classmethod(is_fully_connected) #Run vllm below this gtek_engineer66 • 6...
- **gtek_engineer66** (Score: 10): gtek_engineer66 • 6mo ago Ah someone who coded before llm's existed! Long live the monkey patch zipperlein • 6mo ago Yeah, except it does not work for this sadly because vllm spawns workers processes or sth. I am using it for custom parsers though....
- **zipperlein** (Score: 3): zipperlein • 6mo ago Yeah, except it does not work for this sadly because vllm spawns workers processes or sth. I am using it for custom parsers though....

### [5070 Ti (New) vs 3090 (Used) to pair with 4070 for local LLMs?](https://www.reddit.com/r/LocalLLaMA/comments/1spwk7h/5070_ti_new_vs_3090_used_to_pair_with_4070_for/)

**Post Summary:**
I'm upgrading my setup to run larger models and need a second GPU to pair with my current RTX 4070 (12GB).
My Workloads:
LLMs: Up to 32B dense (Gemma 4 31B) and ~120B MoE (Qwen 122B10A). I mostly run Q4/IQ4/UD MXFP4 quants.
Image diffusion model: FireRed 1.1 (Q4).
Target: 30+ tps at large contexts (up to 256k). Currently hitting a memory ceiling around 131k context (yesterday using Qwen 3.6 35B3A).
The Options & Market Constraints:
RTX 5070 Ti 16GB (New): ~1.2k USD.
RTX 3090 24GB (Used only): ~1k USD. (Pricing is rather complicated, finding it is even more complicated, might go for above 1k)
5060 TI 16 GB (New): ~600 USD
I strictly prefer buying new. There is no proper way to verify how "old" or "used" the GPU is.
My Hardware Limits:
CPU/RAM: Ryzen 9 9950X, 80GB DDR5 (pairing 24gb pairs and 16gb).
Mobo/PSU: X870E, MSI MAG A1000GLS PCIE5 1000W.
Clearance: GC-801 Case with a front-mounted 360 AIO inside. Long cards like the ASUS TUF won't clear the radiator (probably, i'm gu

**Key Community Comments:**
- **FoxiPanda** (Score: 7): FoxiPanda • 4mo ago  Top 1% Commenter If you can find a 3090 for $1000 it's a pretty clear winner, but with your penchant for buying new, I think you'll find it virtually impossible to find a 3090 new. 3090 --> 24GB --> 936.2GB/s 5070 Ti --> 16GB --> 896GB/s 5060 Ti --> 16GB --> 448GB/s Those are the numbers that matter (other than power consumption and perhaps some mildly new tensor core features...
- **TheFunSlayingKing** (Score: 0): TheFunSlayingKing • 4mo ago Even with things like NVFP4 only being viable on a Blackwell card? The 24 gb is very tempting for me but as I keep reading, I feel like 36 gb is like an awkwardly positioned number, I can't think of things that would fit on 36 that can't fit on 28, but I sure can think of things that fit on a 48 but don't on a 36. There's also the fact of size, I think that 3090 wouldn'...
- **FoxiPanda** (Score: 3): FoxiPanda • 4mo ago  Top 1% Commenter So I will fully admit that I haven't messed with NVFP4 that much at this point, but I feel like it's overblown - in general, RTX 30 series+ have enough compute that these small models (<50B by my definition) are running faster than you'll be able to use them generally anyway...and you're pairing with a 4070, so you instantly kick yourself out of being able to ...
- **TheFunSlayingKing** (Score: 1): TheFunSlayingKing • 4mo ago Yeah that's true, and I haven't completely made up my mind yet, I guess that's why I even shoved the 5060 ti in there, because money wise it is the cheapest 16gb option available but it's really slow in comparison to the other two, I don't mind "speed", like I don't want to run a model at 500 tps, 40-50 tps is perfect, that's why I tend to go q4 even if I can go higher ...
- **FoxiPanda** (Score: 1): FoxiPanda • 4mo ago  Top 1% Commenter People are still using Volta V100 - 2018 vintage - and Pascal P100 cards - launched in mid-2016 - for AI today. A V100 32GB is now "legacy" by NVIDIA's definition and won't be getting a lot of updates, but is still a great bang for the buck card for what it is (32GB @ 900GB/s) P100 is genuinely starting to show its age (really, really old tensor core designs a...

### [Honest take on running 9× RTX 3090 for AI](https://www.reddit.com/r/LocalLLaMA/comments/1s0p28x/honest_take_on_running_9_rtx_3090_for_ai/)

**Post Summary:**
my home server
3090 4way
I bought 9 RTX 3090s.
They’re still one of the best price-to-VRAM GPUs available.
Here’s the conclusion first: 1. I don’t recommend going beyond 6 GPUs 2. If your goal is simply to use AI, just pay for a cloud LLM subscription 3. Proxmox is, in my experience, one of the best OS setups for experimenting with LLMs
To be honest, I had a specific expectation:
If I could build around 200GB of VRAM, I thought I’d be able to run something comparable to Claude-level models locally.
That didn’t happen.
Reality check
Even finding a motherboard that properly supports 4 GPUs is not trivial.
Once you go beyond that: • PCIe lane limitations become real • Stability starts to degrade • Power and thermal management get complicated
The most unexpected part was performance.
Token generation actually became slower when scaling beyond a certain number of GPUs.
More GPUs does not automatically mean better performance, especially without a well-optimized setup.
What I’m 

**Key Community Comments:**
- **a_beautiful_rhind** (Score: 41): a_beautiful_rhind • 5mo ago  Top 1% Commenter If you didn't use the P2P driver, all your PCIE had to go through the CPU and thus it slows down. Outside_Dance_2799 • 5mo ago I'm just curious about this, but are you talking about NVLink? I'm asking because I believe it only supports a maximum of two. a_beautiful_rhind • 5mo ago  Top 1% Commenter No. Aside from nvlink there is P2P over standard PCIE....
- **Outside_Dance_2799** (Score: 4): Outside_Dance_2799 • 5mo ago I'm just curious about this, but are you talking about NVLink? I'm asking because I believe it only supports a maximum of two. a_beautiful_rhind • 5mo ago  Top 1% Commenter No. Aside from nvlink there is P2P over standard PCIE. FishChillylly • 5mo ago you can get a pcie switch board based on plx chips like pex8748 or pex8796, they are pcie3.0 models but i think when us...
- **a_beautiful_rhind** (Score: 27): a_beautiful_rhind • 5mo ago  Top 1% Commenter No. Aside from nvlink there is P2P over standard PCIE....
- **FishChillylly** (Score: 6): FishChillylly • 5mo ago you can get a pcie switch board based on plx chips like pex8748 or pex8796, they are pcie3.0 models but i think when using p2p it would be enough for 3090s. or you can go for pcie4.0 models like pex88048 or pex88096 but that would be much more expensive. basically pcie switch let the cards communicate only through it when using p2p, without having to pass through cpu, which...
- **heliosythic** (Score: 5): heliosythic • 5mo ago Just looking into this as well, seems not supported on my 2 P100s but you could check on yours with command: nvidia-smi topo -m Mine: nvidia-smi topo -m 	GPU0	GPU1	CPU Affinity	NUMA Affinity	GPU NUMA ID GPU0	X 	PHB	0-27	0		N/A GPU1	PHB	X 	0-27	0		N/A Legend:   X    = Self   SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)   ...

### [Before I buy a used RTX 3090…](https://www.reddit.com/r/LocalLLaMA/comments/1r2skzl/before_i_buy_a_used_rtx_3090/)

**Post Summary:**
So I had fun for a couple of weeks with my old 1080 just to test local llm and it was fun.
Now I have an opportunity to buy a rtx 3090 but I’m like, do I really need this?
For every day general models, I will never be as good as chatgpt.
So I feel that local llm shines for precise tasks with smaller models.
For example, I currently run gemma3:4b for cameras motion analysis with home assistant and LLM Vision. But it works great with my 1080
Any other fun projects you use with local llm?
I was thinking that a 3090 could run multiples smaller LLM for different tasks but I’m out of ideas.
I was also planning to test OpenClaw (yes I know the security flaws, just to test) but I read that no local llm works well.
So, what is your used cases for local llm other than testing?
So I had fun for a couple of weeks with my old 1080 just to test local llm and it was fun.
Now I have an opportunity to buy a rtx 3090 but I’m like, do I really need this?
For every day general models, I will nev

**Key Community Comments:**
- **Lissanro** (Score: 6): Lissanro • 6mo ago  Top 1% Commenter With 3090 you could run Qwen3-Coder-Next with partial RAM offloading, which is going to be far better even as general model than any 4B model. Or you can fully fit in VRAM something like Qwen3 30B-A3B for the best speed. But ultimately it is up to you to decide. One of the best local LLMs is K2.5 currently and it has everything including image vision support; I...
- **Dentifrice** (Score: 3): Dentifrice • 6mo ago I have 2 choices, my old pc : i5-8400 with 16gb of DDR4 And my gaming PC with 64gb of DDR5 and a amd 7900x...
- **exceptioncause** (Score: 4): exceptioncause • 6mo ago check r/StableDiffusion for the opportunities, you can run locally much more stuff than mere LLMs, but if you want a modern but less noisy and power hungry GPU with just enough vram check 5060ti/16gb Dentifrice • 6mo ago I’m really torn apart between a use 3090 and a 5060 ti 16gb… I know it’s not the same power processing but … exceptioncause • 6mo ago btw, if you run most...
- **Dentifrice** (Score: 2): Dentifrice • 6mo ago I’m really torn apart between a use 3090 and a 5060 ti 16gb… I know it’s not the same power processing but … exceptioncause • 6mo ago btw, if you run mostly LLMs, consider buying TWO 5060ti/16, they're quite compact and easy to install in a normal PC case and you will have total 32gb around the price of a single 3090 Dentifrice • 6mo ago Running llm on two cards works well? i ...
- **exceptioncause** (Score: 0): exceptioncause • 6mo ago btw, if you run mostly LLMs, consider buying TWO 5060ti/16, they're quite compact and easy to install in a normal PC case and you will have total 32gb around the price of a single 3090 Dentifrice • 6mo ago Running llm on two cards works well? i usually use ollama exceptioncause • 6mo ago not sure about ollama, it kinda fell out of favor here, but llama.cpp or lmstudio or f...

### [Anyone running HUANANZHI H12D-8D + BMC with 4x RTX 3090 for LLM inference?](https://www.reddit.com/r/LocalLLaMA/comments/1t2hejy/anyone_running_huananzhi_h12d8d_bmc_with_4x_rtx/)

**Post Summary:**
Hi everyone,
I'm considering building a home LLM inference rig around:
- HUANANZHI H12D-8D + BMC
- AMD EPYC 7002/7003
- 4x RTX 3090 24GB
- DDR4 ECC RDIMM, 8-channel
- Linux + vLLM / SGLang / llama.cpp
- Open frame, PCIe 4.0 x16 risers
The board looks very attractive for the price: EPYC SP3, 8-channel memory, BMC/IPMI, 4x PCIe 4.0 x16 physical slots, 3x M.2, etc. But documentation and real-world reports are a bit scattered, so I’d love to hear from actual owners.
Questions:
Do all 4 PCIe slots run electrically at x16, or is one of them limited to x8?
Could you share lspci -vv / nvidia-smi link width output if possible?
Does Above 4G Decoding work properly with 3-4 GPUs?
Does Resizable BAR work after the newer BIOS update?
I saw that HUANANZHI has a BIOS note mentioning Resizable BAR / PCIe split optimization.
Any issues booting with RTX 3090 specifically?
I’ve seen some reports about GPU compatibility quirks on this board.
How stable is the BMC/IPMI module?
Does remote

**Key Community Comments:**
- **Nepherpitu** (Score: 5): Nepherpitu • 4mo ago Running 8 3090 on this board with 7702 CPU. All slots are x16 4.0 with bifurcation up to 4x4. Zero issues so far (since October 2025). Maybe when running 4x4 bifurcation with cheap $20 oculink splitter and $5 cables I see interference errors on gpu lanes, but it's still stable (disabled AER reporting in bios, LOL). awfulalexey • 4mo ago Thank u a lot! awfulalexey • 4mo ago Bro...
- **awfulalexey** (Score: 1): awfulalexey • 4mo ago Thank u a lot!...
- **awfulalexey** (Score: 1): awfulalexey • 4mo ago Bro, could you please show a photo of your system? I'm trying to figure out what kind of case to build so that 8 cards will fit. I'm getting a bit lost with it all now. Nepherpitu • 4mo ago Its in progress now. Waiting for x8 splitters instead of 4x4 oculinks. Two cards on x16, two on x8 and four on x4. I'm bought server in pc case, so just made simple rack from aluminum prof...
- **Nepherpitu** (Score: 1): Nepherpitu • 4mo ago Its in progress now. Waiting for x8 splitters instead of 4x4 oculinks. Two cards on x16, two on x8 and four on x4. I'm bought server in pc case, so just made simple rack from aluminum profiles and rivets. awfulalexey • 4mo ago why 4 on x4? Is it possible to have 8 x8 cards? Nepherpitu • 4mo ago Of course. Board has 4 x16 ports, all ports equal. It's just me waiting for shippin...
- **awfulalexey** (Score: 1): awfulalexey • 4mo ago why 4 on x4? Is it possible to have 8 x8 cards? Nepherpitu • 4mo ago Of course. Board has 4 x16 ports, all ports equal. It's just me waiting for shipping of 3 more x8 splitters. I didn't knew I will go for 8 cards, so I didn't had 4 x8 splitters in my drawer....

### [Reddit - The heart of the internet](https://www.reddit.com/r/SwordAndSupperGame/comments/1vv6qej/)

### [24GB VRAM llama-server config exchange thread](https://www.reddit.com/r/LocalLLaMA/comments/1uukj2m/24gb_vram_llamaserver_config_exchange_thread/)

**Post Summary:**
For whom is this tread:
Everyone with a 24GB GPU (rtx 3090, 7900xtx, rtx 4090)
What this Thread is for:
Sharing proven/well working llama-server start configs.
Requirements for the configs:
- Utilizes the the VRAM as much as possible
- Provides at least 200.000 tokens KV Cache
State next to your start command, how much System RAM (normal RAM) you have, as this could very well influence caching performance/viability of your command.
Also, if you possible, include infos regarding you OS and CPU, as this might affect available RAM/VRAM für llama-server.
For whom is this tread:
Everyone with a 24GB GPU (rtx 3090, 7900xtx, rtx 4090)
What this Thread is for:
Sharing proven/well working llama-server start configs.
Requirements for the configs:
- Utilizes the the VRAM as much as possible
- Provides at least 200.000 tokens KV Cache
State next to your start command, how much System RAM (normal RAM) you have, as this could very well influence caching performance/viability of your command.


**Key Community Comments:**
- **L0ren_B** (Score: 13): L0ren_B • 1mo ago Google Club 3090 ;) libregrape • 1mo ago llama.cpp Holy hell! NigaTroubles • 1mo ago What is that L0ren_B • 1mo ago https://github.com/noonghunna/club-3090 see discussions, se all configs .latest 24gb and 48gb models, tests etc. best condensed place for 3090 users! CATLLM • 1mo ago What an incredible resource! Thank you! NigaTroubles • 1mo ago Thanks but i am 9070 XT user Prepara...
- **libregrape** (Score: 4): libregrape • 1mo ago llama.cpp Holy hell!...
- **NigaTroubles** (Score: 1): NigaTroubles • 1mo ago What is that L0ren_B • 1mo ago https://github.com/noonghunna/club-3090 see discussions, se all configs .latest 24gb and 48gb models, tests etc. best condensed place for 3090 users! CATLLM • 1mo ago What an incredible resource! Thank you! NigaTroubles • 1mo ago Thanks but i am 9070 XT user PreparationTrue9138 • 1mo ago For 16 gigs you can try qwen 3.6 35 b and offload experts...
- **L0ren_B** (Score: 12): L0ren_B • 1mo ago https://github.com/noonghunna/club-3090 see discussions, se all configs .latest 24gb and 48gb models, tests etc. best condensed place for 3090 users! CATLLM • 1mo ago What an incredible resource! Thank you! NigaTroubles • 1mo ago Thanks but i am 9070 XT user PreparationTrue9138 • 1mo ago For 16 gigs you can try qwen 3.6 35 b and offload experts to ram...
- **CATLLM** (Score: 2): CATLLM • 1mo ago What an incredible resource! Thank you!...

### [Hot Experts in your VRAM! Dynamic expert cache in llama.cpp for 27% faster CPU +GPU token generation with Qwen3.5-122B-A10B compared to layer-based single-GPU partial offload](https://www.reddit.com/r/LocalLLaMA/comments/1slue0z/hot_experts_in_your_vram_dynamic_expert_cache_in/)

**Post Summary:**
Claude cooked on the code, but I wrote this post myself, caveman style. I wanted to play with Qwen3.5-122B, but I don't have a unified memory system to work with, and 15 tok/s was rough. 23 tok/s is still rough but honestly noticeably faster when streaming responses.
Tl;dr:
We keep track of which experts get routed to most frequently for the past N tokens. We make a bet that the processing speed-up from loading these frequently routed-to experts into VRAM will outweigh the latency penalty for transferring expert tensors from system RAM (cold) into VRAM (hot). Rinse and repeat every N tokens.
First off, results:
vs. all-CPU experts baseline:
+44.8% token generation (15.65 tok/s -> 22.67 tok/s)
no prompt processing regression
vs. layer-based offload at equivalent VRAM commitment:
+26.8% token generation (17.87 tok/s -> 22.67 tok/s)
very slightly slower prompt processing
Baseline: All experts offloaded to CPU (LLAMA_ARG_OVERRIDE_TENSOR=exps=CPU)
Prompt processing (tok/s, n=2928

**Key Community Comments:**
- **Tartarus116** (Score: 35): Tartarus116 • 4mo ago -ot exps=CPU My system would also be running slow if I did that. Just let llama-server optimize for you with: fit = true fit-target = 1024 fit-ctx = 128000 Also, by offloading non-consecutive layers - e.g. layer 50 in system, then 51 in gpu, then 52 in system - you introduce more graph splits. So, don't do that. Llama's fit starts optimizing by offloading the last few layers ...
- **xaocon** (Score: 3): xaocon • 4mo ago I'm not really clear on what knobs autofit has access to or how "smart" it is in deciding how to use them. Don't the cpumoe options start offloading moe layers from fronts to back as well? Tartarus116 • 4mo ago You can generate the static `ot` params from CLI with `llama-fit-params`. Saves you time on future restarts. E.g. for Qwen3.5-397b, this offloads the last 3 layers' ffn up/...
- **Tartarus116** (Score: 4): Tartarus116 • 4mo ago You can generate the static `ot` params from CLI with `llama-fit-params`. Saves you time on future restarts. E.g. for Qwen3.5-397b, this offloads the last 3 layers' ffn up/down/gate exp tensors and runs at near-native speed: ``` ot = blk\.58\.ffn_(up|down|gate)_(ch|)exps=CPU,blk\.59\.ffn_(up|down|gate)_(ch|)exps=CPU,blk\.60\.ffn_(up|down|gate)_(ch|)exps=CPU ``` `cpumoe` start...
- **buttplugs4life4me** (Score: 2): buttplugs4life4me • 4mo ago Thanks! I didn't know about the fit params tool. Model went from crashing to 500/30 tokens a second...
- **xaocon** (Score: 1): xaocon • 4mo ago Hasn't even looked at that command yet, very slick. Have been trying to figure out the best way to run the large Gemma 4 moe on my 16G of vram. There are so many knobs to adjust, this at least should help narrow down what I should be benchmarking....

### [VRAM Advice? 24GB or 32GB for starters](https://www.reddit.com/r/LocalLLaMA/comments/1prlqi1/vram_advice_24gb_or_32gb_for_starters/)

**Post Summary:**
Hey guys, hope it’s been a great weekend for you all
I’m working to build my rig with primary use case of hosting, fine tuning and maybe doing image/video gen locally.
With all that said, does a 4090 makes any sense as of now or only 5090 will cut it?
The gap is huge for me, if I add the rest of the components as well required for the CPU, but I’ve been waiting and waiting and waiting that I don’t know what makes sense anymore
If 24 GB is just a little slower (30% as per most benchmarks), I can try to live with it but if the performance is insanely different and high end for 32, I’ll have to wait more I guess
Love to know thoughts from all of you
Hey guys, hope it’s been a great weekend for you all
I’m working to build my rig with primary use case of hosting, fine tuning and maybe doing image/video gen locally.
With all that said, does a 4090 makes any sense as of now or only 5090 will cut it?
The gap is huge for me, if I add the rest of the components as well required for the 

**Key Community Comments:**
- **DAlmighty** (Score: 43): DAlmighty • 8mo ago Get as much as you can comfortably afford. Disastrous_Meal_4982 • 8mo ago Yeah, you’ll never regret going bigger as long as you can afford it. I went with multiple 16GB cards and regret not just starting with a bigger card that was easier to expand even further. I’ll probably end up selling my current cards to get bigger ones if prices aren’t astronomical. DAlmighty • 8mo ago I...
- **Disastrous_Meal_4982** (Score: 11): Disastrous_Meal_4982 • 8mo ago Yeah, you’ll never regret going bigger as long as you can afford it. I went with multiple 16GB cards and regret not just starting with a bigger card that was easier to expand even further. I’ll probably end up selling my current cards to get bigger ones if prices aren’t astronomical. DAlmighty • 8mo ago I couldn’t agree more. I should really sell the 3090 and MI50 th...
- **DAlmighty** (Score: 2): DAlmighty • 8mo ago I couldn’t agree more. I should really sell the 3090 and MI50 that I have before it’s too late....
- **TrainingLegal146** (Score: 2): TrainingLegal146 • 8mo ago This is the way - VRAM hunger is real and you'll always find ways to use more once you start experimenting with larger models...
- **__JockY__** (Score: 16): __JockY__ • 8mo ago  Top 1% Commenter As much VRAM as possible, always. You will want more. Always. If I had to choose between a slightly faster GPU with 24GB vs a slower GPU with 32GB I’d choose 32. If I could afford 48GB I’d get that, and if an RTX PRO 6000 96GB was within budget I’d get that. Source: my journey from P40s through 3090s through A6000s to PRO 6000s. The progression happens when yo...

### [Smartest model for 24-28GB vram?](https://www.reddit.com/r/LocalLLaMA/comments/1qucoid/smartest_model_for_2428gb_vram/)

**Post Summary:**
I was super happy to find qwen 30B A3B being so damn clever on my 3090 and then I tried GLM flash 4.7 and I was blown away. Is there any other model that’s smart like this? My use case is using it as an agentic coder but bonus points if it can do rp like GLM flash lol
I was super happy to find qwen 30B A3B being so damn clever on my 3090 and then I tried GLM flash 4.7 and I was blown away. Is there any other model that’s smart like this? My use case is using it as an agentic coder but bonus points if it can do rp like GLM flash lol
For general questions, try Qwen 3 32B, Mistral Small 24B, gpt-oss 20B.
For coding, try Qwen Coder 3 32B, Devstral Small 24B. gpt-oss 20B.
If a model has Unsloth Dynamic quants, use that. It should be better quality than any other static quant or iMatrix quant. Unsloth also have good documentation on the correct llama.cpp flags to use (temperature, min-p, etc).
Actual resuts depend on your topic and questions. Some are better than others at specific things

**Key Community Comments:**
- **suprjami** (Score: 69): suprjami • 7mo ago For general questions, try Qwen 3 32B, Mistral Small 24B, gpt-oss 20B. For coding, try Qwen Coder 3 32B, Devstral Small 24B. gpt-oss 20B. If a model has Unsloth Dynamic quants, use that. It should be better quality than any other static quant or iMatrix quant. Unsloth also have good documentation on the correct llama.cpp flags to use (temperature, min-p, etc). Actual resuts depe...
- **DistanceSolar1449** (Score: 37): DistanceSolar1449 • 7mo ago It’s a bit dated. That advice would have been good last summer. Qwen3 VL 32b is better than Qwen3 32b in all regards. GLM-4.7 flash is better than Qwen Coder 30b and gpt-oss-20b. jubilantcoffin • 7mo ago GLM Flash definitely isn't overall better than Qwen Coder. MutantEggroll • 7mo ago What kindof tasks do you find GLM Flash doing worse than Qwen3 Coder? In my experienc...
- **jubilantcoffin** (Score: 2): jubilantcoffin • 7mo ago GLM Flash definitely isn't overall better than Qwen Coder. MutantEggroll • 7mo ago What kindof tasks do you find GLM Flash doing worse than Qwen3 Coder? In my experience, it's been better across the board. jubilantcoffin • 6mo ago Rust stuff, was code related to layout calculation. GLM Flash didn't manage to get even a scrappy thing working. MutantEggroll • 6mo ago Ah good...
- **MutantEggroll** (Score: 2): MutantEggroll • 7mo ago What kindof tasks do you find GLM Flash doing worse than Qwen3 Coder? In my experience, it's been better across the board. jubilantcoffin • 6mo ago Rust stuff, was code related to layout calculation. GLM Flash didn't manage to get even a scrappy thing working. MutantEggroll • 6mo ago Ah good to know. I've got some Rust projects laying around, but I've been neglecting them. ...
- **jubilantcoffin** (Score: 2): jubilantcoffin • 6mo ago Rust stuff, was code related to layout calculation. GLM Flash didn't manage to get even a scrappy thing working. MutantEggroll • 6mo ago Ah good to know. I've got some Rust projects laying around, but I've been neglecting them.  What's your favorite model for Rust?...

### [Help 24GB vram and openclaw](https://www.reddit.com/r/LocalLLaMA/comments/1sg4ojp/help_24gb_vram_and_openclaw/)

**Post Summary:**
Hey folks,
I’ve been diving into local LLMs as a CS student and wanted to experiment more seriously with OpenCL / local inference setups. I recently got my hands on a second-hand RTX 3090 (24GB VRAM), so naturally I was pretty excited to push things a bit.
I’ve been using Ollama and tried running Qwen 3.5 27B. I did manage to get it up and running, but honestly… the outputs have been pretty rough.
What I’m trying to build isn’t anything super exotic — just a dashboard + a system daemon that monitors the host machine and updates stats in real time (CPU, memory, maybe some logs). But the model just struggles hard with this. Either it gives incomplete code, hallucinates structure, or the pieces just don’t work together. I’ve spent close to 4 hours iterating, prompting, breaking things down… still no solid result.
At this point I’m not sure if:
- I’m expecting too much from a 27B model locally
- My prompting is bad
- Or this just isn’t the kind of task these models handle well witho

**Key Community Comments:**
- **jacek2023** (Score: 2): jacek2023 • 5mo ago llama.cpp  Top 1% Commenter You are running Qwen 3.5 27B on 24GB GPU, but what quant? Also learn llama.cpp instead ollama to understand how things work....
- **CalligrapherFar7833** (Score: 1): CalligrapherFar7833 • 5mo ago Dont use ollama use llama.cpp or vllm...
- **Uninterested_Viewer** (Score: 1): Uninterested_Viewer • 5mo ago I was under the impression that these agentic tools generally need a LOT of kv cache space to hold context. Is 24gb even near enough to hold weights AND enough kv cache to be useful? Are you offloading to ram?...
- **54id56f34** (Score: 1): 54id56f34 • 5mo ago • Edited 5mo ago I've been running Qwen 27B variants on a 4090 with Hermes Agent quite a while, here's my thoughts. Your model quant probably isn't the problem. Q4_K_M is fine for a 27B on 24GB. But your KV cache quantization may be an issue. Here's the exact command I use for Qwopus v3 on my 4090: llama-server \   -m Qwopus3.5-27B-v3-Q4_K_M.gguf \   --host 0.0.0.0 --port 8000 ...
- **tylerrobb** (Score: 2): tylerrobb • 4mo ago Incredibly helpful context for me, thank you! I'm about to try out Qwopus3.5-27B-v3 with Hermes after checking out your benchmark info vs. Gemma 4. That said, if Carnice is purpose-built with Hermes in mind, then I might need to try that as well! 54id56f34 • 4mo ago Just as an aside, Gemma 4 26B (the MoE model) runs surprisingly well in system memory in my testing. On DDR4 3200...

### [How many of you tried BeeLlama.cpp? How's it? Agentic coding possible with 8GB VRAM?](https://www.reddit.com/r/LocalLLaMA/comments/1tbshsl/how_many_of_you_tried_beellamacpp_hows_it_agentic/)

**Post Summary:**
We'll be getting those features(check bottom link) on mainline soon or later anyway. But for now this fork could be useful to see the full potential of our poor GPUs(and also big, large GPUs).
Any 8GB VRAM(and 32GB RAM) folks already doing Agentic coding with models(@ Q4 at least) like Qwen3.6-35B-A3B, Qwen3.6-27B, Gemma-4-31B, Gemma-4-26B-A4B? I would love to see some t/s stats, full commands & more details on that. I'm not expecting any miracle with 8GB VRAM, still want to do something decent with limited constraints. Though I'm getting new rig this month, I want to use my current laptop(8GB VRAM) too for Agentic coding.
Others(who has more than 8GB VRAM), please share your stats, full commands & comparison with mainline.
Below is related thread by creator. Hope the creator adds more features continuously.
BeeLlama.cpp: advanced DFlash & TurboQuant with support of reasoning and vision. Qwen 3.6 27B Q5 with 200k context on 3090, 2-3x faster than baseline (peak 135 tps!)
We'll be g

**Key Community Comments:**
- **FatheredPuma81** (Score: 19): FatheredPuma81 • 3mo ago https://www.reddit.com/r/LocalLLaMA/comments/1t88zvv/comment/okuoxii/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button That comment sums it up imo. I would rather wait for llama.cpp to implement things properly than use a 3 layer fork of dubious quality. One guy did benchmark Qwen3.6-35B-A3B-UD-IQ4_NL_XL turbo tests buun-llama-cpp but...
- **LosEagle** (Score: 1): LosEagle • 3mo ago Why so many levels of fork and not just https://github.com/TheTom/llama-cpp-turboquant which seems to have only the original llama.cpp as upstream and other turboquant forks seem to derive from it anyway? I am asking more from a learning perspective. FatheredPuma81 • 3mo ago TheTom made it more of a proof of concept to test and hasn't really maintained or updated it since. Buun ...
- **FatheredPuma81** (Score: 2): FatheredPuma81 • 3mo ago TheTom made it more of a proof of concept to test and hasn't really maintained or updated it since. Buun merged newer llama.cpp updates and I'm didn't really look at what else it changed. The latest fork was for DFlash and some other things....
- **pmttyji** (Score: 0): pmttyji • 3mo ago  Top 1% Poster But if you're desperate I'd say give it a go if you want to. Come up with some tests to verify quality in your tasks though before committing. Yep, want to do this on my current laptop(8GB VRAM). I'll be staying with mainline on my upcoming rig....
- **R_Duncan** (Score: 16): R_Duncan • 3mo ago Qwen3.6-35B-A3B is the only choice with 8GB VRAM: gemma has huge kv cache (can't fit 128k+ context) and 27B is way slow. trialbuterror • 3mo ago How R_Duncan • 3mo ago • Edited 3mo ago I use Q4K_XL with plain llama.cpp (usually 128k cache at q8_0, only sane setup for now) + one harness of choice: (opencode/pi/ etc.etc.) . iso4 kv cache tempted me but there was no saving of vram ...

### [Best models in 3x3090 (72GB VRAM) in Q2 2026?](https://www.reddit.com/r/LocalLLaMA/comments/1u50rw1/best_models_in_3x3090_72gb_vram_in_q2_2026/)

**Post Summary:**
Sometime around the beginning of the year I setup my LLM computer — 3x3090 in a very old DDR4 computer, so I only use the 72GB VRAM to load the models (for speed)
I’ve been mostly using these three models:
GPT-OSS 120b still pretty sold
Qwen3.5 122b very (very!!) good for one shot coding but extremely over thinking in my opinion
GLM Air 4.5 106B in non-think by default which I use a lot for quick replies
Occasionally I also use:
Gemma 4 31B or Qwen3.6 27B as they are quick to load and offload, and sometimes I need to use a video card for other tasks — I keep the LLM in 2x3090 and 1x3090 for audio-image stuff. Because they also fit nicely in 48GB in Q8 I do trust them over the bigger models in some instances.
Honorables mentions I stopped using without any valid reason:
Nematron Nano Omni 30B A3B is very good, but I just never use it because I default to the big ones for most general tasks
Devstral Small 2 24B used to be my favorite before Qwen 27B completely replaced it for me

**Key Community Comments:**
- **EmPips** (Score: 15): EmPips • 2mo ago +1 for Nemotron-Omni for audio-input use-cases. Glad that model is getting attention. As for something that'd actually use 72GB it's really awkward right now. A quant of Qwen3.5-122B will probably feel the best, Qwen3.6-27B will perform the best at the cost of a good speed-hit (made more bearable by MTP). Outside of that it's pretty awkward right now when you go over 48GB. The ~10...
- **liviuberechet** (Score: 4): liviuberechet • 2mo ago Yeah, it has been like this for over 6 months… feels like there is nothing much in the 70-120gb range: Minimax is too big and the Reap models are just too lobotomised — tried a nice Reap model of m2.1 at one point but it was making tones of mistakes. all the dense 70B models (such as kimi dev or meta ones) are painfully slow. and the big ones are just too big (Qwen 397b, de...
- **frescoj10** (Score: 1): frescoj10 • 2mo ago Do some franken merges on some dense models to get a 50+ dense model...
- **annodomini** (Score: 1): annodomini • 2mo ago +1 for Nemotron-Omni for audio-input use-cases. Glad that model is getting attention. What are you running it on? Audio support for it is still a WIP on llama.cpp. https://github.com/ggml-org/llama.cpp/pull/22520 EmPips • 2mo ago Running it on that branch and having a good time with it...
- **EmPips** (Score: 2): EmPips • 2mo ago Running it on that branch and having a good time with it...

### [Was about to drop $800+ on a 3090 for local LLM. Turns out my CPU was a beast the whole time.](https://www.reddit.com/r/LocalLLaMA/comments/1s6mgmh/was_about_to_drop_800_on_a_3090_for_local_llm/)

**Post Summary:**
Went down the local LLM rabbit hole. Looked at P40s, V100s (almost bought an SXM2 version that doesn’t even plug into a normal motherboard lmao), 3090s ($800+ now cuz AI bros bought them all). Claude literally said “bro just try running it on CPU first.” Qwen 3 30B Q4 on CPU: 18.8 tok/s. Expected 3-5. Got nearly 19. Zen 4 + DDR5 is cracked for inference. Tested on a real coding task. 8B confidently wrote completely wrong code. 30B nailed it first try. Basically GPT-4o level for $0.
Went down the local LLM rabbit hole. Looked at P40s, V100s (almost bought an SXM2 version that doesn’t even plug into a normal motherboard lmao), 3090s ($800+ now cuz AI bros bought them all). Claude literally said “bro just try running it on CPU first.” Qwen 3 30B Q4 on CPU: 18.8 tok/s. Expected 3-5. Got nearly 19. Zen 4 + DDR5 is cracked for inference. Tested on a real coding task. 8B confidently wrote completely wrong code. 30B nailed it first try. Basically GPT-4o level for $0.
I just love you complainin

**Key Community Comments:**
- **Sixhaunt** (Score: 46): Sixhaunt • 5mo ago I just love you complaining that GPU prices are high because of people buying them for AI in a post about you wanting to buy the GPU for AI....
- **robertpro01** (Score: 23): robertpro01 • 5mo ago Now add the 3090 expect much better results...
- **BankjaPrameth** (Score: 14): BankjaPrameth • 5mo ago You are absolutely right! Anyway, try Qwen 3.5 35B and thanks me later....
- **huzbum** (Score: 10): huzbum • 5mo ago Meh, now try with 100k+ context. TG isn’t so bad, but PP is slooooow. Or try a dense model like qwen3.5 27b. If you want a cheap way to run LLMs try a pair of cmp100 - 210. They work fine in pipeline mode for inference. You should get like 80 tokens per second with qwen3 30b and good pp....
- **TheSilentCheese** (Score: 3): TheSilentCheese • 5mo ago Which zen 4? how much ram?...

### [What is the best general-purpose model to run locally on 24GB of VRAM in 2026?](https://www.reddit.com/r/LocalLLaMA/comments/1qlwibf/what_is_the_best_generalpurpose_model_to_run/)

**Post Summary:**
I've been running Gemma 3 27b since its release nine months ago, which is an eternity in the AI field. Has anything better been released since then that can run well on a single 3090ti?
I'm not looking to code, to create agents, or to roleplay; I just want a good model to chat with and get reasonably smart answers to questions. If it can view images, that's even better.
I've been running Gemma 3 27b since its release nine months ago, which is an eternity in the AI field. Has anything better been released since then that can run well on a single 3090ti?
I'm not looking to code, to create agents, or to roleplay; I just want a good model to chat with and get reasonably smart answers to questions. If it can view images, that's even better.
GPT OSS 20B for speed and general use, Nemotron Nano for intelligence
Nemotron nano is faster and dumber for me 😅
After some consideration I'm updating my intelligence rec to GLM 4.7 Flash with the caveat that it hallucinates a fair bit, lacks world k

**Key Community Comments:**
- **MerePotato** (Score: 29): MerePotato • 7mo ago • Edited 7mo ago GPT OSS 20B for speed and general use, Nemotron Nano for intelligence danishkirel • 7mo ago Nemotron nano is faster and dumber for me 😅 MerePotato • 7mo ago After some consideration I'm updating my intelligence rec to GLM 4.7 Flash with the caveat that it hallucinates a fair bit, lacks world knowledge and you shouldn't ask it about politics Limp_Classroom_264...
- **danishkirel** (Score: 8): danishkirel • 7mo ago Nemotron nano is faster and dumber for me 😅 MerePotato • 7mo ago After some consideration I'm updating my intelligence rec to GLM 4.7 Flash with the caveat that it hallucinates a fair bit, lacks world knowledge and you shouldn't ask it about politics...
- **MerePotato** (Score: 1): MerePotato • 7mo ago After some consideration I'm updating my intelligence rec to GLM 4.7 Flash with the caveat that it hallucinates a fair bit, lacks world knowledge and you shouldn't ask it about politics...
- **Limp_Classroom_2645** (Score: 2): Limp_Classroom_2645 • 7mo ago Nemotron Nano is not it MerePotato • 7mo ago After some consideration I'm updating my intelligence rec to GLM 4.7 Flash with the caveat that it hallucinates a fair bit, lacks world knowledge and you shouldn't ask it about politics...
- **MerePotato** (Score: 1): MerePotato • 7mo ago After some consideration I'm updating my intelligence rec to GLM 4.7 Flash with the caveat that it hallucinates a fair bit, lacks world knowledge and you shouldn't ask it about politics...

### [4x 3090, 96gb vram what Model to drive Hermes?](https://www.reddit.com/r/LocalLLaMA/comments/1v6lrre/4x_3090_96gb_vram_what_model_to_drive_hermes/)

**Post Summary:**
3 year lurker, now i finally got my server up and running. dont know which model to choose. llama.cpp or vllm, what makes more sense? mainly single user with maybe 2-3 more additional users in family, if everything checks out. hermes is gonna be used as "ai playground" to manifest ideas on tailscale network and do quick prototyping of thoughts. also ill look into using only 2 3090 for the main model and the other 2 will be dedicated to docling and speech services for a voice agent (speech in-> text out). got some stuff going with my even realities g2 but lost everything when i wiped my ssd for proxmox. yeah...
any advice or stuff i should look into is welcome :)
3 year lurker, now i finally got my server up and running. dont know which model to choose. llama.cpp or vllm, what makes more sense? mainly single user with maybe 2-3 more additional users in family, if everything checks out. hermes is gonna be used as "ai playground" to manifest ideas on tailscale network and do quick prototy

**Key Community Comments:**
- **Hyiazakite** (Score: 12): Hyiazakite • 27d ago Do Qwen 3.6 27B or Qwen 3.5 122B-A10B. Qwen 3.5 122B-A10B will be faster. Use VLLM. 122B fits with 128k context using AWQ 4-bit. vLLM is way superior if you'll have concurrent usage. _TheWolfOfWalmart_ • 27d ago  Top 1% Poster I would have agreed a few days ago, but... Laguna S 2.1 > Qwen 3.5 122B-A10B now uniqueusername649 • 27d ago • Edited 27d ago Yes, I think that part sho...
- **_TheWolfOfWalmart_** (Score: 9): _TheWolfOfWalmart_ • 27d ago  Top 1% Poster I would have agreed a few days ago, but... Laguna S 2.1 > Qwen 3.5 122B-A10B now uniqueusername649 • 27d ago • Edited 27d ago Yes, I think that part should be a given. However, it seems its still not as clear yet if it beats Qwen 3.6 27b at fp8 or bf16 across the board. I have seen tests showing that Laguna is better, although not by much. And I have see...
- **uniqueusername649** (Score: 2): uniqueusername649 • 27d ago • Edited 27d ago Yes, I think that part should be a given. However, it seems its still not as clear yet if it beats Qwen 3.6 27b at fp8 or bf16 across the board. I have seen tests showing that Laguna is better, although not by much. And I have seen tests where Laguna is just about on par and sometimes Qwen beating it. I suspect that has to do with different quantisation...
- **Hyiazakite** (Score: 1): Hyiazakite • 27d ago Nice to know! I thought it looked promising but I haven't had the time to test it myself...
- **techmago** (Score: 1): techmago • 27d ago Is it? (genuine curiosity) I might be able to run laguna. I'm waiting the version inside llama-swap update to a version that suports it. I can run (poorly) Qwen 3.5 122B. But benchmarks say it is worse than Qwen 3.6 27B...? So my current best model is a qwen-fable finetune that is better than plain qwen. But laguna is interesting. lemondrops9 • 26d ago I used to run 122b but aft...

### [RTX 3090 llamacpp flags help](https://www.reddit.com/r/LocalLLaMA/comments/1sla6gd/rtx_3090_llamacpp_flags_help/)

**Post Summary:**
Hi,
my current system hardware
RTX 3090 24GB VRAM & Sysrem RAM 64GB using windows 11
been playing around with hermes agent and local llm (Qwopus3.5-27B-v3-GGUF & gemma-4-26B-A4B-it-GGUF)
when i try asking the hermes agent to do a task with gemma4 keeps giving me an empty response error (CLI) and with qwen takes forever and also leaks to RAM.
below are the commnds i use to run the models
llama-server -m "<windows-path>" --host 0.0.0.0 --port 8000 -ngl 99 -c 262144 -fa on --cache-type-k q4_0 --cache-type-v q4_0 --metrics --slots --props
llama-server -m "<windows-path>" --host 0.0.0.0 --port 8000 -ngl 99 -c 262144 -fa on --cache-type-k q4_0 --cache-type-v q4_0 --metrics --slots --props
can you pls help me or guide me on how i can tune this btter and which is better or how i can benchmark or what parameters to see to make sure which is performing better or what other o

**Key Community Comments:**
- **grumd** (Score: 7): grumd • 4mo ago  Top 1% Commenter Forget about Gemma, you can run Qwen 3.5 27B and it will be much higher quality than Gemma 26B-A4B You just need proper parameters to keep it all in VRAM This is all you need really: llama-server -m "...gguf" --host 0.0.0.0 --port 8000 -ctv q8_0 -ctk q8_0 Don't use q4_0 (too low quality), and don't set the context length manually. llama-server will automatically a...

### [For those wondering about the power consumption of a dual 3090 rig while inferencing](https://www.reddit.com/r/LocalLLaMA/comments/1t4b203/for_those_wondering_about_the_power_consumption/)

**Post Summary:**
Mine is ~760W measured at the wall by a smart plug.
Idle is 90Wish.
I haven't tweaked the power limit of the cards or done anything fancy.
Mine is ~760W measured at the wall by a smart plug.
Idle is 90Wish.
I haven't tweaked the power limit of the cards or done anything fancy.
I get to 500W with 2x3090+3060 during inference, limiting the 3090s to 220W. It doesn't decrease speed, though I'm running without tensor parallelism because the second 3090 hangs on a 1x pcie. 😅 Roughly 110w in idle.
At 220W you're losing some performances in a pretty mesurable way, but the real killer is the 1x PCIe.
A PCIe 4.0 4x is enough for TP, don't you have a free M2 slot ? You can use an M2 to Oculink adapter, that's what I'm using and it's working flawlessly :)
Is pcie 4x 4 really enough? I have 2x 3090 and tried llamacpp TP and vLLM and got worse or similar results to pipeline. Operator error?
There's no TP for llamacpp, only tensor split. The closest thing available to TP with GGUF is graph mode

**Key Community Comments:**
- **Sunija_Dev** (Score: 17): Sunija_Dev • 4mo ago I get to 500W with 2x3090+3060 during inference, limiting the 3090s to 220W. It doesn't decrease speed, though I'm running without tensor parallelism because the second 3090 hangs on a 1x pcie. 😅 Roughly 110w in idle. TacGibs • 4mo ago At 220W you're losing some performances in a pretty mesurable way, but the real killer is the 1x PCIe. A PCIe 4.0 4x is enough for TP, don't y...
- **TacGibs** (Score: 9): TacGibs • 4mo ago At 220W you're losing some performances in a pretty mesurable way, but the real killer is the 1x PCIe. A PCIe 4.0 4x is enough for TP, don't you have a free M2 slot ? You can use an M2 to Oculink adapter, that's what I'm using and it's working flawlessly :) An_Original_ID • 4mo ago Is pcie 4x 4 really enough? I have 2x 3090 and tried llamacpp TP and vLLM and got worse or similar ...
- **An_Original_ID** (Score: 2): An_Original_ID • 4mo ago Is pcie 4x 4 really enough? I have 2x 3090 and tried llamacpp TP and vLLM and got worse or similar results to pipeline. Operator error? TacGibs • 4mo ago There's no TP for llamacpp, only tensor split. The closest thing available to TP with GGUF is graph mode on ikllamacpp. And with PCIe 1x TP isn't beneficial at all because the card on the fastest PCIe port is constantly w...
- **TacGibs** (Score: 6): TacGibs • 4mo ago There's no TP for llamacpp, only tensor split. The closest thing available to TP with GGUF is graph mode on ikllamacpp. And with PCIe 1x TP isn't beneficial at all because the card on the fastest PCIe port is constantly waiting for the one on the PCIe 1x. Yes 4.0 4x is enough, you'll just have a few % of losses (4 to 6%) compared to 16x. traviscthall • 4mo ago TP in llama.cpp is ...
- **traviscthall** (Score: 3): traviscthall • 4mo ago TP in llama.cpp is experimental but somewhat functional now https://github.com/ggml-org/llama.cpp/pull/19378...

### [Stop wasting electricity](https://www.reddit.com/r/LocalLLaMA/comments/1tayu5t/stop_wasting_electricity/)

**Post Summary:**
Run on my rtx4090
llama.cpp params:
llama-server -m ~/Projects/llm/models/Qwen3.6-27B-UD-Q4_K_XL.gguf --flash-attn on -ngl all -ctk q4_0 -ctv q4_0 -t 32 -c 262144
Power limit was set using sudo nvidia-smi -pl N
On my observation, GPU constantly hitting power limit, so its safe to say that it actual consumption. You can cut power consumption to 40% without losing performance(and also reduce noise, heat from pc, and extend lifespan of gpu).
Run on my rtx4090
llama.cpp params:
llama-server -m ~/Projects/llm/models/Qwen3.6-27B-UD-Q4_K_XL.gguf --flash-attn on -ngl all -ctk q4_0 -ctv q4_0 -t 32 -c 262144
Power limit was set using sudo nvidia-smi -pl N
On my observation, GPU constantly hitting power limit, so its safe to say that it actual consumption. You can cut power consumption to 40% without losing performance(and also reduce noise, heat from pc, and extend lifespan of gpu).
Your post is getting popular and we just featured it on our Discord! Come check it out!
You've also been 

**Key Community Comments:**
- **WithoutReason1729** (Score: 1): WithoutReason1729 • 3mo ago Your post is getting popular and we just featured it on our Discord! Come check it out! You've also been given a special flair for your contribution. We appreciate your post! I am a bot and this action was performed automatically....
- **chimpera** (Score: 111): chimpera • 3mo ago can you check the prefill performance? OkFly3388 • 3mo ago llama.cpp BagComprehensive79 • 3mo ago Okay there is a sweet spot more clear than my expectations BobsView • 3mo ago 275w ? or i read it wrong ? BagComprehensive79 • 3mo ago Yes correct, you can check comparison between 150w and 275w on the plot tomByrer • 2mo ago • Edited 2mo ago 275w is the lowest point in the plot, bu...
- **OkFly3388** (Score: 116): OkFly3388 • 3mo ago llama.cpp BagComprehensive79 • 3mo ago Okay there is a sweet spot more clear than my expectations BobsView • 3mo ago 275w ? or i read it wrong ? BagComprehensive79 • 3mo ago Yes correct, you can check comparison between 150w and 275w on the plot tomByrer • 2mo ago • Edited 2mo ago 275w is the lowest point in the plot, but for some (like me where electricity is cheap), I don't m...
- **BagComprehensive79** (Score: 66): BagComprehensive79 • 3mo ago Okay there is a sweet spot more clear than my expectations BobsView • 3mo ago 275w ? or i read it wrong ? BagComprehensive79 • 3mo ago Yes correct, you can check comparison between 150w and 275w on the plot tomByrer • 2mo ago • Edited 2mo ago 275w is the lowest point in the plot, but for some (like me where electricity is cheap), I don't mind spending an extra 25w for ...
- **BobsView** (Score: 9): BobsView • 3mo ago 275w ? or i read it wrong ? BagComprehensive79 • 3mo ago Yes correct, you can check comparison between 150w and 275w on the plot tomByrer • 2mo ago • Edited 2mo ago 275w is the lowest point in the plot, but for some (like me where electricity is cheap), I don't mind spending an extra 25w for a bit extra performance. If I could, I'd aim for 280-290w...

### [A Reminder, Guys, Undervolt your GPUs Immediately. You will Significantly Decrease Wattage without Hitting Performance.](https://www.reddit.com/r/LocalLLaMA/comments/1s9i1gn/a_reminder_guys_undervolt_your_gpus_immediately/)

**Post Summary:**
I am sure many of you already know this, but using MSI Afterburner, you can change the voltage your single or multiple GPUs can draw, which can drastically decrease power consumption, decrease temperature, and may even increase performance.
I have a setup of 2 GPUs: A water cooled RTX 3090 and an RTX 5070ti. The former consumes 350-380W and the latter 250-300W, at stock performance. Undervolting both to 0.900V resulted in decrease in power consumption for the RTX 3090 to 290-300W, and for the RTX 5070ti to 180-200W at full load.
Both cards are tightly sandwiched having a gap as little as 2 mm, yet temperatures never exceed 60C for the air-cooled RTX 5070ti and 50C for the RTX 3090. I also used FanControl to change the behavior of my fans. There was no change in performance, and I even gained a few FPS gaming on the RTX 5070ti.
I am sure many of you already know this, but using MSI Afterburner, you can change the voltage your single or multiple GPUs can draw, which can drastically dec

**Key Community Comments:**
- **MrHaxx1** (Score: 47): MrHaxx1 • 5mo ago I can't speak for LLM, but I remember I had the same result with my RTX 3070 for gaming. Higher frequency, lower temps, better performance. Literally no tradeoff. darktraveco • 5mo ago How did you iterate to find the sweet spot? Running benchmarks? MrHaxx1 • 5mo ago That's basically it. First I googled what undervolt people were getting with the RTX 3070, I picked roughly the ave...
- **darktraveco** (Score: 7): darktraveco • 5mo ago How did you iterate to find the sweet spot? Running benchmarks? MrHaxx1 • 5mo ago That's basically it. First I googled what undervolt people were getting with the RTX 3070, I picked roughly the average number, and if it crashed, I'd undervolt less, and if it didn't crash, I'd undervolt more. I tested with the furmark benchmark, I think? It's a long time ago. CoUsT • 5mo ago J...
- **MrHaxx1** (Score: 17): MrHaxx1 • 5mo ago That's basically it. First I googled what undervolt people were getting with the RTX 3070, I picked roughly the average number, and if it crashed, I'd undervolt less, and if it didn't crash, I'd undervolt more. I tested with the furmark benchmark, I think? It's a long time ago. CoUsT • 5mo ago Just a quick note. Some cards these days have built-in frequency/voltage curve and you ...
- **CoUsT** (Score: 6): CoUsT • 5mo ago Just a quick note. Some cards these days have built-in frequency/voltage curve and you can't adjust all of it. If you put -50 mV, some cards might apply -50 mV for all points, some might scale it and apply -25 mV at halfway and -50 mV at the end of curve. It's important to test card across multiple benchmarks/games OR at least test it in something heavy but adjust power limit all t...
- **darktraveco** (Score: 3): darktraveco • 5mo ago Thanks, I'll do some tinkering today!...

### [Decrease the power limit of your 5090 to at least 480W - the performance penalty for inference is negligible.](https://www.reddit.com/r/LocalLLaMA/comments/1vfdwox/decrease_the_power_limit_of_your_5090_to_at_least/)

**Post Summary:**
I run my inference machine in the living room, so noise and heat output are a significant concern.
Ran a quick test using my daily driver model (Qwen 3.6-27b) and at 480W, the card outputs only 2.1% less t/s in decode and 8.8% in prefill (which is already very fast). Well worth the massive noise reduction, heat output and increased card longevity, IMO. Even 450W would be fine for many use cases, but the output starts dropping off fast (2.1% -> 4.2% for 30W less).
=============
Full data:
=============
Model: Qwen3.6-27B-Q6_K.gguf
Results:
| Limit W | Max GPU C | Steady GPU C | Max GPU fan % | Sustained W | Steady clock MHz | Max case RPM | pp t/s | tg t/s | pp % | tg % |
|--------:|----------:|-------------:|--------------:|------------:|-----------------:|-------------:|-------:|-------:|-----:|-----:|
| 600 | 81 | 74.8 | 59 | 566 | 2818 | 1522 | 3242.9 | 61.5 | 100.0 | 100.0 |
| 510 | 75 | 70.1 | 50 | 509 | 2645 | 1367 | 2980.0 | 61.2 | 91.9 | 99.5 |
| 480 | 77 | 72.8 | 54

**Key Community Comments:**
- **mr_zerolith** (Score: 22): mr_zerolith • 18d ago I've got another trick for you for this card. The memory modules are underrated by about 3ghz ( probably for thermal reasons ) If you OC the memory by 1-2ghz, you'll get your token generation speed, plus some more. Because of the power limit, you are making less heat, so you have thermal headroom to push memory OC. Running a +2.4ghz on my 5090 memory for 6 months now with no ...
- **Makers7886** (Score: 9): Makers7886 • 18d ago This was the mining goto - powerlimit, lock cores, and oc memory until stable. Almost every 3090 had a decent amount of headroom for memory oc - I'd imagine the same for 5090. LTLRedditor • 18d ago Would you happen to know the nvidia-smi commands to do this? Makers7886 • 18d ago For my 3090s I run: -pl 250 and -lgc 0,1500 but do not OC the memory right now - used to back in mi...
- **LTLRedditor** (Score: 3): LTLRedditor • 18d ago Would you happen to know the nvidia-smi commands to do this? Makers7886 • 18d ago For my 3090s I run: -pl 250 and -lgc 0,1500 but do not OC the memory right now - used to back in mining days though. No particular reason other than content with speeds and power draw and not messing with it. mr_zerolith • 18d ago On Linux, i use LACT to control these things....
- **Makers7886** (Score: 3): Makers7886 • 18d ago For my 3090s I run: -pl 250 and -lgc 0,1500 but do not OC the memory right now - used to back in mining days though. No particular reason other than content with speeds and power draw and not messing with it....
- **mr_zerolith** (Score: 2): mr_zerolith • 18d ago On Linux, i use LACT to control these things....

### [3090 owners, what vram tempature do you get under ai load?](https://www.reddit.com/r/LocalLLaMA/comments/1vabgly/3090_owners_what_vram_tempature_do_you_get_under/)

**Post Summary:**
Hello
Can you please share the tempature you get on your rtx 3090 under active llm load?
Im trying to findout if my rtx 3090's tempatures are healthy or not
please share VRAM Tempature only, you can track it via gpu-z on windows
Hello
Can you please share the tempature you get on your rtx 3090 under active llm load?
Im trying to findout if my rtx 3090's tempatures are healthy or not
please share VRAM Tempature only, you can track it via gpu-z on windows
83-84c
Is that core temp or vram temp?
My vram temp is 110, and my gut can feel its not right (i tracked it via gpu-z, under qwen 3.6 27b)
8x 3090s here, just a heads up vram temp at 110 is a red flag. I'd check out what's going on. What type case are you using? Are the 3090s sitting too close to each other? How old are these cards? 110 means they are actively getting throttled. You keep them at 110 for long and they're long term health is really suffering.
Its only one 3090, I've bought it recently from a guy who claimed "lighly

**Key Community Comments:**
- **woswoissdenniii** (Score: 10): woswoissdenniii • 23d ago 83-84c Whole_Alternative_18 • 23d ago Is that core temp or vram temp? My vram temp is 110, and my gut can feel its not right (i tracked it via gpu-z, under qwen 3.6 27b) anitamaxwynnn69 • 23d ago 8x 3090s here, just a heads up vram temp at 110 is a red flag. I'd check out what's going on. What type case are you using? Are the 3090s sitting too close to each other? How old...
- **Whole_Alternative_18** (Score: 8): Whole_Alternative_18 • 23d ago Is that core temp or vram temp? My vram temp is 110, and my gut can feel its not right (i tracked it via gpu-z, under qwen 3.6 27b) anitamaxwynnn69 • 23d ago 8x 3090s here, just a heads up vram temp at 110 is a red flag. I'd check out what's going on. What type case are you using? Are the 3090s sitting too close to each other? How old are these cards? 110 means they ...
- **anitamaxwynnn69** (Score: 7): anitamaxwynnn69 • 23d ago 8x 3090s here, just a heads up vram temp at 110 is a red flag. I'd check out what's going on. What type case are you using? Are the 3090s sitting too close to each other? How old are these cards? 110 means they are actively getting throttled. You keep them at 110 for long and they're long term health is really suffering. Whole_Alternative_18 • 23d ago Its only one 3090, I...
- **Whole_Alternative_18** (Score: 2): Whole_Alternative_18 • 23d ago Its only one 3090, I've bought it recently from a guy who claimed "lighly used" Tempature climbs to 110 in like 5 mins The air flow is bad, but not bad enough to justify it Can you please share what you get on your own? My go-to repair man is suggesting we replace the heatsink and add 2 fans to the top lf it anitamaxwynnn69 • 23d ago My cards vary wildly but my worst...
- **anitamaxwynnn69** (Score: 4): anitamaxwynnn69 • 23d ago My cards vary wildly but my worst is my Dell OEM cards which go up to 104/105 on VRAM but stay steady after that. You should look into changing the thermal pads on the 3090s. It's very doable at home by yourself and it's heavily documented. It's like a 10-20$ process, if that doesn't fix it only then try the heatsink bc that sounds expensive. What vendor card is this? HP/...

### [Reduce your GPU power limit](https://www.reddit.com/r/LocalLLaMA/comments/1teqjjl/reduce_your_gpu_power_limit/)

**Post Summary:**
I'd like to note, I'm effectively a layman at this and have no idea what I'm talking about.
Inspired by another post, I wanted to do some testing on power limit adjustments impact on token processing and generation. I have no idea if this applies to more pro-hardware. But it's absolutely applicable on your gaming GPU! Just open up MSI afterburner from back in highschool when you thought you were going to overclock.
I believe the testing was with qwen3.5:9b, but it was a few days ago and I forgot to write it down.
The second image is data from testing adjustments to core and memory clocks. Very little impact, though if you're really trying to squeeze every last token out, increasing your memory clock by 700-1000mhz will improve token generation moderately across the board (did not test this at stock power limit, but now I'm curious). The only test I think could still be helpful, would be to log the actual power draw by the system, though that would only really be useful to see if adj

**Key Community Comments:**
- **iMrParker** (Score: 15): iMrParker • 3mo ago I feel like undervolting is always a smarter move. Much smaller performance hit with undervolt NotArticuno • 3mo ago Is this adjusting the voltage/frequency curve? I haven't played with this, as it looked more involved than just the single slider lol. Any advice would be appreciated! McSendo • 3mo ago From my experience, power spikes still happen even if you power limit. This i...
- **NotArticuno** (Score: 3): NotArticuno • 3mo ago Is this adjusting the voltage/frequency curve? I haven't played with this, as it looked more involved than just the single slider lol. Any advice would be appreciated! McSendo • 3mo ago From my experience, power spikes still happen even if you power limit. This is not captured in nvtop because it happens in less than a second. You need a wall meter to capture. NotArticuno • 3...
- **McSendo** (Score: 2): McSendo • 3mo ago From my experience, power spikes still happen even if you power limit. This is not captured in nvtop because it happens in less than a second. You need a wall meter to capture. NotArticuno • 3mo ago Yeah that was the one thing I didn't test that I really wanted to....
- **NotArticuno** (Score: 2): NotArticuno • 3mo ago Yeah that was the one thing I didn't test that I really wanted to....
- **trolololster** (Score: 3): trolololster • 3mo ago completely unscientific but i run my 3090 at 300w and my 3060 at 100w power-usage down by ~22% and inferencing down by ~4% and my cards never go above 50-60 degrees...

### [PSA: Throttle GPU power limits, with minor performance deficits](https://www.reddit.com/r/LocalLLaMA/comments/1u15qk3/psa_throttle_gpu_power_limits_with_minor/)

**Post Summary:**
I just feel i need to post this here again so more people see: Test around with throttling the power limits of your GPUs, you will often find that you can save tons of power with only minor performance deficits.
On my dual Radeon VII setup, i went from 250 to 100 watts per card, and the speeds diminished by not even 10%.
I just feel i need to post this here again so more people see: Test around with throttling the power limits of your GPUs, you will often find that you can save tons of power with only minor performance deficits.
On my dual Radeon VII setup, i went from 250 to 100 watts per card, and the speeds diminished by not even 10%.
PSA: the "speeds" original poster talking about is token generation not prompt processing, throttling GPU power will severily hit prompt processing speed: https://files.catbox.moe/gez0rd.png
But if you do not need to process large inputs then power limiting the GPU will be beneficial because token generation speed will not drop much.
I think it's th

**Key Community Comments:**
- **MelodicRecognition7** (Score: 9): MelodicRecognition7 • 2mo ago PSA: the "speeds" original poster talking about is token generation not prompt processing, throttling GPU power will severily hit prompt processing speed: https://files.catbox.moe/gez0rd.png But if you do not need to process large inputs then power limiting the GPU will be beneficial because token generation speed will not drop much. graypasser • 2mo ago I think it's ...
- **graypasser** (Score: 2): graypasser • 2mo ago I think it's the simple fact that, gpus ~70% of powers are used to improve final 20% of computational speed or something like that, so in principle it should work for both cases not that different....
- **milpster** (Score: 3): milpster • 2mo ago no. i was mainly focused on PP actually, since that has been my bottleneck. Throttling the way i mentioned my PP went from ~310 to ~295tps MelodicRecognition7 • 2mo ago then something is wrong with either AMD cards or with your particular setup, because with Nvidia cards the PP speed is linearly dependent on the power limit. tmvr • 2mo ago You'll need to define "severely hit", b...
- **MelodicRecognition7** (Score: -3): MelodicRecognition7 • 2mo ago then something is wrong with either AMD cards or with your particular setup, because with Nvidia cards the PP speed is linearly dependent on the power limit. tmvr • 2mo ago You'll need to define "severely hit", because that is tot what I see with my 4090. For example here are the results with Qwen3.6 35B A3B where going down to 270W (or 60% TGP) drops pp to 84% PL    ...
- **tmvr** (Score: 4): tmvr • 2mo ago You'll need to define "severely hit", because that is tot what I see with my 4090. For example here are the results with Qwen3.6 35B A3B where going down to 270W (or 60% TGP) drops pp to 84% PL            PP ------------------     100% (450W) = 100%  80% (360W) =  96%  70% (315W) =  93%  60% (270W) =  84% MelodicRecognition7 • 2mo ago I did not test MoE, here is 9B dense on 4090: ht...

### [Setting Power Limit on RTX 3090 – LLM Test](https://www.reddit.com/r/LocalLLaMA/comments/1k0mrrt/setting_power_limit_on_rtx_3090_llm_test/)

**Post Summary:**
Click here for Patient Info and additional Important Risk Info.
Applying a 72% power limit reduced the maximum power draw from 348W to 252W (a reduction of about 27-28%). This power reduction resulted in a performance decrease, dropping the generation speed from 29.69 tokens/s to 24.15 tokens/s (a reduction of about 18-19%).
(via Gemini Pro 2.5)
what's your prompt?
nvidia-smi -pl 250
Power limits you to 250w.
Easy
This has already been done. 300w is the best spot.
Depends on what you consider "best". I'm using an undervolted OC card with a 60% limit while being next to the machine, as the fans will run at lowest RPM and thus stay completely quiet then.
I consider 1% loss with as much power down as possible. 65w = 1% is good. Much quieter.
this is where i found to the the optimal trade off point too.
sudo nvidia-smi -i 0 -pl 300 on ubuntu
All these people who didn't just turn off turbo clocks.
The power limits supposedly still let it insta-spike.
I keep the 3 i have at 215W. works f

**Key Community Comments:**
- **Thomas-Lore** (Score: 12): Thomas-Lore • 1y ago Applying a 72% power limit reduced the maximum power draw from 348W to 252W (a reduction of about 27-28%). This power reduction resulted in a performance decrease, dropping the generation speed from 29.69 tokens/s to 24.15 tokens/s (a reduction of about 18-19%). (via Gemini Pro 2.5) Medium_Chemist_4032 • 1y ago what's your prompt?...
- **Medium_Chemist_4032** (Score: 1): Medium_Chemist_4032 • 1y ago what's your prompt?...
- **[deleted]** (Score: 5): [deleted] • 1y ago nvidia-smi -pl 250 Power limits you to 250w. Easy...
- **Linkpharm2** (Score: 9): Linkpharm2 • 1y ago This has already been done. 300w is the best spot. Chromix_ • 1y ago  Top 1% Commenter Depends on what you consider "best". I'm using an undervolted OC card with a 60% limit while being next to the machine, as the fans will run at lowest RPM and thus stay completely quiet then. Linkpharm2 • 1y ago I consider 1% loss with as much power down as possible. 65w = 1% is good. Much qu...
- **Chromix_** (Score: 7): Chromix_ • 1y ago  Top 1% Commenter Depends on what you consider "best". I'm using an undervolted OC card with a 60% limit while being next to the machine, as the fans will run at lowest RPM and thus stay completely quiet then. Linkpharm2 • 1y ago I consider 1% loss with as much power down as possible. 65w = 1% is good. Much quieter....

### [power limit your GPU(s) to reduce electricity costs](https://www.reddit.com/r/LocalLLaMA/comments/1n89wi8/power_limit_your_gpus_to_reduce_electricity_costs/)

**Post Summary:**
many people worry about high electricity costs, the solution is simply power limit the GPU to about 50% of its TDP (nvidia-smi -i $GPU_ID --power-limit=$LIMIT_IN_WATTS) because token generation speed does not increase past some power limit amount so you just waste electricity with the full power. As an example here is a result of llama-bench (pp1024, tg1024, model Qwen3-32B Q8_0 33 GB) running on RTX Pro 6000 Workstation (600W TDP) power limited from 150W to 600W in 30W increments. 350W is the best spot for that card which is obvious on the token generation speed chart, however the prompt processing speed rise is also not linear and starts to slow down at about 350W. And another example: the best power limit for 4090 (450W TDP) is 270W, tested with Qwen3 8B.
Update: did a better testing and published results here: https://old.reddit.com/r/LocalLLaMA/comments/1nkycpq/gpu_power_limiting_measurements_update/
many people worry about high electricity costs, the solution is simply power lim

**Key Community Comments:**
- **Hedede** (Score: 38): Hedede • 1y ago • Edited 1y ago the solution is simply power limit the GPU to about 50% of its TDP because token generation speed does not increase past some power limit amount so you just waste electricity with the full power. That is simply not true for all GPUs. You get improvements, but the scaling is not linear. For example, 3090 at 50% TDP (175W) delivers only ~35% of performance at full pow...
- **McSendo** (Score: 7): McSendo • 1y ago You can also play around with the offset, undervolts, fixed clocks in lact. I was able to get 90% performance in vllm while staying under 250 watts on the 3090. But power limiting is the easiest way for sure. VoidAlchemy • 1y ago llama.cpp Thanks for the tip! I just did a comparison and LACT is better than naieve `nvidia-smi -pl 400` so I did a quick write-up: https://forum.level1...
- **VoidAlchemy** (Score: 1): VoidAlchemy • 1y ago llama.cpp Thanks for the tip! I just did a comparison and LACT is better than naieve `nvidia-smi -pl 400` so I did a quick write-up: https://forum.level1techs.com/t/some-gpu-5090-4090-3090-a600-idle-power-consumption-headless-on-linux-fedora-42-and-some-undervolt-overclock-info/237064/6 DeltaSqueezer • 9mo ago Do you know of of a way of making these setting changes without usi...
- **DeltaSqueezer** (Score: 2): DeltaSqueezer • 9mo ago Do you know of of a way of making these setting changes without using the LACT tool? VoidAlchemy • 9mo ago llama.cpp in windows or linux? in windows you can use msi afterburner or evga precision x1 or whatever... in linux you can use LACT (even headless is fine for servers),or you'd have to likely build a script against either pynvml or nvidia's nvml api directly and pass t...
- **VoidAlchemy** (Score: 3): VoidAlchemy • 9mo ago llama.cpp in windows or linux? in windows you can use msi afterburner or evga precision x1 or whatever... in linux you can use LACT (even headless is fine for servers),or you'd have to likely build a script against either pynvml or nvidia's nvml api directly and pass the desired values yourself.. i have a talk up if you're interested convering some of this: https://blog.aifou...

### [48GB 4090 Power limiting tests 450, 350, 250w - Noise and LLM throughput per power level](https://www.reddit.com/r/LocalLLaMA/comments/1r96pgp/48gb_4090_power_limiting_tests_450_350_250w_noise/)

**Post Summary:**
The 48gb 4090's stock power is 450w but thats kind of alot for that 2 slot format where similar A100/6000Pro cards are 300w max for that format), so the fans really have to go (5k rpm blower) to keep it cool. Stacked in pcie slots the cards with less airflow intake can see upto 80C and all are noisy at 70dB (white noise type sound)
Below is just one model (deepseek 70b and gpt-oss were also tested and included in the github dump below, all models saw 5-15% performance loss at 350w (down from 450w)
Dual RTX 4090 48GB (96GB) — Qwen 2.5 72B Q4_K_M
                        450W    350W    300W    250W    150W
PROMPT PROCESSING (t/s)
  pp512                 1354    1241    1056     877     408
  pp2048                1951    1758    1480    1198     535
  pp4096                2060    1839    1543    1254     561
  pp8192                2043    1809    1531    1227     551
  pp16384               1924    1629    1395    1135     513
  pp32768               1685    1440    1215     995    

**Key Community Comments:**
- **brown2green** (Score: 7): brown2green • 6mo ago Try also playing around with core frequency limiting: nvidia-smi -lgc 0,xxxx where x is the maximum core frequency. You might find that you don't really need the last few hundred MHz where power requirements increase exponentially....
- **Traditional-Gap-3313** (Score: 1): Traditional-Gap-3313 • 6mo ago Anything similar in EU? HumanDrone8721 • 6mo ago • Edited 6mo ago Nope, the VAT and customs makes importing them not feasible and getting two retail 4090 and "frankenstein" them at current prices plus micro-soldering work is not worth as well. The issue is that US is a monstrous huge market and one gets actual cheap defective cards to harvest GPU and VRAM chips, not ...
- **HumanDrone8721** (Score: 3): HumanDrone8721 • 6mo ago • Edited 6mo ago Nope, the VAT and customs makes importing them not feasible and getting two retail 4090 and "frankenstein" them at current prices plus micro-soldering work is not worth as well. The issue is that US is a monstrous huge market and one gets actual cheap defective cards to harvest GPU and VRAM chips, not so much in EU. An RTX Pro 5000, 48GB latest Blackwell g...
- **debackerl** (Score: 2): debackerl • 6mo ago Got mine from eBay, customs were prepaid by carrier. I paid the official 21% Belgian tax rate. It was end of last year. The RTX Pro 5000 is €5000 for me (checked again on tweakers website), so my card was cheaper, good for you if you found it for €4560! HumanDrone8721 • 6mo ago For what price and what seller, all that I see on German EBAY is "we are not responsible of any taxes...
- **HumanDrone8721** (Score: 1): HumanDrone8721 • 6mo ago For what price and what seller, all that I see on German EBAY is "we are not responsible of any taxes", to make it worse an acquaintance had it confiscated at customs because it didn't have CE certification. I've long searched for someone that have them locally in EU, but never found anyboty and now they're not worth anymore. In case it helps someone, this is where they ha...

### [Can you run actually useful LLMs on anything less than 3090 ?](https://www.reddit.com/r/LocalLLaMA/comments/1sl3ztq/can_you_run_actually_useful_llms_on_anything_less/)

**Post Summary:**
I started my LLM self-hosting journey with a 1660 Ti (Bad Choice, I know)
I wanted to get started a bit quickly, and this was the first GPU that I could buy without breaking much bank
However, I soon realized that this is extremely under-powered. So I started looking for a GPU with more VRAM. I came across 3060, which seem to me a good balance between raw GPU performance & cost
Afterwards, I reached out to a colleague who is also very active in self-hosting LLMs. I told him that I got a 3060, and his first response is that it sucks. He is running his setup on a 3090, and is planning to get another one
Honestly, I don't consider myself a AI power-user. I'm mostly self-hosting it for my family, to provide them a more ethical choice to use AI as compared to commercial offerings, and also due to data & privacy concerns
But my main question is that for you LLM experts, is it possible to host a relatively useful LLM on a GPU with 12 GB VRAM ? I did some research before buying, and it se

**Key Community Comments:**
- **Momsbestboy** (Score: 8): Momsbestboy • 4mo ago • Edited 4mo ago 3060 is fine. You just need more time for waiting, until it has run a task. I am using Qwen3.5 35B A3B Q6, with offload to RAM, and while it really isn't fast, it gets the job done - for me: bash scripts, python scripts etc. I need them locally, and I am too lazy /too cautious to post them on ChatGPT, or filter privacy relevant data before uploading to GPT. W...
- **slimdizzy** (Score: 2): slimdizzy • 4mo ago llama.cpp FWIW GPU mining is effectively dead and when the 3000 series dropped Nvidia had them rate limited with only the founders edition getting BIOS hacks, if I recall directly as I used to mine ETH. Used 3090s should be fine less some crazy overclocking gamer. Makers7886 • 4mo ago 3090 mining died about a year after it's release (I bought 12 during that time for mining) wit...
- **Makers7886** (Score: 3): Makers7886 • 4mo ago 3090 mining died about a year after it's release (I bought 12 during that time for mining) with some stragglers holding on for another year or so. I upgraded all thermal pads (they are bad quality almost across the board) and they have all been flawless minus having to replace 2-3 fans total. The good thing about mining "wear" is that you typically downclock the core but OC th...
- **slimdizzy** (Score: 2): slimdizzy • 4mo ago llama.cpp Yep just as I remember then. Glad your cards are doing other work now!...
- **chopticks** (Score: 1): chopticks • 4mo ago What approx tokens/sec are you getting? I’m personally ok with around 10 so curious to see what you’re getting Momsbestboy • 4mo ago • Edited 4mo ago llama-bench -m ./Qwen3.5-35B-A3B-UD-Q6_K_XL.gguf -ncmoe 28 -ngl 99 -b 512  -t 8 -fa 1                                                              ggml_cuda_init: found 1 CUDA devices (Total VRAM: 12037 MiB): Device 0: NVIDIA GeFo...

### [RTX3090 Power Tuning Results on LLM, Vision, TTS, and Diffusion](https://www.reddit.com/r/LocalLLaMA/comments/1egvoqj/rtx3090_power_tuning_results_on_llm_vision_tts/)

**Post Summary:**
I wanted to share some results I have from running an RTX3090 across it's power limit range on a variety of inference tasks including LLM, Vision Models, Text to Speech, and Diffusion.
Before I get into the results and discussion I have a whole video on this subject if you prefer that form: https://www.youtube.com/watch?v=vshdD1Q0Mgs
TLDR/W:
Turn your power limit on your 3090 down to 250W-300W. You will get excellent performance and save 100W of power by doing so. Depending on your inference task you might be able to get away with much lower still.
Data
I collected a ton of data. Go check it out yourself here: https://benchmarks.andromeda.computer/videos/3090-power-limit
I'll point out some of the more interesting results:
* llama3-8B - dual chart, generate tps and generate tps/watt. also ttft (time to first token)
* gemma2-27B - dual chart, generate tps and generate tps/watt. also ttft (time to first token)
* sdxl-base-1.0 - dual chart, compute time to image, avg iter/sec/wat

**Key Community Comments:**
- **Necessary-Donkey5574** (Score: 16): Necessary-Donkey5574 • 2y ago Tokens per Joule (tps/w) interests me! Thanks for your work. I like knowing I’m getting a boost in efficiency. sipjca • 2y ago no problem, glad it's helpful :)...
- **sipjca** (Score: 5): sipjca • 2y ago no problem, glad it's helpful :)...
- **gofiend** (Score: 9): gofiend • 2y ago Just to add on to this, I've found that you can idle your GPU (3090 in my case also) down to ~30-40W even with a model fully loaded into RAM. Makes leaving 2-3 small models (for specific usecases) in VRAM at all times very viable. sipjca • 2y ago Yeah, this is a great point. I am doing this as well, and actually very interested in testing concurrency of small models at the same ti...
- **sipjca** (Score: 5): sipjca • 2y ago Yeah, this is a great point. I am doing this as well, and actually very interested in testing concurrency of small models at the same time. Something like moondream2 + whisper + llama3 8b concurrently....
- **aarongough** (Score: 3): aarongough • 2y ago I found the same with llama.cpp and Aphrodite, idle power usage even with a model loaded is very low which is great!  How are you loading multiple models into VRAM at the same time? gofiend • 2y ago Transformers + python sipjca • 2y ago I’m running llamafile/whisperfile servers on different ports! A bunch of individual ones...

### [Maybe KV cache offload to RAM isn't bad](https://www.reddit.com/r/LocalLLaMA/comments/1txpqru/maybe_kv_cache_offload_to_ram_isnt_bad/)

**Post Summary:**
So, llama.cpp has the -nkvo (--no-kv-offload) option to offload KV cache to RAM instead of VRAM. Many people avoid this because obviously it hurts performance.
But every option exists with a trade off. And in my case, I think it's worth it. Hear me out.
I'm running Qwen3.6 27B (IQ4_XS) on RTX 5060 Ti 16GB and 32GB DDR5. In order to fit 65k context, I have to quantize the KV cache down to q4_0, and keep only 58 layers on the GPU. This gives me 23 tps at peak, down to 16 tps during long generation.
llama-server -m Qwen3.6-27B-IQ4_XS.gguf -c 65000 \
	-ctk q4_0 -ctv q4_0 -fa on -ngl 58 -np 1 \
	--temp 0.6 --top-p 0.95 --top-k 20 --presence-penalty 1.25 \
	--min-p 0.0 --chat-template-kwargs '{"preserve_thinking":true}' \
	--spec-type draft-mtp --spec-draft-n-max 2
Adding -nkvo, I'm able to fit the whole model in GPU, and have the default f16 for KV cache. The speed plunged to 19 tps at peak, and 14 tps during long generation. Not a bad trade off.
llama-server -m Qwen3.6-27B-IQ4_XS.gguf

**Key Community Comments:**
- **JournalistLucky5124** (Score: 23): JournalistLucky5124 • 3mo ago With qwen 3 4B instruct 2507, all 36 layers in my gtx 1650 mobile and kv on ran(unquantized) at 64000 i get around 16 tokens/s on my lm studio Ram is ddr4 btw bobaburger • 3mo ago 16 tps is impressive for a 4GB card! lack_of_reserves • 3mo ago It's a 4b model. JournalistLucky5124 • 3mo ago Is it??(my unquatized kv at 64000, yes exactly, is on system ram). Plus im usin...
- **bobaburger** (Score: 9): bobaburger • 3mo ago 16 tps is impressive for a 4GB card! lack_of_reserves • 3mo ago It's a 4b model. JournalistLucky5124 • 3mo ago Is it??(my unquatized kv at 64000, yes exactly, is on system ram). Plus im using q6 k xl gguf bobaburger • 3mo ago I think so, maybe you can try to run 9B on that card too (q4 or something below, but still enough to see the different). JournalistLucky5124 • 3mo ago I ...
- **lack_of_reserves** (Score: 3): lack_of_reserves • 3mo ago It's a 4b model....
- **JournalistLucky5124** (Score: 1): JournalistLucky5124 • 3mo ago Is it??(my unquatized kv at 64000, yes exactly, is on system ram). Plus im using q6 k xl gguf bobaburger • 3mo ago I think so, maybe you can try to run 9B on that card too (q4 or something below, but still enough to see the different). JournalistLucky5124 • 3mo ago I also run gemma 4 26b a4b at 16384(idr if kv is on ram or gpu) and i get like 7-9 tps with abt 9 layers...
- **bobaburger** (Score: 1): bobaburger • 3mo ago I think so, maybe you can try to run 9B on that card too (q4 or something below, but still enough to see the different). JournalistLucky5124 • 3mo ago I also run gemma 4 26b a4b at 16384(idr if kv is on ram or gpu) and i get like 7-9 tps with abt 9 layers offloaded so idk if thats good too All r on lm studio btw, no mtp...

### [Context, memory, and RAM/VRAM](https://www.reddit.com/r/LocalLLaMA/comments/1tzdp7b/context_memory_and_ramvram/)

**Post Summary:**
This will be a slightly disorganized post, I apologize.
I’m trying to understand the relationship between context, a memory system for the agent, RAM and VRAM.
What I’ve been observing while watching my system performance while using an LLM with pi isn’t what I was expecting, so I’m looking for some clarification. 
I’m running Qwen 27B q4_k_M, using llama.cpp with pi as my harness. I have the pi extension Hermes-memory going along with it (from the pi website). I’m using Q8 for kv cache, and if I’m remembering right getting about 150k context loaded when I load the model in llama.cpp.
However, when running the model, as my cache starts to fill up my RAM starts to fill up. I was under the impression that a certain amount of VRAM was allocated on model load for the cache. I’ll be at 35% used cache and will have added 3-4gb of RAM usage and if I’m not paying attention I’ll OOM myself just for system RAM usage. 
I don’t know if this has any relation to my memory extension or not. I’m 

**Key Community Comments:**
- **wombweed** (Score: 4): wombweed • 3mo ago i have noticed this behavior on my machines too, i think it's actually prompt caching that does this -- keeping the earlier parts of the context "precomputed" in ram so that it doesnt have to redo the entire thing from the beginning every time you send a message or complete a tool call. UniqueIdentifier00 • 3mo ago Maybe so! I suspect it’s something like that, I’m just not sure ...
- **UniqueIdentifier00** (Score: 1): UniqueIdentifier00 • 3mo ago Maybe so! I suspect it’s something like that, I’m just not sure how to verify exactly what is getting loaded to RAM during inference...
- **PepSakdoek** (Score: 2): PepSakdoek • 3mo ago The vram is kind of more important than normal ram and upgrading normal ram might do OK, but the vram is the real bottle neck and you can't order more vram...  UniqueIdentifier00 • 3mo ago Well, I have a 3060 8gb card that’s laying around. I have an upgraded PSU coming along with my RAM so that I can use it along with my 3090, so that will also help. I just didn’t realize that...
- **UniqueIdentifier00** (Score: 1): UniqueIdentifier00 • 3mo ago Well, I have a 3060 8gb card that’s laying around. I have an upgraded PSU coming along with my RAM so that I can use it along with my 3090, so that will also help. I just didn’t realize that cache would be loaded to RAM at all honestly. May be my llama command I’m not sure. PepSakdoek • 3mo ago Yes if you can install both you win 8gb ram as well as some inference. Buuu...
- **PepSakdoek** (Score: 2): PepSakdoek • 3mo ago Yes if you can install both you win 8gb ram as well as some inference. Buuuut it's a lot more complex (I have no idea how to do those things but maybe one of the online llms can help you)....

### [I need some realistic expectations about 1x 3090](https://www.reddit.com/r/LocalLLaMA/comments/1vm2j42/i_need_some_realistic_expectations_about_1x_3090/)

**Post Summary:**
with a single 3090, what sort of speeds, quants and context lengths should i realistically expect out of qwen 3.6 27b? ive been to a few benchmark sites and the speeds look good, until i drill into the recipe and realise they are using 1024 contexts and things of the like. i think i may have set myself some unrealistic expectations of what i can achieve
with a single 3090, what sort of speeds, quants and context lengths should i realistically expect out of qwen 3.6 27b? ive been to a few benchmark sites and the speeds look good, until i drill into the recipe and realise they are using 1024 contexts and things of the like. i think i may have set myself some unrealistic expectations of what i can achieve
Maximum I’m able to get is 160k at q8 kv and q4 model quant
what speeds?
50-60 tokens per second.
Yep, about what I've seen when running on a single card
Realistically need two to have a solid experience
OP, i'm running exactly this setup right now, here are real numbers from 

**Key Community Comments:**
- **sisyphus-cycle** (Score: 7): sisyphus-cycle • 10d ago Maximum I’m able to get is 160k at q8 kv and q4 model quant oldschooldaw • 10d ago what speeds? Civil_Fee_7862 • 10d ago 50-60 tokens per second. sdfgeoff • 10d ago Yep, about what I've seen when running on a single card...
- **oldschooldaw** (Score: 2): oldschooldaw • 10d ago what speeds? Civil_Fee_7862 • 10d ago 50-60 tokens per second....
- **Civil_Fee_7862** (Score: 6): Civil_Fee_7862 • 10d ago 50-60 tokens per second....
- **sdfgeoff** (Score: 2): sdfgeoff • 10d ago Yep, about what I've seen when running on a single card...
- **ThenExtension9196** (Score: 15): ThenExtension9196 • 10d ago Realistically need two to have a solid experience [deleted] • 10d ago...

### [How to improve RAM offload?](https://www.reddit.com/r/LocalLLaMA/comments/1ukrjxa/how_to_improve_ram_offload/)

**Post Summary:**
I have only 12GB VRAM (RTX3060) but have enough RAM to run Qwen3.6 27B Q4 with offload. Something tells me that it won't achieve maximum performance but why DRAM speed is only around 30GB/s (HWiNFO data) during inference with dual channel 5200 RAM? TG is 3.12 tok/sec with 18K tokens result.
I expected slow speed, but can't understand where is the bottleneck, is it how LM Studio works or I need better CPU (I have 7500F). Of course dual 3090 will do the work, but it is what is for now.
Tried smaller prompt with 6 CPU threads, Q8 KV cache, 37 GPU offload, got TG 4.95 tok/sec and bandwidth was 30-35GB/s.
I have only 12GB VRAM (RTX3060) but have enough RAM to run Qwen3.6 27B Q4 with offload. Something tells me that it won't achieve maximum performance but why DRAM speed is only around 30GB/s (HWiNFO data) during inference with dual channel 5200 RAM? TG is 3.12 tok/sec with 18K tokens result.
I expected slow speed, but can't understand where is the bottleneck, is it how LM Studio works or

**Key Community Comments:**
- **slalomz** (Score: 15): slalomz • 2mo ago llama.cpp If you offload layers of a dense model your performance is going to be heavily bottlenecked by your RAM's bandwidth. Your inputs: VRAM_BW: 360 GB/s RAM_BW: 60 GB/s ModelSize: 21.22 GB PCT_VRAM = 11.28/21.22 = 0.53 (percentage of the model you're fitting in VRAM) With no offloading: Dense: tg/s = VRAM_BW / ModelSize MoE: tg/s = VRAM_BW / (ModelSize * ActiveRatio) For you...
- **esw123** (Score: 1): esw123 • 2mo ago • Edited 2mo ago Thank you. I've came up to 4.95 tok/sec but I don't understand why RAM bandwidth is at around 30 GB/s and not 50GB/s+ is it due to the size of model, constant jumps from RAM to VRAM or what? MoE Qwen3.5 122B gave me 3.97 tok/sec on small prompt as well with 30GB/s RAM bandwidth. Only comment I found was on forum that this is normal behavior to get 30% of RAM bandw...
- **slalomz** (Score: 4): slalomz • 2mo ago llama.cpp Try Qwen3.6 35B. esw123 • 2mo ago • Edited 2mo ago 21.43 tok/sec. Update: 20K tokens reply @ 14.84 tok/sec. For my use case I don't see a big difference from 27B. luee29 • 2mo ago I have similar specs, 12GB VRAM + 64GB DDR5-RAM, but I use llama.cpp server and get around 35tok/s with a q6 35b. Maybe with a MTP model you would get even more tok/s but the gain here falls o...
- **esw123** (Score: 2): esw123 • 2mo ago • Edited 2mo ago 21.43 tok/sec. Update: 20K tokens reply @ 14.84 tok/sec. For my use case I don't see a big difference from 27B. luee29 • 2mo ago I have similar specs, 12GB VRAM + 64GB DDR5-RAM, but I use llama.cpp server and get around 35tok/s with a q6 35b. Maybe with a MTP model you would get even more tok/s but the gain here falls off the more you have to offload to RAM. If yo...
- **luee29** (Score: 3): luee29 • 2mo ago I have similar specs, 12GB VRAM + 64GB DDR5-RAM, but I use llama.cpp server and get around 35tok/s with a q6 35b. Maybe with a MTP model you would get even more tok/s but the gain here falls off the more you have to offload to RAM. If you are interested, here is my loading command: llama-server.exe \ --host <private-endpoint> \ --port 8881 \ --model <MODELPATH>/Ornith-1.0-35B-heretic-Q6_K....

### [This is amazing. Token speed doubled + kv cache now need low vram - qwen 27b](https://www.reddit.com/r/LocalLLaMA/comments/1u6bca1/this_is_amazing_token_speed_doubled_kv_cache_now/)

**Post Summary:**
Edited : "Qwen3.6-27B Q4_K_M on a single RTX 3090: native 256K context at 38.6 tok/s with 72 MiB of resident KV, needle recall 88-100% at 6% residency, harness accuracy unchanged (36/36 vs full cache)."
On the same hardware, generation speeds doubled and VRAM usage dropped significantly (21GB to 17.5GB) while maintaining full context accuracy
Yt video of fahd --> https://youtu.be/8rTVCRWvRDo?si=MYiVrQQltbSsMAOP
Link to git hub - https://github.com/Luce-Org/lucebox-hub/tree/main/optimizations/kvflash
Quality loss?? --> "Quality verdict (harness ground truth, base-vs-base control included): full results in RESULTS.md. Outputs are not guaranteed byte-identical to the full cache on long generations (the masked kernel path rounds differently — a different deterministic lineage), but correctness is identical: 36/36 vs 36/36 across HumanEval, GSM, MATH, and agent suites."
Edited : "Qwen3.6-27B Q4_K_M on a single RTX 3090: native 256K context at 38.6 tok/s with 72 MiB of resident KV, needl

**Key Community Comments:**
- **neuroticnetworks1250** (Score: 75): neuroticnetworks1250 • 2mo ago  Top 1% Commenter Anyone has any idea why AI generated explanation videos and images all follow this layout? Is it because most explanation videos did the same? Comfortable_Ebb7015 • 2mo ago It is a trend. AI were trained to make guis like this. If you ask qwen to vibecodeca frontend, it will do it like this. Gemma does it more "google style", less neon SkyFeistyLlam...
- **Comfortable_Ebb7015** (Score: 33): Comfortable_Ebb7015 • 2mo ago It is a trend. AI were trained to make guis like this. If you ask qwen to vibecodeca frontend, it will do it like this. Gemma does it more "google style", less neon SkyFeistyLlama8 • 2mo ago Very Gradio?...
- **SkyFeistyLlama8** (Score: 6): SkyFeistyLlama8 • 2mo ago Very Gradio?...
- **Technical_Hawk_2664** (Score: 10): Technical_Hawk_2664 • 2mo ago "fahd mirza" in the video.... It's all he ever does in his videos. He just 'installs' something in each video.....but doesnt ever tell you WHY you would want to install and use it, or what to do with it. Face/palm." His Channel is complete clickbait. As soon as I saw the video was his = closed the tab immediately. Shoddy-Tutor9563 • 2mo ago He has 600k subs (+100k sin...
- **Shoddy-Tutor9563** (Score: 4): Shoddy-Tutor9563 • 2mo ago He has 600k subs (+100k since last week)... and just a dozen of comments under his videos. He's definitely astroturfing his ego Technical_Hawk_2664 • 2mo ago Shoddy-Tutor9563- Ya. I've 'thumbed' down every video that he has on youtube served up to me. On the odd days that I actually 'google' something, he may show up in the results via his click bait titles. He has a for...

### [It's OK to quantize the KV cache. Model quant matters more. Some Qwen3.6 27B tests with (approximated) KLD](https://www.reddit.com/r/LocalLLaMA/comments/1tlwjsl/its_ok_to_quantize_the_kv_cache_model_quant/)

**Post Summary:**
mildly clickbait title but oh well, too late to change it
EDIT: redid KLD measurements against Q8 with better dataset, included outlier stats.
I've seen a lot of discussion here about KV-cache quantization, especially with the recent llama.cpp improvements, leading to some debate on the tradeoffs between KV quantization vs weight quantization.
Frustratingly, I haven't really seen any comparisons backed by data. At least not any comparisons that help me find the crossover point where cache quantization hurts more than going down a weight quant level (Q5 -> Q4).
I guess part of the reason is that KL-Divergence is expensive to compute, because you need logits from the original unquantized model... or do you?
KLD is just a measure of how similar one probability distribution is to another, so we can approximate the true KLD using a high quality quant as a proxy. So I did that with Qwen3.6 27B Q8_0 using the llama-perplexity tool that comes with llama.cpp.
I'm using unsloth's quants fo

**Key Community Comments:**
- **Finanzamt_Endgegner** (Score: 26): Finanzamt_Endgegner • 3mo ago kld is not enough to test kv cache quantization, you need tail kld too, thats where kv cache quantization breaks apart if its too aggressive. FatheredPuma81 • 3mo ago Exactly: llama : rotate activations for better quantization by ggerganov · Pull Request #21038 · ggml-org/llama.cpp hopbel • 3mo ago • Edited 3mo ago Are you aware of any tool that can measure that? edit...
- **FatheredPuma81** (Score: 2): FatheredPuma81 • 3mo ago Exactly: llama : rotate activations for better quantization by ggerganov · Pull Request #21038 · ggml-org/llama.cpp...
- **hopbel** (Score: 2): hopbel • 3mo ago • Edited 3mo ago Are you aware of any tool that can measure that? edit: main post updated to include P90 and P99.9 KLD outliers Finanzamt_Endgegner • 3mo ago Not 100% sure if llama.cpp or whatever you use exposed it but it's calculated the same way normal kld is just checks the outliers basically hopbel • 3mo ago It already logs stuff like 90th and 99.9th percentile KLD. I can inc...
- **Finanzamt_Endgegner** (Score: 1): Finanzamt_Endgegner • 3mo ago Not 100% sure if llama.cpp or whatever you use exposed it but it's calculated the same way normal kld is just checks the outliers basically hopbel • 3mo ago It already logs stuff like 90th and 99.9th percentile KLD. I can include those after I redo the measurements. Finanzamt_Endgegner • 3mo ago Yeah that's exactly what I mean (;...
- **hopbel** (Score: 3): hopbel • 3mo ago It already logs stuff like 90th and 99.9th percentile KLD. I can include those after I redo the measurements. Finanzamt_Endgegner • 3mo ago Yeah that's exactly what I mean (;...

### [Best use cases for a mismatched RTX 3090 (24GB) + RTX 3060 (12GB) setup?](https://www.reddit.com/r/LocalLLaMA/comments/1spennl/best_use_cases_for_a_mismatched_rtx_3090_24gb_rtx/)

**Post Summary:**
Hey everyone, I have a system with 32GB of system RAM and two GPUs:
​RTX 3090 (24GB) in the primary fast PCIe slot
​RTX 3060 (12GB) in a secondary, slower PCIe slot
​I'm assuming that splitting a single large model across both cards is a bad idea because the slow PCIe slot on the 3060 will severely bottleneck the generation speed.
​With that in mind, is this setup practical for running distinct applications simultaneously?. Or is it not worth the headache and I should just use the 3090 24GB for everything?
Hey everyone, I have a system with 32GB of system RAM and two GPUs:
​RTX 3090 (24GB) in the primary fast PCIe slot
​RTX 3060 (12GB) in a secondary, slower PCIe slot
​I'm assuming that splitting a single large model across both cards is a bad idea because the slow PCIe slot on the 3060 will severely bottleneck the generation speed.
​With that in mind, is this setup practical for running distinct applications simultaneously?. Or is it not worth the headache and I should just us

**Key Community Comments:**
- **Adventurous-Paper566** (Score: 11): Adventurous-Paper566 • 4mo ago • Edited 4mo ago With only 2 GPUs, the PCI slot speed only impacts model loading and prompt processing. The inference speed is almost not affected. It would be a shame not to take advantage of your 32Gb. chucrutcito • 4mo ago I thought having a card on the slow slot affected the inference speed of both cards if i load a big model on both cards Adventurous-Paper566 • ...
- **chucrutcito** (Score: 2): chucrutcito • 4mo ago I thought having a card on the slow slot affected the inference speed of both cards if i load a big model on both cards Adventurous-Paper566 • 4mo ago Your PCI slot limits VRAM loading, but during inference, the exchange file between GPUs is so small that even a PCIe 3.0 x1 slot is more than sufficient. chucrutcito • 4mo ago Thanks very much! I didn’t know that! Adventurous-P...
- **Adventurous-Paper566** (Score: 10): Adventurous-Paper566 • 4mo ago Your PCI slot limits VRAM loading, but during inference, the exchange file between GPUs is so small that even a PCIe 3.0 x1 slot is more than sufficient. chucrutcito • 4mo ago Thanks very much! I didn’t know that! Adventurous-Paper566 • 4mo ago Have fun 👍 rainbyte • 4mo ago That's true when using split by layer or pipeline parallel setup, but tensor parallel setup n...
- **chucrutcito** (Score: 3): chucrutcito • 4mo ago Thanks very much! I didn’t know that! Adventurous-Paper566 • 4mo ago Have fun 👍...
- **Adventurous-Paper566** (Score: 1): Adventurous-Paper566 • 4mo ago Have fun 👍...

### [vLLM: offload KV cache for long context?](https://www.reddit.com/r/LocalLLaMA/comments/1qkqf2i/vllm_offload_kv_cache_for_long_context/)

**Post Summary:**
Problem: 2x3090 not enough to handle extremely long context lengths in vLLM.
The additional 1x 5060 is not helpful for doing tensor parallelism with the others, obviously. And buying two more 3090s is not feasible at this point.
But, is there a way to offload some of the KV cache to the 5060 while using the 3090s in TP 2 so the context can fit?
Problem: 2x3090 not enough to handle extremely long context lengths in vLLM.
The additional 1x 5060 is not helpful for doing tensor parallelism with the others, obviously. And buying two more 3090s is not feasible at this point.
But, is there a way to offload some of the KV cache to the 5060 while using the 3090s in TP 2 so the context can fit?
I don't think you want to offload KV cache to a different GPU. KV cache needs to stay close to compute, or your throughput will be terrible. It's like outsourcing your short term memory and prioperception to your friend - does not make sense. You can offload it only if you want to store KV cache of va

**Key Community Comments:**
- **FullOf_Bad_Ideas** (Score: 2): FullOf_Bad_Ideas • 7mo ago  Top 1% Commenter I don't think you want to offload KV cache to a different GPU. KV cache needs to stay close to compute, or your throughput will be terrible. It's like outsourcing your short term memory and prioperception to your friend - does not make sense. You can offload it only if you want to store KV cache of various concurrent users where you then load it back in...
- **TheJrMrPopplewick** (Score: 2): TheJrMrPopplewick • 7mo ago I don't think there's an easy benefit to doing this. You will be shipping kvcache back and forth constantly because the kvcache is written to (growing) and being read-from constantly. That introduces latency and likely cancels out the benefit of the fast video memory....
- **AllTheCoins** (Score: 1): AllTheCoins • 7mo ago I could be way off here but, I think you need 1 more 5060 to take advantage of tensor parallelism, 3 GPUs throws everything off balance I think? FrozenBuffalo25 • 7mo ago That’s correct and understood. I am wanting to partly offload KV cache to the 5060 only, while using the 3090s for Tensor Parallelism. AllTheCoins • 7mo ago Ohhh I got ya. Have you looked into RAM offload? I...
- **FrozenBuffalo25** (Score: 1): FrozenBuffalo25 • 7mo ago That’s correct and understood. I am wanting to partly offload KV cache to the 5060 only, while using the 3090s for Tensor Parallelism. AllTheCoins • 7mo ago Ohhh I got ya. Have you looked into RAM offload? I’ve heard about it getting better?...
- **AllTheCoins** (Score: 1): AllTheCoins • 7mo ago Ohhh I got ya. Have you looked into RAM offload? I’ve heard about it getting better?...

### [A 2.6B model with tool calling and 128K context now runs at 30 tok/s on a phone](https://www.reddit.com/r/LocalLLaMA/comments/1vfn9vc/a_26b_model_with_tool_calling_and_128k_context/)

**Post Summary:**
Liquid AI released LFM2.5-2.6B today, and this might be more relevant to local AI than another massive model most people cannot run.
The model is only 2.69B parameters, has 128K context, supports tool calling and was post-trained specifically for multi-step agent workflows. The official Q4_K_M GGUF is around 1.67 GB and already works with llama.cpp.
Their reported CPU speeds:
- 30 tok/s on a phone
- 113 tok/s on a Ryzen AI Max+ 395
- 220 tok/s on an M5 Max
- Under 2.5 GB memory during their tests
These are vendor benchmarks, so independent results are obviously needed.
The benchmark results are surprisingly competitive for the size:
- ToolSandbox: 77.83, compared with 76.44 for Qwen3.5-9B
- IFBench: 59.17, compared with 56.47 for Qwen3.5-9B
- BFCLv4: 56.88, still behind Qwen3.5-9B at 60.13
- LiveCodeBench: 59.41, compared with 69.86 for Qwen3.5-9B
So it does not magically replace larger models. Coding and knowledge-heavy work are still weaknesses, and Liquid’s own model ca

**Key Community Comments:**
- **Kidplayer_666** (Score: 69): Kidplayer_666 • 18d ago • Edited 17d ago the tool calling is consistent, can run it well on my rx 6650xt, however, it is still kind of dumb (failing my "find files related to the first year of my bachelors" task, despite on the documents folder there being a Folder named Bachelors in my native language (supported by the model) with yearly folders inside) Edit: partly my skill issue, trying the pro...
- **BTA_Labs** (Score: 19): BTA_Labs • 18d ago Good to know, that pretty much confirms the benchmarks don’t tell the whole story. MoffKalast • 17d ago Well it is getting compared against other drooling smol brains so even if they do, the absolute bar is relatively low....
- **MoffKalast** (Score: 3): MoffKalast • 17d ago Well it is getting compared against other drooling smol brains so even if they do, the absolute bar is relatively low....
- **NigaTroubles** (Score: 4): NigaTroubles • 18d ago What your run args ? Kidplayer_666 • 17d ago default for llamacpp.... oops, this might be the issue... any recommendations?...
- **Kidplayer_666** (Score: 4): Kidplayer_666 • 17d ago default for llamacpp.... oops, this might be the issue... any recommendations?...

### [How much Vram does the kvcache use at 60k or 120k context?](https://www.reddit.com/r/LocalLLaMA/comments/1r1941o/how_much_vram_does_the_kvcache_use_at_60k_or_120k/)

**Post Summary:**
Hi, I’m a total noob and would like to find out if anyone knows how much GRAM the flagship model needs for its kvcache at different context lengths. I have an M3 ultra with 512GB RAM. thank you for any help, I tried looking at it up couldnt find anything specific and Gemini estimates around 80GB for 128k which… sounds very low
Hi, I’m a total noob and would like to find out if anyone knows how much GRAM the flagship model needs for its kvcache at different context lengths. I have an M3 ultra with 512GB RAM. thank you for any help, I tried looking at it up couldnt find anything specific and Gemini estimates around 80GB for 128k which… sounds very low
Depends on the model size and architecture.
You can use something like this to get an idea: https://apxml.com/tools/vram-calculator
yeah I tried and according to that I can barely fit 10k context that can't be right
80 GB, depending on the model, do sound about right. might be less actually. i'm not sure if running 128k context is worth it 

**Key Community Comments:**
- **cakemates** (Score: 4): cakemates • 6mo ago Depends on the model size and architecture. You can use something like this to get an idea: https://apxml.com/tools/vram-calculator Aware_Studio1180 • 6mo ago yeah I tried and according to that I can barely fit 10k context that can't be right...
- **Aware_Studio1180** (Score: 2): Aware_Studio1180 • 6mo ago yeah I tried and according to that I can barely fit 10k context that can't be right...
- **LagOps91** (Score: 1): LagOps91 • 6mo ago 80 GB, depending on the model, do sound about right. might be less actually. i'm not sure if running 128k context is worth it at all, since most models start degrading after 32k context and degrade quite sharply after 64k context. Aware_Studio1180 • 6mo ago hmm well allegedly GLM 4.7 is good at long context but yeah that remains to be seen LagOps91 • 6mo ago GLM 4.7 has relative...
- **Aware_Studio1180** (Score: 1): Aware_Studio1180 • 6mo ago hmm well allegedly GLM 4.7 is good at long context but yeah that remains to be seen LagOps91 • 6mo ago GLM 4.7 has relatively light context. long context performance should be decent, but i would also not go past 64k unless i really had to....
- **LagOps91** (Score: 1): LagOps91 • 6mo ago GLM 4.7 has relatively light context. long context performance should be decent, but i would also not go past 64k unless i really had to....

