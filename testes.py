import datetime
from datetime import *
from calendar import isleap


# Verificar se o array é numérico
def is_numeric(array):
    try:
        int(array[0])
        return True
    except ValueError:
        return False