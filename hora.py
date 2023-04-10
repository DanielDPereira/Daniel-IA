import datetime

hora = datetime.datetime.now()

hora = str(hora).split()
hora = hora[1]
hora = hora.split(":")
hora = hora[0] + " horas e " + hora[1] + " minutos"

print(hora)
