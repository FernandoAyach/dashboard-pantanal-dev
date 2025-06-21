import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import urllib.request

# Carrega GeoJSON
url = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'
with urllib.request.urlopen(url) as response:
    geojson_brasil = json.load(response)

# Dados base
# Lista completa dos estados brasileiros com siglas e coordenadas aproximadas das capitais
estados_completo = [
    ("AC", "Acre", -9.97499, -67.8243),
    ("AL", "Alagoas", -9.66599, -35.735),
    ("AP", "Amapá", 0.034934, -51.0694),
    ("AM", "Amazonas", -3.11866, -60.0212),
    ("BA", "Bahia", -12.9714, -38.5014),
    ("CE", "Ceará", -3.71722, -38.5433),
    ("DF", "Distrito Federal", -15.7797, -47.9297),
    ("ES", "Espírito Santo", -20.3155, -40.3128),
    ("GO", "Goiás", -16.6869, -49.2648),
    ("MA", "Maranhão", -2.52972, -44.3028),
    ("MT", "Mato Grosso", -15.601, -56.0974),
    ("MS", "Mato Grosso do Sul", -20.4697, -54.6201),
    ("MG", "Minas Gerais", -19.9167, -43.9345),
    ("PA", "Pará", -1.45502, -48.5024),
    ("PB", "Paraíba", -7.11509, -34.8641),
    ("PR", "Paraná", -25.4284, -49.2733),
    ("PE", "Pernambuco", -8.04756, -34.877),
    ("PI", "Piauí", -5.08921, -42.8016),
    ("RJ", "Rio de Janeiro", -22.9068, -43.1729),
    ("RN", "Rio Grande do Norte", -5.79448, -35.211),
    ("RS", "Rio Grande do Sul", -30.0346, -51.2177),
    ("RO", "Rondônia", -8.76077, -63.8999),
    ("RR", "Roraima", 2.81972, -60.6733),
    ("SC", "Santa Catarina", -27.5954, -48.548),
    ("SP", "São Paulo", -23.5505, -46.6333),
    ("SE", "Sergipe", -10.9091, -37.0628),
    ("TO", "Tocantins", -10.184, -48.3336)
]

df_brasil = pd.DataFrame(estados_completo, columns=['UF', 'Estado', 'Latitude', 'Longitude'])
df_brasil['CorFixa'] = 1

sigla_para_nome = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}


df_brasil['Estado'] = df_brasil['UF'].map(sigla_para_nome)
df_brasil['CorFixa'] = 1

# Choropleth base azul
fig = px.choropleth(
    df_brasil,
    geojson=geojson_brasil,
    locations='Estado',
    featureidkey='properties.name',
    color='CorFixa',
    color_continuous_scale=[[0, '#add8e6'], [1, '#add8e6']],
    range_color=(0, 1),
)

# Dados dos clusters
df_clusters = pd.DataFrame({
    'Cidade': [
        'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Porto Alegre',
        'São Gonçalo', 'Duque de Caxias', 'Caxias do Sul', 'Campinas', 'Barueri',
        'Guarulhos', 'Franca', 'Dourados', 'Contagem', 'Uberlândia', 'Petrolina',
        'Sobral', 'Parintins', 'Ananindeua', 'Joinville', 'Blumenau', 'Guarapuava',
        'Cascavel', 'Londrina', 'Maringá', 'Anápolis', 'Brasília',
        'Rio Branco', 'Maceió', 'Macapá', 'Manaus', 'Fortaleza', 'Vitória', 'Goiânia',
        'São Luís', 'Cuiabá', 'Campo Grande', 'Belém', 'João Pessoa', 'Curitiba',
        'Recife', 'Teresina', 'Natal', 'Porto Velho', 'Boa Vista', 'Florianópolis',
        'Aracaju', 'Palmas'
    ],
    'Latitude': [
        -23.5505, -22.9068, -19.9167, -12.9714, -30.0346,
        -22.8268, -22.7858, -29.1678, -22.9056, -23.5057,
        -23.4545, -20.5382, -22.2231, -19.9317, -18.9146, -9.38908,
        -3.686, -2.63741, -1.36567, -26.3045, -26.9194, -25.3902,
        -24.9573, -23.3045, -23.4205, -16.3281, -15.7797,
        -9.97499, -9.66599, 0.034934, -3.11866, -3.71722, -20.3155, -16.6869,
        -2.52972, -15.601, -20.4697, -1.45502, -7.11509, -25.4284,
        -8.04756, -5.08921, -5.79448, -8.76077, 2.81972, -27.5954,
        -10.9091, -10.184
    ],
    'Longitude': [
        -46.6333, -43.1729, -43.9345, -38.5014, -51.2177,
        -43.0634, -43.3117, -51.1794, -47.0608, -46.8799,
        -46.5333, -47.4009, -54.812, -44.0539, -48.2754, -40.5024,
        -40.3482, -56.729, -48.3724, -48.8487, -49.0661, -51.4626,
        -53.459, -51.1696, -51.9333, -48.9527, -47.9297,
        -67.8243, -35.735, -51.0694, -60.0212, -38.5433, -40.3128, -49.2648,
        -44.3028, -56.0974, -54.6201, -48.5024, -34.8641, -49.2733,
        -34.877, -42.8016, -35.211, -63.8999, -60.6733, -48.548,
        -37.0628, -48.3336
    ],
    'Perfil_Investidor': [
        'Conservador', 'Moderado', 'Agressivo', 'Conservador', 'Agressivo',
        'Conservador', 'Moderado', 'Agressivo', 'Conservador', 'Moderado',
        'Agressivo', 'Conservador', 'Moderado', 'Agressivo', 'Conservador', 'Moderado',
        'Agressivo', 'Conservador', 'Moderado', 'Agressivo', 'Conservador', 'Moderado',
        'Agressivo', 'Conservador', 'Moderado', 'Agressivo', 'Moderado',
        'Conservador', 'Agressivo', 'Conservador', 'Moderado', 'Agressivo', 'Conservador', 'Agressivo',
        'Moderado', 'Agressivo', 'Conservador', 'Moderado', 'Agressivo', 'Conservador',
        'Moderado', 'Agressivo', 'Conservador', 'Moderado', 'Agressivo', 'Conservador',
        'Moderado', 'Agressivo'
    ],
    'Quantidade': [
        120, 80, 150, 60, 70,
        90, 85, 50, 100, 65,
        110, 40, 30, 55, 60, 35,
        25, 20, 33, 77, 66, 28,
        45, 72, 62, 41, 200,
        22, 58, 18, 89, 95, 36,
        120, 70, 34, 59, 82, 50, 22,
        121, 111, 64, 91, 23, 19,
        73, 32
    ]
})


cores_perfil = {
    'Conservador': 'red',
    'Moderado': 'green',
    'Agressivo': 'purple'
}
for perfil in df_clusters['Perfil_Investidor'].unique():
    dados = df_clusters[df_clusters['Perfil_Investidor'] == perfil]
    fig.add_scattergeo(
        lon=dados['Longitude'],
        lat=dados['Latitude'],
        text=dados['Cidade'] + ' - ' + dados['Perfil_Investidor'],
        marker=dict(
            size=dados['Quantidade'] / 5,
            color=cores_perfil[perfil],
            opacity=0.8,
            line=dict(width=1, color='black')
        ),
        name=perfil
    )

# Ajustes do mapa
fig.update_geos(
    fitbounds="locations",   # ajusta para os dados
    visible=False,
    showcountries=False,
    showcoastlines=False,
    showland=False,
    showocean=False,
    projection_scale=5,      # controla o zoom (maior = mais zoom)
    center=dict(lat=-15.8, lon=-120)  # centraliza no Brasil (aprox)
)

fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
    height=800,
    coloraxis_showscale=False
)

# Streamlit layout com colunas
st.set_page_config(layout="wide")
col1, col2 = st.columns([2, 1])
with col1:
    st.plotly_chart(fig, use_container_width=True)
with col2:
    st.markdown("### PERFIS")
    st.markdown("""
    <style>
        .modebar {
            right: auto !important;
            left: 100px !important;
        }
    </style>
    """, unsafe_allow_html=True)