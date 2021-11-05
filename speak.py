import pyttsx3

engine  = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('rate',100)
engine.setProperty('voice',voice[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


