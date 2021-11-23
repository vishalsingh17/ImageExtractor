# imports
import streamlit as st

# custom imports
from multipage import MultiPage
from pages import data_upload, index, signin, login

# Create instances of the page
app = MultiPage()

# Title of the main page


# Add all the application (pages) here
auth_staus = False
if auth_staus==True:
    app.add_page("Sign In", signin.app)
    app.add_page("Log In", login.app)
else:
    st.title("Image Extractor")
    app.add_page("Upload Data", data_upload.app)
    app.add_page("Index", index.app)

# Main app
app.run()

