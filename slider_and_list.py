import marimo

__generated_with = "0.9.3"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    l = [0]
    return l, mo


@app.cell
def __(mo):
    slider = mo.ui.slider(start=1, stop=10)
    slider
    return (slider,)


@app.cell
def __(l, slider):
    l.append(l[-1]+1)
    slider.value, l
    return


if __name__ == "__main__":
    app.run()
