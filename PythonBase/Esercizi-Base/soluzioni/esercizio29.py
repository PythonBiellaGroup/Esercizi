import os

def cercatrice(percorso):
    if not os.path.isdir(percorso):
        print(f"Il percorso inserito '{percorso}' risulta non essere un percorso idoneo. Verifica e riprova, grazie.\n")
        return None
    contatore = 0
    print(f"Sto effettuando la scansione di '{percorso}' alla ricerca di file .pdf\n")
    for cartella, sottocartelle, files in os.walk(percorso):
        for file in files:
            if file.endswith(".pdf"):
                pdf = os.path.join(cartella,file)
                print(f"Trovato file pdf: {pdf}\n")
                contatore += 1
    print(f"\nScansione Ultimata! Ho trovato {contatore} files con estensione pdf.")