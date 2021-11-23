import streamlit as st

# custom imports
from pages.hashing import make_hashes
from pages.DB import login_user, view_all_users

def app():
    st.title("Welcome to ImgScrapy!!")
    st.subheader("Login Section")