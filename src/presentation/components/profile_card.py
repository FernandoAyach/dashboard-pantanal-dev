import streamlit as st
from logic.profile import InvestorProfile

def profile_card(profile: InvestorProfile): 
    """
    Renders a single investor profile card.
    
    Args:
        profile (InvestorProfile): The profile object to render.
    """

    # Use container with a border for the card
    with st.container(border=True):
        # Create two columns, one for the colored circle, and one for the text
        col1, col2 = st.columns([0.2, 0.8])

        with col1:
            st.markdown(f"""
                <div style="
                    width: 50px;
                    width: 50px;
                    background-color: {profile.color};
                    border-radius: 50%;
                    margin-top: 20px;">
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.subheader(profile.title)
            st.write(profile.description)

        # We create a button that will handle the navigation.
        # The key is unique for each card.
        # When clicked, it will set the session_state.
        if st.button("Ver Dashboard", key=f"btn_{profile.id}"):
            st.session_state['selected_profile_id'] = profile.id
            st.rerun()
