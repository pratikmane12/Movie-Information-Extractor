import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")
st.caption("Welcome! Type 0 to exit the application")

model = ChatMistralAI(model="open-mistral-nemo", temperature=0.7, max_tokens=300)

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="you are a funny AI agent")
    ]

# Show the chat history (the system message is not displayed)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

prompt = st.chat_input("Enter the message")

if prompt:
    if prompt == "0":
        st.info("Goodbye!")
        st.stop()

    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    response = model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))
    with st.chat_message("assistant"):
        st.write(response.content)