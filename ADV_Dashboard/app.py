import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df = pd.read_csv('ErdbebenDaten.csv')

df = pd.concat([df, df['place'].str.split(', ', expand=True)], axis=1)

df.rename(columns={0: 'place', 1: 'state'}, inplace=True)


app.layout = html.Div([

    html.H1("Earthquake Dashboard with Dash", style={'text-align': 'center'}),
    html.H4("Numbers and facts about earthquakes in the world", style={'text-align': 'left'}),

    dcc.Dropdown(id='state',
                 options=[
                     {"label": "Nevada", "value": 'Nevada'},
                     {"label": "Texas", "value": 'Texas'},
                     {"label": "Washington", "value": 'Washington'}],
                 multi=False,
                 value='Nevada',
                 style={"width": "40%"}),

    dcc.Graph(id='plot1', figure={}),
    html.Br(),

    dcc.Graph(id='plot2', figure={})
])


@app.callback(
    [Output(component_id='plot1', component_property='figure'),
     Output(component_id='plot2', component_property='figure')],
    [Input(component_id='state', component_property='value')]
)
def update_graph(option_slctd):
    dff = df.copy()
    dff = dff[dff["state"] == option_slctd]

    # Plotly Express
    fig = px.scatter(dff, x='mag', y='depth', color="depth")

    fig2 = px.scatter(dff, x="latitude", y="longitude",
                      color="mag", size="depth")

    return fig, fig2


if __name__ == '__main__':
    app.run_server(debug=False)