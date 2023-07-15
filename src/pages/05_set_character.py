import os
import streamlit as st
import const
from modules import common
from modules.database import database

st.title("Set character's persona")
db = database.Database()

current_use_chatbot = db.get_openai_settings_use_character()

if current_use_chatbot[0] == 0:
    st.error("You have not enabled the chatbot. Please contact the administrator.")
elif (
    common.check_if_exists_in_session(const.SESSION_INFO_AUTH_STATUS)
    and st.session_state[const.SESSION_INFO_AUTH_STATUS]
):
    persona = db.get_character_persona()[0]
    st.write("Please enter the persona of the character.")
    text = st.text_area(label="Persona", value=persona)
    if st.button("Update persona"):
        # Set persona
        db.update_character_persona(text)
        st.success("Character persona set successfully.")
        st.write("Current persona:")
        text_list = text.splitlines()
        for tcon in text_list:
            st.write(tcon)
    else:
        if len(persona) > 0:
            st.write("Current persona:")
            text_list = persona.splitlines()
            for pcon in text_list:
                st.write(pcon)
            st.write(persona)
        else:
            st.write("No persona is set.")
else:
    st.error("You are not logged in. Please go to the login page.")
