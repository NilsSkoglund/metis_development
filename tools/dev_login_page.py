import yaml
import streamlit as st
import streamlit_authenticator as stauth
from tools import dev_user_session_choice
from tools import dev_database_interactions

def custom_authenticate():
    with open("dunno.yaml") as file:
        config = yaml.load(file, Loader=yaml.SafeLoader)

    credentials = dev_database_interactions.get_config_cred()
    # new session state variable
    st.session_state["authenticator"] = stauth.Authenticate( 
        credentials,
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    # new session state variables
    st.session_state["name"]\
        , st.session_state["authentication_status"]\
        , st.session_state["username"] =\
            st.session_state["authenticator"].login('Login', 'main')

def custom_user_logged_in():
    # backend
        # connect to database
    # database name based on username - new session state variable
    st.session_state["db"] =\
    st.session_state["deta"].Base(st.session_state["username"])

    # frontend/backend
        # start a new session
        # continue on the most recent session
        # choose session from list
    
    # new session state variable
    st.checkbox("Starta ny session", key="start_new_session") 
    if st.session_state["start_new_session"]:
        dev_user_session_choice.start_new_session()

    # new session state variable
    st.checkbox("Fortsätt på senaste", key="continue_most_recent_session") 
    if st.session_state["continue_most_recent_session"]:
        dev_user_session_choice.continue_most_recent_session()

    # new session state variable
    st.checkbox("Välj från lista", key="choose_session_from_list") 
    if st.session_state["choose_session_from_list"]:
        dev_user_session_choice.choose_session_from_list()

def custom_register_user():
    try:
        if st.session_state["authenticator"]\
        .register_user('Register user', preauthorization=False):
            st.success('User registered successfully')   
            dev_database_interactions.register_new_user_in_db()
    except Exception as e:
        st.error(e)
