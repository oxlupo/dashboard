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
    html.H1("World Happiness dashboard"),
    html.P(["This dashboard shows the happiness score.",
            html.Br(),
            html.A("World happiness report Data source",
                   href="https://worldhappiness.report",
                   target="_blank")]),
    dcc.RadioItems(id="region-radio",
                   options=happiness["region"].unique(),
                   value="North America"),

    dcc.Dropdown(id="country-dropdown",
        options=happiness["country"].unique(),
        value="United States"),
    dcc.RadioItems(id="data-radio",
                   options={
                      "Happiness_score:": "Happiness_score",
                      "Happiness_rank:": "Happiness_rank"
                   },
                   value="happiness_score"),
    dcc.Graph(id="happiness-graph",),
    html.Div(id="average-div")
])


@app.callback(
    Output("country-dropdown", "option"),
    Output("country-dropdown", "value"),
    Input("region-radio", "value")
)
def update_dropdown(selected_region):
    filtered_happiness = happiness[happiness["country"] == selected_region]
    country_option=filtered_happiness["country"].unique()
    return country_option, country_option[0]


@app.callback(
    Output(component_id="happiness-graph", component_property="figure"),
    Output(component_id="average-div", component_property='children'),
    Input(component_id="country-dropdown", component_property="value"),
    Input(component_id="data-radio", component_property="value"))
def update_graph(selected_country, selected_data):
    """update the country that choose"""
    filtered_happiness = happiness[happiness["country"] == selected_country]
    line_fig = px.line(filtered_happiness,
                     x="year",
                     y=selected_data,
                     title=f'{selected_data} in {selected_country}')
    selected_avg = filtered_happiness[selected_data].mean()
    return line_fig, f"The average {selected_data} for {selected_country}" \
                     f"is{selected_avg}"


def update_output_div(input_text):
    """update text"""
    return f"text:{input_text}"


if __name__ == "__main__":
    app.run_server(debug=True)
