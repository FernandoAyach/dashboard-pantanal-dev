from dataclasses import dataclass
from data.profile_repository_mockup import ProfileRepositoryMockup
from typing import List
from typing import Optional

@dataclass
class InvestorProfile:
    id: int
    title: str
    description: str
    color: str

class ProfileService:
    def __init__(self, repository: ProfileRepositoryMockup):
        self.repository = repository

    def get_all_profiles(self) -> List[InvestorProfile]:
        df = self.repository.get_profiles_data()
        return [
            InvestorProfile(
                id=row["id"],
                title=row["title"],
                description=row["description"],
                color=row["color"]
            )
            for _, row in df.iterrows()
        ]

    def get_profile_by_id(self, profile_id: int) -> Optional[InvestorProfile]:
        df = self.repository.get_profiles_data()
        row = df[df["id"] == profile_id]
        if row.empty:
            return None
        row = row.iloc[0]
        return InvestorProfile(
            id=row["id"],
            title=row["title"],
            description=row["description"],
            color=row["color"]
        )
