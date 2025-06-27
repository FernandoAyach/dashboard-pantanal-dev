import pandas as pd

class InvestorDetailsRepository:
    def __init__(self, csv_path: str = "data/investor_details_mock.csv"):
        self.csv_path = csv_path

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.csv_path)
