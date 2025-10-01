import json

TEXT_FILE = "dialogues_text.txt"
TOPIC_FILE = "dialogues_topic.txt"
EMOTION_FILE = "dialogues_emotion.txt"
OUTPUT_FILE = "dailydialog_sanitized.jsonl"
KEEP_TOPICS = {1, 4, 5}  

def load_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]

def main():
    texts = load_file(TEXT_FILE)
    topics = load_file(TOPIC_FILE)
    emotions = load_file(EMOTION_FILE)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        kept = 0
        for i, dialog in enumerate(texts):
            topic = int(topics[i])
            if topic not in KEEP_TOPICS:
                continue  

            utterances = [u.strip() for u in dialog.split("__eou__") if u.strip()]

            for j in range(len(utterances) - 1):
                input_text = f"SpeakerA: {utterances[j]}"
                output_text = f"SpeakerB: {utterances[j+1]}"

                entry = {
                    "input": input_text,
                    "output": output_text
                }
                out.write(json.dumps(entry, ensure_ascii=False) + "\n")
                kept += 1

    print(f" Saved {kept} dialogue pairs → {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
