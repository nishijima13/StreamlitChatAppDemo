import streamlit as st


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
