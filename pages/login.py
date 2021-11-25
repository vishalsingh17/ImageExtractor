import streamlit as st

# custom imports
from pages.hashing import make_hashes, check_hashes
from pages.DB import login_user, view_all_users, create_usertable


def app():
    st.title("Welcome to ImgScrapy!!")
    st.subheader("Login Section")
    username = st.text_input("Username")
    password = st.text_input("Password",type='password')
    
    if st.button("Login"):
        create_usertable()
        hashed_pswd = make_hashes(password)
        result = login_user(username,check_hashes(password,hashed_pswd))
        if result:
            st.success("Logged In as {}".format(username))
        else:
            st.warning("Incorrect Username/Password")       
