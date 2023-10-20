from assets import callbacks, constants, utils
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Set app style
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

# Define app layout
app.layout = dbc.Container([

    # Title
    html.Div([
        html.H1(" Underfit vs Overfit for Simple Linear Model",
                style={"display": "inline-block", "marginTop": "1em", "width": "95%"}),
        html.H1("", className="bi bi-bar-chart-line-fill",
                style={"display": "inline-block", "marginTop": "1em", "width": "5%"}),
    ]),
    html.Hr(),

    # Plot Data
    dbc.Card(
        dbc.CardBody([
            dcc.Markdown("""Use the slider below to select the degree of the fitting polynomial."""),
            dbc.Spinner(
                dcc.Graph(id='plot', figure=utils.make_plot(constants.x, constants.y), config=constants.gconfig),
            color="primary"),
            dcc.Slider(1, 100, value=3, marks={1: 1, 3:3, 10: 10, 50:50, 100: 100}, id="slider")
        ])
    )

])

# Callbacks
callbacks.get_callbacks(app)

# Run app
if __name__ == "__main__":

    # Run app on development server
    app.run_server(debug=False)
