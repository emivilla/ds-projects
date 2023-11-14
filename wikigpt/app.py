import webbrowser
from threading import Timer

from dash import Dash, html, dcc, page_registry, page_container
import dash_bootstrap_components as dbc

from assets import callbacks
from assets import constants

# Set app style
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.MORPH, dbc.icons.FONT_AWESOME],
    use_pages=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)
server = app.server

# Set up address and port where to open dash app
PORT = "8000"
ADDRESS = "127.0.0.1"

# Define app layout
app.layout = dbc.Container([

    # Store openai key
    dcc.Store(id="current-key", data=None),

    # Render pages
    page_container

])


# Callbacks
callbacks.get_callbacks(app)


# Define open_browser function
def open_browser():
    webbrowser.open_new(url=f"http://{ADDRESS}:{PORT}")


# Run app
if __name__ == "__main__":

    # Open browser after a couple of seconds at the address where the dash app is running
    Timer(2, open_browser).start()

    # Run app on production server
    app.run_server(debug=False, port=PORT, host=ADDRESS)
