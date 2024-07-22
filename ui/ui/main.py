import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API URL from environment variables
API_URL = os.getenv("API_URL")


def main():
    st.title("API Request Streamlit App")

    with st.form(key="api_form"):
        user_input = st.text_input("Enter some data:")
        submit_button = st.form_submit_button(label="Send POST Request")

    if submit_button:
        if user_input:
            response = send_post_request(user_input)
            if response:
                st.success(f"Response from API: {response.text}")
            else:
                st.error("Failed to get a response from the API.")
        else:
            st.error("Please enter some data.")


def send_post_request(data):
    print(API_URL)
    api_url = f"{API_URL}/chat"  # Replace with the actual API URL
    headers = {"Content-Type": "application/json", "accept": "application/json"}
    payload = {"content": data}
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    main()
