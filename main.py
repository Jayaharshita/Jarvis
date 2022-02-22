import requests
from Functions.online_ops import get_random_advice, get_random_joke, play_on_youtube, search_on_google, \
    search_on_wikipedia, send_whatsapp_message
from Functions.online_ops import getIP, getLOC, get_local_news, get_state_news, get_national_news
import pyttsx3
import webbrowser
import speech_recognition as sr
from decouple import config
from datetime import datetime
from Functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad
from random import choice
from utils import opening_text
from pprint import pprint

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_user():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")


def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        elif 'my ip' in query:
            speak(getIP())

        elif 'find my location' in query:
            speak(getLOC())

        elif 'local news' in query:
            get_local_news()

        elif 'state news' in query:
            get_state_news()

        elif 'national news' in query:
            get_national_news()

        elif ('the time' in query):
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif ('open instagram' in query or 'open insta' in query):
            speak('opening instagram sir')
            webbrowser.open('https://www.instagram.com/')

        elif ('open facebook' in query or 'open fb' in query):
            speak('opening facebook sir')
            webbrowser.open('https://www.facebook.com/')

        elif ('open linkedin' in query):
            speak('opening linkedin sir')
            webbrowser.open('https://www.linkedin.com/')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak(
                'On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        # elif "send an email" in query:
        #     speak("On what email address do I send sir? Please enter in the console: ")
        #     receiver_address = input("Enter email address: ")
        #     speak("What should be the subject sir?")
        #     subject = take_user_input().capitalize()
        #     speak("What is the message sir?")
        #     message = take_user_input().capitalize()
        #     if send_email(receiver_address, subject, message):
        #         speak("I've sent the email sir.")
        #     else:
        #         speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)