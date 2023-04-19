import speech_recognition as sr
import pyttsx3
from art import *
import os
import time
import datetime
import keyboard as kb
import psutil

SysName = "DEISE" #Daniel Especialista Inteligente de Serviço Especial
UserName = "Senhor Daniel"

print("Loading DEISE system...")

#Inicializando e configurando o mecanismo de voz do programa
engine = pyttsx3.init()
voice = engine.getProperty('voices') #get the available voices
#eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
engine.setProperty('voice', voice[0].id) #changing voice to index 1 for female voice

tprint("Welcome   Mr.   Daniel")

"""
engine.say(f"Olá {UserName}! Eu sou a {SysName}, sua assistente pessoal e estou aqui para te ajudar")
engine.runAndWait()
engine.stop()
"""

def DEISE_():

        #print("Pode falar que eu vou gravar")

        print("...")

        time.sleep(0.3)
        
        audio = rec.listen(mic)
        
        try:
            
            texto = rec.recognize_google(audio, language="pt-BR")

            texto = texto.capitalize()
            print("O senhor(a) disse:")
            print(texto)

            texto = texto.lower()

            if texto == "olá" or texto == "oi":
                
                engine.say(f"Olá {UserName}, seja bem vindo!")
                engine.runAndWait()
                engine.stop()

            if texto == "quem é você":
                
                engine.say(f"Eu sou a {SysName}, o meu nome significa Especialista Inteligente de Serviço Especial do Daniel e existo para ajudá-lo!")
                engine.runAndWait()
                engine.stop()

            if texto == "alpha" or texto == "alfa":

                engine.say("BOTS!!!")
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

                #"C:\Users\danip\AppData\Local\Programs\Microsoft VS Code\Code.exe"

            if texto == "abrir spotify" or texto == "abrir o spotify":
                os.startfile(r"C:\Users\danip\AppData\Roaming\Spotify\Spotify.exe")

                engine.say(f"Programa Spotify aberto, conforme as suas ordens {UserName}")
                engine.runAndWait()
                engine.stop()

            pesquisa1 = texto.split()

            if pesquisa1[0] == "pesquisar" or pesquisa1[0] == "search":

                pesquisa1.pop(0)

                pesquisa2 = "+".join(pesquisa1) 

                url = "https://www.google.com/search?q="+str(pesquisa2)

                os.system(f"start {url}")

                engine.say(f"{UserName}, pesquisa {pesquisa1} aberta com sucesso!")
                engine.runAndWait()
                engine.stop()

            if pesquisa1[0] == "abrir" and pesquisa1[1] == "site" or pesquisa1[1] == "url":

                pesquisa1.pop(0)
                pesquisa1.pop(0)

                url = pesquisa1[0]

                os.system(f"start https://www.{url}")

                engine.say(f"{UserName}, o site {pesquisa1} foi aberto com sucesso!")
                engine.runAndWait()
                engine.stop()

            #if
                #https://www.google.com.br/search?q={pesquisa_img}&hl=pt-PT&authuser=0&tbm=isch&sxsrf=APwXEdf9Yrp3qrP3T0qfiPVe8QXkYrxwcg%3A1681901722200&source=hp&biw=1366&bih=663&ei=msg_ZJ6vCrSJ1sQP3veJwAM&iflsig=AOEireoAAAAAZD_WqrbxVfUsC4H5L4O4XilGz7YWVJ9y&ved=0ahUKEwie5MmV5LX-AhW0hJUCHd57AjgQ4dUDCAc&uact=5&oq={pesquisa_img}&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEOoCECc6BAgjECdQ_wZYmRJg5BVoAXAAeACAAWyIAbYEkgEDNC4ymAEAoAEBqgELZ3dzLXdpei1pbWewAQo&sclient=img

            if texto == "encerrar o expediente":

                engine.say(f"Desligando o sistema, até a próxima {UserName}")
                engine.runAndWait()
                engine.stop()
                
                os.system("shutdown /s /t 1")

        except Exception as e:
            return "None"

    
rec = sr.Recognizer()
#print(sr.Microphone().list_microphone_names())
with sr.Microphone(device_index=0) as mic:
        rec.adjust_for_ambient_noise(mic)

        while True:

                DEISE_()
