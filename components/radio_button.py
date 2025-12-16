import gradio as gr
from typing import List


def create_radio_button(choices: List[str], label: str) -> gr.Radio:
    """
    Create a radio button group.

    :param choices: List of choices corresponding to one radio button each.
    :param label: Label shown above the radio button group.
    :return: A Gradio Radio component.
    """

    return gr.Radio(
        choices=choices,
        label=label,
        interactive=True,
        value=choices[0] if choices else None,
    )
