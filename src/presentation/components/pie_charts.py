import streamlit as st
import plotly.express as px

def show_profile_pies(df):
    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.pie(df, names="genero", title="Gênero")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.pie(df, names="faixa_etaria", title="Faixa etária")
        st.plotly_chart(fig2, use_container_width=True)
