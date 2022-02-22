# -*- coding: utf-8 -*-

import pyttsx3
import speech_recognition as sr
import datetime
import shutil
import random

# Defining the voice for pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio:str):
    '''Function to make the Voice Assistant speak.
    Args:
        audio : text (str)
    '''
    engine.say(audio)
    engine.runAndWait()
 
def greet(assname):
    '''Function to greet the user.
    '''

    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon  !")  
  
    else:
        speak("Good Evening  !") 
  
    # assname =("NATE")
    speak("I am your Assistant")
    speak(assname)

def talk_expressions(name):
    '''Function with NATE's expressions, randomly choosing one.
    args:
    name : user's name (str)
    '''
    list = ['Hello there! How are you doing today?',    'How are you feeling?','What are you up to today?',
    'Hey, how’s it going?','Anything I can support you with?',f'Are you doing alright, {name}?']
    speak(random.choice(list))
 
def username():
    '''Function to get user's name
    '''

    speak("What should i call you?")
    name = takeCommand()
    speak(f"Welcome {name}!")

    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome ", name.center(columns))
    print("#####################".center(columns))

    return name

def takeCommand():
    '''Function to receive a voice command from the microphone.
    '''

    r = sr.Recognizer()

    with sr.Microphone() as source:
        speak("I'm listening")
        print("Listening...")
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except sr.UnknownValueError:

        print("Unable to Recognize your voice.")
        return None

    except sr.RequestError() as e:
        print('could not request results from Google speech recognition source; {0}'.format(e))
        return None


    return query
  
