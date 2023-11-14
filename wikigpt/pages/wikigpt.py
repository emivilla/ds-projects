import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import assets.constants as constants

# Def dash register page
dash.register_page(__name__, path="/page-2", order=2)

# Def layout
layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        html.Div(
                            [
                                html.H1("Menu", style={"marginTop": "5%"}),
                                dbc.Nav(
                                    [
                                        dbc.NavLink(
                                            [
                                                html.I(
                                                    className="fa-solid fa-house me-2"
                                                ),
                                                html.Span("Home"),
                                            ],
                                            href="/",
                                            active="exact",
                                        ),
                                        dbc.NavLink(
                                            [
                                                html.I(
                                                    className="fa-solid fa-key me-2"
                                                ),
                                                html.Span("Insert your OPENAI API KEY"),
                                            ],
                                            href="/page-1",
                                            active="exact",
                                        ),
                                        dbc.NavLink(
                                            [
                                                html.I(
                                                    className="fa-solid fa-face-smile-wink me-2"
                                                ),
                                                html.Span("Have fun!"),
                                            ],
                                            href="/page-2",
                                            active="exact",
                                        ),
                                    ],
                                    vertical=True,
                                    pills=True,
                                    style={"marginTop": "2rem"},
                                ),
                                html.Img(
                                    src="assets/pic1.jpg",
                                    style={
                                        "height": "32%",
                                        "width": "100%",
                                        "marginTop": "15%",
                                    },
                                ),
                                dcc.Markdown(
                                    """Designed in **Milan** on the **13th of November 2023**.""",
                                    style=constants.FOOTER_STYLE,
                                ),
                            ],
                            style=constants.SIDEBAR_STYLE,
                        ),
                        dbc.Col(
                            [
                                html.Center(
                                    [
                                        html.H6("Input below the Wikipedia page URL"),
                                        dbc.Input(
                                            id="input-url",
                                            placeholder="Type url here...",
                                            type="text",
                                            style={"width": "100%"},
                                        ),
                                        html.Div(
                                            [
                                                dbc.Button(
                                                    "Delete URL",
                                                    n_clicks=0,
                                                    id="reset-url-btn",
                                                    style={
                                                        "width": "25%",
                                                        "display": "inline-block",
                                                    },
                                                    disabled=True,
                                                ),
                                                dcc.Markdown(
                                                    """""",
                                                    style={
                                                        "width": "50%",
                                                        "display": "inline-block",
                                                    },
                                                ),
                                                dbc.Button(
                                                    "Do Magic!",
                                                    n_clicks=0,
                                                    id="confirm-url-btn",
                                                    style={
                                                        "width": "25%",
                                                        "display": "inline-block",
                                                    },
                                                    disabled=True,
                                                ),
                                            ],
                                            style={
                                                "marginTop": "2.5%",
                                                "width": "90%",
                                                "display": "inline-block",
                                            },
                                        ),
                                        dcc.Markdown(""""""),
                                        dbc.Spinner(
                                            html.Div(id="output"),
                                            spinner_style={"marginTop": "30%"},
                                        ),
                                    ],
                                    style=constants.HOME_CONTENT_STYLE,
                                )
                            ]
                        ),
                    ]
                )
            ],
            fluid=True,
        ),
        # Add blocking alert if given url is not correct
        dcc.ConfirmDialog(
            id="url-alert",
            message="The provided URL does not respect the requirements. "
            "Please use the URL of an English version of a Wikipedia page instead.",
            displayed=False,
        ),
        # Add blocking alert if provided openai api key is incorrect
        dcc.ConfirmDialog(
            id="key-alert",
            message="The provided OPENAI API KEY is incorrect. "
            "Please check you copied it correctly from https://platform.openai.com/account/api-keys.",
            displayed=False,
        ),
        # Add blocking alert advising to contact developer because of unkown issues
        dcc.ConfirmDialog(
            id="general-alert",
            message="Something went wrong but we do not really know what. "
            "Please open an issue on GitHub or contact the maintainers of the app directly. "
            "Thank you.",
            displayed=False,
        ),
    ]
)
