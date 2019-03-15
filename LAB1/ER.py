import graph
import random

def ERNotOrientedGraph(nodeL,p):
    # desc : Crea un grafo non orientato casuale con probabilità
    #        di presenza di ogni arco pari a p
    # nodeL : array con le label iniziali 
    # p : probabilita' di pescare un nodo p in [0,100)
    #     numero di biglietti inseriti a estrazione
    # tempo = O(len(nodeL)^2)

    #empty graph
    G=graph.NotOrientedGraph()

    for label in nodeL:
        G.addNode(label)
    label=G.nodes.keys()
    for i in range(len(label)):
        for j in range(len(label)):
            a=random.uniform(0,1)
            if a<p and i<j:
                G.addEdge(label[i],label[j])

    return G