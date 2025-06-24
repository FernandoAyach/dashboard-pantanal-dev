import pandas as pd

def load_states():
    states = [
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

    df = pd.DataFrame(states, columns=['UF', 'Estado', 'Latitude', 'Longitude'])
    df['CorFixa'] = 1
    return df
