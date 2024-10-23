def es_bisiesto(anio):
    # Un año es bisiesto si es divisible por 4, pero no por 100, a menos que sea divisible por 400
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def nextday(dia, mes, anio):
    # Número de días en cada mes, tomando en cuenta Febrero (mes 2) en años bisiestos
    dias_por_mes = [31, 29 if es_bisiesto(anio) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Incrementar el día
    dia += 1
    # Verificar si se ha pasado del último día del mes
    if dia > dias_por_mes[mes - 1]:
        dia = 1
        mes += 1
    # Verificar si se ha pasado del último mes del año
    if mes > 12:
        mes = 1
        anio += 1
    return dia, mes, anio
