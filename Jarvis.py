import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:

        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello Harsh. I am Jarvis. Please tell me how may i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        user_query = r.recognize_google(audio, language='en-in')
        print(f"Your input: {user_query}")

    except Exception:
        print("Say that again please...")
        return "None"
    return user_query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia:")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com")

        elif 'open google' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("google.com")

        elif 'play music' in query:
            songs = os.listdir('D:\\Music')
            os.startfile(os.path.join('D:\\Music', random.choice(songs)))

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        elif 'open visual' in query:
            os.startfile("C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'open pycharm' in query:
            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2\\bin\\pycharm64.exe")

        elif 'offline' in query:
            exit()