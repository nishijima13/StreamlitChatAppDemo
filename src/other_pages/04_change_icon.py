# This page is used to change the icon of the user.
import os
import streamlit as st
from st_pages import add_page_title
import const
import numpy as np
from PIL import Image
from modules import common
from modules.authenticator import common_auth
from modules.database import database

# Setting paage title
add_page_title()
authenticator = common_auth.get_authenticator()
db = database.Database()
if (
    common.check_if_exists_in_session(const.SESSION_INFO_AUTH_STATUS)
    and st.session_state[const.SESSION_INFO_AUTH_STATUS]
):
    username = st.session_state[const.SESSION_INFO_USERNAME]
    st.markdown(
        "## Change *{0}* icon".format(st.session_state[const.SESSION_INFO_NAME])
    )
    # Show current icon
    user_info = db.get_user_info(st.session_state[const.SESSION_INFO_USERNAME])
    if user_info is None:
        image_path = None
        st.error(const.ERR_MSG_GET_USER_INFO)
    else:
        image_path = user_info[4]
    if image_path is not None and os.path.isfile(image_path):
        image = Image.open(image_path)
        st.image(image, caption="current icon")
    else:
        st.markdown("No icon is set for this user")

    # Upload new icon
    uploaded_file = st.file_uploader(
        "Please upload an image file.",
        type=["jpeg", "png", "jpg", "JPEG", "PNG", "JPG"],
    )

    if uploaded_file is not None:
        # Show new icon
        image = Image.open(uploaded_file)
        image.thumbnail((100, 100), Image.Resampling.LANCZOS)
        img_array = np.array(image)
        image_path = os.path.join(const.IMAGE_DIR_PATH, "{0}.png".format(username))
        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        image.save(image_path)
        db.update_user_info_image_path(username, image_path)
        st.success("Icon changed successfully.")
        st.image(image, caption="new icon")
else:
    st.error("You are not logged in. Please go to the login page.")
