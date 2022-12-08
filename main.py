#Data Source
import yfinance as yf
from dash import Dash, html,dcc
import pandas as pd
import plotly.express as px

happiness = pd.read_csv("13 - worldhappiness.csv")
region = happiness["region"].unique()
country = happiness["country"].unique()

app = Dash()

app.layout = html.Div([
    html.H1("World Happiness Dashboard"),
    html.P(["This dashboard shows the happiness score.",
           html.Br(),
           html.A("World Happiness Report Data Source",
                  href="https://worldhappiness.report",
                  target="_blank")]),
    dcc.RadioItems(options=region, value="North America"),
    dcc.Checklist(options=region, value=["North America"]),
    dcc.Dropdown(options=country, value="United State"),
    dcc.Graph(figure=px.line(happiness[happiness["country"] == "United States"],
                             x="year", y="happiness_score",
                             title="Happiness Score in the USA"))
])

if __name__ == "__main__":
    app.run_server(debug=True)
