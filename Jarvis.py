import pyttsx3                           #"pip install pypiwin32" type in terminal for installing this module
import speech_recognition as sr          #"pip install speechRecognition" type in terminal for installing this module
import datetime
import wikipedia                         #"pip install wikipedia" type in terminal for installing this module
import webbrowser
import os
import smtplib
import subprocess

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')     #getting details of current voice
'#print(voices[0].id)'

engine.setProperty('voice', voices[0].id)
# voice[0].id = Male voice 
# voice[1].id = Female voice

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()                  #Without this command, speech will not be audible to us.

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("I am Jarvis Tell me how may I help you Sir")

def takeCommand():
    '''It takes microphone input from the user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')      #Using google for voice recognition.
        print(f"User said: {query}\n")                           #User query will be printed.
    
    except Exception as e:
        # print(e)    
        print("Please say that again...")                        #Say that again will be printed in case of improper voice 
        return "None"                                            #None string will be returned
    return query
 
#def sendEmail(to, content):
#    server = smtplib.SMTP('smtp.gmail.com', 587)
#    server.ehlo()
#    server.starttls()
#    server.login('youremail@gmail.com', 'your-password')
#    server.sendmail('youremail@gmail.com', to, content)
#    server.close()

if __name__ == "__main__":
    #speak("Hi Master, What a nice day")
    WishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
        #logic for executing yask based on query

        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            #print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            subprocess.call("C:\Program Files\Google\Chrome\Application\\chrome.exe")
            subprocess.Popen("C:\Program Files\Google\Chrome\Application\\chrome.exe")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Mohammed Salman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(codePath)
        
        #elif 'send email' in query:
        #    try:
        #        speak("What should I say?")
        #        content = takeCommand()
        #        to = "harryyourEmail@gmail.com" 
        #        sendEmail(to, content)
        #        speak("Email has been sent!")
        #    except Exception as e:
        #        print(e)
        #        speak("Sorry Bhai. I am not able to send this email") 

        #elif 'open  chrome' in query:
        #    codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        #    os.startfile(codePath)


        elif 'shut up' in query:                            #to exit from the program
            break                           
