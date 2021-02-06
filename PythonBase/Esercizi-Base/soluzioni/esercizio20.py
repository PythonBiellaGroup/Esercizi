# due possibili soluzioni per l'esercizio proposto

def rimario(elenco):
    rime = []
    parola = input("Inserisci la parola di cui desideri cercare le rime: ")
    for elemento in elenco:
        if elemento[-3:] == parola[-3:]:
          rime.append(elemento)

    if not rime:
        print("Non sono state trovate rime corrispondenti alla parola passata!")
    else:
        output = ", ".join(el for el in rime)
        print(f"Le rime corrispondenti alla parola {parola} sono le seguenti: {output}")

def rimario_pro(elenco):
    rime = []
    parola = input("Inserisci la parola di cui desideri cercare le rime: ")
    rime = [el for el in elenco if el[-3:] == parola[-3:]]
    if not rime:
        print("Non sono state trovate rime corrispondenti alla parola passata!")
    else:
        output = ", ".join(el for el in rime)
        print(f"Le rime corrispondenti alla parola {parola} sono le seguenti: {output}")