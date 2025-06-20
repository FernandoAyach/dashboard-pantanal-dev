import streamlit as st
import plotly.express as px
import pandas as pd

#import layers
from data.profile_repository_mockup import ProfileRepositoryMockup
from logic.profile import ProfileService
from presentation.investor_profiles_view import investor_profiles_view


# **** Dependency Injection Setup ****
# This is where we wire up our application layers.
# We could easily swap implementations here (e.g., use a different repository).
profile_repository = ProfileRepositoryMockup()
profile_service = ProfileService(repository= profile_repository)


def dashboard_profile_view(profile_id: int):
    """
    Placeholder for the future profile dashboard
    """
    st.title(f"Dashboard do Perfil ID: {profile_id}")
    st.write("Esta página irá mostrar os detalhes e análises do perfil selecionado.")
    
    if st.button("Voltar para a lista"):
        # Unset the selected profile to return to the main view
        del st.session_state['selected_profile_id']
        st.rerun()

def main():
    
    if 'selected_profile_id' in st.session_state:
        dashboard_profile_view(st.session_state['selected_profile_id'])
    
    else:
        all_profiles = profile_service.get_all_profiles()
        investor_profiles_view(profiles=all_profiles)

if __name__ == "__main__":
    main()



st.title("Teste de Streamlit com Plotly")

df = pd.DataFrame({
    "Categoria": ["A", "B", "C", "D"],
    "Valores": [23, 17, 35, 29]
})

fig = px.bar(df, x="Categoria", y="Valores", title="Gráfico de Barras - Plotly")

st.plotly_chart(fig)
