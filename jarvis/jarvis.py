import pyttsx3   #library to convert the text to speech

import speech_recognition as sr #python library to take voice command from the user

import webbrowser
import wikipedia
import os
import datetime

''' music dictionary '''
dictionary = {
        1:"https://www.youtube.com/watch?v=eBI23_Sjfeo&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=1",
        2:"https://www.youtube.com/watch?v=uuCFRaFWjwY&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=2",
        3:"https://www.youtube.com/watch?v=pfVODjDBFxU&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=3",
        4:"https://www.youtube.com/watch?v=qk2WMmiiVFE&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=4",
        5:"https://www.youtube.com/watch?v=GgmFC8y8q3k&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=5",
        6:"https://www.youtube.com/watch?v=Az-mGR-CehY&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=6",
        7:"https://www.youtube.com/watch?v=7wtfhZwyrcc&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=7",
        8:"https://www.youtube.com/watch?v=UiVErlUAi_U&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=8",
        9:"https://www.youtube.com/watch?v=PqFMFVcCZgI&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=9",
        10:"https://www.youtube.com/watch?v=II4Lx4S1KQQ&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=10",
        11:"https://www.youtube.com/watch?v=5Gowkz2BaUM&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=11",
        12:"https://www.youtube.com/watch?v=pqjLhOcXgcs&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=12",
        13:"https://www.youtube.com/watch?v=NrXdauEv9HY&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=13",
        14:"https://www.youtube.com/watch?v=KUyAL9n_qXE&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=14",
        15:"https://www.youtube.com/watch?v=giAk9fuMn4c&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=15",
        16:"https://www.youtube.com/watch?v=NbyHNASFi6U&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=16",
        17:"https://www.youtube.com/watch?v=OIv0FLrbnGE&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=17",
        18:"https://www.youtube.com/watch?v=ZgHXpvVw4GE&list=PLy8I8xYNEbpKhdErVDZv8PLiBH64mTlB6&index=18"
    }


'''           '''
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def music_dictionary(number):
    return dictionary[number]

def wishme():
    hour = int(datetime.datetime.now().hour)
    if(hour > 0 and hour < 12):
        speak("Good Morning, Master")
    elif(hour > 12 and hour < 16):
        speak("Good afternoon, Master")
    elif(hour > 16 and hour < 19):
        speak("Good Evening, Master")
    else:
        speak("Good night, Master")

    today_date()
    current_time()

    

def today_date():
    date_day = datetime.datetime.now().day
    date_year= datetime.datetime.now().year
    # date_day = datetime.datetime.now().day

    day = datetime.datetime.today().strftime("%A")
    month = datetime.datetime.today().strftime("%B")
    statement = "Master, the Current date is "+str(date_day) + " " + str(month) + " " + str(date_year)
    speak(statement)

    statement = "Master, the today's day is "+str(day)
    speak(statement)

def current_time():
    c_hour = datetime.datetime.now().hour
    c_min = datetime.datetime.now().minute
    c_sec = datetime.datetime.now().second

    statement = "Sir the time is "+str(c_hour)+" hours"+" " + str(c_min) + " minutes" +" and "+str(c_sec)+" seconds"
    speak(statement)
    
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshhold = 1

        audio = r.listen(source)

    try:
        print("Recognizing ...")
        query = r.recognize_google(audio,lang = 'en-in')

        print(f"Order given - {query}\n\n")

    except Exception as e:
        speak(e)

        print("please say that again")
        return "None"

    return query

def send_email():
    pass
    #to be done later

if __name__ == "__main__":
    wishme()

    while(True):

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia ...')
            results = wikipedia.summary(query,sentences = 2)

            speak("According to Wikipedia..")
            print(results)
            speak(results)

        elif "youtube" in query:
            webbrowser.open("youtube.com")

        elif "google" in query:
            webbrowser.open("google.com")

        elif "music" in query:
            # code for music
            pass

        elif "time" in query:
            current_time()

        elif "vs code" in query:
            path = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code"
            os.startfile(path)

