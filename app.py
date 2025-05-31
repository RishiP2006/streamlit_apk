import streamlit as st
import requests

st.title("Drosophila Gender Classifier")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
    try:
        response = requests.post("https://drosophila-api.onrender.com/predict", files=files)
        if response.status_code == 200:
            result = response.json().get("result", {})
            males = result.get("males", 0)
            females = result.get("females", 0)
            st.success(f"Detected: {males} males and {females} females.")
        else:
            st.error(f"Something went wrong: {response.text}")
    except Exception as e:
        st.error(f"Request failed: {e}")