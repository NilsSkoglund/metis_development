import streamlit as st
import time

def register_new_session_in_db():
    dct_wells = st.session_state["dct_wells"]
    name_wells = st.session_state["name_wells"]

    dct_perc = st.session_state["dct_perc"]
    name_perc = st.session_state["name_perc"]
    # Create temporary dict to use for updating db and include ...
        # date
        # session_starttime
        # session_name
    temp_dct = {"date":st.session_state["date_today_str"]\
        , "starttime":st.session_state["time_session_start_str"]
        , "name":st.session_state["session_name"]}

    # create dict with all questions from wells'
    temp_dct_wells = {}
    for i, j in enumerate(dct_wells):
        key = f"{name_wells}_{i}"
        temp_dct_wells[key] = False
    # add wells to temp 
    temp_dct[name_wells] = temp_dct_wells

    # create dict with all questions from wells'
    temp_dct_perc = {}
    for i, j in enumerate(dct_perc):
        key = f"{name_perc}_{i}"
        temp_dct_perc[key] = False
    # add wells to temp 
    temp_dct[name_perc] = temp_dct_perc

    # Create row in db including session key
    st.session_state["db"].put(temp_dct\
                                , key=st.session_state["db_session_key"])

def get_all_items_from_db(db):
    # Get items from db (limit is 1000 so while loop is added for robustness)
    res = db.fetch()
    all_items = res.items
    # fetch until last is 'None'
    while res.last:
        res = db.fetch(last=res.last)
        all_items += res.items
    return all_items

def set_session_state_for_questionnaire_from_db(questionnaire):
    dict_from_db = st.session_state["db"]\
                    .get(st.session_state["db_session_key"])\
                    .get(questionnaire)

    for index, j in enumerate(dict_from_db):
        key = f"{questionnaire}_{index}"
        value = dict_from_db[key]
        st.session_state[key] = value

def wells_update_db():
    dct_wells = st.session_state["dct_wells"]
    name_wells = st.session_state["name_wells"]

    dct_perc = st.session_state["dct_perc"]
    name_perc = st.session_state["name_perc"]

    temp_dct_wells = {}
    for i, j in enumerate(dct_wells):
        key = f"{name_wells}_{i}"
        temp_dct_wells[key] = st.session_state[key]

    st.session_state["db"].update(\
                            {name_wells:temp_dct_wells}\
                            , key=st.session_state["db_session_key"])
    time.sleep(0.5)

    temp_dct_perc = {}
    for i, j in enumerate(dct_perc):
        if i <= 4: 
            key_perc = f"{name_perc}_{i}"
            key_wells = f"{name_wells}_{i}"
            temp_dct_perc[key_perc] = st.session_state[key_wells]
        else:
            key_perc = f"{name_perc}_{i}"
            value_perc = st.session_state["db"]\
                            .get(st.session_state['db_session_key'])\
                            .get(name_perc).get(key_perc)
            temp_dct_perc[key_perc] = value_perc

    st.session_state["db"].update(\
                            {name_perc:temp_dct_perc}\
                            , key=st.session_state["db_session_key"])
    time.sleep(0.5)

def perc_update_db():
    dct_perc = st.session_state["dct_perc"]
    name_perc = st.session_state["name_perc"]
    temp_dct_perc = {}
    for i, j in enumerate(dct_perc):
        key = f"{name_perc}_{i}"
        temp_dct_perc[key] = st.session_state[key]

    st.session_state["db"].update(\
                            {name_perc:temp_dct_perc}\
                            , key=st.session_state["db_session_key"])
    time.sleep(0.5)