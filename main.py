#<----------------------------------Query Processeses---------------------------------->
import subprocess
import time
import os
import pyautogui
import pyjokes
import webbrowser as wb
from Features.base import date, open_chrome, search_wikipedia
from Features.base import take_command, time1, wishme, wishme2
from Features.custom_voice import speak
from Features.spotify_automation import *
import config

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

if __name__ == "__main__":

    wishme()

    while True:
        query = take_command().lower()
        print(f'You : {query}')
        
        if 'time' in query:
            time1()

        elif 'hello' in query or 'good' in query or 'hey' in query:

            wishme2()

            query2=take_command().lower()
            print(f'You : {query2}')
            
            if 'yes' in query2 or 'absolutely' in query2:

                print("Shiina : I am pleased to hear of this, my honored one.")
                speak('I am pleased to hear of this, my honored one.')
                
            
            elif 'not yet' in query2 or 'no' in query2:

                print("Shiina : Your well-being is of utmost importance to me, my honoured one. If there is anything troubling you, please know that I am here to assist you in every way possible.")
                
            print("Shiina : In what way may I assist you today, my gracious master?")
            speak("In what way may I assist you today, my gracious master?")
            
            
        elif 'how are you' in query or "whats up" in query or "what's up" in query:

            print("Shiina : I am faring splendidly, my esteemed lord. Your concern honors me.")
            speak("I am faring splendidly, my esteemed lord. Your concern honors me.")
            
            print("Shiina : In what way may I assist you today, my gracious master?")
            speak("In what way may I assist you today, my gracious master?")
            
        elif 'date' in query:
            date()
            
        elif 'open chrome' in query:
            open_chrome()
            
        elif 'wikipedia' in query:
            search_wikipedia(query)
            
        # elif 'search' in query:
        #     print("Shiina : Your command, master. What shall I search for?")
        #     speak("Your command, master. What shall I search for?")
        #     search=take_command().lower()
        #     wb.get(chrome_path).open_new_tab(search + '.in')

        #open notepad
        elif 'open notepad' in query:
            print("Shiina : Initiating notepad for you.")
            speak("Initiating notepad for you")
            location = "C:/WINDOWS/system32/notepad.exe"
            notepad = subprocess.Popen(location)
        #close notepad
        elif 'close notepad' in query:
            print("Shiina : Notepad is now being closed, my noble master.")
            speak("Notepad is now being closed, my noble master.")
            notepad.terminate()
        
        elif 'joke' in query or 'jokes' in query:
            speak(pyjokes.get_joke())

#<------------------------Logout/Shutdown/Restart------------------------------->

        elif 'logout' in query:
            print("Shiina : Commencing the conclusion of your session.")
            speak("Commencing the conclusion of your session.")
            time.sleep(5)
            os.system('shutdown - l')

        elif 'shutdown' in query or 'shut down' in query:
            print("Shiina : Commencing the cessation of operations.")
            speak('Commencing the cessation of operations.')
            time.sleep(5)
            os.system('shutdown /s /t 1')

        elif 'restart' in query:
            print("Shiina : Initiating a ceremonial reactivation.")
            speak("Initiating a ceremonial reactivation.")
            time.sleep(5)
            os.system('shutdown /r /t 1')
        
#<----------------------------PyAutoGUI features---------------------------->
        elif 'hidden menu' in query:
            #Win + X : open the hidden menu
            print("Shiina : By your grace, I will now reveal the Hidden Menu for your perusal.")
            speak("By your grace, I will now reveal the Hidden Menu for your perusal.")
            pyautogui.hotkey('winleft', 'x')
        
        elif 'task manager' in query:
            #Ctrl + Shift + Esc : open task manager
            print("Shiina : At your service, my honoured one. Allow me to present the Task Manager.")
            speak("At your service, my honoured one. Allow me to present the Task Manager.")
            pyautogui.hotkey('ctrl', 'shift', 'esc')

        elif 'task view' in query:
            #Win + tab : open task view
            print("Shiina : As you wish, I am now opening the Task View for your convenience.")
            speak("As you wish, I am now opening the Task View for your convenience.")
            pyautogui.hotkey('winleft','tab')

        elif 'take screenshot' in query:
            #Win + prtsc : captures screenshot
            pyautogui.hotkey('winleft','prtscr')
            print("Shiina : With reverence, I have captured the screenshot you desired, my lord.")
            speak("With reverence, I have captured the screenshot you desired, my lord.")

        # elif 'take screenshot' in query:
        #     img = pyautogui.screenshot()
        #     img.save(Location)
        #     print()
        #     speak()

        elif 'snip' in query:
            #Win + Shift + s : opens snip
            pyautogui.hotkey('winleft', 'shift', 's')
            print("Shiina : The Snipping Tool is now ready for your use, my lord. You may proceed as you wish.")
            speak("The Snipping Tool is now ready for your use, my lord. You may proceed as you wish.")

        elif 'close app' in query or 'close the app' in query or 'close this app' in query:
            #Alt + f4 : closes the app, may pull out the shutdown menu
            pyautogui.hotkey('alt','f4')
            print("Shiina : The application has been gracefully terminated, my honoured one.")
            speak("The application has been gracefully terminated, my honoured one.")

        elif 'new virtual desktop' in query or 'new desktop' in query:
            #winleft + ctrl + d : creates new virtual desktop
            pyautogui.hotkey('winleft', 'ctrl', 'd')
            print("Shiina : A new virtual environment has been prepared, my honoured one.")
            speak("A new virtual environment has been prepared, my honoured one.")

#<-----------------------------------Spotify Features----------------------------------------------------------->
        
        elif 'open spotify' in query:
            print("Shiina : Honoured Master, I shall now open Spotify for you.")
            speak("Honoured Master, I shall now open Spotify for you.")
            login(config.username, config.password)

        elif 'search a song' in query or "open search" in query or "search for a song" in query:
            print("Shiina : May I inquire which melody you would desire to hear, my esteemed master?")
            speak("May I inquire which melody you would desire to hear, my esteemed master?")
            song = take_command()
            search_song(song)

        elif "play" in query:
            play_song()

        elif 'like this song' in query:
            print("Shiina : Honoured Master, I am now favouring this song for you.")
            speak("I am now favouring this song for you, honoured one")
            like_song()

        elif 'download' in query:
            download()

        elif 'add to playlist' in query:
            playlist()