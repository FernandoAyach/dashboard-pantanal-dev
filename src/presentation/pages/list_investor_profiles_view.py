import streamlit as st
from typing import List
from st_click_detector import click_detector
from logic.profile import InvestorProfile
from presentation.components.profile_card import profile_card

def list_investor_profiles_view(profiles: List[InvestorProfile]):
    st.title("Perfis de investidores")

    col1, col2 = st.columns(2)

    html_col1 = ""
    html_col2 = ""

    for index, profile in enumerate(profiles):
        card_html = profile_card(profile)

        if index % 2 == 0:
            html_col1 += card_html
        else:
            html_col2 += card_html

    with col1:
        clicked = click_detector(html_col1)

    with col2:
        clicked_right = click_detector(html_col2)

    clicked_id = clicked or clicked_right
    if clicked_id:
        st.session_state["selected_profile_id"] = clicked_id
        st.rerun()

    if "selected_profile_id" in st.session_state:
        st.success(f"Navegar para o perfil {st.session_state['selected_profile_id']}")