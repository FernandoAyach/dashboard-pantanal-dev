import streamlit as st
from typing import List
from logic.profile import InvestorProfile
from presentation.components.profile_card import profile_card

def list_investor_profiles_view(profiles: List[InvestorProfile]):
    st.title("Perfis de investidores")

    col1, col2 = st.columns(2)

    with col1:
        for index, profile in enumerate(profiles):
            if index % 2 == 0:
                profile_card(profile)
    
    with col2:
        for index, profile in enumerate(profiles):
            if index % 2 != 0:
                profile_card(profile)


