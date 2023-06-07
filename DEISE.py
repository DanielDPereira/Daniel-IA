import speech_recognition as sr
import pyttsx3
from art import *
import os
import time
import datetime
from tkinter import *
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

engine.say(f"Olá {UserName}! Seja bem vindo!")
engine.runAndWait()
engine.stop()

#Funções que podem ser usadas no programa

def TabelaJogos():
    print("Jogo\t\tNúmero")
    print(30*"-")
    print("Brawlhalla\t\t1")
    print("Minecraft\t\t2")
    print("Valorant\t\t3")
    #print("%s:\t\t\t%f" % "Minecraft", "2")
    print(30*"-")
    
def calculadora():

    win = Tk() # This is to create a basic window
    win.geometry("312x324")  # this is for the size of the window 
    win.resizable(0, 0)  # this is to prevent from resizing the window
    win.title("Calculatora")

    ###################Starting with functions ####################
    # 'btn_click' function : 
    # This Function continuously updates the 
    # input field whenever you enter a number

    def btn_click(item):
        global expression
        expression = expression + str(item)
        input_text.set(expression)

        # 'bt_clear' function :This is used to clear 
        # the input field

    def bt_clear(): 
        global expression 
        expression = "" 
        input_text.set("")

    # 'bt_equal':This method calculates the expression 
    # present in input field

    def bt_equal():
        global expression
        result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
        input_text.set(result)
        expression = ""

    expression = ""

    # 'StringVar()' :It is used to get the instance of input field

    input_text = StringVar()

    # Let us creating a frame for the input field

    input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)

    input_frame.pack(side=TOP)

    #Let us create a input field inside the 'Frame'

    input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)

    input_field.grid(row=0, column=0)

    input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field

    #Let us creating another 'Frame' for the button below the 'input_frame'

    btns_frame = Frame(win, width=312, height=272.5, bg="grey")

    btns_frame.pack()

    # first row

    clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

    divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

    # second row

    seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)

    eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)

    nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)

    multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

    # third row

    four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)

    five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)

    six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)

    minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

    # fourth row

    one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)

    two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)

    three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)

    plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

    # fourth row

    zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)

    point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)

    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

    win.mainloop()

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
        print(entrada_lista)

        if texto_entrada == "descansar":

            time.sleep(1)    
                
            engine.say(f"Até a próxima {UserName}, precisando, é só me chamar")
            engine.runAndWait()
            engine.stop()

            time.sleep(1)
                
            exit()

        if "olá" in entrada_lista or "oi" in entrada_lista or len(entrada_lista) == 1 and entrada_lista[0] == "deise":
                
            engine.say(f"Olá {UserName}, estou aqui para ajudar, precisando de algo é só pedir!")
            engine.runAndWait()
            engine.stop()

        if texto_entrada == "quem é você":
                
                engine.say(f"Eu sou a {SysName}, o meu nome significa Especialista Inteligente de Serviço Espetacular do Daniel e existo para ajudá-lo!")
                engine.runAndWait()
                engine.stop()

        if texto_entrada == "alpha" or texto_entrada == "alfa":

            engine.say("BOTS!!!")
            engine.runAndWait()
            engine.stop()

        if "status" and "bateria" in entrada_lista:
            
            bateria = psutil.sensors_battery()
            percentual_bateria = str(bateria.percent)
            
            engine.say(f"{UserName}, o sistema está com um total de {percentual_bateria}% de bateria!")
            engine.runAndWait()
            engine.stop()

        if texto_entrada == "que horas são":

            hora = datetime.datetime.now()

            hora = str(hora).split()
            hora = hora[1]
            hora = hora.split(":")
            hora = hora[0] + " horas e " + hora[1] + " minutos"
            
            engine.say(f"Agora são {hora} {UserName}")
            engine.runAndWait()
            engine.stop()
            
        if texto_entrada == "vamos jogar":

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
            
            if jogo == 2:
                os.startfile(r"C:\Users\danip\AppData\Roaming\.minecraft\TLauncher.exe")
                print("Iniciando Minecraft...")

                engine.say(f"{UserName} o jogo Minecraft está sendo iniciado")
                engine.runAndWait()
                engine.stop()
            
            '''   
            if jogo == 3:
                os.startfile(r"C:\Riot Games\Riot Client\RiotClientServices.exe --launch-product=valorant --launch-patchline=live")
                print("Iniciando Valorant...")

                engine.say(f"{UserName} o jogo Valorant está sendo iniciado")
                engine.runAndWait()
                engine.stop()
            '''
             
        if "abrir" or "inciar" and "calculadora" in entrada_lista:
            
            calculadora()

            engine.say(f"Calculadora aberta, conforme as suas ordens {UserName}")
            engine.runAndWait()
            engine.stop()

        if "abrir" or "inciar "and "google" in entrada_lista:
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

            engine.say(f"Programa Google Chrome aberto, conforme as suas ordens {UserName}")
            engine.runAndWait()
            engine.stop()

            #"C:\Users\danip\AppData\Local\Programs\Microsoft VS Code\Code.exe"

        if "abrir" or "executar" or "iniciar" in entrada_lista and "spotify" in entrada_lista or texto_entrada == "abrir o spotify":
            os.startfile(r"C:\Users\danip\AppData\Roaming\Spotify\Spotify.exe")

            engine.say(f"Programa Spotify aberto, conforme as suas ordens {UserName}")
            engine.runAndWait()
            engine.stop()

        if texto_entrada == "abrir visual studio code" or texto_entrada == "abrir o visual studio code":
            os.startfile(r"C:\Users\danip\AppData\Local\Programs\Microsoft VS Code\Code.exe")

            engine.say(f"Programa Visual Studio Code aberto, conforme as suas ordens {UserName}")
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

        if pesquisa1[0] == "abrir" and pesquisa1[1] == "site" or pesquisa1[1] == "url":

            pesquisa1.pop(0)
            pesquisa1.pop(0)

            url = pesquisa1[0]

            os.system(f"start https://www.{url}")

            engine.say(f"{UserName}, o site {pesquisa1} foi aberto com sucesso!")
            engine.runAndWait()
            engine.stop()
            
        if "obrigado" or "valeu" in entrada_lista:
            
            engine.say(f"Por nada {UserName}, precisando é só me chamar")
            engine.runAndWait()
            engine.stop()

        if texto_entrada == "limpar registros":

            os.system("cls")

            engine.say(f"Registros limpados com sucesso {UserName}!")
            engine.runAndWait()
            engine.stop()

            tprint("Welcome   Mr.   Daniel")

        if texto_entrada == "encerrar o expediente" or texto_entrada == "encerrar expediente":

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
