import streamlit as st
from pyprojroot.here import here
import sys
sys.path.append(str(here()))

from components.layout import create_input_columns, display_chat_messages
from src.webapp.models.prompt_model import get_vertexai_response  # Absolute import

API_URL = "http://127.0.0.1:8888/get_prompt_response"

def streamlit():
    st.title("MY CHATBOT")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    display_chat_messages(st.session_state["messages"])

    media_input = st.radio("Do you want to provide a PDF URL?", ("Yes", "No"))

    if media_input == "Yes":
        file_uri = st.text_input("Enter PDF URL:")
    else:
        file_uri = None

    model = "gemini-1.5-pro-001" if file_uri else st.selectbox(
        "Choose Model",
        ["gemini-1.5-pro-001", "gemini-1.5-flash-001"],
        index=0,
        format_func=lambda x: x.lower()
    )

    vdb = st.selectbox(
        "Choose Vector Database",
        ["ChromaDB", "Pinecone", "Weaviate", "Milvus", "Qdrant"],
        index=0,
        format_func=lambda x: x.lower()
    )

    cols = create_input_columns()

    with cols[0]:
        prompt = st.text_area("Ask a question:")

    if st.button("Get Response"):
        user_message = {"role": "user", "content": prompt}
        st.session_state["messages"].append(user_message)
        with st.chat_message("user"):
            st.markdown(prompt)

        response = get_vertexai_response(prompt, model, file_uri)

        assistant_message = {"role": "assistant", "content": response}
        st.session_state["messages"].append(assistant_message)
        with st.chat_message("assistant"):
            st.markdown(response)

# streamlit()

if __name__ == "__main__":
    streamlit()


