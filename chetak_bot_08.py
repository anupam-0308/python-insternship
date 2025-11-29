import streamlit as st
import google.generativeai as genai

key = "AIzaSyCZd5zgG3lRkAVS22dD65lPP5E-Ze4hU8M"
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash")


st.title(" Chetak The Chatbot ")
st.text("How can Chetak help with?")

st.sidebar.header("Settings")
temperature = st.sidebar.slider("Creativity Level", 0.0, 1.0, 0.5)
clear = st.sidebar.button("Clear Chat History")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if clear:
    st.session_state.chat_history = []


user_msg = st.text_input("Ask chetak:")

if st.button("Send"):
    if user_msg.strip() != "":
        # Save user message
        st.session_state.chat_history.append(("You", user_msg))

        # Bot reply
        try:
            response = model.generate_content(
                user_msg,
                generation_config={"temperature": temperature}
            )
            bot_reply = response.text

        except Exception as e:
            bot_reply = "Error: " + str(e)

        # Save bot reply
        st.session_state.chat_history.append(("Bot", bot_reply))
    else:
        st.warning("Please type something before sending!")


st.header("Chat Output")

for sender, msg in st.session_state.chat_history:
    st.write(f"{sender}:** {msg}")


with st.expander("See Example Prompts"):
    st.write("""
    - What is Captial  of India ?
    - home workout plan ?
    - Write an email for leave application.
    - Explain AI in simple words.
    """)
