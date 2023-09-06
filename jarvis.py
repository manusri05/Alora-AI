from platform import python_branch
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
# import google
import googlesearch
import webbrowser
import os
import smtplib
import pywhatkit
from googlesearch import search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

MASTER = "Soumya"

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!"+ MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon!"+ MASTER)

    else:
        speak("Good Evening!"+ MASTER)

    speak("I am Jarvis. How may I help you") 

def takeCommand():
    # It takes microphone input from the user and returns string output               
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        # passes the power to except block if for ex. microphone is not working
        # which is here the source
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        # using 'Google' here as the whole recognization process of our voice is performed through Google API
        print(f"User said: {query}\n")
        #print("User said:", query)
    
    except Exception as e:
        #print e
        print("Say that again please...")
        return "None"
    return query

# def sendEmail(to, content):


speak("Initializing Jarvis...")   
if __name__ == "__main__":
    # speak("You can do it Chinky")
    WishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
        # query is nothing but a command that we give to assistant

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            ''' it means that if we have wikipedia said in our command i.e,query,
            it replaces wikipedia with an empty string as is displayed in the code
            query=query.replace("wikipedia", "")

            '''
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        # Not working
        # if 'google' in query:
        #     speak("Searching google...")
        #     query = query.replace("google", "")
        #     results = google.summary(query, sentences=2)
        #     speak("According to google")
        #     print(results)
        #     speak(results)
        # below code opens each of them in windows explorer ,but we want it to open in chrome.
        # hence, finding out how to use this web browser module to open chrome by searching in chrome
        # search "web browser open in chrome"
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        # elif 'open youtube' in query:
            # url = "youtube.com"
            # Windows
            # chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
# Linux
# chrome_path = '/usr/bin/google-chrome %s'

            # webbrowser.get(chrome_path).open(url)
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            # works
            # webbrowser.get("C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s").open("http://google.com")
            # open_google = webbrowser.get('windows-default').open('https://google.com')
            # works

        # To search something in Google
        elif 'google' in query:
            speak("Searching google...")
            query = query.replace('google',"")
            # speak('playing'+ query)
            results = googlesearch.search(query, num_results=10, lang="en")
            speak("According to google")
            print(results)
            speak(results)
        
        elif 'open new tab in google' in query:
            webbrowser.open_new_tab("http://www.google.com")
        # elif 'open stackoverflow' in query:
            # webbrowser.open("stackoverflow.com") 
        
        elif 'open github' in query:
            chrome_path = "C://Program Files (x86)//Google//Chrome//Application//Chrome.exe %s"
            webbrowser.get(chrome_path).open("https://github.com/")

        # elif 'open reddit' in query.lower():
        #     # url = 'reddit.com'
        #     webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://reddit.com")
        #     # chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        #     # webbrowser.get(chrome_path).open(url)
        
        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # elif 'open Whatsapp' in query:
            # WhatsappPath = "C:\\Users\\hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            # os.startfile(WhatsappPath)

        

        elif 'open whatsapp' in query:
            whatsapp = query.replace("open whatsapp","")
            speak('opening'+ whatsapp)
            pywhatkit.sendwhatmsg("+917680835116","Chotuuuuuu",15,27)
        # trying to play song in youtube
        # tried saying play...msn opened
        elif 'play' in query:
            song = query.replace('play',"")
            speak('playing'+song)
            pywhatkit.playonyt(song)

        # elif 'open email' in query:
        #     gmail = query.replace("open email","")
        #     speak('opening'+ gmail)
        #     pywhatkit.sendwhatmsg("+7680835116","ok done",12,42)

            # elif 'email to soumya' in query:
            # try:
                # speak("What should I say?")
                # content = takeCommand()
                # to = "soumyayourEmail@gmail.com"
                # sendEmail(to, content)
                # speak("Email has been sent!")
            # except Exception as e:
                # print(e)
                # speak("Sorry my friend, I am unable to send this email")

        # if quit in query:
# exit function usage



        


        




            