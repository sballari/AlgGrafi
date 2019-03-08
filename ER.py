import graph
import random

# nodeL : array con le label iniziali 
# p : probabilita' di pescare un nodo p = (0,100)
#     numero di biglietti inseriti a estrazione
def ERNotOrientedGraph(nodeL,p):
    G=graph.NotOrientedGraph() #empty own graph

    for label in nodeL:
        G.addNode(label)
    label=G.nodes.keys()
    for i in range(len(label)):
        for j in range(len(label)):
            a=random.randint(0,10)
            if a<p and i<j:
                G.addEdge(label[i],label[j])

    return G

def EROrientedGraph(nodeL,p):
    G=graph.OrientedGraph() #empty own graph

    for label in nodeL:
        G.addNode(label)
    label=G.nodes.keys()
    for i in range(len(label)):
        for j in range(len(label)):
            a=random.randint(0,10)
            if a<p and i!=j:
                G.addEdge(label[i],label[j])

    return G