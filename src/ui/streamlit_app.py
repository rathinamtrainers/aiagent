import streamlit as st
import requests

API_URL = "http://localhost:8000/get_prompt_response"

def streamlit_example():
    st.title("MY CHATBOT")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    cols = st.columns([5, 2])

    with cols[0]:
        prompt = st.chat_input("Ask a question:")

    with cols[1]:
        model = st.selectbox(
            "Choose Model",
            ["gemini-1.5-pro-001","gemini-1.5-flash-001"],
            index=1,  # Default selection (optional)
            format_func=lambda x: x.lower()  # Custom format     (optional)
        )
        vdb = st.selectbox(
            "Choose Vector Database",
            ["ChromaDB", "Pinecone", "Weaviate", "Milvus", "Qdrant"],
            index=0,  # Default selection (optional)
            format_func=lambda x: x.lower()  # Custom format (optional)
        )

    if not prompt:
        return

    user_message = {"role": "user", "content": prompt}
    st.session_state["messages"].append(user_message)
    with st.chat_message("user"):
        st.markdown(prompt)

    response = requests.post(API_URL, json={"prompt": prompt, "model": model, "vdb": vdb})

    try:
        reply = response.json().get("response")
    except ValueError:
        st.error("Error decoding response from server.")
        st.write(response.text)  # Print the raw response for debugging
        return

    assistant_message = {"role": "assistant", "content": reply}
    st.session_state["messages"].append(assistant_message)
    with st.chat_message("assistant"):
        st.markdown(reply)

def main():
    streamlit_example()

if __name__ == "__main__":
    main()
