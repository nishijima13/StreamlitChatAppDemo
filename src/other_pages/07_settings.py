import streamlit as st
from st_pages import add_page_title
import const
from modules.database import database
from modules import common

add_page_title()

db = database.Database()

if (
    common.check_if_exists_in_session(const.SESSION_INFO_AUTH_STATUS)
    and st.session_state[const.SESSION_INFO_AUTH_STATUS]
):
    if st.button("Delete all chat logs"):
        db.delete_all_chat_logs()
        st.success("All chat logs deleted successfully.")
else:
    st.error("You are not logged in. Please go to the login page.")
