import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from tools import dev_database_interactions
from PIL import Image
from tools import dev_init_session_state_vars

dev_init_session_state_vars.init_session_state()

with st.sidebar:
    image = Image.open(f"pages/tågstationer wells.png")
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
    namn = st.session_state["db"]\
                            .get(st.session_state['db_session_key'])\
                            .get("name")

    dct_wells = st.session_state["dct_wells"]
    name_wells = st.session_state["name_wells"]

    dev_database_interactions.\
        set_session_state_for_questionnaire_from_db(name_wells)
    
    st.header(f"Wells' Lungemboli {namn}")
    for i, j in enumerate(dct_wells.items()):
        wells_x = f"{name_wells}_{i}"
        st.checkbox(
            j[0]\
            ,key=wells_x\
            , on_change=dev_database_interactions.wells_update_db\
            )
