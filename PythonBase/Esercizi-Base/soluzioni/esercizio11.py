# due possibili soluzioni per l'esercizio proposto

def char_counter(lista_a):
    lista_b = []
    for parola in lista_a:
        lista_b.append(len(parola))
    return lista_b

def char_counter_pro(lista_a):
    return [len(parola) for parola in lista_a]