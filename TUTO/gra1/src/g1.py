import gradio as gr
from rich.traceback import install

install(show_locals=True)


def App1():
    def greet(name, intensity):
        return "Hello " + name + ", " + int(intensity)

    demo = gr.Interface(
        fn=greet,
        inputs=["text", "slider"],
        outputs="text",
        title="SmellPanty",
        description="Sucking and Fucking",
    )
    demo.launch()
