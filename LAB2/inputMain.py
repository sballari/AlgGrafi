import graph
import sys
import heap
import dijkstra

G = graph.OrientedGraph.inputGraph("/home/rossidaniel/ownCloud/viaggi.csv")

From="200417051"
Hour="02340"
To="140701016"
h=dijkstra.algo(G,From,Hour)

i=To
print i,[str(j) for j in h.data[i]]
while h.parent[i]!=None:
    print h.parent[i],[str(j) for j in h.data[i]]
    i=h.parent[i]


"""
print "------------------"
z="220402027"
print "posso prendere un bus da "
for i in G.nodes:
    if z in G.nodes[i].adj:
        print i
print "per andare in ",z
print "+++++++++++++++++++"
print "da ",z,"posso andare in"
for i in G.nodes[z].adj:
    print i
for i in h.data:
    print i,[str(j) for j in h.data[i]]
"""
