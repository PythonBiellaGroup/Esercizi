def trova_ascii():
    carattere = input("Inserisci il carattere che ti interessa convertire: ")
    valore = ord(carattere)
    output = f"Il valore ASCII associato a '{carattere}' è {valore}"
    return output