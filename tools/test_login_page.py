import yaml
import streamlit as st
import streamlit_authenticator as stauth
from tools import test_user_session_choice

with open("dunno.yaml") as file:
        config = yaml.load(file, Loader=yaml.SafeLoader)

def custom_authenticate():
        st.session_state["authenticator"] = stauth.Authenticate( # new session state variable
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days'],
            config['preauthorized']
        )

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
    
    st.checkbox("Starta ny session", key="start_new_session") # new session state variable
    if st.session_state["start_new_session"]:
        test_user_session_choice.start_new_session()

    st.checkbox("Fortsätt på senaste", key="continue_most_recent_session") # new session state variable
    if st.session_state["continue_most_recent_session"]:
        test_user_session_choice.continue_most_recent_session()

    st.checkbox("Välj från lista", key="choose_session_from_list") # new session state variable
    if st.session_state["choose_session_from_list"]:
        test_user_session_choice.choose_session_from_list()

def custom_register_user():
    try:
        if st.session_state["authenticator"].register_user('Register user', preauthorization=False):
            st.success('User registered successfully')
            with open('dunno.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)    
    except Exception as e:
        st.error(e)
