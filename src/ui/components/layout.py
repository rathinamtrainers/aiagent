import streamlit as st

def create_input_columns():
    """Create input columns for the prompt and selection of model and vector database."""
    return st.columns([5, 2])

def display_chat_messages(messages):
    """Display chat messages from the session state."""
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
