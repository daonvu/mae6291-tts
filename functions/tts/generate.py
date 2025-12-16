import base64
from functions.tts.model_loader import get_tts_model
from functions.constants import SAMPLE_RATE
import io
import numpy as np
import random
import soundfile as sf
import torch
from typing import Optional, Tuple

def generate_speech(
    text_prompt: str,
    pace: float,
    exaggeration: float,
    temperature: float,
    seed: int,
    audio_path: Optional[str]
) -> Tuple[int, np.ndarray]:
    """
    Generate a speech waveform from the given inputs.

    :param text_prompt: Text to be synthesized.
    :param pace: Pace / cfg weight parameter for the model.
    :param exaggeration: Exaggeration parameter for prosody.
    :param temperature: Sampling temperature.
    :param seed: Random seed.
    :param audio_path: Optional path to a reference audio file.
    :return:
        - Synthesized waveform.
        - Embedding for playback
    """
    random.seed(seed)
    np.random.seed(seed)

    model = get_tts_model()

    if not audio_path and hasattr(model, "_base_conds"):
        model.conds = model._base_conds

    kwargs = {
        'text': text_prompt,
        'cfg_weight': pace,
        'exaggeration': exaggeration,
        'temperature': temperature,
        'audio_prompt_path': audio_path or None
    }

    wav = model.generate(**kwargs)
    wav = wav.squeeze().cpu().numpy() if isinstance(wav, torch.Tensor) else np.asarray(wav)

    buffer = io.BytesIO()
    sf.write(buffer, wav, SAMPLE_RATE, format='WAV')
    audio_bytes = buffer.getvalue()
    audio_b64 = base64.b64encode(audio_bytes).decode('utf-8')

    return SAMPLE_RATE, wav, audio_b64