# Project: Dialogue dataset sanitization and merging

This repository contains small scripts and a notebook to convert conversation exports into a combined JSONL dataset suitable for fine-tuning a custom conversational model.

Watch the youtube video ! :
https://www.youtube.com/watch?v=HIVIlWDrseQ

<img width="640" height="420" alt="Press Start 2P (1)" src="https://github.com/user-attachments/assets/0048f0d7-4aa0-41e5-96b1-89f91e259eb8" />


Files in this repo

- `Sanitize_instagram_data.py` — convert an Instagram/Facebook messages JSON export into dialogue pairs (`dialogue_pairs.jsonl`). Edit `MY_NAME` and `HER_NAME` to match the names used in your export.
- `sanitize_dailyDialogue_data.py` — convert DailyDialog text/topic files into pairwise JSONL (`dailydialog_sanitized.jsonl`).
- `Merge_datasets.py` — merge `dialogue_pairs.jsonl` (Instagram) and `dailydialog_sanitized.jsonl` into `combined_dataset.jsonl`. (used dailydialog dataset to get more cohearency for the high max new tokens (human text messages are short and bland :) )
- `Joi.ipynb` — Colab notebook showing how to fine-tune with LoRA/PEFT using the combined dataset (4-bit quantization + LoRA). This notebook expects `combined_dataset.jsonl` in the working directory.

Quick overview

1. Download your Instagram/Facebook message archive (see detailed steps below).
2. Put the exported JSON message file (commonly named `message_1.json` inside the `messages` folder of the archive) in the same folder as these scripts.
3. Edit `Sanitize_instagram_data.py` to set `MY_NAME` and `HER_NAME`.
4. Run the scripts to create `dialogue_pairs.jsonl`, sanitize DailyDialog if needed, and merge with `Merge_datasets.py` to produce `combined_dataset.jsonl`.
5. Open `Joi.ipynb` in Colab (or locally) to fine-tune or experiment.

How to download your Instagram / Facebook messages (JSON)

1. Go to https://www.facebook.com/settings (Facebook) while signed in.
2. Click "Your Facebook Information" → "Download Your Information".
3. Under "Select information to download", uncheck everything except "Messages".
4. Choose "Format: JSON", the date range you need, and a reasonable media quality. For messages only, a small/medium media quality is fine.
5. Click "Create File" and wait for Facebook to prepare the archive. When ready, download the zip archive.
6. Extract the archive and locate the `messages` folder. Inside it you'll find one or more `message_*.json` files. The script expects `message_1.json` by default — either rename your file to that or change `INPUT_FILE` in `Sanitize_instagram_data.py`.

Notes about the message export

- The exported JSON structure varies slightly by account and export date. The sanitizer script reads `messages` and looks for `sender_name` and `content`. If your messages use a different structure (for example, media-only messages or reactions) you may need to adapt the script.

Running the sanitizer scripts (Windows PowerShell examples)

1. Instagram sanitizer (after adjusting names inside the file):

```powershell
python .\Sanitize_instagram_data.py
```

This creates `dialogue_pairs.jsonl` (one JSON object per line with `{"input": ..., "output": ...}`).

2. DailyDialog sanitizer (if you have the original DailyDialog text/topic/emotion files):

Place `dialogues_text.txt`, `dialogues_topic.txt`, and `dialogues_emotion.txt` next to `sanitize_dailyDialogue_data.py`, then:

```powershell
python .\sanitize_dailyDialogue_data.py
```

This writes `dailydialog_sanitized.jsonl`.

3. Merge the two datasets:

```powershell
python .\Merge_datasets.py
```

This writes `combined_dataset.jsonl`.

Using the notebook

- Upload `combined_dataset.jsonl` to Colab (or place it next to `Joi.ipynb` if running locally).
- Open `Joi.ipynb` and follow the cells. The notebook includes installation steps and an end-to-end example for applying LoRA adapters.

Dependencies

- The sanitizer and merging scripts use only the Python standard library (no extra packages needed).
- The notebook lists heavy ML dependencies. For convenience a `requirements.txt` is included with the main packages used in the notebook.


