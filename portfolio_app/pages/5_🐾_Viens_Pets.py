import streamlit as st

st.markdown(f"<style>[data-testid='stAppViewContainer'] {{ background-color: {st.session_state.get('main_bg', '#800000')}; }} [data-testid='stSidebar'] {{ background-color: {st.session_state.get('side_bg', '#4d0000')} !important; }} h1, h2, h3, p {{ color: white !important; }}</style>", unsafe_allow_html=True)

st.title("My Pets(Nakshie)")

# DOG SECTION
st.subheader("🐕 Dog")
st.image("portfolio_app/images/Hikaro2.jpg", caption="My Dog")
st.write("**Name:** Hikaro")
st.write("**Description:** He was our first dog, his name is hikaro, he was a loving dog, but sadly he passed away last December 16, 2025.  He was my first Heartbreak")

st.divider()

# CAT SECTION
st.subheader("🐈 Cats")
cats = [
    {"name": "Prism", "desc": "Prism is a boy cat, he is cute, it's eyes are different, the left eye is blue and the right eye is yellow. He likes licking his self and our bedsheet as well", "img": "portfolio_app/images/Prism.jpg"},
    {"name": "Caelum", "desc": "This is Caelum, she is a girl, she is malambing and likes to cudddle, prism is his brother", "img": "portfolio_app/images/Caelum.jpg"},
    {"name": "Cosmo", "desc": "This is cosmo, our one and only black cat, the bunso in the family, he likes to sleep with us, and he loves biting me", "img": "portfolio_app/images/Cosmo.jpg"},
]

cols = st.columns(3)
for i, cat in enumerate(cats):
    with cols[i]:
        st.image(cat["img"])
        st.write(f"**Name:** {cat['name']}")
        st.write(cat['desc'])
