import csv
import math
#la funzione getDuplicatesWithInfo è stata trovata in rete:ha lo scopo di restituire il valore che si ripete e le  sue occorrenze
def getDuplicatesWithInfo(listOfElems):

    dictOfElems = dict()
    index = 0
    for elem in listOfElems :
# If element exists in dict then keep its index in lisr & increment its frequency
        if elem in dictOfElems:
            dictOfElems[elem][0] += 1
            dictOfElems[elem][1].append(index)
        else:
# Add a new entry in dictionary 
            dictOfElems[elem] = [1, [index]]
            index += 1    
    dictOfElems = { key:value for key, value in dictOfElems.items() if value[0] > 1}
    return dictOfElems

#main

mylist2=[]
with open('curr.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        mylist2.append(row)
        print(mylist2)
        
#convertendo in nel tipo di numero intero, calcolo le 9 distanze     da Z  
#nella lista cerco_min pongo le varie distanze   
cerco_min=[]
for j in range(1,10):
        somma=0
        for i in range(1,7):
            somma +=(int(mylist2[j][i])-int(mylist2[10][i]))**2
        somma=math.sqrt(somma)
        cerco_min.append(somma)
        print(somma)
#la funzione min mi consente di visualizzare direttamente il valore del minimo        
print (min(cerco_min))
#controllo l'unicità dell'esistenza del minimo
if min(cerco_min) in getDuplicatesWithInfo(cerco_min):
    print('il minimo è presente puù volte')
else:
    print('il minimo si presenta solo una volta')
    simile_index=cerco_min.index(min(cerco_min))+1
    print(mylist2[simile_index][0])
    for i in range(3,7):
        if mylist2[simile_index][i]>mylist2[10][i]:
            print(mylist2[0][i])
#print (getDuplicatesWithInfo(cerco_min))
