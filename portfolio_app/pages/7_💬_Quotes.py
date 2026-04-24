import streamlit as st

# Sync Colors from Session State
st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{ background-color: {st.session_state.get('main_bg', '#800000')}; }}
    [data-testid="stSidebar"] {{ background-color: {st.session_state.get('side_bg', '#4d0000')} !important; }}
    h1, h2, h3, p, label, li {{ color: white !important; }}
    
    /* Quote Styling */
    .quote-box {{
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-left: 5px solid white;
        border-radius: 10px;
        margin-bottom: 20px;
        font-style: italic;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("💬 Daily Inspiration")
st.write("Words have the power to change the world. Here are a few of my favorites:")

# --- STATIC QUOTES ---
st.markdown("""
    <div class="quote-box">
        "The only way to do great work is to love what you do." <br>
        <b>— Steve Jobs</b>
    </div>
    <div class="quote-box">
        "Success is not final, failure is not fatal: it is the courage to continue that counts." <br>
        <b>— Winston Churchill</b>
    </div>
    <div class="quote-box">
        "Computer Science is not just about the code you write; it's about the problems you are brave enough to solve and the persistence to keep learning when the logic doesn't make sense yet." <br>
    </div>
""", unsafe_allow_html=True)

st.divider()

# --- USER INPUT SECTION ---
st.header("✨ Share Your Favorite Quote")
st.write("Is there a quote that inspires you? Share it below!")

with st.form("quote_form"):
    user_quote = st.text_area("Write the quote here:")
    author = st.text_input("Who said it?")
    submit_button = st.form_submit_button("Send Quote")

    if submit_button:
        if user_quote and author:
            # For now, this displays a success message as per instructions
            st.success(f"Thank you for sharing! \"{user_quote}\" — {author}")
            
            # Tip: In a real app, you would save this to a database or a file.
            # st.balloons() 
        else:
            st.error("Please provide both the quote and the author.") 