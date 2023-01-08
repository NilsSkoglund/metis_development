from deta import Deta
import streamlit as st
import time
from tools import test_login_page

# Connect to Deta Base with your Project Key
st.session_state["deta"] = Deta(st.secrets["deta_key"])

test_login_page.custom_authenticate()

if st.session_state["authentication_status"]:
    # litet hack för bättre ui/ux
    time.sleep(1)

    # frontend
    st.session_state["authenticator"].logout('Logout', 'main')
    # litet hack för bättre ui/ux
    time.sleep(1)
    st.write(f'Welcome {st.session_state["name"]}')

    # backend
    # connect to database
    # database name based on username - new session state variable
    st.session_state["db"] =\
    st.session_state["deta"].Base(st.session_state["username"])

    test_login_page.custom_user_logged_in()

# frontend
    # fel inloggningsuppgifter
if st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')

# frontend
    # ej angett inloggningsuppgifter
if st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')

    # frontend/backend
        # användare väljar att registrera ny profil
        # widget - new session state variable
    st.checkbox("Registrera", key="register_user")
    if st.session_state["register_user"]:
        test_login_page.custom_register_user()