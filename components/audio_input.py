import gradio as gr


def create_audio_input_component() -> gr.Audio:
    """
    Create the reference audio input component.

    :return: A Gradio Audio component configured to return a file path.
    """

    return gr.Audio(
        label='Reference Audio File (Optional)',
        type='filepath',
    )
