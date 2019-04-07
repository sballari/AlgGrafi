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
        longitud = float(data[1])
        lat = float(data[2])
        bfkoord[codStaz]=[longitud,lat]        
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



def hourPlusMinuts(hour_string, min_int):
    #return : tupla con ora di arrivo in stringa "01020", e giorni di viaggio in numero

    if ( min_int >= 60*24) : print "allert: viaggio di piu' di un giorno"
    next_day = 0

    vhour_l = list(hour_string)
    minut = int("".join(vhour_l[-2:])) #prendo i minuti
    ore = int ("".join(vhour_l[1:3])) ##prendo le ore
    new_min = minut + (min_int % 60)
    new_h = ore + (min_int //60) 
    if (new_h>=24): 
        new_h = new_h % 24 
        next_day = new_h//24

    #se serve aggiungo zero
    if len(str(new_h))!=2 : new_h = "0"+str(new_h)
    else: new_h = str(new_h)

    if len(str(new_min))!=2 : new_min = "0"+str(new_min)
    else: new_min = str(new_min)

    new_time = "0"+new_h+new_min
    return (new_time, next_day)

