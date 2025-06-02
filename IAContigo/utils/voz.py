import pyttsx3

def hablar(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(texto)
    engine.runAndWait()
