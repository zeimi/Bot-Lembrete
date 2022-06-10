import pytz
from pytz import *
import datetime
from datetime import *

horario = "02:59"
tz = pytz.timezone('America/Sao_Paulo')


datahoje = datetime.now(tz=tz)

# Coleta a string passada pelo usuário (xx:xx) e transforma em um objeto datetime
horalembretehoje = datetime.strptime(horario, "%H:%M")
horalembretehoje = horalembretehoje.replace(tzinfo=datahoje.tzinfo)
horalembretehoje = horalembretehoje.replace(day=int(datahoje.day))
horalembretehoje = horalembretehoje.replace(month=int(datahoje.month))
horalembretehoje = horalembretehoje.replace(year=int(datahoje.year))

print(datahoje.tzname())
print(horalembretehoje.tzname())
print(horalembretehoje)
print(datahoje)

deltatempo = horalembretehoje - datahoje
print(deltatempo.total_seconds())