"""Quick E2E test: load items_lite, build prompts with Qwen tokenizer, run evaluator (dummy predictor)."""
import sys
from pathlib import Path

week7 = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(week7))

from dotenv import load_dotenv
load_dotenv(override=True)

from pricer.items import Item
from util import evaluate

ITEMS_DATASET = "ed-donner/items_lite"
CUTOFF = 110
BASE_MODEL = "Qwen/Qwen2.5-3B"

def main():
    print("Loading items_lite...")
    train_items, val_items, test_items = Item.from_hub(ITEMS_DATASET)
    print(f"Train: {len(train_items)} Val: {len(val_items)} Test: {len(test_items)}")

    print("Loading Qwen tokenizer...")
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)

    print("Building prompts...")
    for item in train_items + val_items:
        item.make_prompts(tokenizer, CUTOFF, True)
    for item in test_items:
        item.make_prompts(tokenizer, CUTOFF, False)

    test_dataset = [{"prompt": i.prompt, "completion": i.completion} for i in test_items]
    print(f"Test dataset size: {len(test_dataset)}")
    print("Sample completion:", test_dataset[0]["completion"])

    def dummy_predict(item):
        return item["completion"]

    print("Running evaluate (dummy predictor, size=5)...")
    evaluate(dummy_predict, test_dataset, size=5)
    print("E2E test done.")

if __name__ == "__main__":
    main()
