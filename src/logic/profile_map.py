from dataclasses import dataclass
from typing import List, Dict, Optional
from data.profile_map_repository_mockup import ProfileMapRepository
from data.profile_repository_mockup import ProfileRepositoryMockup
from logic.profile import ProfileService
import pandas as pd

@dataclass
class InvestorCluster:
    city: str
    investor_profile: int
    latitude: float
    longitude: float
    quantity: int

@dataclass
class ProfileMapData:
    geojson: Dict
    states_df: pd.DataFrame
    cluster: List[InvestorCluster]
    color_map: Dict[int, str]
    title_map: Dict[int, str]
    profile_filter: Optional[int] = None

class ProfileMapService:

    def __init__(self, repository: ProfileMapRepository):
        self._repository = repository

    def get_map_data(self, profile_filter: Optional[int] = None) -> ProfileMapData:
        geojson = self._repository.get_geojson_data()
        states_df = self._repository.get_states_data()
        clusters_df = self._repository.get_cluster_data()

        if profile_filter is not None:
            clusters_df = clusters_df[clusters_df["Perfil_Investidor"] == profile_filter]

        profile_repo = ProfileRepositoryMockup()
        profile_service = ProfileService(profile_repo)
        profiles = profile_service.get_all_profiles()

        color_map = {p.id: p.color for p in profiles}
        title_map = {p.id: p.title for p in profiles}

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
            cluster=investor_clusters,
            color_map=color_map,
            title_map=title_map,
            profile_filter=profile_filter
        )
