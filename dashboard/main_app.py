from assets import callbacks, constants, utils
from dash import Dash, html, dcc, dash_table
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
                dcc.Graph(id='plot', figure=utils.make_plots(constants.x, constants.y)[0],
                          config=constants.gconfig),
            color="primary"),
            dcc.Slider(1, 100, value=3, marks={1: 1, 3: 3, 10: 10, 50: 50, 100: 100}, id="slider")
        ])
    ),

    # Plot residuals and add table with metrics
    dbc.Row(
      [
          dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dbc.Spinner(
                        dcc.Graph(id='plot-residuals', figure=utils.make_plots(constants.x, constants.y)[1],
                                  config=constants.gconfig),
                    color="primary"),
                ])
            , style={"height": "100%"})
          ),
          dbc.Col(
              dbc.Card(
                  dbc.CardBody([
                      html.Div(
                          children=[
                              dash_table.DataTable(
                                  id='table',
                                  columns=(
                                      {"id": "Metric", "name": "Metric", "type": "text"},
                                      {"id": "Value", "name": "Value", "type": "number"},
                                  ),
                                  data=utils.make_plots(constants.x, constants.y)[2],
                                  style_cell={
                                      'overflow': 'hidden',
                                      'textOverflow': 'ellipsis',
                                      'font-family': 'sans-serif',
                                      'textAlign': 'left'
                                  },
                                  editable=False,
                              )]
                      )
                  ], style={"align": "center"})
              , style={"height": "100%"})
          ),
      ]
    , className="g-0")

])

# Callbacks
callbacks.get_callbacks(app)

# Run app
if __name__ == "__main__":

    # Run app on development server
    app.run_server(debug=False)
