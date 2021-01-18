import pyttsx3
#this module is not in-built in your python
#you had to install it using pip command

engine = pyttsx3.init('sapi5')
#sapi5, windows voice

rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[5].id)
#may be you have many voices inn your Pc, choose one out of them in "voices[<>]"
#Example-<engine.setProperty('voice', voices[0].id)>

engine.setProperty('rate', 125)
#rate is speed of speaking, you can change it

#inetialing a function
def spk(audio):
    engine.say(audio)
    engine.runAndWait()

spk('I can speak')
#write in spk(<here>),what you had to make your code speak
