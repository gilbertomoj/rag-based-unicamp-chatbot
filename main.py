import streamlit as st
from qa_chain import setup_qa_chain

st.set_page_config(page_title="RAG Unicamp", page_icon="📚")
st.title("Vestibular Unicamp")

with st.sidebar:
    st.button("Reset", type="primary")
    st.button("Application", type="primary")
    st.download_button('Histórico do chat', 'text_contents')
    with st.echo():
        st.write("This code will be printed to the sidebar.")


    st.success("Done!")
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
