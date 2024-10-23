def discount_college(mes: str, colegiatura:int) -> float:
    total : float = 0.0

    if(mes in {'enero','febrero','marzo'}):
        total = colegiatura - colegiatura*0.3
    elif(mes in {'abril','mayo','junio'}):
        total = colegiatura - colegiatura*0.2
    elif(mes in {'julio','agosto','septiembre'}):
        total = colegiatura - colegiatura*0.1
    else:
        total = colegiatura
    
    return total


"""if(__name__=='__main__'):
    print(discount_collage('febrero'))
"""