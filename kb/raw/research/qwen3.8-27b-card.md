# Raw Capture: Unsloth Qwen3.8-27B-GGUF Model Card & Hardware Specs

- Source: https://huggingface.co/unsloth/Qwen3.8-27B-GGUF
- Date Captured: 2026-04-18
- Upstream Commit: `4ca720788d1e01f1bff70c033e0d0028fd02e502`

## Architecture Highlights
- Hybrid Attention architecture: 64 layers organized as $16 \times (3 \times (\text{Gated DeltaNet} \to \text{FFN}) \to 1 \times (\text{Gated Attention} \to \text{FFN}))$.
- DeltaNet linear attention significantly cuts compute and memory complexity on long contexts.
- Native Multi-Token Prediction (MTP) layer enables self-speculative decoding (draft-MTP) without needing an external draft model, boosting generation speed by ~30-60% in llama.cpp / unsloth.
- Context window: 262,144 tokens native (up to 1M with YaRN RoPE scaling).
- Multimodal support: Native multimodal vision/video capabilities supported when paired with compatible `mmproj` tensor.

## Recommended Sampling Settings

### Thinking Mode (Default)
```json
{
  "temperature": 1.0,
  "top_p": 0.95,
  "top_k": 20,
  "min_p": 0.0,
  "presence_penalty": 0.0,
  "repetition_penalty": 1.0
}
```

### Non-Thinking / Instruct Mode
```json
{
  "temperature": 0.7,
  "top_p": 0.80,
  "top_k": 20,
  "min_p": 0.0,
  "presence_penalty": 1.5,
  "repetition_penalty": 1.0
}
```

### Recommended Token Limits
- Reasoning Tokens: Up to 262,144
- Output Tokens: Up to 131,072
