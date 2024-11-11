import string
import random

def password_generator(config:list[int,int,int,int,int], longitud:int):
    sets = [string.ascii_lowercase, string.ascii_uppercase, string.digits, {' '}, string.punctuation]
    contrasenia = []
    cont = 0
    callowed = []

    n_options = config.count(1) # [0, 5]
    if(n_options > 0 and n_options <= longitud):
        for option in config:
            if(option == 1):
                contrasenia.append(random.choice(list(sets[cont])))
                callowed += list(sets[cont])
            cont += 1
        
        longitud = longitud - n_options
        contrasenia_ = [random.choice(callowed) for _ in range(longitud)]
        contrasenia += contrasenia_
    elif(n_options > longitud):
        raise ValueError("Longitud demasiado pequeña en comparación de los requisitos")

    random.shuffle(contrasenia)
    contrasenia = "".join(contrasenia)
    return  contrasenia

# if (__name__ == "__main__"):
#     c = password_generator([1,1,1,1,1],6)
#     print(c)

#     c = password_generator([1,0,0,0,0],6)
#     print(c)
