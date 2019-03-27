import graph
import sys

 
sys.setrecursionlimit(1000000)

print "inizio lettura viaggi"
G1 = graph.OrientedGraph.inputGraph("viaggi.csv")
print "fine"

roma = G1.nodes["200403018"]
for key in roma.adj:
    print 'dest:',key, 'corresponds to', roma.adj[key]