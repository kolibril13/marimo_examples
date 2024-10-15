# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "numpy==2.1.2",
# ]
# ///

import marimo

__generated_with = "0.9.8"
app = marimo.App(width="medium")


@app.cell
def __():
    import numpy
    numpy.rad2deg(3.14)
    return (numpy,)


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
