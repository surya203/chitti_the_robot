import streamlit as st
import os
from dotenv import load_dotenv
from openai import DefaultHttpxClient, OpenAI

load_dotenv()   
api_key = os.getenv("OPENAI_API_VALUE")

#line number 13 can be removed if you are not using httpx2 2.14
http_client = DefaultHttpxClient(headers={"Accept-Encoding": "gzip, deflate"})
client = OpenAI(api_key=api_key, http_client=http_client)

st.title("Human Resource Chatbot")

# Remember the chat thread for this browser session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show the conversation so far
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask me anything about human resources:")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    response = client.responses.create(
        model="gpt-4.1",
        instructions="Your are a human resource assistant. You are helpful and friendly. You are always willing to help the user. if the user asks about a topic that is not related to human resources, you should say that you're here only to answer questions related to human resources. If the user asks about a topic that is not related to human resources, you should suggest the user to ask about a topic that is related to human resources.",
        input=st.session_state.messages,
        temperature=0.5,
    )

    st.session_state.messages.append({"role": "assistant", "content": response.output_text})
    with st.chat_message("assistant"):
        st.write(response.output_text)
