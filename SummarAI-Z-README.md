---
title: SummarAI Z
emoji: 🌖
colorFrom: yellow
colorTo: gray
sdk: gradio
sdk_version: 5.22.0
app_file: app.py
pinned: false
short_description: Audio to text summary
---

# SummarAI-Z

**Talk, get a summary.** SummarAI-Z takes audio — from your microphone or an uploaded file —
transcribes it to text, and condenses the transcript into a short summary.

## How it works
1. **Speech recognition** — `jonatasgrosman/wav2vec2-large-xlsr-53-english` (Hugging Face Transformers) converts audio to text
2. **Summarization** — `facebook/bart-large-cnn` summarizes the transcript
3. **Interface** — Gradio, with two tabs: *Transcribe Microphone* and *Transcribe Audio File*

## Run it
```bash
pip install -r requirements.txt
python app.py
```

## Tech
Python · Gradio · Hugging Face Transformers (wav2vec2, BART)
