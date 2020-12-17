import pyttsx3
#this module is not in-built in your python
#you had to install it using pip command

engine = pyttsx3.init('sapi5')
#sapi5, windows voice

rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[5].id)
#may be your Pc have many voices choose one out of them in "voices[<>]"

engine.setProperty('rate', 125)
#rate is speed of speaking, you can change it

#inetialing a function
def spk(audio):
    engine.say(audio)
    engine.runAndWait()

spk('I can speak')
#write in spk(<here>),what you had to make your code speak
