def moltiplicatore(lista):
    risultato = 1
    for numero in lista:
        if numero != 0:
            risultato *= numero
    print("Il risultato della moltiplicazione tra tutti gli elementi della lista è... " + str(risultato))