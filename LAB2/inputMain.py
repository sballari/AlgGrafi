import graph
import sys
from tqdm import tqdm
import heap
import dijkstra
sys.setrecursionlimit(1000000)

G = graph.OrientedGraph.inputGraph("/home/rossidaniel/ownCloud/viaggi.csv")

h=dijkstra.algo(G)
i="300000044"
#while h.parent[i]!=None:
#    print h.parent[i],[str(j) for j in h.data[i]]
#    i=h.parent[i]

#for i in h.data:
#    print [str(j) for j in h.data[i]]