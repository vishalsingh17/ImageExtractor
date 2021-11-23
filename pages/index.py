import streamlit as st
from flask import Flask, request, jsonify

def app():
    st.title("Welcome to Image Extractor")
    st.write("This is a simple image extractor that can be used to extract bulk images.")
    image_type = st.sidebar.selectbox("Select the image type", ["Any","JPG/JPEG", "PNG", "TIFF", "GIF", "EPS", "RAW"]) 
    image_resolution = st.sidebar.selectbox("Select the image resolution", ["Any","LOW", "MEDIUM", "HD", "4K"])
    st.text_input("Enter the image you want to extract. Eg - Car, Laptop, Shoes")
    col1, col2 = st.columns(2)
    download = col1.button("Download Now")
    schedule = col2.button("Schedule for Later")