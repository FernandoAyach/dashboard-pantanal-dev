from dataclasses import dataclass
from typing import Optional
import pandas as pd

@dataclass()
class InvestorProfile:
    """
    Represents an investor profile.
    This is a Plain Old Python Object (POPO) with no logic,
    only data attributes. It represents our core domain entity.
    """
    id: int
    title: str 
    description: str
    color: str


class ProfileService:
    """
    This class contains the business logic related to investor profiles.
    It decouples the application logic from the data source and the presentation.
    """

    def __init__(self, repository):
       
        self._repository = repository

    
    def get_all_profiles(self) -> List[InvestorProfile]:
        """
        Gets raw data from the repository and maps it to a list of
        InvestorProfile domain objects.
        """
        
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
