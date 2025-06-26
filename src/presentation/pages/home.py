import streamlit as st
from data.profile_repository_mockup import ProfileRepositoryMockup
from logic.profile import ProfileService
from presentation.pages.list_investor_profiles_view import list_investor_profiles_view
from presentation.pages.profile_details_view import profile_details_view
from data.profile_map_repository_mockup import ProfileMapRepository
from logic.profile_map import ProfileMapService
from presentation.map_builder import build_map_figure

def render_home():
    st.set_page_config(layout="wide")

    # Se um perfil estiver selecionado, mostrar tela de detalhes
    if "selected_profile_id" in st.session_state:
        profile_details_view(st.session_state["selected_profile_id"])
        return

    # Spinner centralizado
    spinner_html = st.empty()
    spinner_html.markdown("""
        <style>
            .spinner-overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background: rgba(255, 255, 255, 0.8);
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 9999;
            }
            .loader {
                border: 8px solid #f3f3f3;
                border-top: 8px solid #3498db;
                border-radius: 50%;
                width: 60px;
                height: 60px;
                animation: spin 1s linear infinite;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
        <div class="spinner-overlay">
            <div class="loader"></div>
        </div>
    """, unsafe_allow_html=True)

    # Carregamento real
    repo = ProfileMapRepository()
    service = ProfileMapService(repo)
    map_data = service.get_map_data()
    mapa = build_map_figure(map_data)
    profile_repository = ProfileRepositoryMockup()
    profile_service = ProfileService(repository=profile_repository)
    all_profiles = profile_service.get_all_profiles()

    # Remove o spinner
    spinner_html.empty()

    # Layout com colunas
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

        st.plotly_chart(mapa, use_container_width=True)

    with col2:
        st.markdown("""
            <div style="text-align: center;">
                <h3 style="margin-top: 0; margin-bottom: 16px; 
                        border: 1px solid #ccc; padding: 8px; 
                        border-radius: 6px;">Perfis de investidores</h3>
            </div>
        """, unsafe_allow_html=True)
        list_investor_profiles_view(profiles=all_profiles)


