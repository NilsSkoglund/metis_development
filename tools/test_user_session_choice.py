import datetime
import streamlit as st
from tools import test_database_interactions
from streamlit_extras.switch_page_button import switch_page

# om användare har loggat in
    # ny session
    # fortsätt på senaste
    # välj från lista

def start_new_session():

    # Get string with time when session was started
    st.session_state["time_session_start_str"] =\
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get string with date when session was started
    st.session_state["date_today_str"] = str(datetime.date.today())

    # Count number of previous sessions today and add 1
    daily_session_no = len(st.session_state["db"]\
                    .fetch({"date":st.session_state["date_today_str"]}).items\
                    )+1
    
    # Create session/primary key for db interactions
    st.session_state["db_session_key"] =\
         f"{st.session_state['date_today_str']} {daily_session_no}" # database unique key - new session state variable

    # Create user friendly generic name for session
    # name for session - new session state variable
    st.session_state["session_name"] =\
             f"Patient nummer {daily_session_no} för dagen"

    # User can write their own name for the session
    st.text_input(\
        "Ange eget namn på sessionen eller gå vidare med förifyllt namn.\
        (Starttid inkluderas alltid)"
        , key = "session_name_from_user") # widget - new session state variable

    # If user decides to write their own name
    if st.session_state["session_name_from_user"]: # session state variable
            st.session_state["session_name"] =\
                 st.session_state["session_name_from_user"] # session state variable
            st.info(f"Tryck gå vidare för att påbörja sessionen.\
                 Sessionen sparas som:\
                 {st.session_state['session_name']}\
                 | {st.session_state['time_session_start_str']}")
    
    # If user decides to keep the generic name
    else:
        st.info(f"Tryck gå vidare för att påbörja sessionen.\
                Session sparas som:\
                Patient nummer {daily_session_no} för dagen\
                | {st.session_state['time_session_start_str']}]")
    
    # User is done and presses a button to enter the session / go to next page
    st.button("Gå vidare", key="new_session_next_page") # widget - new session state variable

    # if user presses button, we want to write info for new session to db ...
    # before entering the session / going to the next page
    if st.session_state["new_session_next_page"]:
        # call function to create record of session in db
        test_database_interactions.register_new_session_in_db()
        st.write("Haj")

        # Finished, move on to page 2 with wells
        switch_page("wells")

def continue_most_recent_session():
    # get all records from db
    all_items = test_database_interactions.\
                get_all_items_from_db(st.session_state["db"])

    if len(all_items) == 0:
        st.info("Det finns inga sessioner kopplade till denna användare.\
        Starta en ny session eller testa att logga in på en annan användare")
    else:
        # get key & starttime from all records
        selected_items = [[i.get('key')\
                    , i.get('starttime')]\
                    for i in all_items]

        # sort based on starttime
        selected_items.sort(reverse=True, key=lambda x: x[1])

        # return key for most recent starttime
        most_recent_key = selected_items[0][0]

        # set key for session
        st.session_state["db_session_key"] = most_recent_key

        # now move user to next page
        switch_page("wells")


def choose_session_from_list():
    all_items = test_database_interactions.\
        get_all_items_from_db(st.session_state["db"])
    if len(all_items) == 0:
        st.info("Det finns inga sessioner kopplade till denna användare.\
        Starta en ny session eller testa att logga in på en annan användare")

    else:
        # Get items to ... 
            # 1) Keep track of session key
            # 2) present user friendly options in list
        selected_items = [
            [i.get('key')\
            , i.get('name')\
            , i.get('starttime')]\
                for i in all_items]
        
        # sort based on starttime
        selected_items.sort(reverse=True, key=lambda x: x[2])

        # format func to be used in selectbox
        def format_selectbox_options(label):
            if label != "Se alternativ":
                name = label[1]
                starttime = label[2]
                return f"{name} | Starttid: {starttime}"
            else:
                return label

        # selectbox displaying sessions in descending order based on starttime
            # with formatted user friendly options labels
        st.selectbox(\
            "Välj session från listan för att läsa in info för berörd patient"\
            , options = ["Se alternativ"] + selected_items\
            , format_func=format_selectbox_options\
            , key="selectbox_choose_session")

        if st.session_state["selectbox_choose_session"] != "Se alternativ":
            st.session_state["db_session_key"] =\
                st.session_state["selectbox_choose_session"]\
                [0] # <-- key at index 0
            
            st.write(st.session_state["db_session_key"])
            # now move user to next page
            switch_page("wells")
