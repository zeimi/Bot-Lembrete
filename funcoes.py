import datetime
from datetime import *
from calendar import isleap

horaEscolhida = "10:19"
dataEscolhida = "-1234/07"
datahoje = datetime.now()


# Início da função verificação de horário e data
def verificacao(hora: str, data: str = ""):
    #                                                    # 0     1
    # Separa a hora em um array, separado por : Exemplo: ['23', '59']
    verificaHora = hora.split(sep=":")
    # Separa a data em um array, separado por / Exemplo: ['04', '09']
    verificaData = data.split(sep="/")
    anoEscolhido = datahoje.year  # Ano atual

    # Verificação horário válido
    try:
        test1 = int(verificaHora[0]) # Verifica se o horário é numérico
        test2 = int(verificaHora[1])

        horavalida = True

    except ValueError: # Se não for numérico, retorna False
        horavalida = False

    if horavalida == False:
        None
    elif horavalida == True:
        # Verifica se a hora é maior que 23:59
        if int(verificaHora[0]) > 23 or int(verificaHora[1]) > 59:
            horavalida = False
        # Verifica se a hora é menor que 00:00
        elif int(verificaHora[0]) < 0 or int(verificaHora[1]) < 0:
            horavalida = False
        else:
            horavalida = True

    # Verificação Data Válida
    listaMes31 = [1, 3, 5, 7, 8, 10, 12]  # Meses que possuem 31 dias
    listaMes30 = [4, 6, 9, 11]  # Meses que possuem 30 dias

    # Se não for passado nenhuma data, a data sempre será válida (data atual)
    if data == "":
        datavalida = True

    else:
        try:
            test1 = int(verificaData[0]) # Verifica se o dia é numérico
            test2 = int(verificaData[1]) 

            datavalida = True

        except ValueError:
            datavalida = False

        if datavalida == False:
            None

        elif datavalida == True:

            if int(verificaData[1]) == 2:  # Verifica se o mês é fevereiro
                if isleap(anoEscolhido):  # Verifica se é ano bissexto
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
                for i in listaMes31:  # Verifica se é um mês terminado em dia 31
                    if int(verificaData[1]) == i and int(verificaData[0]) <= 31:
                        datavalida = True
                        break
                    else:
                        datavalida = False

                if datavalida == False:
                    for i in listaMes30:  # Verifica se é um mês terminado em dia 30
                        if int(verificaData[1]) == i and int(verificaData[0]) <= 30:
                            datavalida = True
                            break
                        else:
                            datavalida = False
            if datavalida == True:
                if int(verificaData[0]) < 0 or int(verificaData[1]) < 0: # Verifica se o dia ou mês é negativo
                    datavalida = False

    if horavalida == True and datavalida == True:  # Se a hora e data forem válidas, retorna True
        return True
    else:
        return False

print(verificacao(horaEscolhida, dataEscolhida))