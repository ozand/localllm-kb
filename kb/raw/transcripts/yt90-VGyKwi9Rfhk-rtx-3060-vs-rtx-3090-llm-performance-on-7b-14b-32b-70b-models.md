---
source_url: https://www.youtube.com/watch?v=VGyKwi9Rfhk
video_id: VGyKwi9Rfhk
uploader: "BlueSpork"
title: "RTX 3060 vs RTX 3090: LLM Performance on 7B, 14B, 32B, 70B Models"
captured_date: 2026-08-26
status: raw_capture
provenance: youtube_video_transcript
research_run: youtube-local-llm-2026-08
---

# RTX 3060 vs RTX 3090: LLM Performance on 7B, 14B, 32B, 70B Models

first test uses deep seek R1 distilled Quin 7B model an Nvidia RTX 3060 with 12 GB of vram on the left part of the screen and an Nvidia RTX 3090 with 24 GB of vram on the right both examples are running on the same computer with 128 GB of RAM and a ryzen 5,800 x CPU the RTX 3060 example inference speed is 5064 tokens per second while the RTX 390 speed is 10.76 tokens per second moving on to the second test this time with the 54 14b model this model fully fits into vram on both gpus just like the previous 7B model the RTX 360 inference speed is 28.97 tokens per second while the RTX 390 speed is 6060 tokens per second now for the Third test we have qwq 32b this model does not fit completely into the 3060 GPU vram so it partially offloads weights into system Ram while it fully fits into the 39 DV Ram qwq 32b is a reasoning model known for often overthinking so its response was much longer than other models in this video I'll let the 3090 finish the answer since it's faster but I'll cut part of the 3060 response because it's too long e [Music] the RTX 360 inference speed is 2.04 tokens per second while the RTX 3090 speed is 28.7 to tokens per second for the last test we're using llama 3.3 70b model this model doesn't fit into either gpus vram so it partially offloads weights into system RAM for both examples this substantially slows down the inference speed since this will take a while to complete I'll cut the response in both examples so we don't wait too long the RTX 3060 inference speed is 0.70 speed is 1.10 tokens per second deep seek R1 distilled quen 7B ran 1.99 times faster on the RTX 3090 the model fits entirely in vram on both gpus allowing both to deliver strong performance 544b fits entirely in vram on the RTX 3060 and RTX 390 avoiding offloading the RTX 390 was 2.09 times faster quen 32b is too large for the RTX 360s vram forcing it to offload a significant portion of the model to system Ram drastically reducing speed the RTX 390 loads the entire model into vram avoiding offloading and running 14.8 times faster llama 337b exceeds the vram capacity of both gpus requiring offloading to system Ram as a result both experience a significant slowdown with the RTX 3090 running only 1.57 times faster than the
