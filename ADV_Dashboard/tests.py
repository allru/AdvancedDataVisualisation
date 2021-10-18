import pandas as pd
import plotly.express as px


df = pd.read_csv('ErdbebenDaten.csv')

df = pd.concat([df, df['place'].str.split(', ', expand=True)], axis=1)
df.rename(columns={0: 'place', 1: 'state'}, inplace=True)



fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="state", hover_data=["mag"],
                        color_discrete_sequence=["fuchsia"], zoom=2.5, height=800)
fig.update_layout(mapbox_style="open-street-map")
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
