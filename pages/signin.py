import streamlit as st

# custom imports
from pages.hashing import make_hashes
from pages.DB import add_userdata, create_usertable

def app():
    st.title("Welcome to ImgScrapy!!")
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type='password')

    if st.button("Signup"):
        create_usertable()
        add_userdata(new_user,make_hashes(new_password))
        st.success("You have successfully created a valid Account. Please LogIn Now!!")
        st.info("Go to Login Menu to login")



