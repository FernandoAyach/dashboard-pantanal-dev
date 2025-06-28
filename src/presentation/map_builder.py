# src/presentation/map_builder.py

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from logic.profile_map import ProfileMapData

def build_map_figure(map_data: ProfileMapData) -> go.Figure:
    """
    Constrói a figura do mapa usando os dados encapsulados em ProfileMapData.
    Essa função cuida apenas da visualização.
    """

    # Mapa base com estados coloridos fixamente
    fig = px.choropleth(
        map_data.states_df,
        geojson=map_data.geojson,
        locations='Estado',
        featureidkey='properties.name',
        color='CorFixa',
        color_continuous_scale=[[0, '#add8e6'], [1, '#add8e6']],  # azul claro
        range_color=(0, 1),
    )

    # Converter lista de clusters para DataFrame
    clusters_df = pd.DataFrame(map_data.cluster)

    if not clusters_df.empty:
        for profile_id in clusters_df['investor_profile'].unique():
            profile_data = clusters_df[clusters_df['investor_profile'] == profile_id]

            cor = map_data.color_map.get(profile_id, '#999999')  # cor fallback
            titulo = map_data.title_map.get(profile_id, f"Perfil {profile_id}")

            fig.add_scattergeo(
                lon=profile_data['longitude'],
                lat=profile_data['latitude'],
                text=profile_data['city'] + ' - ' + titulo,
                marker=dict(
                    size=profile_data['quantity'] / 5,
                    color=cor,
                    opacity=0.8,
                    line=dict(width=1, color='black')
                ),
                name=titulo
            )

    # Aparência do mapa
    fig.update_geos(
        fitbounds="locations",
        visible=False,
        showcountries=False,
        showcoastlines=False,
        showland=False,
        showocean=False,
        projection_scale=5,
        center=dict(lat=-15.8, lon=-55)
    )

    fig.update_layout(
        plot_bgcolor="white",             # Cor do fundo do mapa            
        height=510,
        showlegend=False,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        coloraxis_showscale=False,
        modebar=dict(orientation='h'),
    )

    return fig