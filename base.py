import speech_recognition as sr
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

    if texto == "Olá" or "olá":
        print("Olá capitão")

input()
