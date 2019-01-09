import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from selenium import webdriver
from time import sleep
import sys

temp=0;
def speak(audioString):
    print("\n\t\t\t\tJ.A.R.V.I.S Reporting Sir")
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("audio.mp3")





def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
    	r.adjust_for_ambient_noise(source)
    	print("Say something sir!")
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        speak("Google Speech Recognition could not understand audio")
        sleep(5)
        pass
        
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service")
        speak("Could not connect")
        sleep(5)
        exit()

    return data


def jar(con):
    if "how are you" in con:
        speak("I am fine")
 	return (2)
    elif "locate me" in con:
        con = con.split(" ")
        location = con[2]
        speak("Hold on sir, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

    elif "who are you" in con:
        speak("i'm your assistant sir")
    	return (5)
    elif "what time is it" in con:
        speak(ctime())
        return (8)
    elif "WhatsApp" in con:
        speak("Just searching for answers to life's")
        return (5)
    elif "bye" in con:
        speak("have a nice day sir")
       	exit(0)
    elif "tell me a joke" in con:
    	speak("What did one snowman say to the other? , Do you smell carrots?")
    	return(6)
    elif "hello" in con:
        speak("hi sir , what can i do for you")
        return (5)
    
    elif "shut up" in con:
        speak("sorry sir for disturb , have a nice day")
        sys.exit()
       


time.sleep(2)
speak("Hi sir, Say something")
time.sleep(1)

if temp==0:
    while 1:
        try:
            data=recordAudio()
            t=jar(data)
            time.sleep(t)
        
        except SystemExit:
            exit(0)

        except:
            speak("Could not recognize")
            print("Could not recognize")
            data=""
            time.sleep(6)
        pass
else:
    exit(0)