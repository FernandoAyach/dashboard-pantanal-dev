from logic.profile import InvestorProfile

def profile_card(profile: InvestorProfile) -> str:
    return f"""
    <a href="#" id="{profile.id}" style="text-decoration: none; color: inherit;">
        <div style="
            border: 1px solid #DDD;
            border-radius: 8px;
            padding: 16px;
            margin: 10px 0;
            display: flex;
            cursor: pointer;
            transition: box-shadow 0.3s ease;
        " onmouseover="this.style.boxShadow='0 4px 12px rgba(0,0,0,0.1)'" 
          onmouseout="this.style.boxShadow='none'">

            <div style="
                flex: 0 0 50px;
                height: 50px;
                background-color: {profile.color};
                border-radius: 50%;
                margin-right: 16px;
                margin-top: 8px;">
            </div>

            <div>
                <h4 style="margin: 0 0 8px 0;">{profile.title}</h4>
                <p style="margin: 0; color: #555;">{profile.description}</p>
            </div>
        </div>
    </a>
    """
