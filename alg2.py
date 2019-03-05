import graph
import random
import DPATrial as DPA

G=graph.Graph() #empty own graph
for i in range(20):
    G.addNode(graph.Node(i))

n=1

initial_nodes=[]
for i in range(n):
    label=random.choice([i for i in G.nodes])
    initial_nodes.append(label)

dpa = DPA.DPATrial(initial_nodes)

for node1 in G.nodes:
    Vi=dpa.RunTrial(node1)
    for node2 in Vi:
        G.addEdge(node1,node2)

G.plotGraph()