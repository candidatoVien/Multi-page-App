import streamlit as st

# Combined CSS for Page Background and Metric Font Scaling
st.markdown(f"""
    <style>
    /* Background and Global Text */
    [data-testid="stAppViewContainer"] {{ 
        background-color: {st.session_state.get('main_bg', '#800000')}; 
    }}
    [data-testid="stSidebar"] {{ 
        background-color: {st.session_state.get('side_bg', '#4d0000')} !important; 
    }}
    h1, h2, h3, p, label {{ 
        color: white !important; 
    }}

    /* Target the Metric Label (Title like GitHub, VS Code) */
    [data-testid="stMetricLabel"] p {{
        font-size: 24px !important;
        font-weight: bold !important;
        color: white !important;
    }}

    /* Target the Metric Value (The "Beginner" text) */
    [data-testid="stMetricValue"] div {{
        font-size: 14px !important;
        color: rgba(255, 255, 255, 0.7) !important;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("My Skills")
st.write("Click the tabs below to explore my expertise!")

tab1, tab2, tab3 = st.tabs(["💻 Programming", "🎨 Creative", "🛠️ Tools"])

with tab1:
    st.subheader("Technical Proficiency")
    st.progress(85, text="Python Development")
    st.progress(60, text="Networking (Cisco)")
    st.progress(90, text="Web Development (HTML/CSS)")

with tab2:
    st.subheader("Creative Interests")
    st.write("- **Dancing:** Hip-hop & TikTok")
    st.write("- **Crocheting:** Bags, Cat Hats, Headbands & Clothing")
    st.write("- **Gaming:** Mobile Legends (ML) & Honor of Kings (HOK)")

with tab3:
    st.subheader("Toolbox")
    # Using 3 columns for better spacing on mobile/smaller screens, 
    # but you can keep 6 if you prefer them all in one row.
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    
    col1.metric("GitHub", "Beginner")
    col2.metric("VS Code", "Beginner")
    col3.metric("HTML", "Beginner")
    col4.metric("CSS", "Beginner")
    col5.metric("JavaScript", "Beginner")
    col6.metric("Streamlit", "Beginner")