import speech_recognition as sr
import pyttsx3
from art import *
import os
import datetime
import keyboard as kb
import psutil

SysName = "DAISE" #Daniel Asistente Inteligente de Serviço Especial
UserName = "Senhor Daniel"

def DAISE_():
    
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
        engine.say(f"Olá {UserName}! Eu sou a {SysName}, seu assistente pessoal e estou aqui para te ajudar")
        engine.runAndWait()
        engine.stop()
        '''

        tprint("Welcome   Mr.   Daniel")
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language="pt-BR")

        texto = texto.capitalize()
        print("O senhor(a) disse:")
        print(texto)

        texto = texto.lower()

    if texto == "olá" or texto == "oi":
        
        engine.say(f"Olá {UserName}, seja bem vindo!")
        engine.runAndWait()
        engine.stop()

    if texto == "status da bateria":
        
        bateria = psutil.sensors_battery()
        percentual_bateria = str(bateria.percent)
        
        engine.say(f"{UserName}, o sistema está com um total de {percentual_bateria}% de bateria!")
        engine.runAndWait()
        engine.stop()

    if texto == "que horas são":

        hora = datetime.datetime.now()

        hora = str(hora).split()
        hora = hora[1]
        hora = hora.split(":")
        hora = hora[0] + " horas e " + hora[1] + " minutos"
        
        engine.say(f"Agora são {hora} {UserName}")
        engine.runAndWait()
        engine.stop()

    if texto == "abrir google" or texto == "abrir o google" or texto == "abrir o chrome":
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

        engine.say(f"Programa Google Chrome aberto, conforme as suas ordens {UserName}")
        engine.runAndWait()
        engine.stop()

    if texto == "abrir spotify" or texto == "abrir o spotify":
        os.startfile(r"C:\Users\danip\AppData\Roaming\Spotify\Spotify.exe")

        engine.say(f"Programa Spotify aberto, conforme as suas ordens {UserName}")
        engine.runAndWait()
        engine.stop()

    if texto == "encerrar o expediente":

        engine.say(f"Desligando o sistema, até a próxima {UserName}")
        engine.runAndWait()
        engine.stop()
        
        os.system("shutdown /s /t 1")

while True:
    DAISE_()

input()
