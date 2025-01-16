import gradio as gr


def App1():
    def greet(name, intensity):
        return "Hello " + name + ", " + int(intensity)

    demo = gr.Interface(fn=greet, inputs=["text", "slider"], outputs="text")
    demo.launch()
