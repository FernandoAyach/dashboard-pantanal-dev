import streamlit as st

from data.profile_repository_mockup import ProfileRepositoryMockup
from logic.profile import ProfileService
from presentation.pages.list_investor_profiles_view import list_investor_profiles_view
from presentation.pages.profile_details_view import profile_details_view

profile_repository = ProfileRepositoryMockup()
profile_service = ProfileService(repository= profile_repository)

def main():
    if 'selected_profile_id' in st.session_state:
        profile_details_view(st.session_state['selected_profile_id'])
        return
    
    all_profiles = profile_service.get_all_profiles()
    list_investor_profiles_view(profiles=all_profiles)

if __name__ == "__main__":
    main()