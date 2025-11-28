import pyttsx3

engine = pyttsx3.init()

for i in range(10):
    engine.say(" hello world ")
    engine.runAndWait()
   