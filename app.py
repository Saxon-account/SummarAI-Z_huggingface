import os
import gradio as gr
from transformers import pipeline

demo = gr.Blocks()

asr = pipeline("automatic-speech-recognition", model="jonatasgrosman/wav2vec2-large-xlsr-53-english")

asr2 = pipeline("summarization", model="facebook/bart-large-cnn")

def transcribe_and_summarize(filepath):
    if filepath is None:
        gr.Warning("No audio found, please retry.")
        return ""
    
    transcription = asr(filepath)
    transcribed_text = transcription.get("text", "")

    summarized_output = asr2(transcribed_text, max_length=20, do_sample=False)
    summary = summarized_output[0].get("summary_text", "")

    return transcribed_text, summary

# Gradio Interfaces
mic_transcribe = gr.Interface(
    fn=transcribe_and_summarize,
    inputs=gr.Audio(sources="microphone", type="filepath"),
    outputs=[
        gr.Textbox(label="Transcript", lines=3),
        gr.Textbox(label="Summary", lines=3)
    ],
    allow_flagging="never"
)

file_transcribe = gr.Interface(
    fn=transcribe_and_summarize,
    inputs=gr.Audio(sources="upload", type="filepath"),
    outputs=[
        gr.Textbox(label="Transcript", lines=3),
        gr.Textbox(label="Summary", lines=3)
    ],
    allow_flagging="never"
)

with demo:
    gr.TabbedInterface(
        [mic_transcribe,
         file_transcribe],
        ["Transcribe Microphone",
         "Transcribe Audio File"],
    )
demo.launch()