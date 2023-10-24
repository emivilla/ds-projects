from dash import Input, Output, State
import dashboard.assets.utils as utils
import dashboard.assets.constants as constants

def get_callbacks(app):

    # Fit with polynomial of degree d where d is slider value
    @app.callback(
        Output("plot", "figure"),
        Output("plot-residuals", "figure"),
        Output("table", "data"),
        Input("slider", "value"),
        prevent_initial_call=True
    )
    def fit_with_polynomial_of_degree_d(d):
         plot, residuals, data = utils.make_plots(constants.x, constants.y, degree=d)
         return plot, residuals, data
