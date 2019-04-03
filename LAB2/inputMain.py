from dijkstra import dijkstra
from graph import OrientedGraph,Hour

#creo il grafo orientato
G = OrientedGraph.inputGraph("viaggi.csv")

#informazioni viaggio magari da buttare su un file
From="200417051"
tm="02355"
To="140701016"

#lancio dijkstra che mi restituisce d
data,parent=dijkstra(G,From,Hour(tm))

#stampo soluzione di viaggio
i=To
print i,[str(j) for j in data[i]]
while parent[i]!=None:
    print parent[i],[str(j) for j in data[i]]
    i=parent[i]
