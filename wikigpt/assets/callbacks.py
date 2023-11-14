import dash_bootstrap_components as dbc
import time
from dash import Input, Output, State, dcc
import assets.utils as utils


def get_callbacks(app):

    #########################
    # OPENAI API KEY        #
    #########################

    # Activate confirm button
    @app.callback(
        Output("confirm-key-btn", "disabled"),
        Input("input-key", "value"),
        prevent_initial_call=True
    )
    def activate_confirm_btn(text):
        if (text is None) | (text == ""):
            return True
        else:
            return False

    # Activate reset button
    @app.callback(
        Output("reset-key-btn", "disabled"),
        Input("current-key", "data"),
        prevent_initial_call=True
    )
    def activate_reset_btn(text):
        if text is None:
            return True
        else:
            return False

    # Set / Reset OPENAI API KEY
    @app.callback(
        Output("current-key", "data"),
        Output("input-key", "value"),
        Output("confirm-toast", "is_open"),
        Output("reset-toast", "is_open"),
        Output("confirm-key-btn", "n_clicks"),
        Output("reset-key-btn", "n_clicks"),
        State("input-key", "value"),
        Input("confirm-key-btn", "n_clicks"),
        Input("reset-key-btn", "n_clicks"),
        prevent_initial_call=True
    )
    def set_key(key, con_btn, res_btn):
        if con_btn > 0:
            return key, key, True, False, 0, 0
        elif res_btn > 0:
            return None, None, False, True, 0, 0
        else:
            pass

    #########################
    # WIKI-JOKE             #
    #########################

    # Activate confirm button
    @app.callback(
        Output("confirm-url-btn", "disabled"),
        Input("input-url", "value"),
        prevent_initial_call=True
    )
    def activate_confirm_btn(text):
        if (text is None) | (text == ""):
            return True
        else:
            return False

    # Activate reset button
    @app.callback(
        Output("reset-url-btn", "disabled"),
        Input("input-url", "value"),
        prevent_initial_call=True
    )
    def activate_reset_btn(text):
        if (text is None) | (text == ""):
            return True
        else:
            return False

    # Clear URL
    @app.callback(
        Output("input-url", "value"),
        Input("reset-url-btn", "n_clicks"),
        prevent_initial_call=True
    )
    def reset_url(fire):
        return None

    # Run GPT
    @app.callback(
        Output("output", "children"),
        State("input-url", "value"),
        Input("confirm-url-btn", "n_clicks"),
        prevent_initial_call=True
    )
    def run_gpt(url, fire):
        #output = utils.make_jokes(url=url)
        time.sleep(5)
        class Output:
            jokes = ["joke 1", "joke 2"]
        output = Output()
        return dbc.Card(
            dbc.CardBody(
                dcc.Markdown(
                    f"""
                        **GPT-3.5-TURBO** has come up with the following two **jokes**:


                        1. {output.jokes[0]}

                        2. {output.jokes[1]}
                    """,
                    style={"textAlign": "left"}
                )
            ), style={"marginTop": "10%"}
        )
