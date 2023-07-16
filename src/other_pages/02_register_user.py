# This page is used to register a new user
import streamlit as st
from st_pages import add_page_title
import const
from modules import common
from modules.authenticator import common_auth
from modules.database import database

common.set_pages()
add_page_title()

authenticator = common_auth.get_authenticator()
db = database.Database()

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
