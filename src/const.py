import os

# DB Settings
DATABSE_PATH = "resource/database.db"
# Resource Settings
IMAGE_DIR_PATH = "resource/user_images"
# Cookie Settings
COOKIE_NAME = "streamlit_chat"
COOKIE_KEY = "streamlit_chat_signature_key"
COOKIE_EXPIRY_DAYS = 30
# Streamlit authenticator settings
PREAUTHORIZED = False
# Session Settings
SESSION_INFO_USERNAME = "username"
SESSION_INFO_NAME = "name"
SESSION_INFO_AUTH_STATUS = "authentication_status"
# Admin user settings
USER_SETTINGS = {
    "username": "admin",
    "email": "",
    "name": "Admin",
    "password": "admin_password",
    "image_path": None,
}
# Error messages
ERR_MSG_UNEXPECTED = "An unexpected error has occurred."
ERR_MSG_GET_USER_INFO = "Failed to get user information."
ERR_MSG_GET_CHAT_LOGS = "Failed to get chat logs."
# Chat settings
MAX_CHAT_LOGS = 100
# Auto refresh settings[ms]
REFRESH_INTERVAL = 2 * 1000
