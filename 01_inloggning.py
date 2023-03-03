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
    st.session_state["authenticator"].logout('Logout', 'main')
    # litet hack för bättre ux
    time.sleep(1)
    st.write(f'Welcome {st.session_state["name"]}')
    # connect to database
    st.session_state["db"] =\
    st.session_state["deta"].Base(st.session_state["username"])
    dev_login_page.custom_user_logged_in()

# fel inloggningsuppgifter
if st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')

    options = ["Logga in", "Registrera ny användare",
               "Glömt inloggningsuppgifter"]
    st.radio("Välj meny"
             , options
             , key="options_inloggning_1"
             , horizontal=True
             , label_visibility="collapsed")
    
    if st.session_state["options_inloggning_1"] == "Registrera ny användare":
        dev_login_page.custom_register_user()
    if st.session_state["options_inloggning_1"] == "Glömt inloggningsuppgifter":
        st.write("---")
        options_credentials = ["Glömt lösenord", "Glömt användarnamn"]
        st.radio("Välj meny"
             , options_credentials
             , key="options_credentials_1"
             , horizontal=True
             , label_visibility="collapsed")
        if st.session_state["options_credentials_1"] == "Glömt lösenord":
            st.info("Ange ditt användarnamn så skickas ett lösenord\
                    till den kopplade emailen.")
            dev_login_page.custom_forgot_pw()
        if st.session_state["options_credentials_1"] == "Glömt användarnamn":
            st.info("Ange den kopplade emailen så visas användarnamnet.")
            dev_login_page.custom_forgot_username()

    #if st.session_state["options_inloggning_1"] == "Glömt användarnamn":


    # st.checkbox("Registrera", key="register_user_v1")
    # if st.session_state["register_user_v1"]:
    #     dev_login_page.custom_register_user()

    # st.checkbox("Glömt lösenord", key="forgot_pw_v1")
    # if st.session_state["forgot_pw_v1"]:
    #     dev_login_page.custom_forgot_pw()
    
    # st.checkbox("Glömt användarnamn", key="forgot_username_v1")
    # if st.session_state["forgot_username_v1"]:
    #     dev_login_page.custom_forgot_username()

# ej angett inloggningsuppgifter
if st.session_state["authentication_status"] == None:
    options = ["Logga in", "Registrera ny användare",
               "Glömt inloggningsuppgifter"]
    st.radio("Välj meny"
             , options
             , key="options_inloggning_2"
             , horizontal=True
             , label_visibility="collapsed")
    
    if st.session_state["options_inloggning_2"] == "Registrera ny användare":
        dev_login_page.custom_register_user()
    if st.session_state["options_inloggning_2"] == "Glömt inloggningsuppgifter":
        st.write("---")
        options_credentials = ["Glömt lösenord", "Glömt användarnamn"]
        st.radio("Välj meny"
             , options_credentials
             , key="options_credentials_2"
             , horizontal=True
             , label_visibility="collapsed")
        if st.session_state["options_credentials_2"] == "Glömt lösenord":
            st.info("Ange ditt användarnamn så skickas ett lösenord\
                    till den kopplade emailen.")
            dev_login_page.custom_forgot_pw()
        if st.session_state["options_credentials_2"] == "Glömt användarnamn":
            st.info("Ange den kopplade emailen så visas användarnamnet.")
            dev_login_page.custom_forgot_username()
# if st.session_state["authentication_status"] == None:
#     st.warning('Please enter your username and password')

#     st.checkbox("Registrera", key="register_user_v2")
#     if st.session_state["register_user_v2"]:
#         dev_login_page.custom_register_user()

#     st.checkbox("Glömt lösenord", key="forgot_pw_v2")
#     if st.session_state["forgot_pw_v2"]:
#         dev_login_page.custom_forgot_pw()

#     st.checkbox("Glömt användarnamn", key="forgot_username_v2")
#     if st.session_state["forgot_username_v2"]:
#         dev_login_page.custom_forgot_username()

