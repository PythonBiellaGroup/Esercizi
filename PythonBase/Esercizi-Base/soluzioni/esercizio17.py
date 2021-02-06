def calcola_secondi():
    print("Questa funzione converte un dato numero di Giorni, Ore e Minuti in Secondi.")
    da_giorni = int(input("Inserisci il numero di giorni: ")) * 24 * 3600
    da_ore = int(input("Inserisci il numero di ore: ")) * 3600
    da_minuti = int(input("Inserisci il numero di minuti: ")) * 60
    totale = da_giorni + da_ore + da_minuti
    print(totale)