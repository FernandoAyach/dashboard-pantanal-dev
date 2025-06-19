import streamlit as st
from typing import List
from logic.profile import InvestorProfile
from presentation.components.profile_card import profile_card

def investor_profiles_view(profiles: List[InvestorProfile]):
    """
    Renders the main view with the grid of investor profiles.

    Args:
        profiles (List[InvestorProfile]): A list of profile objects to display.
    """

    st.title("Perfis de investidores")

    # Create two main columns to displau the cards
    col1, col2 = st.columns(2)

    with col1:
        for index, profile in enumerate(profiles):
            if index % 2 == 0:
                profile_card(profile)
    
    with col2:
        for index, profile in enumerate(profiles):
            if index % 2 != 0:
                profile_card(profile)


