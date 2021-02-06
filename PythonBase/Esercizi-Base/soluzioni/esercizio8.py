def palindrome_check(parola):
    indice = (len(parola) -1)
    nuova_parola = ""
    while indice >= 0:
        nuova_parola += parola[indice]
        indice -= 1
    if nuova_parola == parola:
        print(nuova_parola + ": la parola passata è un palindromo!")
    else:
        print(nuova_parola + ": mi dispiace, la parola inserita non è un palindromo...")