import yaml
import streamlit as st
import streamlit_authenticator as stauth
from tools import dev_user_session_choice
from tools import dev_database_interactions
import yagmail


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
    # connect to database
    st.session_state["db"] =\
    st.session_state["deta"].Base(st.session_state["username"])

    options = ["Starta ny session"
               , "Fortsätt på senaste"
               , "Välj från lista"]
    st.radio("Välj meny"
             , options
             , key="session_choice"
             , horizontal=True
             , label_visibility="hidden")
    
    if st.session_state["session_choice"] == "Starta ny session":
        dev_user_session_choice.start_new_session()
    if st.session_state["session_choice"] == "Fortsätt på senaste":
        dev_user_session_choice.continue_most_recent_session()
    if st.session_state["session_choice"] == "Välj från lista":
        dev_user_session_choice.choose_session_from_list()
    

    # st.checkbox("Starta ny session", key="start_new_session") 
    # if st.session_state["start_new_session"]:
    #     dev_user_session_choice.start_new_session()

    # # new session state variable
    # st.checkbox("Fortsätt på senaste", key="continue_most_recent_session") 
    # if st.session_state["continue_most_recent_session"]:
    #     dev_user_session_choice.continue_most_recent_session()

    # # new session state variable
    # st.checkbox("Välj från lista", key="choose_session_from_list") 
    # if st.session_state["choose_session_from_list"]:
    #     dev_user_session_choice.choose_session_from_list()

def custom_register_user():
    try:
        if st.session_state["authenticator"]\
        .register_user('Register user', preauthorization=False):
            st.success('User registered successfully')   
            dev_database_interactions.register_new_user_in_db()
    except Exception as e:
        st.error(e)

def custom_forgot_pw():
    try:
        username_forgot_pw, email_forgot_password, random_password =\
             st.session_state["authenticator"]\
            .forgot_password('Forgot password')
        if username_forgot_pw:
            send_email_forgot_password(random_password\
                                        , email_forgot_password\
                                        , username_forgot_pw)
            # Random password to be transferred to user securely
            # ...
        elif username_forgot_pw == False:
            st.error('Username not found')
    except Exception as e:
        st.error(e)

def custom_forgot_username():
    try:
        username_forgot_username, email_forgot_username =\
             st.session_state["authenticator"].\
                forgot_username('Forgot username')
        if username_forgot_username:
            st.info(f'Username: {username_forgot_username}')
            # Username to be transferred to user securely
        elif username_forgot_username == False:
            st.error('Email not found')
    except Exception as e:
        st.error(e)



def send_email_forgot_password(pw, email_receiver, username):
    email_sender = 'metis.dev.noreply@gmail.com'
    yag = yagmail.SMTP(email_sender, st.secrets["gmail_pw"])
    contents = [f'This is your new password: {pw} \n\
        For user: {username} \nLog in at: https://metis-dev.streamlit.app/']
    subject = "Metis Password Reset"
    yag.send(email_receiver, subject, contents)
    dev_database_interactions.update_credentials_in_db(username)
    if email_receiver.endswith("gmail.com"):
        st.success(f"Password successfully sent\
             to [{email_receiver}](https://gmail.com/)")
    else:
        st.success(f"Password successfully sent\
             to the email associated with your account")



