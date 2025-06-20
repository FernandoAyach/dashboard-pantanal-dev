import streamlit as st

def profile_details_view(profile_id: int):
    st.title(f"Dashboard do Perfil ID: {profile_id}")
    st.write("Esta página irá mostrar os detalhes e análises do perfil selecionado.")
    
    if st.button("Voltar para a lista"):
        del st.session_state['selected_profile_id']
        st.rerun()