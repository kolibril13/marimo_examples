

import marimo

__generated_with = "0.9.32"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo

    mo.ui.text_area("hello world")
    return (mo,)


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
