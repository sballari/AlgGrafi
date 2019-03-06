import graph
import random

# nodeL : array con le label iniziali 
# p : probabilita' di pescare un nodo p = (0,100)
#     numero di biglietti inseriti a estrazione
def ERGraph(nodeL,p):
    G=graph.Graph() #empty own graph

    for label in nodeL:
        G.addNode(graph.Node(label))

    for node1 in G.nodes:
        for node2 in G.nodes:
            a=random.randint(0,100)
            if a<p and node1.label!=node2.label:
                G.addEdge(node1.label,node2.label)

    return G