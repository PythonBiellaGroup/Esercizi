# Due possibili soluzioni per questo esercizio

def reverser(stringa):
    indice = (len(stringa) -1)
    nuova_stringa = ""
    while indice >= 0:
        nuova_stringa += stringa[indice]
        indice -= 1
    print(nuova_stringa)

def reverser_pro(stringa):
    reverse = stringa[::-1]
    print(reverse)