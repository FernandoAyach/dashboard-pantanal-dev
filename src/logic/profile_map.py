from dataclasses import dataclass
from typing import List, Dict, Optional
from data.profile_map_repository_mockup import ProfileMapRepository
import pandas as pd

@dataclass
class InvestorCluster:
    city: str
    investor_profile: str
    latitude: float
    longitude: float
    quantity: int

@dataclass
class ProfileMapData:
    geojson: Dict
    states_df: pd.DataFrame
    cluster: List[InvestorCluster]

class ProfileMapService:

    def __init__(self, repository: ProfileMapRepository):
        self._repository = repository

    def get_map_data(self, profile_filter: Optional[str] = None) -> ProfileMapData:
        geojson = self._repository.get_geojson_data()
        states_df = self._repository.get_states_data()
        clusters_df = self._repository.get_cluster_data()

        # Df to list of domain objects
        investor_clusters = [
            InvestorCluster(
                city=row['Cidade'],
                investor_profile=row['Perfil_Investidor'],
                latitude=row['Latitude'],
                longitude=row['Longitude'],
                quantity=row['Quantidade']
            )
            for _, row in clusters_df.iterrows()
        ]

        return ProfileMapData(
            geojson=geojson,
            states_df=states_df,
            clusters=investor_clusters
        )
    

        
