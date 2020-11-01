import sys
nome_script,primo,myfile=sys.argv
#le righe sopra: il programma deve essere lanciato in ambiente "terminale" con il seguente ordine: python exercise1.py <numero email> <testo email>
"""txt = "Purtroppo il dispositivo è quasi sempre in queste condizioni..se ne richiede pertanto, ASSISTENZA RISOLUTIVA, per via anche, delle continue lamentele e dei continui rimborsi ai clienti.\
Cordiali Saluti"
"""
wordict = {
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
f = open(myfile, "r")
txt=f.read()
#alle righe sotto si possono aggiungere tutti i caratteri che si riscontrano precedere o seguire le parole chiavi immediatamente (senza lo spazio)
txt=txt.lower()
txt=txt.replace(', ',' ')
txt=txt.replace('?',' ')
txt=txt.replace("’",' ')
txt=txt.replace(".",' ')
txt=txt.replace("!",' ')
#txt=txt.replace("\n",' ')
x=txt.split(' ')
y=[]
#le righe sotto, trovate in stackoverflow, servono a rendere flat una lista di liste
for i in x:
    if type(i) is list:
        y.extend(i)
    else:
        y.append(i)
print (y)
#segue il codice che si applica ad una lista di elementi separati da spazi, normalmente parole
media=0.0
count=0
k=wordict.keys()
print(k)
for i in y:
   if i in k:
       media=media+wordict[i]
       count=count+1
print(media/count)
print ('è stata elaborata la mail numero ', primo)
#print ('media complessiva',(float(primo) + media)/(count+1))
