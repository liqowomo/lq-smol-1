import marimo

__generated_with = "0.10.12"
app = marimo.App(width="medium")


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
    import marimo as mo
    return (mo,)


@app.cell
def _():
    # Importing packages to haveit installed 

    return


if __name__ == "__main__":
    app.run()
