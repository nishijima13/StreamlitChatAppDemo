# This page is for chat
import streamlit as st
import const
import datetime
import os
from PIL import Image
from streamlit_autorefresh import st_autorefresh
from modules import common
from modules.authenticator import common_auth
from modules.database import database

CHAT_ID = "0"
st.title("Chat")

authenticator = common_auth.get_authenticator()
db = database.Database()
if (
    common.check_if_exists_in_session(const.SESSION_INFO_AUTH_STATUS)
    and st.session_state[const.SESSION_INFO_AUTH_STATUS]
):
    user_infos = {}

    username = st.session_state[const.SESSION_INFO_USERNAME]
    name = st.session_state[const.SESSION_INFO_NAME]
    user_msg = st.chat_input("Enter your message")

    # Show old chat messages
    chat_log = db.get_chat_log(chat_id=CHAT_ID, limit=const.MAX_CHAT_LOGS)
    if chat_log is not None:
        for msg_info in chat_log:
            log_chat_id, log_username, log_name, log_message, log_sent_time = msg_info
            # Get user info
            if log_username not in user_infos:
                tmp_user_info = db.get_user_info(log_username)
                if tmp_user_info is None:
                    st.error(const.ERR_MSG_GET_USER_INFO)
                else:
                    user_infos[log_username] = {
                        "username": log_username,
                        "name": tmp_user_info[2],
                        "image_path": tmp_user_info[4],
                        "image": None,
                    }
            # Show chat message
            if log_username in user_infos:
                if (
                    user_infos[log_username]["image"] is None
                    and user_infos[log_username]["image_path"] is not None
                    and os.path.isfile(user_infos[log_username]["image_path"])
                ):
                    # Load user image
                    user_infos[log_username]["image"] = Image.open(
                        user_infos[log_username]["image_path"]
                    )
                with st.chat_message(
                    log_name, avatar=user_infos[log_username]["image"]
                ):
                    st.write(log_name + "> " + log_message)
    else:
        st.error(const.ERR_MSG_GET_CHAT_LOGS)
    if user_msg:
        # Show new chat message
        db.insert_chat_log(
            chat_id=CHAT_ID,
            username=username,
            name=name,
            message=user_msg,
            sent_time=datetime.datetime.now(),
        )
        if username not in user_infos:
            # Get user info
            tmp_user_info = db.get_user_info(username)
            if tmp_user_info is None:
                st.error(const.ERR_MSG_GET_USER_INFO)
            else:
                user_infos[username] = {
                    "username": username,
                    "name": tmp_user_info[2],
                    "image_path": tmp_user_info[4],
                    "image": None,
                }
        if (
            username in user_infos
            and user_infos[username]["image"] is None
            and user_infos[username]["image_path"] is not None
            and os.path.isfile(user_infos[username]["image_path"])
        ):
            user_infos[username]["image"] = Image.open(
                user_infos[username]["image_path"]
            )
        with st.chat_message(name, avatar=user_infos[username]["image"]):
            st.write(name + "> " + user_msg)

    # Refresh the page every (REFRESH_INTERVAL) seconds
    count = st_autorefresh(
        interval=const.REFRESH_INTERVAL, limit=None, key="fizzbuzzcounter"
    )
else:
    st.error("You are not logged in.")
