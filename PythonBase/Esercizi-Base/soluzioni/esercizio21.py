scaffale = {"Così parló Zarathustra": 10, "Elon Musk - Biografia": 7, "End Of Jobs": 5,
            "L'Alchimista": 1, "I Fratelli Karamazov": 2, "Delitto e Castigo": 1}
ordini = []

def vendi_libri(scaffale, libro):
    vendita = False
    if libro in scaffale:
        vendita = True
        scaffale[libro] -= 1
        print(f"Il libro '{libro}' è stato venduto!")
        if scaffale[libro] == 0:
            del scaffale[libro]
    else:
        print(f"Mi dispiace, ma il libro richiesto '{libro}' non è presente nello scaffale.")
        print("Sto effettuando un ordine!")
        ordini.append(libro)
        print(f"Da Ordinare: {ordini}")
    print("Di seguito un elenco aggiornato dei volumi presenti nel nostro scaffale:")
    print(scaffale)
    return vendita