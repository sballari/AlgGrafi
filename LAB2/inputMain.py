import graph
import sys
from tqdm import tqdm
import heap
import dijkstra
sys.setrecursionlimit(1000000)

G = graph.OrientedGraph.inputGraph("/home/rossidaniel/ownCloud/viaggi.csv")

d,p=dijkstra.algo(G)
i="300000044"
#while p[i]!=None:
#    print p[i],d[i]
#    i=p[i]