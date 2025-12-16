import gradio as gr


def create_button(label: str) -> gr.Button:
    """
    Create a button with a given label.

    :param label: The text displayed on the button.
    :return: A Gradio Button component.
    """

    return gr.Button(
        value=label,
        size='md',
    )
