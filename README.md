# Text-to-Speech Demo

This project is a final project for GWU MAE 6291 and demonstrates a customizable
text-to-speech (TTS) system focused on Air Traffic Control (ATC) speech.

Users can:

- Enter a text prompt to synthesize speech
- Optionally supply a reference audio file for voice cloning
- Adjust parameters such as exaggeration, pace, and temperature

The system uses the Chatterbox TTS model by Resemble AI, a state-of-the-art
zero-shot English TTS model, and is presented via a Gradio web UI.

---

## Motivation

The project draws inspiration from the paper:

> *“My aircraft talks to me: Current developments on voice synthesis as a modality
> in the cockpit of future fighter aircraft.”*

The paper highlights that many shortcomings of TTS in the cockpit are not about
basic intelligibility, but about naturalness and expressiveness: cadence, pauses,
emphasis, intensity, and other prosodic features. Our goal is to explore some of
these aspects using a flexible TTS framework.

---

## Project Structure

```text
mae6291-tts/
├── components/
│ ├── init.py
│ ├── audio_input.py
│ ├── button.py
│ ├── radio_button.py
│ ├── slider.py
│ └── textbox.py
├── functions/
│ ├── audio/
│ │ ├── init.py
│ │ └── denoise.py
│ ├── inputs/
│ │ ├── init.py
│ │ └── process.py
│ ├── tts/
│ │ ├── init.py
│ │ ├── generate.py
│ │ └── model_loader.py
│ ├── init.py
│ ├── constants.py
│ └── history.py
├── styles/
│ ├── init.py
│ └── main.css
├── templates/
│ ├── init.py
│ └── history_entry.html
├── utils/
│ ├── init.py
│ └── templates.py
├── .gitattributes
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```
---

## Getting Started

### Python Version

Python 3.11 is required.

### Dependencies
Run `pip install -r requirements.txt` to install dependencies.


### Gradio
Run `python app.py` to bring up the Gradio app locally.