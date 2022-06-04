import datetime
from datetime import *
from calendar import isleap

horaEscolhida = "23:59"
dataEscolhida = "04/06"
datahoje = datetime.now()


# Início da função
def verificacao(hora:str, data:str=""):

    verificaHora = hora.split(sep=":")
    verificaData = data.split(sep="/")
    anoEscolhido = datahoje.year

    # Verificação horário válido
    if int(verificaHora[0]) > 23 or int(verificaHora[1]) > 59:
        print("Tá errado fi")
    else:
        print("Pode pá")

    # Verificação Data Válida
    listaMes31 = [1, 3, 5, 7, 8, 10, 12]
    listaMes30 = [4, 6, 9, 11]

    if data == "":
        None
    else:
        if int(verificaData[1]) == 2:
            if isleap(anoEscolhido):
                if int(verificaData[0]) <= 29:
                    print("Pode pá")
                else:
                    print("Tá errado fi")
            else:
                if int(verificaData[0]) <= 28:
                    print("Pode pá")
                else:
                    print("Tá errado fi")

        else:
            for i in listaMes31:
                if int(verificaData[1]) == i and int(verificaData[0]) <= 31:
                    print("Pode pá")
                else:
                    None

            for i in listaMes30:
                if int(verificaData[1]) == i and int(verificaData[0]) <= 30:
                    print("Pode pá")
                else:
                    None

    return None

verificacao(hora=horaEscolhida, data=dataEscolhida)
