import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from tools import test_database_interactions


dct_perc = {
    "Kliniska tecken på DVT": 1,
    "Tidigare LE/DVT diagnos": 1,
    "Hjärtfrekvens >100/min": 1,
    "Hemoptys": 1,
    "Immobiliserad i >3 dagar / Opererad senaste 4 v.": 1,
    "Ålder ≥50": 1,
    "Saturation >94% utan syrgas": 1,
    "Östrogenbehandling": 1
    }
name_perc = "perc"


if "authentication_status" not in st.session_state:
    st.button("Logga in"
                , key = "login_page3")
    if st.session_state["login_page3"]:
        switch_page("inloggning")
elif not st.session_state["authentication_status"]:
    st.button("Logga in"
                , key = "login_page3_v2")
    if st.session_state["login_page3_v2"]:
        switch_page("inloggning")
elif st.session_state["authentication_status"] and\
"db_session_key" not in st.session_state:
    st.button("Välj session"
                , key = "choose_session_page3")
    if st.session_state["choose_session_page3"]:
        switch_page("inloggning")
else:
    st.write(st.session_state["db"]\
                            .get(st.session_state['db_session_key'])\
                            .get("name"))

    st.write("Starttid:", st.session_state["db"]\
                            .get(st.session_state['db_session_key'])\
                            .get("starttime"))

    with st.expander("Klicka för info"):
        st.info("5 av 8 frågor i PERC ingår i Wells' kriterier för lungemboli.\
        När dessa frågor besvaras i formuläret för Wells'\
        ges de samma svar i PERC-formuläret nedan")

    st.header("Formulär: PERC")

    test_database_interactions.\
        set_session_state_for_questionnaire_from_db(name_perc)

    # create checkboxes
    for i, j in enumerate(dct_perc.items()):
        perc_x = f"{name_perc}_{i}"
        st.checkbox(
            j[0]\
            ,key=perc_x\
            , on_change=test_database_interactions.perc_update_db\
            #, args=(lungemboli_x,)\
            )