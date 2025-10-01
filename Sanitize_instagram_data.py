import json

INPUT_FILE = "message_1.json"    
OUTPUT_FILE = "dialogue_pairs.jsonl"
MY_NAME = "your name here"           
HER_NAME = "her name here"         

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    messages = data.get("messages", [])
    messages = list(reversed(messages))

    pairs = []
    prev_sender, prev_text = None, None

    for msg in messages:
        sender_raw = msg.get("sender_name", "")
        text = msg.get("content", "")

        if not text:
            continue

        if sender_raw == MY_NAME:
            sender = "ME"
        elif sender_raw == HER_NAME:
            sender = "HER"
        else:
            continue

        if prev_sender == "ME" and sender == "HER":
            pairs.append({
                "input": f"ME: {prev_text.strip()}",
                "output": f"HER: {text.strip()}"
            })

        prev_sender, prev_text = sender, text

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        for p in pairs:
            out.write(json.dumps(p, ensure_ascii=False) + "\n")

    print(f" Built {len(pairs)} dialogue pairs → saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
