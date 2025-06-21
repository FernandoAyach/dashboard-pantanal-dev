import pandas as pd

class ProfileRepositoryMockup:
    def get_profiles_data(self) -> pd.DataFrame:
        data = {
            'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'title': [
                'Poupança forte em SP', 'Depósitos à prazo BA', 'Poupança paulista',
                'Depósitos à prazo MG', 'Depósitos a prazo no RS', 'Depósitos à prazo MG',
                'Crédito rural no RJ', 'Crédito rural no RJ', 'Poupança forte em SP',
                'Depósitos à prazo no PR'
            ],
            'description': [
                'Investidores de São Paulo que gostam de poupança',
                'Investidores de São Paulo que gostam de poupança',
                'Investidores de São Paulo que gostam de poupança',
                'Investidores de São Paulo que gostam de poupança',
                'Investidores de São Paulo que gostam de poupança',
                'Investidores de São Paulo que gostam de poupança',
                'Investidores de São Paulo que gostam de poupança',
                'Investidores de São Paulo que gostam de poupança',
                'Investidores de São Paulo que gostam de poupança',
                'Investidores de São Paulo que gostam de poupança'
            ],
            'color': [
                '#002776', '#FFDE00', '#2E8B57', '#4B0082', '#ADFF2F', '#FF69B4',
                '#DC143C', '#FFA500', '#8A2BE2', '#C70039'
            ]
        }
        return pd.DataFrame(data)