from functions.tts import get_tts_model
import os
import torch
from typing import Optional
from utils.templates import render_template


def get_audio_name(audio_path: Optional[str]) -> str:
    """
    Get the name of the audio file.

    :param audio_path: Path of the uploaded audio file.
    :return: Name of the audio file.
    """
    if not audio_path:
        return 'None'
    return os.path.basename(audio_path).replace('_denoised', '')


def build_history_entry(
    generation_number: int,
    audio_name: str,
    text_prompt: str,
    style: str,
    exaggeration: float,
    pace: float,
    temperature: float,
    seed: int,
    latency: float,
    audio_b64: str,
    is_open: bool = False
) -> str:
    """
    Build the Markdown block for a single generation history entry.

    :param generation_number: Current generated entry number.
    :param audio_name: Name of the audio file.
    :param text_prompt: Text prompt of the generated audio.
    :param style: Speaker style.
    :param exaggeration: Exaggeration control parameter.
    :param pace: Pace / cfg weight parameter.
    :param temperature: Sampling temperature.
    :param seed: Random seed.
    :param latency: Latency of the generated audio.
    :param audio_b64: Audio playback option.
    :param is_open: Whether this entry should be open by default.
    :return: A summary of the generation.
    """
    audio_player = f"""
        <audio controls style="width:100%; margin-top:12px;">
          <source src="data:audio/wav;base64,{audio_b64}" type="audio/wav">
          Your browser does not support audio playback.
        </audio>
    """
    context = {
        'open_attr': ' open' if is_open else '',
        'generation_number': generation_number,
        'audio_name': audio_name,
        'text_prompt': text_prompt,
        'style': style,
        'exaggeration': exaggeration,
        'pace': pace,
        'temperature': temperature,
        'seed': seed,
        'latency_formatted': f"{latency:.3f}",
        'audio_player': audio_player,
        'model_name': 'ChatterboxTTS (Pretrained)',
        'device': get_tts_model().device,
        'gpu': torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None',
        'vram_used_formatted': f'{(torch.cuda.memory_allocated() / (1024 * 1024)):.2f}'
    }
    return render_template('history_entry.html', **context)


def render_history_markdown(history_data: list) -> str:
    """
    Take a list of data dictionaries and render them in chronological order.

    :param history_data: A list of generation data dictionaries.
    :return: HTML string with all entries.
    """
    html_entries = []
    for i, entry_data in enumerate(history_data):
        is_open = (i == 0)

        html_entry = build_history_entry(
            generation_number=entry_data['generation_number'],
            audio_name=entry_data['audio_name'],
            text_prompt=entry_data['text_prompt'],
            style=entry_data['style'],
            exaggeration=entry_data['exaggeration'],
            pace=entry_data['pace'],
            temperature=entry_data['temperature'],
            seed=entry_data['seed'],
            latency=entry_data['latency'],
            audio_b64=entry_data['audio_b64'],
            is_open=is_open
        )
        html_entries.append(html_entry)
    return '\n'.join(html_entries)
