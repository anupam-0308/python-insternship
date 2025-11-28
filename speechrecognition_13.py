import speech_recognition as sr
mic= sr.Recognizer()
with sr.Microphone() as source:
    print("start speaking ....")
    voice = mic.listen(source)
    text=mic.recognize_google(voice)
    print ("you said this :",text)