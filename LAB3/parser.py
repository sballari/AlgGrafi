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
    data=[]
    for line in lines:
        rigo=line.split(" ")
        data.append(filter(lambda r : r!="", rigo))
    weightType = data[4][1]

    i=5
    find = False
    city = []
    while data[i][0] != 'EOF':

        if (find == False):
            if data[i][0] == 'NODE_COORD_SECTION': 
                find = True
        else:
            index = data[i][0]
            x_coord = data[i][1]
            y_coord = data[i][2]
            tupla = (index,x_coord,y_coord)
            city.append(tupla)
        i+=1
     
    return weightType,city
