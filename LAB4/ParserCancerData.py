from os import listdir
from os.path import isfile, join
import unicodedata
import string
from Coord import *

# Ogni riga dei file corrisponde ad una contea ed e' composta da cinque campi:
# codice della contea, coordinata x, coordinata y, popolazione e rischio di cancro.
def ParserCancerData(file_name): 

    mypath="Data/"+file_name
    #struttura dati di output
    # return : [[id_contea, x_val, y_val, population, risk]]

    f=open(mypath)
    s=f.read()
    lines=s.split('\n')
    data=[]
    for line in lines:
        rigo=line.split(',')
        contea = rigo[0]
        x = float(rigo[1])
        y = float(rigo[2])
        pop = float(rigo[3])
        risk = float(rigo[4])
        point = Point(contea,x,y,pop,risk)
        data.append(point)

    return data
