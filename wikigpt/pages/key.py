import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import assets.constants as constants

# Def dash register page
dash.register_page(__name__, path="/page-1", order=1)

# Def layout
layout = html.Div([

    # Layout
    dbc.Container([
        dbc.Row([
            html.Div(
                [
                    html.H1("Menu", style={"marginTop": "5%"}),
                    dbc.Nav(
                        [
                            dbc.NavLink([html.I(className="fa-solid fa-house me-2"),
                                         html.Span("Home")],
                                        href="/", active="exact"),
                            dbc.NavLink([html.I(className="fa-solid fa-key me-2"),
                                         html.Span("Insert your OPENAI API KEY")],
                                        href="/page-1", active="exact"),
                            dbc.NavLink([html.I(className="fa-solid fa-face-smile-wink me-2"),
                                         html.Span("Have fun!")],
                                        href="/page-2", active="exact"),
                        ],
                        vertical=True,
                        pills=True,
                        style={"marginTop": "2rem"}
                    ),
                    html.Img(src="assets/pic1.jpg", style={'height': '32%', 'width': '100%', "marginTop": "15%"}),
                    dcc.Markdown(
                        """Designed in **Milan** on the **13th of November 2023**.""",
                        style=constants.FOOTER_STYLE
                    )
                ],
                style=constants.SIDEBAR_STYLE,
            ),
            dbc.Col([
                html.Center([
                    html.H6("Input below your OPENAI API KEY"),
                    dbc.Input(
                        id="input-key",
                        placeholder="Type key here...",
                        type="text",
                        style={"width": "100%"}
                    ),
                    html.Div([
                        dbc.Button(
                            "Reset",
                            n_clicks=0,
                            id="reset-key-btn",
                            style={"width": "20%", "display": "inline-block"},
                            disabled=True
                        ),
                        dcc.Markdown("""""", style={"width": "60%", "display": "inline-block",}),
                        dbc.Button(
                            "Confirm",
                            n_clicks=0,
                            id="confirm-key-btn",
                            style={"width": "20%", "display": "inline-block"},
                            disabled=True
                        )
                    ], style={"marginTop": "2.5%", "width": "90%", "display": "inline-block"}),
                    ], style=constants.HOME_CONTENT_STYLE

                )
            ])
        ])
    ], fluid=True),

    # Set key confirmation given as a toast in top right corner
    dbc.Toast(
        children="OPENAI API KEY set successfully",
        id="confirm-toast",
        header="Set Key",
        is_open=False,
        dismissable=True,
        duration=4000,
        icon="info",
        style={"position": "fixed", "top": 20, "right": 50, "width": 250},
    ),

    # Reset key confirmation given as a toast in top left corner
    dbc.Toast(
        children="OPENAI API KEY reset successfully",
        id="reset-toast",
        header="Reset Key",
        is_open=False,
        dismissable=True,
        duration=4000,
        icon="info",
        style={"position": "fixed", "top": 20, "right": 50, "width": 250},
    ),

])
