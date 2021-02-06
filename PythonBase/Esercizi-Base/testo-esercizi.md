# Esercizi Base su Python

Elenco di esercizi base su Python.

Grazie al blog Programmare in Python: https://www.programmareinpython.it/esercizi-python/  
Questi esercizi sono presi da questo bellissimo blog.


Di seguito l'elenco degli esercizi

## Esercizio 1

**Max tra due numeri**

Scrivi una funzione che prende due numeri come parametro e manda in print il più grande tra i due.
Per quanto Python disponga di una funzione max(), sei invitato a utilizzare le istruzioni If, Elif ed Else per la scrittura dell'algoritmo.

## Esercizio 2

**Max tra tre numeri**

Scrivi una funzione che prende stavolta tre numeri come parametro e restituisce il più grande tra loro!

## Esercizio 3

**Il maggiore tra tutti!**

Scrivi un programma che, passata come parametro una lista di interi, fornisce in output il maggiore tra i numeri contenuti nella lista.

## Esercizio 4

**Sei una vocale?**

Scrivi una funzione a cui viene passato un carattere come parametro, e che ci dice se il carattere è o meno una vocale.

## Esercizio 5

**Sommatrice inarrestabile**

Scrivi una funzione "sommatrice" che somma tra loro tutti gli elementi di una lista di numeri.

## Esercizio 6

**Moltiplicatore inarrestabile**

Scrivi una funzione "moltiplicatrice" che moltiplica tra loro tutti gli elementi di una lista di numeri.

## Esercizio 7

**Reverser**

Scrivi una funzione a cui passerai come parametro una stringa, e che manderà in print una versione inversa (al contrario) della stessa stringa (ad esempio "abcd" diventerà "dcba")

## Esercizio 8

**Palindromo o non palindromo?**

Scrivi una funzione a cui viene passata una parola e riconosce se si tratta di un palindromo (parole che si leggono uguali anche al contrario) oppure meno.

## Esercizio 9

**Scriviamo la nostra versione di len()**

Scrivi una funzione che restituisca la lunghezza di una stringa o lista passata come parametro. In sostanza, seppur presente, provate a scrivere la vostra versione della funzione len()!

## Esercizio 10

**Generatore di Istogrammi**

Scrivi una funzione che, data una lista di numeri, fornisce in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.

Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:
```
***

*******

*********

*****
```

## Esercizio 11

**A ciascuno il suo**

Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.

## Esercizio 12

**Il frequenzimetro**

Scrivi una funzione a cui passare una stringa come parametro, e che restituisca un dizionario rappresentante la "frequenza di comparsa" di ciscun carattere componente la stringa. 

Semplicemente, data una stringa "ababcc", otterremo in risultato {"a": 2, "b": 2, "c": 2}!

## Esercizio 13

**Solamente per soci**

Scrivi una funzione a cui vengono passati come parametro un elemento e una lista di elementi, e che ti dica in output se l'elemento passato sia presente o meno nella lista.

Qualora l'elemento sia presente nella lista, la funzione dovrà inoltre comunicarci l'indice dell'elemento.


## Esercizio 14

**Il linguaggio dei furfanti**

In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto "rövarspråket", che significa "linguaggio dei furfanti": consiste nel raddoppiare ogni consonante di una parola e inserire una "o" nel mezzo. Ad esempio la parola "mangiare" diventa "momanongogiarore".

Scrivi una funzione in grado di tradurre una parola o frase passata tramite input in "rövarspråket".

Dopo aver tradotto una frase, il programma dovrà chiedere all'utente se intende tradurne un'altra, e in caso di risposta positiva, dovrà attendere l'inserimento di una nuova parola da parte dell'utente.

## Esercizio 15

**Il geometra**

Scrivi una funzione che, a scelta dell'utente, calcoli l'area di:

- un cerchio
- un quadrato
- un rettangolo
- un triangolo

Sentiti libero/a di estendere le potenzialità della funzione quanto meglio credi...

## Esercizio 16

**L'americana**

Scrivi una funzione che, dato in ingresso un valore espresso in metri, mandi in print l'equivalente in miglia terrestri, iarde, piedi e pollici.

## Esercizio 17

**Il signore del tempo**

Scrivi una semplice funzione che converta un dato numero di giorni, ore e minuti, passati dall'utente tramite funzione input, in secondi.

## Esercizio 18

**Generatore di Password**

Scrivi una funzione generatrice di password.

La funzione deve generare una stringa alfanumerica di 8 caratteri qualora l'utente voglia una password semplice, o di 20 caratteri ascii qualora desideri una password più complicata.

## Esercizio 19

**Funzione Genera MAC**

Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, a un chipset per comunicazioni wireless (es WiFi o Bluetooth), composto da 6 coppie di cifre esadecimali separate da due punti.

Un esempio di MAC è 02:FF:A5:F2:55:12.

Scrivi una funzione genera_mac che generi degli indirizzi MAC pseudo casuali.

## Esercizio 20

**Poesia Elettronica**

Scrivi una semplice funzione rimario, a cui viene passato un elenco di parole come parametro e che riceva una parola inserita dall'utente tramite la funzione input.

La funzione rimario dovrà confrontare la parola inserita dall'utente con quelle presenti nell'elenco passato, alla ricerca di rime, intese come parole le cui ultime 3 lettere siano uguali alla parola inserita dall'utente.

Le rime dovranno essere quindi mostrate in output dall'utente.

## Esercizio 21

**La libreria**

Scrivi una funzione "vendi_libri" che:

- Controlla se il libro richiesto è presente sugli scaffali della libreria
- Qualora il libro sia presente, ne decrementa il numero di copie (eventualmente rimuovendo il titolo) e ci segnala che la vendita ha avuto successo
- Se il libro non è disponibile, viene messo in un elenco di libri da ordinare e ci viene comunicato che la vendita non ha avuto successo
- La funzione restituisce valore Booleano True o False in base all'esito della vendita.


## Esercizio 22

**Crittografia ROT-13**

Il ROT-13 è un semplice cifrario monoalfabetico, in cui ogni lettera del messaggio da cifrare viene sostituita con quella posta 13 posizioni più avanti nell'alfabeto.

Scrivi una semplice funzione in grado di criptare una stringa passata, o decriptarla se la stringa è già stata precedentemente codificata.


## Esercizio 23

**Funzione fattoriale ricorsiva**

Scrivi una funzione ricorsiva che calcola il fattoriale di un numero dato.

## Esercizio 24

**La serie di Fibonacci**

Nella serie di Fibonacci, ciascun numero della serie è la somma dei due numeri nella serie che lo precedono, ad esempio:

1, 1, 2, 3, 5, 8, 13 (...)

Scrivi una funzione ricorsiva che restituisce in output i numeri della sequenza di Fibonacci, entro una soglia specifica impostata dall'utente.

## Esercizio 25

**Info di Sistema**

Scrivi una funzione che fornisca in output il nome del Sistema Operativo utilizzato con eventuali relative informazioni sulla release corrente.

## Esercizio 26

**Trova ASCII**

Scrivi una funzione che, dato un carattere in ingresso, restituisca in output il codice ASCII associato al carattere passato.

## Esercizio 27

**Il peso di una cartella**

Scrivi una funzione che calcoli la somma (espressa in MB) delle dimensioni dei file presenti nella cartella di lavoro.

## Esercizio 28

**Il postino**

Scrivi una funzione "postino" che sia in grado di spedire delle eMail tramite Gmail! (aiuto: puoi usare il modulo smtplib)

## Esercizio 29

**La cercatrice**

Scrivi una funzione "cercatrice" che scansioni un dato percorso di sistema alla ricerca di file di tipo pdf.
La funzione dovrà avere le seguenti caratteristiche:

- Il percorso fornito dovrà essere anzitutto validato, in quanto deve portare a una cartella esistente
- La funzione dovrà fornire un elenco dei file pdf (con/relativo/percorso) man mano che questi vengono trovati
- In fine la funzione dovrà fornire in output il totale dei file .pdf che sono stati trovati durante la scansione.

## Esercizio 30

**Il Salvatore**

Scrivi una funzione "file_backup" che sia in grado di effettuare copie di backup di determinati tipi di file, con le seguenti caratteristiche:

- Percorso da scansionare, di backup e tipologia di file da copiare dovranno essere passati dall'utente tramite input
- Il programma dovrà verificare la presenza o meno di una cartella di backup al percorso fornito, e qualora questa non fosse presente dovrà crearla
- La funzione dovrà anche gestire l'eventuale scelta da parte dell'utente, di un percorso da scansionare che non esiste