import streamlit as st

# Custom session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def check_password(password_input):
    correct_password = st.secrets["password"]
    if password_input == correct_password:
        return True
    return False

def main_app():
    """
    Your main app goes here
    """
    st.title("Welcome to the Protected App!")
    st.write("You are now logged in and can see this content.")

# If not logged in, show login. Else show main app.
if not st.session_state.logged_in:
    st.title("Please log in")
    password_input = st.text_input("Enter Password", type='password')

    if st.button("Login"):
        if check_password(password_input):
            st.session_state.logged_in = True
            main_app()
        else:
            st.warning("Incorrect password. Please try again.")
else:
    main_app()
