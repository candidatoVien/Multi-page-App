import streamlit as st

# Sync Colors and Custom Font Scaling
st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{ background-color: {st.session_state.get('main_bg', '#800000')}; }}
    [data-testid="stSidebar"] {{ background-color: {st.session_state.get('side_bg', '#4d0000')} !important; }}
    h1, h2, h3, p, label, li {{ color: white !important; }}
    .stExpander {{ background-color: rgba(255, 255, 255, 0.1); border-radius: 10px; }}

    /* Custom class to make the Personal Information text bigger */
    .personal-info {{
        font-size: 22px !important;
        line-height: 1.6;
    }}
    .name-title {{
        font-size: 42px !important;
        font-weight: bold;
        margin-bottom: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("About Me")

# --- PERSONAL INFORMATION ---
# Adjusted column ratios to give text more room to be "Big"
col1, col2 = st.columns([1.5, 3]) 

with col1:
    st.image("images/My profile1.jpg", caption="Profile Picture", use_container_width=True)

with col2:
    # Large Name Header
    st.markdown('<p class="name-title">Vien Adah O. Candidato</p>', unsafe_allow_html=True)
    
    # Large Body Text
    st.markdown(f"""
        <div class="personal-info">
            <b>Age:</b> 20<br>
            <b>Birthday:</b> August 25, 2005<br>
            <b>Place of Birth:</b> Poblacion, Baleno, Masbate<br>
            <b>Citizenship:</b> Filipino<br>
            <b>Sex:</b> Female<br>
            <b>Civil Status:</b> Single<br>
            <b>Religion:</b> Roman Catholic<br>
            <b>Address:</b> Poblacion, Baleno, Masbate
        </div>
    """, unsafe_allow_html=True)

st.divider()

# --- FAMILY BACKGROUND ---
st.header("👨‍👩‍👦‍👦 Family Background")

with st.expander("Father's Information"):
    st.write("**Full Name:** Vicente S. Candidato. Jr.")
    st.write("**Age:** 56 | **Birthdate:** June 13, 1970")
    st.write("**CP #:** 09075496679 | **Address:** Poblacion, Baleno, Masbate")

with st.expander("Mother's Information"):
    st.write("**Full Name:** Florence O. Candidato.")
    st.write("**Age:** 56 | **Birthdate:** October 21, 1970")
    st.write("**CP #:** 09684456731 | **Address:** Poblacion, Baleno, Masbate")

with st.expander("1st Brother's Information"):
    st.write("**Full Name:** Vince Joshua O. Candidato")
    st.write("**Age:** 25 | **Birthdate:** April 21, 2001")
    st.write("**CP #:** 09075512925 | **Address:** Poblacion, Baleno, Masbate")

with st.expander("2nd Brother's Information"):
    st.write("**Full Name:** Vince Emman O. Candidato")
    st.write("**Age:** 18 | **Birthdate:** March 26, 2008")
    st.write("**CP #:** 09994576532 | **Address:** Poblacion, Baleno, Masbate")

with st.expander("3rd Brother's Information"):
    st.write("**Full Name:** Vince Floyd O. Candidato")
    st.write("**Age:** 16 | **Birthdate:** January 20, 2010")
    st.write("**CP #:** 09684296678 | **Address:** Poblacion, Baleno, Masbate")

st.divider()

# --- EDUCATIONAL ATTAINMENT ---
st.header("🎓 Educational Attainment")
st.write("**College:** Bachelor of Science in Computer Science - DEBESMSCAT")
st.write("**Secondary:** Liceo De Baleno (Graduated 2023)")
st.write("**Primary:** Polot Elementary School (Graduated 2016)")

st.divider()

# --- HOBBIES WITH MEDIA ---
st.header("🧶 My Hobbies")
h_col1, h_col2 = st.columns(2)

with h_col1:
    st.subheader("🎤 Singing")
    st.image("images/Singing.jpg", caption="Me performing")
    
    st.subheader("🎮 Playing ML")
    st.image("images/Ml.jpg", caption="Rank: Mythical Glory")
    
    st.subheader("🧶 Crocheting")
    st.image("images/crocheting.jpg", caption="Handmade with love")
with h_col2:
    st.subheader("💃 Dancing")
    st.video("videos/dancing.mp4") 
    st.video("videos/Dancing2.mp4") 
    
    