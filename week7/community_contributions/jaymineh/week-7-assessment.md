# Week 7 Assessment — Beat the Instructor (MAE 39.85)

**By:** Jaymineh  
**Dataset:** `ed-donner/items_lite`  
**Model:** Qwen 2.5 3B (QLoRA fine-tuned). *Official Qwen2.5 has 3B/7B; Qwen3.5-4B is multimodal.*

## Goal

Beat the instructor's MAE of **39.85** on the "Price is Right" test set via hyperparameter tuning and/or data manipulation.

## Approach

- **Data:** Load `items_lite` from HuggingFace; build prompt/completion pairs with Qwen tokenizer (CUTOFF=110).
- **Model:** Qwen/Qwen2.5-4B (4-bit QLoRA, LoRA on attention + MLP).
- **Training:** SFTTrainer (TRL), 1 epoch lite / 2+ epochs for full run; push adapter to Hub.
- **Eval:** Load fine-tuned model, run `evaluate(model_predict, test)` from `util`, report Error (MAE).

## Usage

1. **Colab (recommended):** Upload `week-7-assessment.ipynb`, set Colab secrets `HF_TOKEN`, optionally `WANDB_API_KEY`. Runtime → GPU (T4 or better).
2. **Local:** Set `HF_TOKEN` in `.env`; run cells. Training needs a CUDA GPU.
3. After training, set `RUN_NAME` and `REVISION` in the Eval section to your Hub run, then run evaluation cells.

## Result

*(Fill after running: Best MAE = $____)*
