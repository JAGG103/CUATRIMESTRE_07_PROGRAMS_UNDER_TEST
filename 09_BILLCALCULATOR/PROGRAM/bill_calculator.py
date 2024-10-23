# Se da como entrada el total de la cuenta, un porcentaje y de salida el total a pagar

def bill_calculator(cuenta:float, porcentaje:int):
    propina: float = 0.0
    total: float = 0.0

    if(porcentaje<0):
        propina = -1
        total = -1
    else:
        propina = (cuenta*porcentaje)/100
        total = cuenta + propina

    return total



# if(__name__=="__main__"):
#     print(tip_calculator(7000, -1))
#     print(tip_calculator(7000, 200))
#     print(tip_calculator(700, 10))