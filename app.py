from components.audio_input import create_audio_input_component
from components.button import create_button
from components.radio_button import create_radio_button
from components.slider import create_slider
from components.textbox import create_prompt_textbox, create_integer_textbox
from functions.inputs.process import (
    process_inputs,
    clear_history,
    clear_text,
    default_text_prompt
)
from functions.tts.model_loader import get_tts_model
import gradio as gr
import logging
import os
from utils.templates import load_css
import warnings

warnings.filterwarnings('ignore')
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'
logging.getLogger('transformers').setLevel(logging.ERROR)
logging.getLogger('diffusers').setLevel(logging.ERROR)
logging.getLogger('torch').setLevel(logging.ERROR)
logging.getLogger('gradio').setLevel(logging.ERROR)


def build_interface() -> gr.Blocks:
    with gr.Blocks(
        fill_width=True,
        theme='freddyaboulton/dracula_revamped'
    ) as demo:
        gr.Markdown('## MAE 6291 TTS Demo')

        with gr.Row(equal_height=True):
            with gr.Column(scale=2):
                with gr.Row(equal_height=True):
                    text_prompt = create_prompt_textbox()
                    tts_output = gr.Audio(label='Generated Audio')

                with gr.Row():
                    with gr.Column(scale=1):
                        with gr.Row():
                            default_button = create_button('Set Default Text')
                            clear_text_button = create_button('Clear Text')
                    with gr.Column(scale=1):
                        with gr.Row():
                            generate_button = create_button('Generate Audio')

                with gr.Row():
                    with gr.Column(scale=1):
                        with gr.Accordion(label='Advanced Settings', open=True):
                            audio_input = create_audio_input_component()

                            style_radio = create_radio_button(
                                choices=['Standard', 'ATC'],
                                label='Style Selection',
                            )

                            exaggeration_slider = create_slider(
                                label='Exaggeration',
                                minimum=0.25,
                                maximum=2.0,
                                step=0.01,
                                default_value=0.3,
                            )

                            pace_slider = create_slider(
                                label='Pace',
                                minimum=0.2,
                                maximum=1.0,
                                step=0.01,
                                default_value=0.2,
                            )

                            temperature_slider = create_slider(
                                label='Temperature',
                                minimum=0.05,
                                maximum=5.0,
                                step=0.01,
                                default_value=0.8,
                            )

                            seed_value = create_integer_textbox()

            with gr.Column(scale=3):
                with gr.Column(elem_classes='fixed-height-container history-column'):
                    generation_history = gr.State([])
                    gr.Markdown('### Generation History', elem_classes='centered-header')

                    with gr.Column(elem_classes='scrollable-history'):
                        history_display = gr.HTML()

                    clear_history_button = create_button('Clear History')

        demo.css = load_css('styles/main.css')

        clear_history_button.click(
            fn=clear_history,
            inputs=[],
            outputs=[generation_history, history_display]
        )

        default_button.click(
            fn=default_text_prompt,
            inputs=[],
            outputs=[text_prompt],
        )

        clear_text_button.click(
            fn=clear_text,
            inputs=[],
            outputs=[text_prompt],
        )

        generate_button.click(
            fn=process_inputs,
            inputs=[
                audio_input,
                exaggeration_slider,
                pace_slider,
                style_radio,
                temperature_slider,
                text_prompt,
                seed_value,
                generation_history
            ],
            outputs=[
                tts_output,
                generation_history,
                history_display
            ]
        )
    return demo


def main() -> None:
    get_tts_model()
    interface = build_interface()
    interface.launch()


if __name__ == '__main__':
    main()