import streamlit as st
import requests
import json

def send_request(user_input):
    response = requests.post("http://local:8000/process", json={"data": user_input})
    return response.json()

def save_json(data):
    file_path = "processed_data.json"
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    return file_path

st.title("AI Orchestrator")

user_input = st.text_area("Enter your request:")

if st.button("Process"):
    if user_input.strip():
        response_data = send_request(user_input)
        st.json(response_data)
        file_path = save_json(response_data)
        
        with open(file_path, "rb") as file:
            st.download_button(label="Download Processed JSON", data=file, file_name="processed_data.json", mime="application/json")
    else:
        st.warning("Please enter a valid input.")