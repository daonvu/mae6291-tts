from functions.audio.denoise import denoise_audio_file
from functions.constants import SAMPLE_RATE
from functions.history import (
    get_audio_name,
    render_history_markdown
)
from functions.tts.generate import generate_speech
import numpy as np
import time
from typing import Optional, Tuple


def clear_history():
    """
    Clear the Generation History logs.
    """
    return [], ''


def clear_text() -> str:
    """
    Clear the Text Prompt box.
    """
    return ''


def default_text_prompt() -> str:
    """
    Return a default text prompt.
    """
    return 'The quick brown fox jumps over the lazy dog near the quiet riverbank.'


def process_inputs(
    audio_path: Optional[str],
    exaggeration: float,
    pace: float,
    speaking_style: str,
    temperature: float,
    text_prompt: str,
    seed_value: int,
    history: list
) -> Tuple[int, np.ndarray]:
    """
    Top-level function used by Gradio to process user inputs.

    :param audio_path: Path to the uploaded reference audio file or None.
    :param exaggeration: Exaggeration control parameter.
    :param pace: Pace / cfg weight parameter.
    :param speaking_style: Selected speaking style (e.g. 'Standard', 'ATC').
    :param temperature: Sampling temperature.
    :param text_prompt: Text to synthesize.
    :param seed_value: Random seed.
    :param history: Logging output.
    :return:
        - Generated Audio
        - Model Info
        - Generation History
    """
    _ = speaking_style

    if audio_path:
        audio_path = denoise_audio_file(
            audio_path=audio_path,
            sample_rate=SAMPLE_RATE
        )
    else:
        audio_path = None

    start = time.time()
    sample_rate, waveform, audio_b64 = generate_speech(
        text_prompt=text_prompt,
        pace=pace,
        exaggeration=exaggeration,
        temperature=temperature,
        seed=seed_value,
        audio_path=audio_path
    )

    latency = time.time() - start

    audio_name = get_audio_name(audio_path)
    entry = {
        'generation_number': len(history) + 1,
        'audio_name': audio_name,
        'text_prompt': text_prompt,
        'style': speaking_style,
        'exaggeration': exaggeration,
        'pace': pace,
        'temperature': temperature,
        'seed': seed_value,
        'latency': latency,
        'audio_b64': audio_b64
    }
    history = [entry] + history
    full_history = render_history_markdown(history)

    return (
        (sample_rate, waveform),
        history,
        full_history
    )
