#Data Source
import yfinance as yf
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

happiness = pd.read_csv("13 - worldhappiness.csv")
region = happiness["region"].unique()
country = happiness["country"].unique()

app = Dash()

app.layout = html.Div([
    dcc.Input(id="input_text", value="Change this text",
              type="text"),
    html.Div(id="output_text")
])

@app.callback(
    Output(component_id="output_text", component_property="children"),
    Input(component_id="input_text", component_property="value")
)
def update_output_div(input_text):
    """update text"""
    return f"text:{input_text}"
if __name__ == "__main__":
    app.run_server(debug=True)
