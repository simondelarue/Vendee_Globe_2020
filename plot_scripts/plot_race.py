import plotly.graph_objects as go
import pandas as pd
from plotly.offline import plot

test = pd.read_csv('data/plot.csv')

skippers = test['Skipper'].unique()
skipper1 = skippers[0]
temp = test[test['Skipper']==skipper1]
nl = '\n'
bateau = temp['Bateau'].unique()[0]
vitesse_kmh = temp['Vitesse kmh'].unique()[0]
position = temp['Position'].unique()[0]
foil = temp['Foil'].unique()[0]
nb_skip = test['Skipper'].nunique()

fig = go.Figure(go.Scattermapbox(
        mode = "markers+lines",
        lon = temp['Longitude'].values,
        lat = temp['Latitude'].values,
        name = skipper1,
        hovertemplate = f'<b>Bateau</b>: {bateau}<br>' +
                        f'<b>Skipper</b>: {skipper1}<br>' +
                        f'<b>Position</b>: {position}<br>' +
                        f'<b>Vitesse kmh</b>: {vitesse_kmh}<br>' + 
                        f'<b>Foil</b>: {foil}<br>',
        marker = {'size': 2}))

for skip in skippers[1:len(skippers)]:
    temp = test[test['Skipper']==skip]
    nl = '\n'
    bateau = temp['Bateau'].unique()[0]
    vitesse_kmh = temp['Vitesse kmh'].unique()[0]
    position = temp['Position'].unique()[0]
    foil = temp['Foil'].unique()[0]

    fig.add_trace(go.Scattermapbox(
        mode = "markers+lines",
        lon = temp['Longitude'].values,
        lat = temp['Latitude'].values,
        hovertemplate = f'<b>Bateau</b>: {bateau}<br>' +
                        f'<b>Skipper</b>: {skip}<br>' +
                        f'<b>Position</b>: {position}<br>' +
                        f'<b>Vitesse kmh</b>: {vitesse_kmh}<br>' + 
                        f'<b>Foil</b>: {foil}<br>',
        name = skip,
        marker = {'size': 2}))

fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": ["https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"]
        }
      ])
fig.update_layout(
    autosize = True,
    margin ={'l':0,'t':0,'b':0,'r':0},
    mapbox = {
        'center': {'lon': 10, 'lat': 10},
        'style': "stamen-terrain",
        'center': {'lon': -20, 'lat': -20},
        'zoom': 1})

plot(fig, validate = False, filename='plot_race.html',
   auto_open=True)
#fig.show()
