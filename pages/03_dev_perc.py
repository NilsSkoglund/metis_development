import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from tools import dev_database_interactions
from PIL import Image

with st.sidebar:
    image = Image.open(f"pages/tågstation v2 perc.png")
    st.image(image)

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
"db_session_key" not in st.session_state or st.session_state["db"]\
.get(st.session_state['db_session_key']) == None:
    st.button("Välj session"
                , key = "choose_session_page3")
    if st.session_state["choose_session_page3"]:
        switch_page("inloggning")
else:
    if "perc_radio_index" not in st.session_state:
        st.session_state["perc_radio_index"] = 0
    st.radio(""
             , ["Pågående", "Avslutad"]
             , index=st.session_state["perc_radio_index"]
             , key="perc_radio"
             , horizontal=True)
    is_disabled = False
    if st.session_state["perc_radio"] == "Avslutad":
        is_disabled = True

    namn = st.session_state["db"]\
                            .get(st.session_state['db_session_key'])\
                            .get("name")

    with st.expander("Klicka för info"):
        st.info("5 av 8 frågor i PERC ingår i Wells' kriterier för lungemboli.\
        När dessa frågor besvaras i formuläret för Wells'\
        ges de samma svar i PERC-formuläret nedan")

    st.subheader(f"PERC - {namn}")

    dct_perc = st.session_state["dct_perc"]
    name_perc = st.session_state["name_perc"]

    
    dev_database_interactions.sync_perc_wells()

    dev_database_interactions.\
        set_session_state_for_questionnaire_from_db(name_perc)

    # create checkboxes
    for i, j in enumerate(dct_perc.items()):

        if i <= 4:
            perc_x = f"{name_perc}_{i}"
            st.checkbox(
                j[0]
                ,key=perc_x
                ,disabled=True
                , on_change=dev_database_interactions.perc_update_db
                )
        else:
            perc_x = f"{name_perc}_{i}"
            st.checkbox(
                j[0]
                ,key=perc_x
                ,disabled=is_disabled
                , on_change=dev_database_interactions.perc_update_db
                )