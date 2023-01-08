import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from tools import test_database_interactions

dct_wells = {
    "Kliniska tecken på DVT": 3,
    "Tidigare LE/DVT diagnos": 1.5,
    "Hjärtfrekvens >100/min": 1.5,
    "Hemoptys": 1,
    "Immobiliserad i >3 dagar / Opererad senaste 4 v.": 1.5,
    "LE mer sannolik än annan diagnos": 3,
    "Malignitet behandlad inom 6 mån alt. palliation": 1
    }
name_wells = "wells"


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

    test_database_interactions.\
        set_session_state_for_questionnaire_from_db(name_wells)
    
    st.header("Formulär: Wells' Lungemboli")
    for i, j in enumerate(dct_wells.items()):
        wells_x = f"{name_wells}_{i}"
        st.checkbox(
            j[0]\
            ,key=wells_x\
            , on_change=test_database_interactions.wells_update_db\
            #, args=(lungemboli_x,)\
            )
