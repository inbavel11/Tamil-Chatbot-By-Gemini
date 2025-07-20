# tamil_ui.py
import streamlit as st
import requests

st.title("🗣️ தமிழ் Gemini உதவியாளர்")

user_input = st.text_input("உங்கள் கேள்வியை தமிழில் எழுதுங்கள்:")

if user_input:
    with st.spinner("பதிலை தயாராக்குகிறது..."):
        res = requests.post("http://localhost:8000/tamilchat/", json={"prompt": user_input})
        if res.status_code == 200:
            st.success(res.json()['reply'])
        else:
            st.error("பிழை ஏற்பட்டது!")
