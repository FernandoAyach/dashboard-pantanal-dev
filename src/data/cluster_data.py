import pandas as pd

def carregar_clusters():
    dados = {
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
    }
    return pd.DataFrame(dados)