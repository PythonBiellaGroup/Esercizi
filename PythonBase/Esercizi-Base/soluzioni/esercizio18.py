# due possibili soluzioni per l'esercizio esposto

import random
import string

def psw_generator():
    print("Il programma permette di scegliere tra due livelli di complessità della password.")

    ascii_chars = string.digits + string.ascii_letters + string.punctuation
    alphanum_chars = string.digits + string.ascii_letters

    if input("Desideri una password Semplice o Complessa? S/C ") == "C":
        lunghezza = 20
        tipo = ascii_chars
    else:
        lunghezza = 8
        tipo = alphanum_chars

    psw = ""
    counter = 0

    while counter < lunghezza:
        char = random.choice(tipo)
        psw += char
        counter += 1

    print(f"La password generata è: {psw}")


###########

import secrets
import string

def psw_generator_pro():
    print("Il programma permette di scegliere tra due livelli di complessità della password.")

    ascii_chars = string.digits + string.ascii_letters + string.punctuation
    alphanum_chars = string.digits + string.ascii_letters

    if input("Desideri una password Semplice o Complessa? S/C ") == "C":
        lunghezza = 20
        tipo = ascii_chars
    else:
        lunghezza = 8
        tipo = alphanum_chars

    psw = "".join(secrets.choice(tipo) for _ in range(lunghezza))
    print(f"La password generata è: {psw}")