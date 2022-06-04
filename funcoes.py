import datetime
from datetime import *
from calendar import isleap

horaEscolhida = "23:59"
dataEscolhida = "04/10"
datahoje = datetime.now()


# Início da função
def verificacao(hora:str, data:str=""):

    verificaHora = hora.split(sep=":")
    verificaData = data.split(sep="/")
    anoEscolhido = datahoje.year

    # Verificação horário válido
    if int(verificaHora[0]) > 23 or int(verificaHora[1]) > 59:
        horavalida = False
    else:
        horavalida = True

    # Verificação Data Válida
    listaMes31 = [1, 3, 5, 7, 8, 10, 12]
    listaMes30 = [4, 6, 9, 11]

    if data == "":
        datavalida = True
    else:
        if int(verificaData[1]) == 2: # Verifica se o mês é fevereiro
            if isleap(anoEscolhido): # Verifica se é ano bissexto
                if int(verificaData[0]) <= 29:
                    datavalida = True

                else:
                    datavalida = False
            else:
                if int(verificaData[0]) <= 28:
                    datavalida = True
                else:
                    datavalida = False

        else:
            for i in listaMes31: # Verifica se é um mês terminado em dia 31
                if int(verificaData[1]) == i and int(verificaData[0]) <= 31:
                    datavalida = True
                    break
                else:
                    datavalida = False

            if datavalida == False:
                for i in listaMes30: # Verifica se é um mês terminado em dia 30
                    if int(verificaData[1]) == i and int(verificaData[0]) <= 30:
                        datavalida = True
                        break
                    else:
                        datavalida = False

    if horavalida == True and datavalida == True:
        return True
    else:
        return False
