import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

# Set default template for figures
pio.templates.default = "plotly_white"


# Make plot without fit
def make_plot(x, y, degree=3):

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
    elif d == 3:
        quality_of_fit = "perfect! :)"
    else:
        quality_of_fit = "overfit :("
    title = f"Fit with polynomial of degree {degree}, {quality_of_fit}"

    # Return plot
    fig = go.Figure()
    fig.add_trace(go.Scattergl(x=x, y=y, mode='markers', name="y_true",
                                   hovertemplate='<extra></extra>y: %{y:.2f}<br>' + 'x: %{x:.2f}<br>'))
    fig.add_trace(go.Scattergl(x=x, y=y_pred, mode='lines', name="y_pred",
                                   hovertemplate='<extra></extra>y: %{y:.2f}<br>' + 'x: %{x:.2f}<br>'))
    fig.update_layout(xaxis_title="x", yaxis_title="y",
                      title=title, title_x=0.5)
    return fig
