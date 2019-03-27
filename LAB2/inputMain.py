import graph
import sys

 
sys.setrecursionlimit(1000000)

print "porcoddio"
G1 = graph.OrientedGraph.inputGraph("viaggi.csv")
print "fine"

for i in G1.nodes:
    for j in G1.nodes[i].adj:
        for k in G1.nodes[i].adj[j]:
            print k