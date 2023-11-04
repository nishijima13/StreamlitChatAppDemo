# This page is used to login to the application
import streamlit as st
from st_pages import add_page_title
import argparse
import const
from modules import common
from modules.authenticator import common_auth
from modules.database import database

# Setting page title
common.set_pages()
add_page_title()

# Get the command line arguments
parser = argparse.ArgumentParser(
    description="This page is used to login to the application",
)
parser.add_argument(
    "--use_chatbot",
    help="Use chatbot",
    action="store_true",
)
args = parser.parse_args()
use_chatbot = args.use_chatbot

# Update the use_chatbot setting
db = database.Database()
current_use_chatbot = db.get_openai_settings_use_character()
if int(use_chatbot) != current_use_chatbot:
    db.update_openai_settings_use_character(use_chatbot)

authenticator = common_auth.get_authenticator()
name, authentication_status, username = authenticator.login("Login", "main")

if (
    common.check_if_exists_in_session(const.SESSION_INFO_AUTH_STATUS)
    and st.session_state[const.SESSION_INFO_AUTH_STATUS]
):
    if common.check_if_exists_in_session(const.SESSION_INFO_NAME):
        # Sucessfully logged in
        authenticator.logout("Logout", "main", key="unique_key")
        st.write(f"Welcome *{st.session_state[const.SESSION_INFO_NAME]}*")
        st.write("Go to the chat page and start chatting!")
        common.set_pages()
    else:
        st.error("User name is not set in session state.")
elif common.check_if_exists_in_session(const.SESSION_INFO_AUTH_STATUS):
    # Not logged in
    if st.session_state["authentication_status"] is False:
        st.error("Username/password is incorrect")
    elif st.session_state["authentication_status"] is None:
        st.warning("Please enter your username and password")
    else:
        st.error(const.ERR_MSG_UNEXPECTED)
else:
    st.error(const.ERR_MSG_UNEXPECTED)
