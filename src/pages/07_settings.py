import streamlit as st
from modules.database import database

st.title("Settings")

db = database.Database()

if st.button("Delete all chat logs"):
    db.delete_all_chat_logs()
    st.success("All chat logs deleted successfully.")
