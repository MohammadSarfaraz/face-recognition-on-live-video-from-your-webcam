#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("mohammadsarfaraz978@gmail.com", "password")
    server.sendmail("mohammadsarfaraz978@gmail.com", to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open notepad' in query:
            notebook = "C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
            os.startfile(notebook)
        
        elif 'open cv' in query:
            cv = "E:\\cv\\current cv - Copy.DOCX"
            os.startfile(cv)
        
        elif 'open my photo' in query:
            codePath = "C:\\Users\\hp\\project ml\\sar.jpg"
            os.startfile(codePath)
            
        elif 'play music' in query:
            music_dir = 'D:\\sarfaraz\\SARFARZ\\New song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))
        
        
        elif 'current position' in query:
            speak("Sir Let me check")
            cd=os.getcwd()
            print(cd)
            speak(f"my current Working dir {cd}")
 


        elif 'play movie' in query:
            music_dir = 'E:\\Movies'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

            
        elif 'who are you' in query:
            speak("Sir,I am jarvis the AI robot Working for your service.How may I help you")

        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\project ml\\face recognition.ipynb"
            os.startfile(codePath)

        elif 'email to sarfaraz' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mohammadsarfaraz978@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend sarfaraz bhai. I am not able to send this email")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




