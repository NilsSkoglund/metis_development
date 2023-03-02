from deta import Deta
import streamlit as st
import time
from tools import dev_login_page
from tools import dev_init_session_state_vars

dev_init_session_state_vars.init_session_state()
dev_login_page.custom_authenticate()

if st.session_state["authentication_status"]:
    # litet hack för bättre ux
    time.sleep(1)
    # frontend

    st.session_state["authenticator"].logout('Logout', 'main')
    # litet hack för bättre ux
    time.sleep(1)
    st.write(f'Welcome {st.session_state["name"]}')

    # backend
    # connect to database
    # database name based on username - new session state variable
    st.session_state["db"] =\
    st.session_state["deta"].Base(st.session_state["username"])

    dev_login_page.custom_user_logged_in()

# frontend
    # fel inloggningsuppgifter
if st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')

    # frontend/backend
    # användare väljar att registrera ny profil
    # widget - new session state variable
    st.checkbox("Registrera", key="register_user_v1")
    if st.session_state["register_user_v1"]:
        dev_login_page.custom_register_user()

    st.checkbox("Glömt lösenord", key="forgot_pw_v1")
    if st.session_state["forgot_pw_v1"]:
        dev_login_page.custom_forgot_pw()
    
    st.checkbox("Glömt användarnamn", key="forgot_username_v1")
    if st.session_state["forgot_username_v1"]:
        dev_login_page.custom_forgot_username()
# frontend
    # ej angett inloggningsuppgifter
if st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')

    # frontend/backend
    # användare väljar att registrera ny profil
    # widget - new session state variable
    st.checkbox("Registrera", key="register_user_v2")
    if st.session_state["register_user_v2"]:
        dev_login_page.custom_register_user()

    st.checkbox("Glömt lösenord", key="forgot_pw_v2")
    if st.session_state["forgot_pw_v2"]:
        dev_login_page.custom_forgot_pw()

    st.checkbox("Glömt användarnamn", key="forgot_username_v2")
    if st.session_state["forgot_username_v2"]:
        dev_login_page.custom_forgot_username()

