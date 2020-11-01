## Esercizio 1

Siete stati chiamati dal responsabile IT del Contact Center della vostra ditta per scrivere un programma Python che calcoli il  sentiment (sentiment analysys) delle mail che arrivano in modo da poterlo misurare mese per mese.

Non conosciamo ancora i metodi del machine learning, quindi proviamo ad usare un semplice ma efficace metodo basato sui Dictionary.

Un collega esperto del contact center ci fornisce un Dictionary in cui sono presenti parole chiavi e per ciascuna un punteggio da 0 a 5, con questa scala:

- 1 = negativo
- 2 = parzialmente negativo
- 3 = neutro
- 4 = parzialmente positivo
- 5 = positivo

 Di seguito il Dictionary:

 wordict = { "purtroppo" : 2, "anomalia" : 1, "errore" : 1,  "lamentele" : 2,  "rimborsi" : 1, "disservizi" : 1, "ritardi" : 2, "problema" : 1, "grande": 4, "ringraziare": 4, "eccellente": 5, "bravissimi": 5 }



**L’esercizio consiste nello scrivere un programma python** che legge il contenuto delle mail (per semplicità le considereremo una string) e in caso di presenza delle parole contenute nel dizionario, effettui la media dei punteggi ottenuti.

 Esempio:

- Buongiorno, purtroppo si tratta della stampante principale, alla quale fano riferimento 5 colleghi per le stampe quotidiane

  Stiamo sollecitando la sistemazione da oltre un mese con esito vano, Vi chiedo cortesemente d'intervenire per la sistemazione dell'anomalia

 Quindi il Punteggio dovrà considerare: 2 di “purtroppo” e 1 di “anomalia”

La media finale sarà**: 1,5** quindi una mail decisamente non positiva, che andrebbe gestita con priorità nelle code.



**Di seguito le 3 stringhe su cui calcolare il punteggio tramite il programma python che avete scritto:**

1. Purtroppo il dispositivo è quasi sempre in queste condizioni..se ne richiede pertanto, ASSISTENZA RISOLUTIVA, per via anche, delle continue lamentele e dei continui rimborsi ai clienti.

   Cordiali Saluti

   *Punteggio=?*

2. con la presente segnaliamo numerosi disservizi alla Clientela, nelle ultime settimane, derivanti dai ritardi nella generazione/spedizione dei documenti che si aspettano.

   Abbiamo difficoltà a tranquillizzare i Clienti in quanto il problema e’ diffuso e si protrae da molto tempo. Sapete dirci se e’ stata analizzata la questione e se e’ gia’ stata individuata una data potenziale di risoluzione dell’anomalia? 

   *Punteggio=?*

3. Ciao, mi prendo un momento per ringraziare te e tutta la squadra per il grande lavoro che state facendo in queste settimane. Avete consentito in modo eccellente di continuare a lavorare, funzionare, servire i clienti.  Un grazie sincero. Siete stati bravissimi. Davvero! Non ci sono tante aziende in Italia che hanno avuto la stessa continuità

   *Punteggio=?*
