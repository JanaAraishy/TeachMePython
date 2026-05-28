import streamlit as st
import requests

st.title("TeachMePython Login")

with st.form("login"):

    name = st.text_input("Add your name:")

    level = st.slider(
        "Select your level (1–5):",
        1,
        5,
        1
    )

    submit = st.form_submit_button("Start Learning")


if submit and name:

    try:

        response = requests.post(
            "http://127.0.0.1:8000/login",
            json={
                "name": name,
                "level": level
            }
        )

        print(response.status_code)
        print(response.text)

        response.raise_for_status()

        data = response.json()

        st.success(
            f"Welcome {name}! You selected level {level}."
        )

        st.write("User ID:", data["user_id"])

        greet_code = f"""
def greeting(name):
    print("Hello {name}, this is your guide to learn Python")
"""

        st.code(greet_code, language="python")

    except Exception as e:

        st.error(f"Error: {e}")
