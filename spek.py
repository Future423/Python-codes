import pyttsx3
engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[5].id)
engine.setProperty('rate', 125)

def spk(audio):
    engine.say(audio)
    engine.runAndWait()

spk('''I'm fine
very fine''')
