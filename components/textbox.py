import gradio as gr


def create_prompt_textbox() -> gr.Textbox:
    """
    Create the main text prompt box.

    :return: A Gradio Textbox component for the main text prompt.
    """

    return gr.Textbox(
        label='Text Prompt',
        placeholder='Please type your text prompt here.',
        info='The text below will be synthesized into audio.',
        lines=5,
        max_lines=5,
        show_label=True,
        interactive=True,
        container=True,
        text_align='left',
        type='text',
    )

def create_integer_textbox(default_value: int = 42):
    """
    Create the random seed textbox.

    :param default_value:
    :return: A Gradio Textbox component for the random seed input.
    """

    return gr.Number(
        label='Random Seed',
        value=default_value,
        precision=0,
        interactive=True,
    )
