import gradio as gr


def create_slider(
    label: str,
    minimum: float,
    maximum: float,
    step: float,
    default_value: float,
) -> gr.Slider:
    """
    Create a numeric slider.

    :param label: Label displayed for the slider.
    :param minimum: Minimum slider value.
    :param maximum: Maximum slider value.
    :param step: Step size between slide values.
    :param default_value: Initial slider value.
    :return: A Gradio Slider component.
    """

    return gr.Slider(
        label=label,
        minimum=minimum,
        maximum=maximum,
        step=step,
        value=default_value,
    )
