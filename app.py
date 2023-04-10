import speech_recognition as sr
import pyttsx3
from art import *
import os
import datetime

#Inicializando e configurando o mecanismo de voz do programa
engine = pyttsx3.init()
voice = engine.getProperty('voices') #get the available voices
#eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
engine.setProperty('voice', voice[0].id) #changing voice to index 1 for female voice

rec = sr.Recognizer()
#print(sr.Microphone().list_microphone_names())
with sr.Microphone(device_index=0) as mic:
    rec.adjust_for_ambient_noise(mic)
    #print("Pode falar que eu vou gravar")

    '''
    engine.say("Olá Daniel! Eu sou o seu sistema de assistência personalizado e estou aqui para te ajudar")
    engine.runAndWait()
    engine.stop()
    '''

    tprint("WELCOME MR. DANIEL")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")

    texto = texto.capitalize()
    print("O senhor disse:")
    print(texto)

    texto = texto.lower()

if texto == "olá" or texto == "oi":
    
    engine.say("Olá Daniel, seja bem vindo!")
    engine.runAndWait()
    engine.stop()

if texto == "que horas são":

    hora = datetime.datetime.now()

    hora = str(hora).split()
    hora = hora[1]
    hora = hora.split(":")
    hora = hora[0] + " horas e " + hora[1] + " minutos"
    
    engine.say("Agora são " + hora + " senhor Daniel")
    engine.runAndWait()
    engine.stop()

if texto == "abrir google":
    os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

    engine.say("Programa Google Chrome aberto, conforme as suas ordens senhor Daniel")
    engine.runAndWait()
    engine.stop()

if texto == "abrir spotify":
    os.startfile(r"C:\Users\danip\AppData\Roaming\Spotify\Spotify.exe")

    engine.say("Programa Spotify aberto, conforme as suas ordens senhor Daniel")
    engine.runAndWait()
    engine.stop()

if texto == "encerrar o expediente":

    engine.say("Até a próxima chefia")
    engine.runAndWait()
    engine.stop()
    
    os.system("shutdown /s /t 1")

input()
