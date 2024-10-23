def temperature_converter(temperature: float, KoF: str) -> float:
    if(KoF=='F'):
        C = (5/9)*(temperature - 32)
    elif(KoF=='K'):
        C = temperature - 273.15
    
    return C