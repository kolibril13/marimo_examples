# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "numpy==2.1.3",
# ]
# ///

import marimo

__generated_with = "0.9.32"
app = marimo.App(width="medium")


@app.cell
def __():
    import numpy as np
    import marimo as mo
    return mo, np


@app.cell
def __(mo, np):
    mo.md(str(np.random.randint(34)))
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
