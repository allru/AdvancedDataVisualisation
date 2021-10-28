import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

state_names = pd.read_csv('stateAbbreviations.csv')
df = pd.read_csv('clean_data.csv')


app.layout = html.Div([

    html.H1("Earthquake Dashboard with Dash", style={'text-align': 'center'}),
    html.H4("Numbers and facts about earthquakes on the U.S. Mainland", style={'text-align': 'left'}),

    dcc.Dropdown(id='state',
                 options=[{"label": x, "value": x}
                          for x in df["state"]],
                 multi=False,
                 value='Texas',
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
def update_graph(state):
    dff = df.copy()
    dff = dff[dff["state"] == state]
    print(dff)

    # Plotly Express
    fig = px.scatter_mapbox(dff, lat="latitude", lon="longitude", hover_name="state",
                            hover_data=["mag"],
                            color_discrete_sequence=["fuchsia"], zoom=2.5, height=800, color='mag',
                            size='mag')
    fig.update_layout(mapbox_style="open-street-map")

    fig2 = px.histogram(df, x="state", title="Earthquakes in US since 01.01.2016-31.12.2020", height=800,
                        color_discrete_sequence=["fuchsia"]).update_xaxes(categoryorder='total descending')

    return fig, fig2


if __name__ == '__main__':
    app.run_server(debug=False)