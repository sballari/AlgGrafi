import parserCoord
from dijkstra import dijkstra
from graph import Hour, OrientedGraph
import time

#creo il grafo orientato
G = OrientedGraph.inputGraph("viaggi.csv")

#informazioni viaggio magari da buttare su un file
From="200417051"
tm="02355"
To="140701016"

#lancio dijkstra che mi restituisce d
elapsedtime=time.time()
data,parent=dijkstra(G,From,Hour(tm))
print time.time()-elapsedtime

#stampo soluzione di viaggio
i=To
print i,[str(j) for j in data[i]]
while parent[i]!=None:
    print parent[i],[str(j) for j in data[i]]
    i=parent[i]
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
