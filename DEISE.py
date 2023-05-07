import speech_recognition as sr
import pyttsx3
from art import *
import os
import time
import datetime
import keyboard as kb
import psutil

SysName = "DEISE" #Daniel Especialista Inteligente de Serviço Espetacular (Daniel É Inteligente Sem Esforço)
UserName = "Senhor Daniel"

print("Loading DEISE system...")

#Inicializando e configurando o mecanismo de voz do programa
engine = pyttsx3.init()
voice = engine.getProperty('voices') #get the available voices
#eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
engine.setProperty('voice', voice[0].id) #changing voice to index 1 for female voice

tprint("Welcome   Mr.   Daniel")

engine.say(f"Olá {UserName}! seja bem vindo!")
engine.runAndWait()
engine.stop()

#Funções

def TabelaJogos():
    print("Jogo\t\tNúmero")
    print(30*"-")
    print("Brawlhalla\t\t1")
    print("Minecraft\t\t2")
    print("Valorant\t\t3")
    #print("%s:\t\t\t%f" % "Minecraft", "2")
    print(30*"-")

def DEISE_():

    print("...")

    time.sleep(0.3)
        
    audio = rec.listen(mic)
        
    try:
            
        fala_entrada = rec.recognize_google(audio, language="pt-BR")

        texto = fala_entrada

        #texto = "texto"

        texto = texto.capitalize()
        print("O senhor(a) disse:")
        print(texto)

        texto = texto.lower()

        if texto == "descansar":

            time.sleep(1)    
                
            engine.say(f"Até a próxima {UserName}, precisando, é só me chamar")
            engine.runAndWait()
            engine.stop()

            time.sleep(1)
                
            exit()

        if texto == "olá" or texto == "oi" or texto == "oi deise":
                
            engine.say(f"Olá {UserName}, estou aqui para ajudar, precisando de algo é só pedir!")
            engine.runAndWait()
            engine.stop()

        if texto == "quem é você":
                
                engine.say(f"Eu sou a {SysName}, o meu nome significa Especialista Inteligente de Serviço Espetacular do Daniel e existo para ajudá-lo!")
                engine.runAndWait()
                engine.stop()

        if texto == "alpha" or texto == "alfa":

            engine.say("BOTS!!!")
            engine.runAndWait()
            engine.stop()

        if texto == "status da bateria" or texto == "deise qual o status da bateria" or texto == "deise qual é o status da bateria":
            
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
            
        if texto == "vamos jogar":

            engine.say(f"{UserName}, qual jogo gostaria de jogar? Insira um valor numérico conforme a tabela a seguir")
            engine.runAndWait()
            engine.stop()

            TabelaJogos()

            jogo = int(input())

            if jogo == 1:
                os.startfile(r"steam://rungameid/291550")
                print("Iniciando Brawlhalla...")
            if jogo == 2:
                os.startfile(r"C:\Users\danip\AppData\Roaming\.minecraft\TLauncher.exe")
                print("Iniciando Minecraft...")
            if jogo == 3:
                os.startfile(r"C:\Riot Games\Riot Client\RiotClientServices.exe --launch-product=valorant --launch-patchline=live")
                print("Iniciando Valorant...")
                

        if texto == "abrir google" or texto == "abrir o google" or texto == "abrir o chrome" or texto == "abrir chrome":
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

        if texto == "abrir visual studio code" or texto == "abrir o visual studio code":
            os.startfile(r"C:\Users\danip\AppData\Local\Programs\Microsoft VS Code\Code.exe")

            engine.say(f"Programa Visual Studio Code aberto, conforme as suas ordens {UserName}")
            engine.runAndWait()
            engine.stop()                

        pesquisa1 = texto.split()

        #Descobrir o modelo de URL do Google Imagens e arrumar essa parte do código comentada para conseguir abrir 
        if pesquisa1[0] == "pesquisar" and pesquisa1[1] == "imagem":

            pesquisa1.pop(0)
            pesquisa1.pop(1)

            pesquisa2 = "+".join(pesquisa1)

            pesquisa_img = pesquisa2

            url_img = r"https://www.google.com/search?tbm=isch&q="+str(pesquisa_img)
            
            os.system(f"start {url_img}")

        if pesquisa1[0] == "pesquisar" or pesquisa1[0] == "search":

            pesquisa1.pop(0)

            pesquisa2 = "+".join(pesquisa1) 

            url = "https://www.google.com/search?q="+str(pesquisa2)

            os.system(f'start {url}')

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

        if texto == "limpar registros":

            os.system("cls")

            engine.say(f"Registros limpados com sucesso {UserName}!")
            engine.runAndWait()
            engine.stop()

            tprint("Welcome   Mr.   Daniel")

        if texto == "encerrar o expediente" or texto == "encerrar expediente":

            engine.say(f"Desligando o sistema, até a próxima {UserName}")
            engine.runAndWait()
            engine.stop()
            
            time.sleep(3)
            
            os.system("shutdown /s /t 1")
                
    except Exception as e:
        return "None"
    
rec = sr.Recognizer()
#print(sr.Microphone().list_microphone_names())
with sr.Microphone(device_index=0) as mic:
        rec.adjust_for_ambient_noise(mic)

        while True:

                DEISE_()
