import datetime
from datetime import *
from calendar import isleap


quebraloop = 1
horaEscolhida = "23:59"
dataEscolhida = "04/09"
datahoje = datetime.now()


verificaHora = horaEscolhida.split(sep=":")
verificaData = dataEscolhida.split(sep="/")
anoEscolhido = datahoje.year

listaMes31 = [1, 3, 5, 7, 8, 10, 12]
listaMes30 = [4, 6, 9, 11]

while quebraloop == 1:

    if quebraloop == 0:
        break
    else:
        for i in listaMes31:
            if int(verificaData[1]) == i and int(verificaData[0]) <= 31:
                print ('True')
                quebraloop == 0
                break
            else:
                None

    if quebraloop == 0:
        break
    else:
        for i in listaMes30:
            if int(verificaData[1]) == i and int(verificaData[0]) <= 30:
                print ('True')
                quebraloop == 0
                break
            else:
                None