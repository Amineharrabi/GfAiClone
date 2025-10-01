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

Git and GitHub: how to upload this project

Option A — create a GitHub repo using the web UI (manual, easy)

1. On GitHub, click "New repository".
2. Choose a name, description, visibility (private or public), and click Create repository.
3. In your project folder (this repository), run the commands below to push the code to the new repo.

Option B — create a repo and push from PowerShell (using the GitHub CLI, optional)

If you have the GitHub CLI (`gh`) installed you can create a new remote repository from PowerShell:

```powershell
# create repo interactively and push
gh repo create your-username/your-repo-name --public --source="." --remote=origin --push
```

If you prefer the standard web-created remote, use these commands in your project folder (PowerShell):

```powershell
# initialize repo (if you haven't already)
git init
# choose files to commit (ignore large exports; see .gitignore)
git add .
git commit -m "Initial commit: sanitizer scripts and notebook"
# add the GitHub remote (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
# set main branch and push
git branch -M main
git push -u origin main
```

Important: do NOT push large archives containing your private chats to a public repo. Use a private repo or remove/mask personal data before publishing. Use `.gitignore` to exclude raw exports.

.gitignore suggestions

- `message_*.json`
- `*.zip`
- `*.jsonl` (if you don't want to push generated datasets — edit this file if you do want to include `combined_dataset.jsonl`)
- `__pycache__/`
- `.ipynb_checkpoints/`

Privacy & security

- Your message exports contain personal and private information. If you plan to publish any data or model checkpoints, sanitize personal identifiers and get consent where required.

Next steps / suggestions

- Add small unit tests around the sanitizers to validate expected input JSON structures.
- Add a short script to sample a few lines from `combined_dataset.jsonl` for quick checks.

If you'd like, I can:

- create a small `.py` utility to sample N lines from a JSONL file,
- add basic unit tests, or
- run the scripts against a sample export (you'll need to upload or point me to the sample file).


