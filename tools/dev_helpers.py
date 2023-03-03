import streamlit as st
from streamlit_extras.switch_page_button import switch_page

def calc_score(dct, name):
	'''
    Takes a dictionary (dct) and a string (name) as inputs and ...
	calculates total score for:
        DVT
        PE
        PERC
        PESI
	'''
	total_score = 0
	for index, question in enumerate(dct):
		key = f"{name}_{index}"
		if st.session_state[key]: # if True means the checkbox is ticked
			total_score += dct.get(question)
	return total_score

def lungemboli_display_txt(total_score):
    if total_score < 2:
        st.success("Patienten har en låg risk för lungemboli. För att kunna\
             utesluta lungemboli rekommenderas genomgång av PERC\
                 (Pulmonary Embolism Rule-out Criteria).")
    elif total_score < 6.5:
        st.warning("Patienten har en måttlig risk för lungemboli. För att\
             undvika onödig strålning rekommenderas att man tar D-dimer för\
             att avgöra om man kan avfärda lungemboli utan ytterligare\
             bildundersökning.")
    else:
        st.error("Patienten har en hög risk för lungemboli. Patienten skall\
             omgående startas på antikoagulantia-behandling och göra en akut\
                 DTLA. D-dimer är ej tillförlitligt för att utesluta lungemboli.")

def lungemboli_display_button(total_score):
    if total_score < 2:
        knapp_låg = st.button("Gå vidare till PERC")
        if knapp_låg:
            switch_page("dev perc")

    elif total_score < 6.5:
        knapp_måttlig = st.button("Ange D-dimer svar")
        if knapp_måttlig:
            switch_page("D-dimer")