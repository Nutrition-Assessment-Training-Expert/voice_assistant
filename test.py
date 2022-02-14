import webbrowser
from utils import *
import wikipedia

greet()
username()    # see if i can save the username



while True:
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'nate' in query:
        speak(" Here you go to NATE's webpage! \n")
        webbrowser.open("https://nate.health/")

    elif 'exit' in query:
        speak("Thanks for giving me your time")
        exit()