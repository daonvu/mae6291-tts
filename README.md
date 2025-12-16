# mae6291-tts: ATC Text-to-Speech Demo

This project is a final project for GWU MAE 6291 and demonstrates a customizable
text-to-speech (TTS) system focused on Air Traffic Control (ATC)-style speech.

Users can:

- Enter a text prompt to synthesize speech
- Optionally supply a reference audio file for voice cloning
- Adjust parameters such as exaggeration, pace, and temperature
- Select gender and speaking style presets (e.g., Standard vs ATC)

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
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── components/
│   ├── __init__.py
│   ├── audio_input.py
│   ├── button.py
│   ├── radio_button.py
│   ├── slider.py
│   └── textbox.py
└── functions/
    ├── __init__.py
    ├── process_inputs.py
    └── tts.py
```
---

## Getting Started

### Python Version

Python 3.11 is required.

### Dependencies
Run `pip install -r requirements.txt` to install dependencies.


### Gradio
Run `python app.py` to bring up the Gradio app locally.