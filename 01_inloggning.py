from deta import Deta
import streamlit as st
import time
from tools import dev_login_page
from tools import dev_init_session_state_vars
from tools import google_oauth
import extra_streamlit_components as stx
from streamlit_lottie import st_lottie
import requests


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

cm = stx.CookieManager(key="init2")

dev_init_session_state_vars.init_session_state()

lottie_url = "https://assets5.lottiefiles.com/packages/lf20_bYskKBq3WY.json"
lottie_json = load_lottieurl(lottie_url)
st_lottie(lottie_json, height=200, width=200)

# st.markdown("""
#     <style>
#     [role=radiogroup]{
#         gap: 0.5rem;
#     }
#     </style>
#     """,unsafe_allow_html=True)

#centered



if st.session_state["authentication_status"] == None and "random_cookie_name" not in cm.get_all():

    client_id = "1047167822945-ohs32k407e6ej3v4ont64rsd3tc6sktf.apps.googleusercontent.com"
    client_secret = "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"
    uri = "https://metis-dev.streamlit.app/"
    login_info = google_oauth.login(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=uri,
            logout_button_text="Logga ut"
        )

    if login_info:
        dev_login_page.custom_authenticate_oauth()

st.write("")
st.write("")
st.write("")


if st.session_state["authentication_status"]:
    # connect to database
    st.session_state["db"] =\
    st.session_state["deta"].Base(st.session_state["username"])
    time.sleep(1)

    dev_login_page.custom_user_logged_in()

with st.expander("Visa övriga alternativ"):

    dev_login_page.custom_authenticate()


    # fel inloggningsuppgifter
    if st.session_state["authentication_status"] == False:
        st.error('Username/password is incorrect')

        options = ["Logga in med registrerad användare"
                , "Registrera ny användare"
                , "Glömt inloggningsuppgifter"]
        st.radio("Välj meny"
                , options
                , key="options_inloggning_1"
                , horizontal=False
                , label_visibility="hidden")
        
        if st.session_state["options_inloggning_1"] == "Registrera ny användare":
            dev_login_page.custom_register_user()
        if st.session_state["options_inloggning_1"] == "Glömt inloggningsuppgifter":
            st.write("---")
            options_credentials = ["Glömt lösenord", "Glömt användarnamn"]
            st.radio("Glömt inloggningsuppgifter"
                , options_credentials
                , key="options_credentials_1"
                , horizontal=True
                , label_visibility="visible")
            if st.session_state["options_credentials_1"] == "Glömt lösenord":
                st.info("Ange ditt användarnamn så skickas ett lösenord\
                        till den kopplade emailen.")
                dev_login_page.custom_forgot_pw()
            if st.session_state["options_credentials_1"] == "Glömt användarnamn":
                st.info("Ange den kopplade emailen så visas användarnamnet.")
                dev_login_page.custom_forgot_username()
            
        

    # ej angett inloggningsuppgifter
    if st.session_state["authentication_status"] == None:
        options = ["Logga in med registrerad användare", "Registrera ny användare",
                "Glömt inloggningsuppgifter"]
        st.radio("Välj meny"
                , options
                , key="options_inloggning_2"
                , horizontal=False
                , label_visibility="hidden")
        
        if st.session_state["options_inloggning_2"] == "Registrera ny användare":
            dev_login_page.custom_register_user()
        if st.session_state["options_inloggning_2"] == "Glömt inloggningsuppgifter":
            st.write("---")
            options_credentials = ["Glömt lösenord", "Glömt användarnamn"]
            st.radio("Glömt inloggningsuppgifter"
                , options_credentials
                , key="options_credentials_2"
                , horizontal=True
                , label_visibility="visible")
            if st.session_state["options_credentials_2"] == "Glömt lösenord":
                st.info("Ange ditt användarnamn så skickas ett lösenord\
                        till den kopplade emailen.")
                dev_login_page.custom_forgot_pw()
            if st.session_state["options_credentials_2"] == "Glömt användarnamn":
                st.info("Ange den kopplade emailen så visas användarnamnet.")
                dev_login_page.custom_forgot_username()
