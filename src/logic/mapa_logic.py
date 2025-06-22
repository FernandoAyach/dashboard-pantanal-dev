import plotly.express as px
import plotly.graph_objects as go
from data.geojson_loader import carregar_geojson
from data.estado_data import carregar_estados
from data.cluster_data import carregar_clusters


def construir_mapa(perfil_filtrado=None):
    geojson = carregar_geojson('https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson')
    df_estados = carregar_estados()
    df_clusters = carregar_clusters()

    fig = px.choropleth(
        df_estados,
        geojson=geojson,
        locations='Estado',
        featureidkey='properties.name',
        color='CorFixa',
        color_continuous_scale=[[0, '#add8e6'], [1, '#add8e6']],
        range_color=(0, 1),
    )

    cores = {'Conservador': 'red', 'Moderado': 'green', 'Agressivo': 'purple'}

    if perfil_filtrado:
        df_clusters = df_clusters[df_clusters['Perfil_Investidor'] == perfil_filtrado]

    for perfil in df_clusters['Perfil_Investidor'].unique():
        dados = df_clusters[df_clusters['Perfil_Investidor'] == perfil]
        fig.add_scattergeo(
            lon=dados['Longitude'],
            lat=dados['Latitude'],
            text=dados['Cidade'] + ' - ' + dados['Perfil_Investidor'],
            marker=dict(
                size=dados['Quantidade'] / 5,
                color=cores[perfil],
                opacity=0.8,
                line=dict(width=1, color='black')
            ),
            name=perfil
        )

    fig.update_geos(
        fitbounds="locations",
        visible=False,
        showcountries=False,
        showcoastlines=False,
        showland=False,
        showocean=False,
        projection_scale=5,
        center=dict(lat=-15.8, lon=-120)
    )

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        height=800,
        coloraxis_showscale=False
    )

    return fig

