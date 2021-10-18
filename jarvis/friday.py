import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import time
import subprocess
import wolframalpha
import json
import requests
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import smtplib, ssl
from mail_infos import password



engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good morning sir")
        speak("The current time is")
        time()
        speak("Today is")
        date()
        speak("I'm at your service. How can i help you?")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir")
        speak("The current time is")
        time()
        speak("Today is")
        date()
        speak("I'm at your service. How can i help you?")
    elif hour >= 18 and hour <24:
        speak("Good evening sir")
        speak("The current time is")
        time()
        speak("Today is")
        date()
        speak("I'm at your service. How can i help you?")
    else:
        speak("Good night sir")
        speak("The current time is")
        time()
        speak("Today is")
        date()
        speak("I'm at your service. How can i help you?")


class WhatsApp():
    def __init__(self):
        self.driver = webdriver.Chrome()
        sleep(3)
        self.driver.maximize_window()
        self.driver.get('https://web.whatsapp.com/')

        name = False
        while True:
            try:
                speak("Whom should I send message?")
                name = takeCommand().title()
                wait = WebDriverWait(self.driver, 30)
                user = wait.until(lambda driver: self.driver.find_element_by_xpath("//span[@title='{}']".format(name)))
                user.click()

                message = False
                while True:
                    try:
                        speak("What should i say?")
                        message = takeCommand()
                        wait = WebDriverWait(self.driver, 30)
                        write_message = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'))
                        write_message.send_keys(message)
                        wait = WebDriverWait(self.driver, 30)
                        send_button = wait.until(lambda driver: self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button'))
                        send_button.click()
                        speak(f"Message has been sent successfully")
                        if "exit" in query:
                            break
                        else:
                            continue

                    except Exception as e:
                        print(e)
                        speak("Say that again")
                        if "exit" in query:
                            break
                        else:
                            continue

            except Exception as e:
                speak("Say that again")
                if "exit" in query:
                    break
                else:
                    continue


def sendEmail():
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "salimkarsanbas@gmail.com"
    receiver_email = "karsanbassalim@gmail.com"
    speak("What should I say?")
    message = takeCommand()

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        speak("Email has been sent!")
    except Exception as e:
        # Print any error messages to stdout
        print(e)
        speak("Sorry. I am not able to send this email")
    finally:
        server.quit()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"You said: {query}\n")  #User query will be printed.

    except Exception as e:
        print(e)    
        speak("Say that again please...")
        return None
    return query

if __name__=="__main__" :
    while True:
        query = takeCommand() #Converting user query into lower case

        if query:
            if 'hello' in query or 'halo' in query or 'hi' in query or 'good morning' in query or 'good afternoon' in query or 'good evening' in query or 'good night' in query:
                wishMe()

            elif 'wikipedia' in query:  
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2) 
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'whatsapp' in query or "send message" in query or "wazzap" in query or "what's up" in query:
                bot = WhatsApp()

            elif 'open youtube' in query or 'youtube' in query:
                driver = webdriver.Chrome()
                driver.get("https://www.youtube.com/")
            
            elif 'open google' in query:
                driver = webdriver.Chrome()
                driver.get("https://www.google.com/")
            
            # elif 'play music' in query.lower:
            #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            #     songs = os.listdir(music_dir)
            #     print(songs)    
            #     os.startfile(os.path.join(music_dir, songs[0]))

            elif 'time' in query:
                time()

            # elif 'open code' in query.lower():
            #     codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            #     os.startfile(codePath)

            elif 'email' in query:
                sendEmail()

            elif "good bye" in query or "ok bye" in query or "stop" in query or "mute" in query or "exit" in query:
                speak('Good bye sir')
                break

            else:
                speak("Say that again please")

        