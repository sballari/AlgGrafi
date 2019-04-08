import parserCoord
from dijkstra import dijkstra
from astar import astar
from graph import Hour, OrientedGraph
import time

#creo il grafo orientato
G = OrientedGraph.inputGraph("viaggi.csv")

#informazioni viaggio magari da buttare su un file
From="300000032"
tm="00530"
To="400000122"

print "A*"
#lancio dijkstra che mi restituisce d
elapsedtime=time.time()
data_astar,parent_astar=astar(G,From,To,Hour(tm))
print "Elapsed Time:",time.time()-elapsedtime

for i in data_astar:
    if data_astar[i] != []:
        data_astar[i] = data_astar[i][2]
points_astar=G.getSolution(From,To,parent_astar,data_astar)


print 
print "DIJKSTRA"
elapsedtime=time.time()
data_dijkstra,parent_dijkstra=dijkstra(G,From,Hour(tm))
print "Elapsed Time:",time.time()-elapsedtime

for i in data_dijkstra:
    if data_dijkstra[i] != []:
        data_dijkstra[i] = data_dijkstra[i][2]
points_dijkstra=G.getSolution(From,To,parent_dijkstra,data_dijkstra)

#G.plotGraph(points_dijkstra)
