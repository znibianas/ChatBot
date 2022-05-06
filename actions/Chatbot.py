import os
from _ast import Import
from datetime import datetime

import pygame
from pygame import mixer
import requests
import speech_recognition as sr
import subprocess
from playsound import playsound
from gtts import gTTS


bot_message = ""
message = ""

#myobj = gTTS(text="Hello I am ABDELALI HLAILI Speak Anything I am Listening", lang='fr', tld='com.au')
#myobj.save("starting.mp3")
#playsound("starting.mp3")


# r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})
#
# print("Bot says, ", end=' ')
# for i in r.json():
#     bot_message = i['text']
#     print(f"{bot_message}")
#
#     myobj = gTTS(text=bot_message)
#     myobj.save("welcome.mp3")
#     print('saved')
#
#     subprocess.call(['mpg321', 'C:/Users/user/firstchatbot/actions/welcome.mp3', '--play-and-exit'])
#


while bot_message != "Bye" or bot_message!='thanks':
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything:")
        audio = r.listen(source)
        try:
            message = r.recognize_google(audio, language="fr-FR")
            print("You said: {}".format(message))

        except:
            print("Sorry could not recognize your voice")

    if len(message)==0:
        continue
    print("Sending message now...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    print("Bot says, ", end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

        myobj = gTTS(text=bot_message, lang="fr")
        date_string = datetime.now().strftime("%d%m%Y%H%M%S%f")
        filename = "voice" + date_string + ".mp3"
        myobj.save(filename)
        print('saved')
        #playsound("welcome.mp3")
        #os.remove("C:/Users/user/firstchatbot/actions/welcome.mp3")
        #subprocess.call(['vlc', 'welcome.mp3', '--play-and-exit'])
        pygame.init()
        mixer.music.load(filename)
        mixer.music.play(0)


