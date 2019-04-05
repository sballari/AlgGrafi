from os import listdir
from os.path import isfile, join
import unicodedata
import string

def parser_LTS(ds_name):

    mypath="dataset/"+ds_name
    #struttura dati di output
    # return : (type_weight, [(node_index, x_val,y_val)])
    # newtype type_weight = GEO | EUC_2D

    f=open(mypath)
    s=f.read()
    lines=s.split('\n')
    for line in lines:
        line=line.split(" ")
        line=filter(lambda r : r!="", line)
    
    weightType = lines[5][-1]
    print weightType

    i=5
    find = False
    city = []
    while lines[i] != "EOF":
        if (find == False):
            if lines[i][0] == "NODE_COORD_SECTION": 
                find = True
        else:
            index = lines[i][0]
            x_coord = lines[i][1]
            y_coord = lines[i][2]
            tupla = (index,x_coord,y_coord)
            print tupla
            city.append(tupla)
        i+=1
     
    return (weightType,city)
