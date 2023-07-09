# This page is used to register a new user
import streamlit as st
import const
from modules import common
from modules.authenticator import common_auth
from modules.database import database

authenticator = common_auth.get_authenticator()
db = database.Database()
if (
    common.check_if_exists_in_session(const.SESSION_INFO_AUTH_STATUS)
    and st.session_state[const.SESSION_INFO_AUTH_STATUS]
):
    st.error("You are already logged in.")
else:
    try:
        if authenticator.register_user("Register user", preauthorization=False):
            # User registered successfully
            # TODO Need to find a better way to get the username
            username = next(iter(reversed(authenticator.credentials["usernames"])))
            user_infos = authenticator.credentials["usernames"][username]
            db.insert_user_info(
                username,
                user_infos["email"],
                user_infos["name"],
                user_infos["password"],
            )
            st.success("User registered successfully. Please login to continue.")
    except Exception as e:
        st.error(e)
