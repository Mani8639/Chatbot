
import streamlit as st
import ollama

st.title("Chat with llama3 (chatbot)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


if prompt := st.chat_input("Type your message here..."):
# Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

# Generate response from LLaMA
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")

      
        response = ollama.chat(model="llama3", messages=st.session_state.messages)
        reply = response["message"]["content"]
       
        

        message_placeholder.markdown(reply)

# Add assistant reply to chat history
    st.session_state.messages.append({"role": "assistant", "content": reply})


