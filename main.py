import pyttsx3 as p
import speech_recognition as sr
import datetime
import webbrowser
from selenium_web import *
from YT_auto import *
from News import *
from jokes import *
from weather import *

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour =int(datetime.datetime.now().strftime("%H"))
    if hour>0 and hour<12:
        return("morning")
    elif hour>=12 and hour<16:
        return("afternoon")
    else:
        return ("evening")


r = sr.Recognizer()

speak("Hello sir, Good" +wish_me()+", I'm your voice assistant. How are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
except LookupError:
    print("Could not understand audio")
print(text)



if "what" and "about" and "you" in text:
    speak("I am having a good day sir")
speak("What can i do for you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    try:
        text2 = r.recognize_google(audio)
    except LookupError:
        print("Could not understand audio")

if "information" in text2:
    speak("you need information related to which topic?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        info = r.recognize_google(audio)

    speak("searching {} in wikipedia". format(info))
    assist = infow()
    assist.get_info(info)

elif "play" and "video" in text2:
    speak("you want to play which video??")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)

    print("playing {} on youtube".format(vid))
    speak("playing {} on youtube".format(vid))
    assist = music()
    assist.play(vid)

elif "news" in text2:
    print("Sure sir, I will now read news for you.")
    speak("Sure sir, I will now read news for you.")
    latest = news()
    speak(news())
    print(news())

elif "joke" in text2:
    speak("sure sir, get ready to crack some ribs")
    f = r"https://official-joke-api.appspot.com/jokes/general/random"
    a = jokes(f)
    for i in (a):
        print(i["type"])
        print(i["setup"])
        speak(i["setup"])
        print(i["punchline"])
        speak(i["punchline"])


elif "date" in text2:
    date = datetime.datetime.now().strftime("%A %B %d, %Y")
    print(date)
    speak("The date today is" + date)


elif "time" in text2:
    speak("Here is the time.")
    time = datetime.datetime.now().strftime("%I:%M:%p")
    print(time)
    speak("The time is" + time)

elif "location" in text2:
    speak("What is the location?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        location = r.recognize_google(audio)

    url = ('https://google.nl/maps/place/' + location)
    webbrowser.get().open(url)
    speak("Here is the location of " + location)

elif "weather" in text2:
    speak("Which city would you like to know the weather status?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        city = r.recognize_google(audio)
    print(main_weather(city))
    speak(main_weather(city))
