import streamlit as st
import time
import base64
import os

# Page Configuration
st.set_page_config(page_title="My Portfolio", page_icon="🏠", layout="wide")

# Function to convert image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Initialize Colors in Session State
if 'main_bg' not in st.session_state:
    st.session_state.main_bg = "#800000"
if 'side_bg' not in st.session_state:
    st.session_state.side_bg = "#4d0000"

# Sidebar Customization Controls
st.sidebar.title("🎨 Theme Settings")
st.session_state.main_bg = st.sidebar.color_picker("Page Background", st.session_state.main_bg)
st.session_state.side_bg = st.sidebar.color_picker("Sidebar Background", st.session_state.side_bg)

# Aesthetic CSS Injection
st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{ background-color: {st.session_state.main_bg}; }}
    [data-testid="stSidebar"] {{ background-color: {st.session_state.side_bg} !important; }}
    h1, h2, h3, p, span, label, li {{ color: white !important; font-family: 'Inter', sans-serif; }}
    
    .profile-container {{
        display: flex;
        justify-content: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }}
    .profile-circle {{
        border-radius: 50%;
        width: 250px;
        height: 250px;
        object-fit: cover;
        border: 5px solid white;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    }}
    </style>
    """, unsafe_allow_html=True)

# LOAD IMAGE LOGIC
img_path = "https://github.com/candidatoVien/Multi-page-App/blob/main/portfolio_app/images/My%20profile_4.jpg"

if os.path.exists(img_path):
    img_base64 = get_base64_of_bin_file(img_path)
    st.markdown(f"""
        <div class="profile-container">
            <img src="data:image/png;base64,{img_base64}" class="profile-circle">
        </div>
        """, unsafe_allow_html=True)
else:
    # Fallback if image is missing
    st.warning(f"Image '{img_path}' not found. Please ensure the file is in the same folder as Home.py")

# Centered Title and Header
st.markdown("<h1 style='text-align: center;'>Welcome to My Personal Website</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>I am Vien Adah O. Candidato, a BSCS 3rd Year Student</h3>", unsafe_allow_html=True)

st.divider()
st.info("I am a 20-year-old student currently in my third year of pursuing a Bachelor of Science in Computer Science at DEBESMSCAT. While I may not be the most expert coder in the room yet, I approach every challenge with a deep commitment to continuous growth and a genuine passion for discovery. I believe that the tech industry isn't just about what you already know, but how quickly and enthusiastically you can explore new knowledge and adapt to emerging tools. Navigate through the sidebar to learn more about me, my skills, and my projects.")

# 30-Second Rating Prompt
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

if time.time() - st.session_state.start_time > 30:
    st.sidebar.divider()
    st.sidebar.write("Rate my Website:")
    st.sidebar.feedback("stars")
