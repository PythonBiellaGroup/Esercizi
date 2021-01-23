# Esercizi in Python

Per lanciare un esercizio utilizzando il virtual environment esistente nella cartella:

- aprire il file python: launchWithVenv.py
- modificare la variabile: `script_file = "./ContaParole.py"` con all'interno il nome dello script che si vuole eseguire
- lanciare da terminale: `python launchWithVenv.py`

## ESERCIZIO 2

Scrivere una funzione contatore_parole_file() che prende un file name in input e ritorna un dizionario contenente i contatori per ciascuna parola. 
PS: rimuovere tutte le punteggiature, tutto in minuscolo

contatore_parole_file('sonetto.txt') => { 'la': 4, 'nebbia': 2, ... }

La soluzione è stata realizzata nel python file: ContaParole.py