# This page is used to reset the password of the user.
import streamlit as st
from st_pages import add_page_title
import const
from modules import common
from modules.authenticator import common_auth
from modules.database import database

add_page_title()
authenticator = common_auth.get_authenticator()
db = database.Database()
if (
    common.check_if_exists_in_session(const.SESSION_INFO_AUTH_STATUS)
    and st.session_state[const.SESSION_INFO_AUTH_STATUS]
):
    try:
        if authenticator.reset_password(
            st.session_state[const.SESSION_INFO_NAME], "Reset password"
        ):
            # Password reset successfully
            username = st.session_state[const.SESSION_INFO_USERNAME]
            password = authenticator.credentials["usernames"][username]["password"]
            db.update_user_info_password(username, password)
            st.success("Password modified successfully")
    except Exception as e:
        st.error(e)
else:
    st.error(
        "You are not logged in. Please login to reset your password. Please go to the login page."
    )
