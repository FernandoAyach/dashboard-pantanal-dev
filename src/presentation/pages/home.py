import streamlit as st
from logic.mapa_logic import construir_mapa

def render_home():
    st.set_page_config(layout="wide")
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.plotly_chart(construir_mapa(), use_container_width=True)
    with col2:
        st.markdown("### PERFIS")
        st.markdown("""
        <style>
            .modebar {
                right: auto !important;
                left: 100px !important;
            }
        </style>
        """, unsafe_allow_html=True)