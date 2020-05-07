import csv
import sys
import math
import string

SexDistance=2.0

lbldict = {}
dbdict = {}
affini =[]

with open(sys.argv[1]) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    line_count=0
    for row in csv_reader:
        if line_count == 0:
            for i, lbl in enumerate(row):
                lbldict.update({i : lbl})
            line_count += 1
        else:
            dbdict.update({row[0]:row})
            line_count += 1

for i in dbdict:
    li=dbdict[i]
    liDV=[]
    for j in dbdict:
        lj=dbdict[j]
        if li[0] == lj[0]:
            continue
        k = 1 
        s = 0
        while k < len(li):
            s += (int(li[k])-int(lj[k]))**2
            k += 1
        if s == 0.0:
            continue
        liDV.append((li[0]+" "+lj[0], math.sqrt(s)))

    t0=(" ", 0.0)
    for k, t in enumerate(sorted(liDV, key=lambda t: t[1])):
        if k == 0:
            if t[1] >= SexDistance:
                break
            affini.append(t[0].split())
            t0=t
            continue
        if t0[1] < t[1]:
            break
        affini.append(t[0].split())

mproduct = {}

for cpl in affini:
    for k, v1 in enumerate(dbdict[cpl[0]]):
        if k == 0:
            continue
        if v1 < dbdict[cpl[1]][k]:
            w=cpl[0]+" "+lbldict[k]
            if w in mproduct.keys():
                v=mproduct[w]
            else:
                v=0
            mproduct.update({w : v+1})

for i in mproduct:
    print("a", i.split()[0], "manca", i.split()[1])
