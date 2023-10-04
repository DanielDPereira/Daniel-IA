import speech_recognition as sr
import pyttsx3
from art import *
import os
import time
import datetime
from tkinter import *
import keyboard as kb
import psutil

SysName = "DEISE" #Daniel Especialista Inteligente de Serviço Espetacular #Daniel Artificial Inteligence System Integrated #Daniel É Inteligente Sem Esforço
UserName = "Senhor Daniel"

print("Loading DEISE system...")

#Inicializando e configurando o mecanismo de voz do programa
engine = pyttsx3.init()
voice = engine.getProperty('voices') #get the available voices
#eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
engine.setProperty('voice', voice[0].id) #changing voice to index 1 for female voice

tprint("Welcome   Mr.   Daniel")

engine.say(f"Olá {UserName}! Seja bem vindo!")
engine.runAndWait()
engine.stop()

#Funções que podem ser usadas no programa

def HoraAtual():
    hora = datetime.datetime.now()

    hora = str(hora).split()
    hora = hora[1]
    hora = hora.split(":")
    
    hora = hora[0]
    minuto = hora[1]
    
    return f"{hora} horas e {minuto} minutos"

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

        texto_entrada = fala_entrada
        
        #texto_entrada = "<teste>"
        
        texto_entrada = texto_entrada.capitalize()
        
        print("O senhor(a) disse:")
        print(texto_entrada)

        texto_entrada = texto_entrada.lower()
        
        entrada_lista = texto_entrada.split(" ")
        
        #print(entrada_lista)

        if texto_entrada == "descansar":

            time.sleep(1)    

            print(f"Até a próxima {UserName}, precisando, é só me chamar")
                
            engine.say(f"Até a próxima {UserName}, precisando, é só me chamar")
            engine.runAndWait()
            engine.stop()

            time.sleep(1)
                
            exit()

        elif "olá" in entrada_lista or "oi" in entrada_lista or len(entrada_lista) == 1 and entrada_lista[0] == "deise":
                
            engine.say(f"Olá {UserName}, estou aqui para ajudar, precisando de algo é só pedir!")
            engine.runAndWait()
            engine.stop()

        elif texto_entrada == "quem é você":

                print(f"Eu sou a {SysName}, o meu nome significa Especialista Inteligente de Serviço Espetacular do Daniel e existo para ajudá-lo!")
    
                engine.say(f"Eu sou a {SysName}, o meu nome significa Especialista Inteligente de Serviço Espetacular do Daniel e existo para ajudá-lo!")
                engine.runAndWait()
                engine.stop()

        elif texto_entrada == "alpha" or texto_entrada == "alfa":

            engine.say("BOTS!!!")
            engine.runAndWait()
            engine.stop()

        elif "status" and "bateria" in entrada_lista:
            
            bateria = psutil.sensors_battery()
            percentual_bateria = str(bateria.percent)

            print(f"{UserName}, o sistema está com um total de {percentual_bateria}% de bateria!")
            
            engine.say(f"{UserName}, o sistema está com um total de {percentual_bateria}% de bateria!")
            engine.runAndWait()
            engine.stop()

        elif texto_entrada == "que horas são":

            agora = HoraAtual()
            
            print(f"agora são {agora}, {UserName}")
                        
            engine.say(f"agora são {agora}, {UserName}")
            engine.runAndWait()
            engine.stop()
            
        elif texto_entrada == "vamos jogar":

            engine.say(f"{UserName}, qual jogo gostaria de jogar? Insira um valor numérico conforme a tabela a seguir")
            engine.runAndWait()
            engine.stop()

            TabelaJogos()

            jogo = int(input())

            if jogo == 1:
                os.startfile(r"steam://rungameid/291550")
                print("Iniciando Brawlhalla...")

                engine.say(f"{UserName} o jogo Brawlhalla está sendo iniciado")
                engine.runAndWait()
                engine.stop()
            
            elif jogo == 2:
                os.startfile(r"C:\Users\danip\AppData\Roaming\.minecraft\TLauncher.exe")
                print("Iniciando Minecraft...")

                engine.say(f"{UserName} o jogo Minecraft está sendo iniciado")
                engine.runAndWait()
                engine.stop()
            
            '''   
            elif jogo == 3:
                os.startfile(r"C:\Riot Games\Riot Client\RiotClientServices.exe --launch-product=valorant --launch-patchline=live")
                print("Iniciando Valorant...")

                engine.say(f"{UserName} o jogo Valorant está sendo iniciado")
                engine.runAndWait()
                engine.stop()
            '''

        elif "abrir" in entrada_lista or "inciar" in entrada_lista or "abra" in entrada_lista or "executar" in entrada_lista:

            if "google" in entrada_lista or "chrome" in entrada_lista:
                os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

                engine.say(f"Programa Google Chrome aberto com sucesso, conforme as suas ordens {UserName}")
                engine.runAndWait()
                engine.stop()

            elif "spotify" in entrada_lista or texto_entrada == "abrir o spotify":
                os.startfile(r"C:\Users\danip\AppData\Roaming\Spotify\Spotify.exe")

                engine.say(f"Programa Spotify aberto com sucesso, conforme as suas ordens {UserName}")
                engine.runAndWait()
                engine.stop()

            elif "visual" in entrada_lista and "studio" in entrada_lista:
                os.startfile(r"C:\Users\danip\AppData\Local\Programs\Microsoft VS Code\Code.exe")

                engine.say(f"Programa Visual Studio Code aberto com sucesso, conforme as suas ordens {UserName}")
                engine.runAndWait()
                engine.stop()

            elif "whatsapp" in entrada_lista or "zap" in entrada_lista and "zap" in entrada_lista:
                os.system(f'start https://web.whatsapp.com/')

                engine.say(f"Whatsapp aberto com sucesso, conforme as suas ordens {UserName}")
                engine.runAndWait()
                engine.stop()

        pesquisa1 = texto_entrada.split()

        if pesquisa1[0] == "pesquisar" or pesquisa1[0] == "search":

            pesquisa1.pop(0)

            pesquisa2 = "+".join(pesquisa1) 

            url = "https://www.google.com/search?q="+str(pesquisa2)

            os.system(f'start {url}')

            engine.say(f"{UserName}, pesquisa {pesquisa1} aberta com sucesso!")
            engine.runAndWait()
            engine.stop()

        elif pesquisa1[0] == "abrir" and pesquisa1[1] == "site" or pesquisa1[1] == "url":

            pesquisa1.pop(0)
            pesquisa1.pop(0)

            url = pesquisa1[0]

            os.system(f"start https://www.{url}")

            engine.say(f"{UserName}, o site {pesquisa1} foi aberto com sucesso!")
            engine.runAndWait()
            engine.stop()
            
        elif "obrigado" in entrada_lista or "valeu" in entrada_lista:
            
            engine.say(f"Por nada {UserName}, precisando é só me chamar")
            engine.runAndWait()
            engine.stop()

        elif texto_entrada == "limpar registros":

            os.system("cls")

            engine.say(f"Registros limpados com sucesso {UserName}!")
            engine.runAndWait()
            engine.stop()

            tprint("Welcome   Mr.   Daniel")

        elif texto_entrada == "encerrar o expediente" or texto_entrada == "encerrar expediente":

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
