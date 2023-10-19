from assets import callbacks
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


# Set app style
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

# Define app layout
app.layout = dbc.Container([

    # To be filled with cool stuff ...

])

# Callbacks
callbacks.get_callbacks(app)

# Run app
if __name__ == "__main__":

    # Run app on development server
    app.run_server(debug=False)
