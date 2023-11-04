import streamlit as st
from st_pages import Page, show_pages, add_page_title, hide_pages
import const
from modules import common
from modules.database import database

db = database.Database()

def set_pages():
    """Set the pages to be shown in the sidebar.
    """
    default_pages = [
        Page("src/01_login.py", "Login/Logout", "🏠"),
        Page("src/other_pages/02_register_user.py", "Register user", "📝"),
    ]
    after_login_pages = [
        Page("src/other_pages/03_reset_password.py", "Reset password", "🔑"),
        Page("src/other_pages/04_change_icon.py", "Change icon", "👤"),
        Page("src/other_pages/06_chat.py", "Chat", "💬"),
        Page("src/other_pages/07_settings.py", "Settings", "⚙️"),
    ]
    pages = default_pages
    
    # Check if chatbot is enabled
    current_use_chatbot = db.get_openai_settings_use_character()
    if current_use_chatbot == 1:
        pages.append(Page("src/other_pages/05_set_character.py", "Set character", "🤖"))

    # Check if user is logged in
    if (
        common.check_if_exists_in_session(const.SESSION_INFO_AUTH_STATUS)
        and st.session_state[const.SESSION_INFO_AUTH_STATUS]
    ):
        pages += after_login_pages
    show_pages(pages)


def check_if_exists_in_session(key: str) -> bool:
    """Check if key exists in session state

    Args:
        key (str): key to check.

    Returns:
        bool : True if key exists in session state, False otherwise.
    """
    if key in st.session_state:
        return True
    else:
        return False
