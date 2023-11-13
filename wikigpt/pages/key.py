import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import assets.constants as constants

# Def dash register page
dash.register_page(__name__, path="/page-1", order=1)

# Def layout
layout = html.Div([

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
                    html.H1("OPENAI KEY in progress..."),
                    ], style=constants.HOME_CONTENT_STYLE
                )
            ])
        ])
    ], fluid=True)

])
