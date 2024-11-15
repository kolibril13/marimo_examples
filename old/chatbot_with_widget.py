# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "ipydrop==0.0.1",
#     "marimo",
#     "openai==1.51.2",
#     "tldraw==3.0.0",
# ]
# ///

import marimo

__generated_with = "0.9.4"
app = marimo.App(width="medium")


@app.cell
def __():
    from ipydrop import Widget
    from tldraw import TldrawWidget
    import marimo as mo

    whiteboard = mo.ui.anywidget(TldrawWidget())
    darg_area = mo.ui.anywidget(Widget())
    return TldrawWidget, Widget, darg_area, mo, whiteboard


@app.cell
def __(darg_area, mo, whiteboard):
    def chat_reply(messages, config):
        last_user_message = messages[-1].content
        if "whiteboard" in last_user_message:
            return whiteboard
        if "drag" in last_user_message:
            return darg_area
        else:
            return "Hello World!"



    mo.ui.chat(
        chat_reply,
    )
    return (chat_reply,)


@app.cell
def __():
    i = 1
    return (i,)


@app.cell
def __():
    j = 2
    exec(f'print("hi {j}")')
    return (j,)


@app.cell
def __():
    import openai
    return (openai,)


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
