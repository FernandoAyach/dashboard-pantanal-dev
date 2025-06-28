# src/data/cluster_data.py

import pandas as pd

def load_clusters():
    data = [
        ("Brasília", -15.7797, -47.9297, 0, 638402),
        ("Belo Horizonte", -19.9167, -43.9345, 0, 14948),
        ("Curitiba", -25.4284, -49.2733, 0, 14138),
        ("Salvador", -12.9714, -38.5014, 0, 13756),
        ("Fortaleza", -3.7172, -38.5433, 0, 13264),
        ("Manaus", -3.1190, -60.0217, 0, 10563),
        ("Goiania", -16.6869, -49.2648, 0, 9818),
        ("Recife", -8.0476, -34.8770, 0, 8183),
        ("Campinas", -22.9056, -47.0608, 0, 8110),
        ("Guarulhos", -23.4545, -46.5333, 0, 8057),
        ("Belém", -1.4550, -48.5024, 0, 6418),
        ("São Bernardo do Campo", -23.6939, -46.5646, 0, 5462),
        ("Santo André", -23.6639, -46.5383, 0, 5244),
        ("Sorocaba", -23.5015, -47.4526, 0, 4861),
        ("Campo Grande", -20.4697, -54.6201, 0, 4839),
        ("São Luis", -2.5387, -44.2825, 0, 4750),
        ("Florianópolis", -27.5954, -48.5480, 0, 4686),
        ("João Pessoa", -7.1151, -34.8641, 0, 4675),

        ("São Paulo", -23.5505, -46.6333, 1, 89173),

        ("Rio de Janeiro", -22.9068, -43.1729, 2, 41289),

        ("Rio de Janeiro", -22.9068, -43.1729, 3, 33909),

        ("Porto Alegre", -30.0346, -51.2177, 4, 9437),

        ("Osasco", -23.5325, -46.7917, 5, 4923),
        ("Belo Horizonte", -19.9167, -43.9345, 5, 2884),
    ]

    return pd.DataFrame(data, columns=[
        "Cidade", "Latitude", "Longitude", "Perfil_Investidor", "Quantidade"
    ])
