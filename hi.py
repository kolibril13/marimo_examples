# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "matplotlib==3.9.2",
#     "numpy==2.1.2",
# ]
# ///

import marimo

__generated_with = "0.9.9"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __():
    import matplotlib.pyplot as plt
    import numpy as np

    plt.style.use('_mpl-gallery')

    # make data
    _y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

    # plot
    _fig, _ax = plt.subplots()

    _ax.stairs(_y, linewidth=2.5)

    _ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))

    plt.gca()
    return np, plt


@app.cell
def __(np, plt):
    plt.style.use('_mpl-gallery')

    # make the data
    np.random.seed(3)
    x = 4 + np.random.normal(0, 2, 24)
    y = 4 + np.random.normal(0, 2, len(x))
    # size and color:
    sizes = np.random.uniform(15, 80, len(x))
    colors = np.random.uniform(15, 80, len(x))

    # plot
    fig, ax = plt.subplots()

    ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()
    return ax, colors, fig, sizes, x, y


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell(disabled=True)
def __():
    import time

    print("This cell will take 10 seconds to run...")
    time.sleep(10)
    print("Done!")
    return (time,)


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
