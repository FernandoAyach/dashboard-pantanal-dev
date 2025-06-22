import pandas as pd

class ProfileRepositoryMockup:
    def get_profiles_data(self) -> pd.DataFrame:
        data = {
            'id': [1, 2, 3, 4, 5, 6, 7, 8],
            'title': [
                'Poupança forte em SP', 'Depósitos à prazo BA', 'Poupança paulista',
                'Depósitos à prazo MG', 'Depósitos a prazo no RS', 'Crédito rural no RJ',
                'Crédito rural no PA', 'Depósitos à prazo no PR'
            ],
            'description': [
                'Investidores paulistas conservadores com foco em poupança',
                'Bahianos moderados com preferência por depósitos a prazo',
                'Poupança com perfil agressivo em SP',
                'Mineiros com foco agressivo em depósitos a prazo',
                'Gaúchos moderados e organizados financeiramente',
                'Crédito rural fluminense com perfil conservador',
                'Perfil agressivo no norte do país',
                'Paranaenses moderados em depósitos'
            ],
            'color': [
                '#002776', '#FFDE00', '#2E8B57', '#4B0082', '#ADFF2F', '#FF69B4',
                '#DC143C', '#C70039'
            ],
            'category': [
                'Conservador', 'Moderado', 'Agressivo',
                'Agressivo', 'Moderado', 'Conservador',
                'Agressivo', 'Moderado'
            ]
        }
        return pd.DataFrame(data)
