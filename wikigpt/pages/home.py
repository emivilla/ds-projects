import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import assets.constants as constants

# Def dash register page
dash.register_page(__name__, path="/", order=0)

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
                    html.H1("Welcome to Wiki-Joke!"),
                    html.H6("Powered with \u2665 by Emilio Villa"),
                    dbc.Card(
                        dbc.CardBody(
                            dcc.Markdown(
                                f"""
                                **Instructions**:


                                **1.** Go the *Insert your OPENAI API KEY* page and insert your openai api key in the input
                                       form. Press *Confirm* button to save the key for further usage.

                                **2.** Then move to the *Have fun!* page and insert the URL of an english version of a 
                                       Wikipedia page in the input form. Press *Do Magic!* button to generate
                                       two jokes with GPT-3.5-TURBO based on the content of the Wikipedia page.
                                   
                                   
                                **Important:** Please note that using GPT-3.5-TURBO is not for free. 
                                Be aware of this and check billing and usage in your openai account profile settings.  
                                
                                
                                **Enjoy!**
                                """,
                                style={"textAlign": "left"}
                            )
                        ), style={"marginTop": "5%"}
                    )
                    ], style=constants.HOME_CONTENT_STYLE
                )
            ])
        ])
    ], fluid=True)

])
