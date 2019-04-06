import parserCoord
from dijkstra import dijkstra
from graph import Hour, OrientedGraph
import time

#creo il grafo orientato
G = OrientedGraph.inputGraph("viaggi.csv")

#informazioni viaggio magari da buttare su un file
From="300000032"
tm="00530"
To="400000122"

#lancio dijkstra che mi restituisce d
elapsedtime=time.time()
data,parent=dijkstra(G,From,Hour(tm))
print "Elapsed Time:",time.time()-elapsedtime

#stampo soluzione di viaggio
i=To

points=[]

stazioni = []

while parent[i]!=None:
    points.append([i,parent[i]])
    stazioni.append((i,data[i]))
    i=parent[i]

print "Viaggio da",From,"a",To
print "Orario di partenza:",data[From][2]
print "Orario di arrivo:",data[To][0]
i=len(stazioni)-1

cod=''
staz=From
while i >= 0:
    if cod != data[stazioni[i][0]][3]:
        if i+1 == len(stazioni):
            print stazioni[i][1][2],"corsa",data[stazioni[i][0]][3],data[stazioni[i][0]][4],"da",staz,"a",
        else:
            print staz
            print stazioni[i][1][2],"corsa",data[stazioni[i][0]][3],data[stazioni[i][0]][4],"da",stazioni[i][0],"a",
        cod = data[stazioni[i][0]][3]
        staz=stazioni[i][0]
    i-=1
print To

G.plotGraph(points)
"""

#########################
### codice prova dist ###
#########################
coordMap = parserCoord.readCord()
distanza = parserCoord.distance("200419036", "200802002", coordMap)
print distanza

# A: 200419036	logn lat ('6.121555', '49.616270',
# B : 200802002	('6.135915', '49.671235')
"""
