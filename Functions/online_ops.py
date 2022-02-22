import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

# NEWS_API_KEY = config("NEWS_API_KEY")
# OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
# TMDB_API_KEY = config("TMDB_API_KEY")
# EMAIL = config("EMAIL")
# PASSWORD = config("PASSWORD")


def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results


def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    kit.search(query)


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


# def send_email(receiver_address, subject, message):
#     try:
#         email = EmailMessage()
#         email['To'] = receiver_address
#         email["Subject"] = subject
#         email['From'] = EMAIL
#         email.set_content(message)
#         s = smtplib.SMTP("smtp.gmail.com", 587)
#         s.starttls()
#         s.login(EMAIL, PASSWORD)
#         s.send_message(email)
#         s.close()
#         return True
#     except Exception as e:
#         print(e)
#         return False


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


from urllib.request import urlopen
from json import load
import webbrowser
import pytz


def ipInfo(addr=''):
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    data = load(res)
    for attr in data.keys():
        print(attr, ' ' * 13 + '\t->\t', data[attr])


def getIP(addr=''):
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    data = load(res)
    return data['ip']


def getLOC(addr=''):
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    data = load(res)
    return data['city'] + data['region'] + data['country']


def get_local_news(addr=''):
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    loc = load(res)['city']
    webbrowser.open(f'https://www.google.com/search?q={loc}+local+news')


def get_national_news(addr=''):
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    nation = load(res)['country']
    nation = pytz.country_names[nation]
    webbrowser.open(f'https://www.google.com/search?q={nation}+local+news')


def get_state_news(addr=''):
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    state = load(res)['region']
    webbrowser.open(f'https://www.google.com/search?q={state}+local+news')
