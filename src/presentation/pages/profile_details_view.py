import streamlit as st
from logic.mapa_logic import construir_mapa
from data.profile_repository_mockup import ProfileRepositoryMockup

def profile_details_view(profile_id: int):
    profile_repository = ProfileRepositoryMockup()
    profiles_df = profile_repository.get_profiles_data()

    profile_id = int(profile_id)

    profile = profiles_df[profiles_df["id"] == profile_id]

    if profile.empty:
        st.error("Perfil não encontrado.")
        return

    perfil = profile.iloc[0]

    st.title(perfil.title)
    st.write(perfil.description)

    with st.spinner("Carregando mapa..."):
        fig = construir_mapa(perfil_filtrado=perfil.category)
        st.plotly_chart(fig, use_container_width=True)

    if st.button("Voltar para a lista"):
        del st.session_state['selected_profile_id']
        st.rerun()
