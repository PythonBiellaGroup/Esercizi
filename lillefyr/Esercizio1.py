#!/usr/bin/env python3

worddict = {
    "purtroppo" : 2,
    "anomalia" : 1,
    "errore" : 1,
    "lamentele" : 2,
    "rimborsi" : 1,
    "disservizi" : 1,
    "ritardi" : 2,
    "problema" : 1,
    "grande": 4,
    "ringraziare": 4,
    "eccellente": 5,
    "bravissimi": 5
}

#il punteggio dovrà considerare: 2 di “purtroppo” e 1 di “anomalia”. La media finale sarà: 1,5 quindi

messagio = [ "Buongiorno, purtroppo si tratta della stampante principale, alla quale fano riferimento 5 colleghi per le stampe quotidiane Stiamo sollecitando la sistemazione da oltre un mese con esito vano, Vi chiedo cortesemente d'intervenire per la sistemazione dell'anomalia", 
"Purtroppo il dispositivo è quasi sempre in queste condizioni..se ne richiede pertanto, ASSISTENZA RISOLUTIVA, per via anche, delle continue lamentele e dei continui rimborsi ai clienti.  Cordiali Saluti",
"con la presente segnaliamo numerosi disservizi alla Clientela, nelle ultime settimane, derivanti dai ritardi nella generazione/spedizione dei documenti che si aspettano.  Abbiamo difficoltà a tranquillizzare i Clienti in quanto il problema e’ diffuso e si protrae da molto tempo. Sapete dirci se e’ stata analizzata la questione e se e’ gia’ stata individuata una data potenziale di risoluzione dell’anomalia?",
"Ciao, mi prendo un momento per ringraziare te e tutta la squadra per il grande lavoro che state facendo in queste settimane. Avete consentito in modo eccellente di continuare a lavorare, funzionare, servire i clienti.  Un grazie sincero.  Siete stati bravissimi. Davvero! Non ci sono tante aziende in Italia che hanno avuto la stessa continuità", "tutto bene" ]

# range does NOT include the last value
for counter in range(0, len(messagio)):

    # remove chars causing trouble for split
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~’'''
    for char in messagio[counter]:
        if char in punctuations:
           messagio[counter] = messagio[counter].replace(char," ");

    # Split string into a list
    splitString = messagio[counter].split()

    # check the words from the string against the dict
    # count how many are found
    # calculate the average 
    cnt = 0
    punteggio = 0
    for word in splitString:
        retval = worddict.get(word, 0)
        if retval > 0:
            cnt = cnt + 1
            punteggio = punteggio + retval

    if ( cnt > 0 ):
        print ("Messagio numero ", counter, " punteggio=", punteggio/cnt, " ", sep=" ")
        if punteggio/cnt == 5:
             print ( "positivo" )
        elif punteggio/cnt >= 4:
            print ( "parzialmente positivo" )
        elif punteggio/cnt >= 3:
            print ( "neutro" )
        elif punteggio/cnt >= 2:
            print ( "parzialmente negativo" )
        elif punteggio/cnt >= 1:
            print ( "negativo" )
