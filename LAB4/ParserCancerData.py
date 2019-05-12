from os import listdir
from os.path import isfile, join
import unicodedata
import string

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
        data.append(rigo)
    return data