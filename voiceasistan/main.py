from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import pyaudio
import os
import time
from datetime import datetime
import random
from random import choice
import webbrowser

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            print("Asistan : Sistem çalışmıyor")
        return voice

def response(voice):
    if "merhaba" in voice:
        speak("sana da merhaba")
    if "selam" in voice:
        speak("sana 3000 kere selam olsun")
    if "teşekkür ederim" in voice or "teşekkürler" in voice:
        speak("rica ederim efendim")
    if "görüşürüz" in voice or "güle güle" in voice or "kapat" in voice:
        speak("görüşürüz kendine iyi bak")
        exit()
    if "bugün günlerden ne" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"
        elif today == "Tuesday":
            today ="Salı"
        elif today == "Wednesday":
            today ="Çarşamba"
        elif today == "Thursday":
            today ="Perşembe"
        elif today == "Friday":
            today ="Cuma"
        elif today == "Saturday":
            today ="Cumartesi"
        elif today == "Sunday":
            today ="Pazar"
        speak(today)
    if "saat kaç" in voice:
        selection = ["saat şu an: ", "hemen bakıyorum: "]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection + clock)
    if "google'da ara" in voice:
        speak("ne aramamı istersin")
        search = record()
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        speak("{} bulduklarımı listeliyiyorum.".format(search))
    if "not et" in voice:
        speak("dosya ismi ne olsun?")
        txtFile = record() + ".txt"
        speak("lütfen kaydediceğin şeyleri söyle kayıta başlıyorum.")
        theText = record()
        f = open(txtFile, "w",encoding="utf-8")
        f.writelines(theText)
        speak("kayıt başarılı")
        f.close()



def speak(string):
    tts = gTTS(text=string,lang="tr")
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

#speak("Selam Hoşgeldin")
playsound("HOME.mp3")

while True:
    voice = record()
    if voice !='':
        voice = voice.lower()
        print(voice)
        response(voice)

