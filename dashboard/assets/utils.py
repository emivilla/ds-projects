import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Set default template for figures
pio.templates.default = "plotly_white"


# Make plots and table
def make_plots(x, y, degree=3):

    # Make df
    df = pd.DataFrame({"x": x, "y_true": y})

    # Create features till given degree
    for d in range(2, degree+1):
        df[f"x ** {d}"] = df["x"] ** d

    # Divide features and target
    X = df[df.columns.drop("y_true")]
    Y = df["y_true"]

    # Train model and make predictions
    lr = LinearRegression()
    lr.fit(X, Y)
    y_pred = lr.predict(X)

    # Title
    if degree < 3:
        quality_of_fit = "underfit :("
    elif degree == 3:
        quality_of_fit = "perfect! :)"
    else:
        quality_of_fit = "overfit :("
    title = f"Fit with polynomial of degree {degree}, {quality_of_fit}"

    # Plot with fit
    fig1 = go.Figure()
    fig1.add_trace(go.Scattergl(x=x, y=y, mode='markers', name="y_true",
                                hovertemplate='<extra></extra>y: %{y:.2f}<br>' + 'x: %{x:.2f}<br>'))
    fig1.add_trace(go.Scattergl(x=x, y=y_pred, mode='lines', name="y_pred",
                                hovertemplate='<extra></extra>y: %{y:.2f}<br>' + 'x: %{x:.2f}<br>'))
    fig1.update_layout(xaxis_title="x", yaxis_title="y", title=title, title_x=0.5)

    # Plot residuals
    fig2 = go.Figure()
    fig2.add_trace(go.Histogram(x=y - y_pred))
    fig2.update_layout(xaxis_title="error", yaxis_title="count", title="Residuals", title_x=0.5)

    # Make dict of metrics
    metrics_name = ["R2", "MSE", "MAE"]
    metrics = [r2_score(y, y_pred), mean_squared_error(y, y_pred), mean_absolute_error(y, y_pred)]
    metrics = list(map(lambda x: round(x, 4), metrics))
    data = [{
        "Metric": m,
        "Value": v
    } for m, v in zip(metrics_name, metrics)]

    return fig1, fig2, data