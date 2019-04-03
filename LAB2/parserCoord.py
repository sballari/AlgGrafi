from os import listdir
from os.path import isfile, join
import unicodedata
import string

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
    f.write("\n")
