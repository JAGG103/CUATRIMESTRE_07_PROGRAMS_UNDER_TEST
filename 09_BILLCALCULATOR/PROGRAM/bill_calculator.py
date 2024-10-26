# Se da como entrada el total de la cuenta, un porcentaje y de salida el total a pagar

def bill_calculator(cuenta:float, porcentaje:int):
    propina: float = 0.0
    total: float = 0.0

    if(cuenta >= 0 and porcentaje >= 0):
        propina = (cuenta*porcentaje)/100
        total = cuenta + propina
    elif(cuenta < 0):
        total = -1
    else:
        total = cuenta

    return total

