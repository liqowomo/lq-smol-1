import marimo

__generated_with = "0.10.12"
app = marimo.App(width="full")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Running Smol Agents 
        1. Following the tutorial to run smol agents inside this notebook
        2. Doing it this way since , kaggle is throwing errors
        3. Note that packages are not being installed and will be done form inside this notebook
        """
    )
    return


@app.cell
def _():
    # Running Beatuifiers
    # Rich Prettifier Code 
    # ------------------------------------------------------
    from rich import print as rprint # For rprinting
    from rich.pretty import pprint # For pretty printing
    from rich import inspect # For inspect
    from rich.console import Console # For console.print
    from rich.markdown import Markdown # For markdow
    from rich.panel import Panel # For Panel()
    from rich import box # For Panel Boxes
    from rich.prompt import Prompt # For Prompting 
    from rich.style import Style # For styles colors
    from rich.text import Text # For text Styles
    console = Console() # Standard code to access console
    from rich.traceback import install
    install(show_locals=True)
    # -------------------------------------------------------

    return (
        Console,
        Markdown,
        Panel,
        Prompt,
        Style,
        Text,
        box,
        console,
        inspect,
        install,
        pprint,
        rprint,
    )


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""## Running HF Login for token""")
    return


app._unparsable_cell(
    r"""
    hf_NrGMcOdJkyZrFhACqytlkKZUqDIgwECyPwfrom huggingface_hub import login
    login()
    """,
    name="_"
)


@app.cell
def _():
    from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
    return CodeAgent, DuckDuckGoSearchTool, HfApiModel


@app.cell
def _():
    # Defining the model_id ti be called in the subsequent cell 
    model_id="hexgrad/Kokoro-82M"
    return (model_id,)


@app.cell
def _(CodeAgent, DuckDuckGoSearchTool, HfApiModel, model_id):
    agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel(model_id))
    return (agent,)


@app.cell
def _(agent):
    agent
    return


@app.cell
def _(agent):
    agent.run("Write a poem about sniffing womens panty")
    return


if __name__ == "__main__":
    app.run()
