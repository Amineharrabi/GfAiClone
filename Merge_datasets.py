import json

EX_DATASET = "dialogue_pairs.jsonl"         
DAILYDIALOG_DATASET = "dailydialog_sanitized.jsonl" 
OUTPUT_FILE = "combined_dataset.jsonl"

def load_jsonl(filename):
    data = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    return data

def save_jsonl(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

def main():
    ex_pairs = load_jsonl(EX_DATASET)
    daily_pairs = load_jsonl(DAILYDIALOG_DATASET)

    combined = ex_pairs + daily_pairs

    save_jsonl(combined, OUTPUT_FILE)

    print(f" Combined {len(ex_pairs)} ex-pairs + {len(daily_pairs)} DailyDialog pairs")
    print(f" Saved merged dataset to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
