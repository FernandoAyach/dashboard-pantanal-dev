import streamlit as st
from data.profile_map_repository_mockup import ProfileMapRepository
from logic.profile_map import ProfileMapService
from presentation.map_builder import build_map_figure
from data.profile_repository_mockup import ProfileRepositoryMockup
from logic.profile import ProfileService

def profile_details_view(profile_id: int):
    profile_repo = ProfileRepositoryMockup()
    profile_service = ProfileService(profile_repo)
    all_profiles = profile_service.get_all_profiles()

    perfil = next((p for p in all_profiles if p.id == int(profile_id)), None)

    if not perfil:
        st.error("Perfil não encontrado.")
        return

    col1, col2 = st.columns([1.5, 1])

    with col1:
        st.markdown("""
            <div style="text-align: center;">
                <h3 style="margin-top: 0; margin-bottom: 16px; 
                        border: 1px solid #ccc; padding: 8px; 
                        border-radius: 6px;">Mapa de Investidores</h3>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
            <style>
                .modebar {
                    top: 10px !important;
                    left: 10px !important;
                    right: auto !important;
                }
            </style>
        """, unsafe_allow_html=True)
        repo = ProfileMapRepository()
        service = ProfileMapService(repo)
        map_data = service.get_map_data(profile_filter=perfil.id)
        fig = build_map_figure(map_data)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown(f"""
            <div style="
                text-align: center;
                border: 1px solid #ccc;
                padding: 8px;
                border-radius: 6px;
                margin-top: 0;
                margin-bottom: 16px;
                height: 54px;
                display: flex;
                align-items: center;
                justify-content: center;
            ">
                <h3 style="margin: 0;">{perfil.title}</h3>
            </div>
        """, unsafe_allow_html=True)

        st.markdown(perfil.description)

        if st.button("Voltar para lista"):
            del st.session_state["selected_profile_id"]
            st.rerun()
