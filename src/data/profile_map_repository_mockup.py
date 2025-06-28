import pandas as pd
from data.geojson_loader import load_geojson
from data.state_data import load_states
from data.cluster_data import load_clusters

class ProfileMapRepository:

    def get_geojson_data(self) -> dict:
        geojson_url = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'
        return load_geojson(geojson_url)
    
    def get_states_data(self) -> pd.DataFrame:
        return load_states()
    
    def get_cluster_data(self) -> pd.DataFrame:
        return load_clusters()
