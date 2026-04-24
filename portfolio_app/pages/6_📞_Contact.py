import streamlit as st

st.markdown(f"<style>[data-testid='stAppViewContainer'] {{ background-color: {st.session_state.get('main_bg', '#800000')}; }} [data-testid='stSidebar'] {{ background-color: {st.session_state.get('side_bg', '#4d0000')} !important; }} h1, h2, h3, p, label {{ color: white !important; }}</style>", unsafe_allow_html=True)

st.title("Get in Touch")

with st.container():
    st.write("Send me a message for collaborations or inquiries.")
    with st.form("contact"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        msg = st.text_area("Message")
        btn = st.form_submit_button("Send")
        if btn:
            if name and email and msg:
                st.success(f"Message received from {name}! I will reach out soon.")
            else:
                st.error("Please fill in all fields.")

st.divider()
st.subheader("My Socials")
st.write("🔵 [Facebook Messenger](https://www.facebook.com/ien.candidato)")
st.write("📸 [Instagram](https://www.instagram.com/vi_en_ny")
st.write("📞 Phone: +63 9204576841")
st.write("📧 Email: candidatovien327@gmail.com")