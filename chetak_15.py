import streamlit as st
import pandas as pd
import google.generativeai as genai
from audio_recorder_streamlit import audio_recorder
import base64
import speech_recognition as sr
from gtts import gTTS
import tempfile

key = "AIzaSyAUhV5chgzPOj-vOl7AcZ9z0gd1lTnt53I"
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Chetak – Voice Enabled Chatbot")
st.text("Ask with text or speak using microphone")

st.sidebar.header("Settings")
temperature = st.sidebar.slider("Creativity Level", 0.0, 1.0, 0.5)
clear = st.sidebar.button("Clear Chat History")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if clear:
    st.session_state.chat_history = []

st.subheader(" Speak to Chetak")
audio_bytes = audio_recorder()

user_msg = ""

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")
    st.success("Voice received! Converting to text...")

    recognizer = sr.Recognizer()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_bytes)
        temp_audio_path = temp_audio.name

    with sr.AudioFile(temp_audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            user_msg = recognizer.recognize_google(audio_data)
            st.write(f" You said: **{user_msg}**")
        except:
            st.error("Could not understand the audio")

text_input = st.text_input(" Type your message:")
send_button = st.button("Send")

if send_button and text_input.strip() != "":
    user_msg = text_input

if user_msg != "":
    st.session_state.chat_history.append(("You", user_msg))

    try:
        response = model.generate_content(
            user_msg,
            generation_config={"temperature": temperature}
        )
        bot_reply = response.text
    except Exception as e:
        bot_reply = "Error: " + str(e)

    st.session_state.chat_history.append(("Bot", bot_reply))

    tts = gTTS(text=bot_reply, lang="en")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
        tts.save(temp_audio_file.name)
        audio_file_path = temp_audio_file.name

    st.audio(audio_file_path, format="audio/mp3")

st.header(" Chat Output")

for sender, msg in st.session_state.chat_history:
    st.write(f"**{sender}:** {msg}")

with st.expander("See Example Prompts"):
    st.write("""
    - What is Python?
    - Create a 1-day workout plan.
    - Write an email for leave application.
    - Explain AI in simple words.
    """)
