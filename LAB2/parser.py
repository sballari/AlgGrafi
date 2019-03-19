from os import listdir
from os.path import isfile, join
import unicodedata
import string

mezzi = set()
corse = set()


mypath="/home/rossidaniel/Documenti/data_transport/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print onlyfiles

for t_file in onlyfiles:
    f=file(str(mypath)+t_file)
    s=f.read()
    s=''.join(x if x in string.printable else " " for x in s)
    s=s.split('*Z ')
    s.pop(0)
    for first_run in s:
        #print first_run
        first_run = first_run.split("\n")
        ciao= first_run.pop(0).split(" ")
        ciao= filter(lambda a: a != "", ciao)
        ciao[1]=ciao[1].replace("-","")
        corse.add(ciao[0])
        mezzi.add(ciao[1])

        
        #corsa=intestazione[0]
        #print corsa
    #print "-----------------------------------"
    f.close()

for i in mezzi:
    print i
print corse