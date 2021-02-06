def membro_di(el, lista):
    if el in lista:
        print(f"Il carattere '{el}' è presente nella lista passata, all'indice {lista.index(el)}!")
    else:
        print(f"Il carattere '{el}' NON è presente nella lista passata...")