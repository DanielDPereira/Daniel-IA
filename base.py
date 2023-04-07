import speech_recognition as sr
import pyttsx3
from art import *
import os

rec = sr.Recognizer()
#print(sr.Microphone().list_microphone_names())
with sr.Microphone(device_index=0) as mic:
    rec.adjust_for_ambient_noise(mic)
    #print("Pode falar que eu vou gravar")
    tprint("WELCOME MR. DANIEL")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)

if texto == "Olá":
    
    engine = pyttsx3.init()
    voice = engine.getProperty('voices') #get the available voices
    #eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
    engine.setProperty('voice', voice[1].id) #changing voice to index 1 for female voice

    engine.say("Olá Daniel, seja bem vindo!")
    engine.runAndWait()
    engine.stop()

input()
