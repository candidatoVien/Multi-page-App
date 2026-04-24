import streamlit as st

st.markdown(f"<style>[data-testid='stAppViewContainer'] {{ background-color: {st.session_state.get('main_bg', '#800000')}; }} [data-testid='stSidebar'] {{ background-color: {st.session_state.get('side_bg', '#4d0000')} !important; }} h1, h2, h3, p {{ color: white !important; }}</style>", unsafe_allow_html=True)

st.title("Certificates & Awards")

certs = [
    {"name": "Dean's Lister for 3rd Year First Sem", "date": "March 18, 2026", "img": "portfolio_app/images/Deans_List_3rdyr_1stSem.jpg"},
    {"name": "Best in Backend Development", "date": "December 17, 2025", "img": "portfolio_app/images/Best in Backend Development.jpg"},
    {"name": "Best in UI/UX Design", "date": "December 17, 2025", "img": "portfolio_app/images/Best in UI UX Design.jpg"},
    {"name": "Web Development Hackathon 2025-S3 | First Runner Up ", "date": "December 17, 2025", "img": "portfolio_app/images/Webdev_Hackathon_S3_1strunnerup.jpg"},
    {"name": "Top 7 in Web Development Hackathon 2025-S3 | Semi-Finals ", "date": "December 17, 2025", "img": "portfolio_app/images/Semi_finalsTop7.jpg"},
    {"name": "Python for Beginners", "date": "March 25, 2026", "img": "portfolio_app/images/Python_for_Beginners.jpg"},
    {"name": "Python Essential 1", "date": "March 23, 2026", "img": "portfolio_app/images/Python_Essesntial_1.jpg"},
    {"name": "Introduction to Artificial Intelligence", "date": "March 25, 2026", "img": "portfolio_app/images/Intro_to_AI.jpg"},
    {"name": "Introduction to Generative AI Studio", "date": "March 25, 2026", "img": "portfolio_app/images/Intro_to_Generative_AI_Studio.jpg"},
    {"name": "Encoder-Decoder Architecture", "date": "March 25, 2026", "img": "portfolio_app/images/Encoder_Decoder_Architecture.jpg"},
    
]

for c in certs:
    st.image(c["img"])
    st.subheader(c["name"])
    st.write(f"**Date Acquired:** {c['date']}")
    st.divider()
