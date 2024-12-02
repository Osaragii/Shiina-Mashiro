import datetime
import pyttsx3 as p
import speech_recognition as sr
import webbrowser as wb
from Features.custom_voice import speak
import wikipedia

#<------------------------Initial point--------------------------------------->
engine=p.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 200)

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#<--------------------------Functions----------------------------------------->
# def speak(text):

#     engine.say(text)
#     engine.runAndWait()

def take_command():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("Prepared to serve, my gracious master...")
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-us')
    except Exception as e:
        print('--')
        return '--'
    return query

def time1():

    time = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'Shiina : {time}')
    speak(time)

def date():
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    speak(f'Your grace, this day is the {day} of {month}, in the year {year}.')
    print(f'Shiina : Your grace, this day is the {day} of {month}, in the year {year}.')

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

def open_chrome():
    url = 'https://www.google.com/'
    wb.get(chrome_path).open(url)

def search_wikipedia(query):
    search_query = query.replace('wikipedia', '').strip()
    print(f'Shiina : Initiating the quest for information on {search_query} on Wikipedia, my gracious master. I kindly ask for your patience while I retrieve the information.')
    speak(f'Initiating the quest for information on {search_query} on Wikipedia, my gracious master. I kindly ask for your patience while I retrieve the information.')
    try:
        result = wikipedia.summary(search_query, sentences=2)
        print(f'Shiina : {result}')
        speak(result)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Shiina : There are multiple entries for this topic. Please be more specific.")
        speak("There are multiple entries for this topic. Please be more specific.")
        
    except wikipedia.exceptions.PageError:
        print("Shiina : I could not find any information on this topic.")
        speak("I could not find any information on this topic.")
    
    except Exception as e:
        print("Shiina : An error occurred while fetching the information.")
        speak("An error occurred while fetching the information.")

def wishme():

    print("Shiina : Welcome back, your grace. Mashiro Shiina stands ready to serve.")
    speak("Welcome back, your grace. Mashiro Shiina stands ready to serve.")

def wishme2():
    hour=datetime.datetime.now().hour
    if hour>=5 and hour<=12:
        print("Shiina : Good morning, my honoured one. May I inquire if you have had breakfast today?")
        speak("Good morning, my honoured one. May I inquire if you have had breakfast today?")

    elif hour>=12 and hour<=18:
        print("Shiina : A fine afternoon to you, my honoured one. May I ask if you have enjoyed your lunch?")
        speak("A fine afternoon to you, my honoured one. May I ask if you have enjoyed your lunch?")

    elif hour>=18 and hour<=21:
        print("Shiina : A lovely evening to you, my honoured one. May I inquire if you have dined well tonight?")
        speak("A lovely evening to you, my honoured one. May I inquire if you have dined well tonight?")

    else:
        print("Shiina : Good night, my honoured one. I hope you had a delightful dinner and are ready for a restful sleep.")
        speak("Good night, my honoured one. I hope you had a delightful dinner and are ready for a restful sleep.")
    # print("Shiina : In what way may I assist you today, my gracious master?")
    # speak("In what way may I assist you today, my gracious master?")