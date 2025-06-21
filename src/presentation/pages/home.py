import streamlit as st

from logic.mapa_logic import construir_mapa
from data.profile_repository_mockup import ProfileRepositoryMockup
from logic.profile import ProfileService
from presentation.pages.list_investor_profiles_view import list_investor_profiles_view
from presentation.pages.profile_details_view import profile_details_view

def render_home():
    st.set_page_config(layout="wide")

    if "selected_profile_id" in st.session_state:
        profile_details_view(st.session_state["selected_profile_id"])
        return
    
    col1, col2 = st.columns([1.5, 1])  # Ajuste conforme quiser

    with col1:
        st.plotly_chart(construir_mapa(), use_container_width=True)

    with col2:
        profile_repository = ProfileRepositoryMockup()
        profile_service = ProfileService(repository=profile_repository)
        all_profiles = profile_service.get_all_profiles()
        list_investor_profiles_view(profiles=all_profiles)

       