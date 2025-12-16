import librosa
import noisereduce as nr
import soundfile as sf
import os


def denoise_audio_file(
    audio_path: str,
    sample_rate: int,
) -> str:
    """
    Apply noise reduction to an audio file and save a new denoised file.

    :param audio_path: Path to the original audio file.
    :param sample_rate: Target sample rate for loading and saving.
    :return: Path to the denoised audio file.
    """
    if not audio_path:
        return audio_path

    audio, sr = librosa.load(
        audio_path,
        sr=sample_rate,
        mono=True,
    )
    denoised_audio = nr.reduce_noise(
        y=audio,
        sr=sr,
        prop_decrease=0.75,
    )

    base, ext = os.path.splitext(audio_path)
    denoised_path = f'{base}_denoised{ext}'
    sf.write(denoised_path, denoised_audio, sr)
    return denoised_path