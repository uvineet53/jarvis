import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os,sys,subprocess
import smtplib
import wolframalpha
from selenium import webdriver

master= "VEENEET"
print("Initializing Jarvis")

engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# speak function will pronounce the string which is passed
def speak(text) :
    engine.say(text)
    engine.runAndWait()

# This function will wish me as per the current time
def wishMe():
    hour=int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<12:
        speak("Good Morning..."+ master)
    elif hour>=12 and hour<18:
        speak("Good Afternoon..."+ master)
    else:
        speak("Good Evening..."+ master)

    speak("Taanhaaaji ka bhaalaa , Samakash Bosariwaaala")
    speak("I am jarvis. How may I help you ?")
# this function will take command from the microphone
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
    try :
        print("Recognizing")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said : {query}\n")
    except Exception as e :
        print("Say that again please")
        speak("Say that again please.")
        query=None
    return query
# main program starts here..
speak("Initializing Jarvis...")
wishMe()
query = takeCommand()
#logic for executing basic tasks
def another() :

    print("Do you want to ask other questions ?")
    speak("Do you want to ask other questions ?")
    value= input("Enter yes or no : ")
    if 'yes' in value.lower() :
     takeCommand()
    else :
        speak(f"Bye {master}")
         


if 'youtube' in query.lower(): 
    
            
    indx = query.lower().split().index('youtube') 
    query = query.split()[indx + 1:] 
    speak(f"Opening youtube {query}")
    webbrowser.get('safari').open_new_tab(f"http://www.youtube.com/results?search_query={query}") 
        
    
elif 'wikipedia' in query.lower():
    speak('Searching wikipedia')
    query = query.replace("wikipedia","")
    results= wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)

elif 'open facebook' in query.lower() :
    speak("Opening facebook")
    webbrowser.get('safari').open_new_tab("facebook.com")

elif 'time' in query.lower() :
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{master} the time is {strTime}")

elif 'who made you' in query.lower() :
    speak("I was made by Vineet Upadhyay.")
    print("I was made by Vineet Upadhyay.")
    

elif 'how are you' in query.lower():
    speak(f"I am fine {master}")
    
    
