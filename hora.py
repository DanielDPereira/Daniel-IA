import datetime

hora = datetime.datetime.now()

hora = str(hora).split()

hora = hora[1]
hora = hora.split(":")

print(hora)
