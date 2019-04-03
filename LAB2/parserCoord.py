from os import listdir
from os.path import isfile, join
import unicodedata
import string
from math import radians, sin, cos, acos


def readCord():
    #return: una mappa key:codStaz -> value:(long,lat)
    mypath="bfkoord"

    f=file(mypath)
    s=f.read()
    s=''.join(x if x in string.printable else "?" for x in s)
    s=s.split('\n')
    s=s[2:]
    s.pop(-1)

    bfkoord = dict() # key:codStaz -> value:(long,lat)
    for row in s:
        data = row.split(" ")
        data = filter(lambda r : r!="", data)

        codStaz=data[0]
        longitud = data[1]
        lat = data[2]
        nameStaz = "".join(data[4:])
        bfkoord[codStaz]=(longitud,lat,nameStaz)
        
    f.close()

    f=open("coord.csv","w")
    for i in bfkoord:
        f.write(i)
        f.write("\t")
        f.write(str(bfkoord[i]))
        f.write("\n")
    f.close()
    
    return bfkoord


def distance(stazA, stazB, coordMap):
    #approssimata per difetto
    coordA = coordMap[stazA]
    coordB = coordMap[stazB]
    slat = radians(float(coordA[1]))
    slon = radians(float(coordA[0]))
    elat = radians(float(coordB[1]))
    elon = radians(float(coordB[0]))
    dist = dist = float(6371.01) * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
    return int(dist)



