import streamlit as st
from logic.profile import InvestorProfile

def profile_card(profile: InvestorProfile): 
    with st.container(border=True):
        col1, col2 = st.columns([0.2, 0.8])

        with col1:
            st.markdown(f"""
                <div style="
                    width: 50px;
                    height: 50px;
                    background-color: {profile.color};
                    border-radius: 50%;
                    margin-top: 20px;">
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.subheader(profile.title)
            st.write(profile.description)

        if st.button("Ver Dashboard", key=f"btn_{profile.id}"):
            st.session_state['selected_profile_id'] = profile.id
            st.rerun()
