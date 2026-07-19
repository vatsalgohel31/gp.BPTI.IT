# voice system for this Program !
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id,)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def starting_speech():
    speak("Welcome to Market Place!")
    speak("Here is the all item available in the market!")

def ending_speech():
    speak("Thanks for the visit!\n Visit Again")