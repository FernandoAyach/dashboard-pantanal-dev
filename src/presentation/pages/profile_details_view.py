import streamlit as st
import plotly.express as px
from data.profile_map_repository_mockup import ProfileMapRepository
from logic.profile_map import ProfileMapService
from presentation.map_builder import build_map_figure
from data.profile_repository_mockup import ProfileRepositoryMockup
from logic.profile import ProfileService
from data.investor_details_repository_mockup import InvestorDetailsRepository
from logic.investor_details import InvestorDetailsService
from presentation.components.pie_charts import show_profile_pies

def profile_details_view(profile_id: int):
    profile_repo = ProfileRepositoryMockup()
    profile_service = ProfileService(profile_repo)
    all_profiles = profile_service.get_all_profiles()

    perfil = next((p for p in all_profiles if p.id == int(profile_id)), None)

    if not perfil:
        st.error("Perfil não encontrado.")
        return

    details_repo = InvestorDetailsRepository()
    details_service = InvestorDetailsService(details_repo)
    df_investidores = details_service.get_by_profile_id(perfil.id)

    def gerar_pizza(dados, coluna, titulo):
        contagem = dados[coluna].value_counts().reset_index()
        contagem.columns = [coluna, "quantidade"]
        fig = px.pie(contagem, names=coluna, values="quantidade", title=titulo, hole=0.4)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        return fig

    genero_fig = gerar_pizza(df_investidores, "genero", "Gênero")
    faixa_etaria_fig = gerar_pizza(df_investidores, "faixa_etaria", "Faixa etária")

    # Gráfico de distribuição pelos estados
    estado_fig = gerar_pizza(df_investidores, "estado", "Distribuição pelos estados do Brasil")

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

        st.plotly_chart(estado_fig, use_container_width=True)
        st.plotly_chart(genero_fig, use_container_width=True)
        st.plotly_chart(faixa_etaria_fig, use_container_width=True)

        if st.button("Voltar para lista"):
            del st.session_state["selected_profile_id"]
            st.rerun()
