# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "matplotlib==3.9.3",
#     "numpy==2.1.3",
# ]
# ///

import marimo

__generated_with = "0.9.32"
app = marimo.App(width="medium")


@app.cell
def __():
    import matplotlib.pyplot as plt
    import numpy as np

    plt.style.use('_mpl-gallery-nogrid')

    # make data
    X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
    Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)
    levels = np.linspace(Z.min(), Z.max(), 7)

    # plot
    fig, ax = plt.subplots()

    ax.contourf(X, Y, Z, levels=levels)

    plt.show()
    return X, Y, Z, ax, fig, levels, np, plt


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
