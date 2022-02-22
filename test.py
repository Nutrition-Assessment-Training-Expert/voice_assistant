import webbrowser
from utils import *
import wikipedia

# greet('NATE')

name = username()    # see if i can save the username
talk_expressions(name)

while True:
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak(f'Ok {name}, searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'website' in query or 'Nutrition Assessment Training Expert' in query:
        speak(f"Ok {name}, here you go to NATE's webpage! \n")
        webbrowser.open("https://nate.health/")

    elif "don't listen" in query or "stop listening" in query:
        speak(f"Ok {name}, for how much time you want me to stop from listening commands?")
        a = int(takeCommand())
        time.sleep(a)
        print(a)

    elif 'hello' in query or 'good morning' in query or 'good afternoon'  in query or 'good night' in query:
        talk_expressions()

    elif "who are you" in query or "define yourself" in query:
        text = f" I'm Nutrition Assessment Training Expert. Feel free to call me NATE. It’s a pleasure to meet you {name}!”"
        speak(text)

    elif 'exit' in query:
        speak(f"Thanks for giving me your time {name}. Nice talking to you!")
        exit()