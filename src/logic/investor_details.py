from dataclasses import dataclass
import pandas as pd
from data.investor_details_repository_mockup import InvestorDetailsRepository

@dataclass
class InvestorDetailsService:
    repository: InvestorDetailsRepository

    def get_by_profile_id(self, profile_id: int) -> pd.DataFrame:
        df = self.repository.load_data()
        return df[df["perfil_id"] == profile_id]
