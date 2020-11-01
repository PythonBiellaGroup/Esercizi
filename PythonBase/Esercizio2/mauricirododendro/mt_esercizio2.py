import re



dizionario={}
def contatore_parole_file(miofile):
    testo=miofile.read()
    print(testo)
    
    #la conversione in minuscolo
    testo=testo.lower()
    #l'eliminazione di tutto ciò che non è carattere o numero
    testo= re.sub('[^A-Za-zÀ-ÿ0-9]+', ' ', testo)
    
    print(testo)

    #segue la scrittura in una lista.Ogni parola è un elemento della lista
    
    y=testo.split()
    print(y)
    #creazione set di parole.Nel set non si presentano le ridondanze.
    parole=set(y)
   
    #senza l'operazione sottostante avrei avuto errore nella riga dell'incremento
    for i in parole:
        dizionario[i]=0
        
 
    #conteggio occorrenze
    for elemento in y:
       dizionario[elemento] +=1
    return dizionario
f = open("sonnet.txt", "r")
dizionario1=contatore_parole_file(f)
for elem in sorted (dizionario1.items()):
    print (elem[0],"::",elem[1])
                             

