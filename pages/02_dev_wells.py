import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from tools import dev_database_interactions
from PIL import Image
from tools import dev_init_session_state_vars
from tools import dev_helpers

# import asyncio

dev_init_session_state_vars.init_session_state()

with st.sidebar:
    image = Image.open(f"pages/tågstation wells v2.png")
    st.image(image)


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
"db_session_key" not in st.session_state or st.session_state["db"]\
.get(st.session_state['db_session_key']) == None:
    st.button("Välj session"
                , key = "choose_session_page2")
    if st.session_state["choose_session_page2"]:
        switch_page("inloggning")
else:
    if "wells_radio_index" not in st.session_state:
        st.session_state["wells_radio_index"] = 0
    st.radio(""
             , ["Pågående", "Avslutad"]
             , index=st.session_state["wells_radio_index"]
             , key="wells_radio"
             , horizontal=True)
    st.write("---")
    
    namn = st.session_state["db"]\
                            .get(st.session_state['db_session_key'])\
                            .get("name")

    dct_wells = st.session_state["dct_wells"]
    name_wells = st.session_state["name_wells"]

    dev_database_interactions.\
        set_session_state_for_questionnaire_from_db(name_wells)
        

    st.subheader(f"Wells' Lungemboli - {namn}")

    is_avslutad = False
    if st.session_state["wells_radio"] == "Avslutad":
        is_avslutad = True

    if 'request_in_progress' not in st.session_state:
        st.session_state['request_in_progress'] = False
    

    def display_dct_wells(dct):
        for i, j in enumerate(dct.items()):
            is_in_progress = st.session_state['request_in_progress']
            wells_x = f"{name_wells}_{i}"
            st.checkbox(
                j[0]\
                ,key=wells_x\
                , on_change=dev_database_interactions.wells_update_db
                , disabled=True in [is_avslutad, is_in_progress]
                )
        

    dct_lungemboli = {
    "Kliniska tecken på DVT": 3,
    "Tidigare LE/DVT diagnos": 1.5,
    "Hjärtfrekvens >100/min": 1.5,
    "Hemoptys": 1,
    "Immobiliserad i >3 dagar / Opererad senaste 4 v.": 1.5,
    "LE mer sannolik än annan diagnos": 3,
    "Malignitet behandlad inom 6 mån alt. palliation": 1
    }

    display_dct_wells(dct_lungemboli)

    total_score = dev_helpers.calc_score(dct_lungemboli, name_wells)
    dev_helpers.lungemboli_display_txt(total_score)
    dev_helpers.lungemboli_display_button(total_score)
