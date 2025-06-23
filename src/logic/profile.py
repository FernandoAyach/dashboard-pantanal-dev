from dataclasses import dataclass
from typing import List

@dataclass()
class InvestorProfile:
    id: int
    title: str 
    description: str
    color: str


class ProfileService:
    def __init__(self, repository):
       
        self._repository = repository

    def get_all_profiles(self) -> List[InvestorProfile]:
        profile_df = self._repository.get_profiles_data()
        profiles_list = []

        for _, row in profile_df.iterrows():
           profiles_list.append(
               InvestorProfile(
                   id = row['id'],
                   title = row['title'],
                   description = row['description'],
                   color = row['color']
               )
           )
        return profiles_list
