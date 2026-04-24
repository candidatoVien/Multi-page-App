import streamlit as st

st.markdown(f"<style>[data-testid='stAppViewContainer'] {{ background-color: {st.session_state.get('main_bg', '#800000')}; }} [data-testid='stSidebar'] {{ background-color: {st.session_state.get('side_bg', '#4d0000')} !important; }} h1, h2, h3, p, .stCaption {{ color: white !important; }}</style>", unsafe_allow_html=True)

st.title("My Projects")

# To add more projects, just add another dictionary to this list:
my_projects = [
    {"title": "Beach Reservation System", "desc": "A simple Beach Reservation system with input and Output using Python", "img": "images/Case Study.jpg"},
    {"name": "Asia Novo Hotel Reservation System", "desc": "A database system using MS Access", "img": "images/Asia_Novo_Botique_Hotel_Reservation_DataBase_System.jpg"},
    {"title": "Chravian Photobooth", "desc": "A Photobooth Website using Html, CSS, and JavaScript", "img": "images/Chravian_Photobooth.jpg"},
    {"title": "CPU Instruction Cycle Simulator", "desc": "A simple simulator, presenting the cycle of CPU using Python.", "img": "images/CPU_Instruction_Simulator.jpg"},
    {"title": "Personal Site", "desc": "A personal site using HTML, CSS, and JavaScript that have been uploaded on GitHub.", "img": "images/Personal_Site.jpg"},
    {"title": "Hotel  Reservation", "desc": "A simple Hotel Reservation using Xampp", "img": "images/Hotel_Reservation_Using_Xampp.jpg"},
    {"title": "Library Management System", "desc": "A simple Library Management System Handling Borrowing and returning Books using Python", "img": "images/Library_Management_System.jpg"},
]

for p in my_projects:
    st.image(p["img"], use_container_width=True)
    st.subheader(p.get("title") or p.get("name"))
    st.write(p["desc"])
    st.divider()