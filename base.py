import speech_recognition as sr

rec = sr.Recognizer()
print(sr.Microphone().list_microphone_names())
with sr.Microphone(device_index=0) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar que eu vou gravar")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)

    if texto == "Olá" or "olá":
        print(1+1)
