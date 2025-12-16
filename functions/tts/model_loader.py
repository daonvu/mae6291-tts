import torch
from chatterbox.tts import ChatterboxTTS
import copy

_TTS_MODEL = None


def get_device() -> str:
    """
    Return the device to use for inference.
    """
    return 'cuda' if torch.cuda.is_available() else 'cpu'


def get_tts_model() -> ChatterboxTTS:
    """
    Lazy-load and cache the Chatterbox TTS model.

    :return: An instance of the ChatterboxTTS model loaded on the appropriate device.
    """
    global _TTS_MODEL

    if _TTS_MODEL is not None:
        return _TTS_MODEL

    device = get_device()
    try:
        model = ChatterboxTTS.from_pretrained(device)
        if hasattr(model, 'to') and str(model.device) != device:
            model.to(device)

        print('TTS model loaded on:', device)

        model._base_conds = (
            copy.deepcopy(model.conds)
            if getattr(model, 'conds', None) is not None
            else None
        )
        _TTS_MODEL = model
    except Exception as error:
        print(f'Error loading TTS model: {error}')
        raise

    return _TTS_MODEL
