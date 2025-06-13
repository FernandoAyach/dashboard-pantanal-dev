import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Teste de Streamlit com Plotly")

df = pd.DataFrame({
    "Categoria": ["A", "B", "C", "D"],
    "Valores": [23, 17, 35, 29]
})

fig = px.bar(df, x="Categoria", y="Valores", title="Gráfico de Barras - Plotly")

st.plotly_chart(fig)
