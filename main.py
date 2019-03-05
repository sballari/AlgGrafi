import graph
import random

G=graph.Graph() #empty own graph

for i in range(10):
    G.addNode(graph.Node(i))

p=10

for i in range(10):
    for j in range(10):
        a=random.randint(0,100)
        if a<p and i!=j:
            G.addEdge(i,j)

G.plotGraph()