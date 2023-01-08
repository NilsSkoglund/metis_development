import streamlit as st
from deta import Deta

def init_session_state():
    # Connect to Deta Base with your Project Key
    if "deta" not in st.session_state:
        st.session_state["deta"] = Deta(st.secrets["deta_key"])

    if "dct_wells" not in st.session_state:
        st.session_state["dct_wells"] = {
            "Kliniska tecken på DVT": 3,
            "Tidigare LE/DVT diagnos": 1.5,
            "Hjärtfrekvens >100/min": 1.5,
            "Hemoptys": 1,
            "Immobiliserad i >3 dagar / Opererad senaste 4 v.": 1.5,
            "LE mer sannolik än annan diagnos": 3,
            "Malignitet behandlad inom 6 mån alt. palliation": 1
            }

    if "name_wells" not in st.session_state:
        st.session_state["name_wells"] = "wells"


    if "dct_perc" not in st.session_state:
        st.session_state["dct_perc"] = {
            "Kliniska tecken på DVT": 1,
            "Tidigare LE/DVT diagnos": 1,
            "Hjärtfrekvens >100/min": 1,
            "Hemoptys": 1,
            "Immobiliserad i >3 dagar / Opererad senaste 4 v.": 1,
            "Ålder ≥50": 1,
            "Saturation >94% utan syrgas": 1,
            "Östrogenbehandling": 1
            }

    if "name_perc" not in st.session_state:
        st.session_state["name_perc"] = "perc"