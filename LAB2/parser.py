from os import listdir
from os.path import isfile, join
import unicodedata
import string
from math import radians, sin, cos, acos


def parser(mypath):
    coppia = []

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    for t_file in onlyfiles:
        f = file(str(mypath)+t_file)
        s = f.read()
        s = ''.join(x if x in string.printable else "?" for x in s)
        s = s.split('*Z ')
        s.pop(0)
        for trip in s:
            lines = trip.split("\n")

            first_line = lines.pop(0).split(" ")[:2]
            second_line = lines[0].split(" ")[:2]
            first_line[1] = first_line[1].replace("-", "")+second_line[1]

            corsa = first_line[0]
            linea = first_line[1]

            while lines[0].split(" ")[0][0] == '*':
                lines.pop(0)
            fermate = []
            for line in lines:
                cod_fermata = line[0:9]
                # stazione=line[10:30]
                start = line[32:37]
                finish = line[39:44]

                if cod_fermata != '':
                    fermate.append([cod_fermata, start, finish])
                    if start != "     ":
                        stazione1 = fermate[len(fermate)-2]
                        stazione2 = fermate[len(fermate)-1]
                        coppia.append(
                            [stazione1[0], stazione2[0], stazione1[2], stazione2[1], corsa, linea])
        f.close()

    f = open("data/viaggi.csv", "w")
    for i in coppia:
        for j in i:
            f.write(j+"\t")
        f.write("\n")


def readCord(mypath):
    # return: una mappa key:codStaz -> value:(long,lat)

    f = file(mypath)
    s = f.read()
    s = ''.join(x if x in string.printable else "?" for x in s)
    s = s.split('\n')
    s = s[2:]
    s.pop(-1)

    bfkoord = dict()  # key:codStaz -> value:(long,lat)
    for row in s:
        data = row.split(" ")
        data = filter(lambda r: r != "", data)

        codStaz = data[0]
        longitud = float(data[1])
        lat = float(data[2])
        bfkoord[codStaz] = [longitud, lat]
    f.close()

    return bfkoord
