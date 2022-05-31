import datetime
from datetime import *
from time import sleep

horario = "15:30"
dia =  "31/05"
objetivo = horario+" "+dia
datahoje = datetime.now()

hora = datetime.strptime(objetivo, "%H:%M %d/%m")
hora = hora.replace(year=datahoje.year)
print(f"Data armazenada: {str(hora)}")
print(f"Data atual: {str(datahoje)}")


# --------------------------------------------------
deltatempo = hora-datahoje
print(deltatempo.total_seconds())

if deltatempo.total_seconds() < 0:
    print("---------------------------")
    print("Impossível guardar lembrete! O horário expirou.")
    print("---------------------------")
else:
    print("---------------------------")
    print("O lembrete foi ativado!")
    sleep(deltatempo.total_seconds())
    print("Funfo")
#     while deltatempo.total_seconds() > 0:
#         datahoje = datetime.now() 

#         if deltatempo.total_seconds() < 0:
#             print(f"Lembrete marcado para dia {hora}! @everyone")
#         else:
#             print(deltatempo.total_seconds())
#             datahoje = datetime.now()
#             continue
#     print("---------------------------")

# print(hora-datahoje)
# print(deltatempo)
# print(deltatempo.total_seconds())

# sleep(deltatempo.total_seconds())
# print("@everyone")
# print("---------------------------")