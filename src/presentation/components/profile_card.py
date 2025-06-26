from logic.profile import InvestorProfile

def profile_card(profile: InvestorProfile) -> str:
    return f"""
    <a href="#" id="{profile.id}" style="text-decoration: none; color: inherit;">
        <div style="
            border: 1px solid #DDD;
            border-radius: 12px;
            padding: 16px;
            margin: 12px 0;
            height: 120px;  
            display: flex;
            align-items: center;
            gap: 16px;
            cursor: pointer;
            transition: box-shadow 0.3s ease;
            overflow: hidden;
        " onmouseover="this.style.boxShadow='0 4px 12px rgba(0,0,0,0.1)'" 
          onmouseout="this.style.boxShadow='none'">

            <div style="
                flex: 0 0 50px;
                height: 50px;
                background-color: {profile.color};
                border-radius: 50%;">
            </div>

            <div style="flex: 1; overflow: hidden;">
                <h4 style="
                    margin: 0 0 4px 0;
                    font-size: 16px;
                    white-space: nowrap;
                    overflow: hidden;
                    text-overflow: ellipsis;
                ">{profile.title}</h4>
                
                <p style="
                    margin: 0;
                    color: #555;
                    display: -webkit-box;
                    -webkit-line-clamp: 2;
                    -webkit-box-orient: vertical;
                    overflow: hidden;
                    font-size: 14px;
                ">{profile.description}</p>
            </div>
        </div>
    </a>
    """

