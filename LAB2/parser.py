from os import listdir
from os.path import isfile, join
import unicodedata
import string

mezzi = set()
corse = set()
fermate = set()
stazioni = set()
passaggio = []

mypath="/home/rossidaniel/Documenti/data_transport/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for t_file in onlyfiles:
    f=file(str(mypath)+t_file)
    s=f.read()
    s=''.join(x if x in string.printable else " " for x in s)
    s=s.split('*Z ')
    s.pop(0)
    for trip in s:
        lines = trip.split("\n")
        


        first_line= lines.pop(0).split(" ")[:2]
        second_line=lines[0].split(" ")[:2]
        first_line[1]=first_line[1].replace("-","")+second_line[1]

        corse.add(first_line[0])
        mezzi.add(first_line[1])

        while lines[0].split(" ")[0][0]=='*':
            lines.pop(0)
        for line in lines:
            fermata=line[0:9]
            stazione=line[10:30]
            start=line[32:37]
            finish=line[39:44]
            
            if fermata != '':
                fermate.add(fermata)
                stazioni.add(stazione)
                passaggio.append([fermata,stazione,start,finish])      

        corse.add(first_line[0])
        mezzi.add(first_line[1])

    f.close()

for i in passaggio:
    print i

f=open("mezzi.csv","w")
for i in mezzi:
    f.write(i+"\n")

f=open("corse.csv","w")
for i in corse:
    f.write(i+"\n")

f=open("fermate.csv","w")
for i in fermate:
    f.write(i+"\n")

f=open("stazioni.csv","w")
for i in stazioni:
    f.write(i+"\n")

f=open("viaggi.csv","w")
for i in passaggio:
    for j in i:
        f.write(j+"\t")
    f.write("\n")