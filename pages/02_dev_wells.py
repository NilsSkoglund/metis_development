import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from tools import dev_database_interactions

if "authentication_status" not in st.session_state:
    st.button("Logga in"
                , key = "login_page2")
    if st.session_state["login_page2"]:
        switch_page("inloggning")
elif not st.session_state["authentication_status"]:
    st.button("Logga in"
                , key = "login_page2_v2")
    if st.session_state["login_page2_v2"]:
        switch_page("inloggning")
elif st.session_state["authentication_status"] and\
"db_session_key" not in st.session_state:
    st.button("Välj session"
                , key = "choose_session_page2")
    if st.session_state["choose_session_page2"]:
        switch_page("inloggning")
else:
    st.write(st.session_state["db"]\
                            .get(st.session_state['db_session_key'])\
                            .get("name"))

    st.write("Starttid:", st.session_state["db"]\
                            .get(st.session_state['db_session_key'])\
                            .get("starttime"))

    dct_wells = st.session_state["dct_wells"]
    name_wells = st.session_state["name_wells"]

    dev_database_interactions.\
        set_session_state_for_questionnaire_from_db(name_wells)
    
    st.header("Formulär: Wells' Lungemboli")
    for i, j in enumerate(dct_wells.items()):
        wells_x = f"{name_wells}_{i}"
        st.checkbox(
            j[0]\
            ,key=wells_x\
            , on_change=dev_database_interactions.wells_update_db\
            )
