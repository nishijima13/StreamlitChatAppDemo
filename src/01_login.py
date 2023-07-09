# This page is used to login to the application
import streamlit as st
import const
from modules import common
from modules.authenticator import common_auth

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
