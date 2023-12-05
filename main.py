import streamlit as st
from qa_chain import setup_qa_chain
import json

st.set_page_config(page_title="ChatCamp", page_icon="📚")
st.title("Unicamp Virtual")

if "messages" not in st.session_state:
    st.session_state.messages = []


def reset_chat_messages():
    st.session_state.messages = []


with st.sidebar:
    st.button("Reset", type="primary", on_click=reset_chat_messages())


class RAGChat:
    def __init__(self):
        self.qa_chain = setup_qa_chain()
        pass

    def main(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("What is up?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = self.qa_chain.run(prompt)
                message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})


if __name__ == '__main__':
    obj = RAGChat()
    obj.main()
