# imports
import streamlit as st

# custom imports
from multipage import MultiPage
from pages import index, signin, login


auth_staus = False
# Create instances of the page
app = MultiPage()

# Title of the main page


# Add all the application (pages) here

if auth_staus==False:
    app.add_page("Sign In", signin.app)
    app.add_page("Log In", login.app)
if auth_staus == True: 
    st.title("Image Extractor")
    app.add_page("Index", index.app)

# Main app
app.run()

