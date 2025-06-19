# data/profile_repository.py
import pandas as pd

class ProfileRepository:
    """
    This class is responsible for loading the investor profile data.
    It simulates loading from a data source (like a CSV or database)
    and returns a pandas DataFrame.
    """

    def get_profiles_data(self) -> pd.DataFrame:
        """
        Loads and returns a DataFrame with profile data.
        In a real-world scenario, this method would connect to a database,
        read a file, or call an API.
        
        The 'category' column has been removed as it's no longer needed.
        """
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