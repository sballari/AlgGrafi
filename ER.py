import graph
import random

# nodeL : array con le label iniziali 
# p : probabilita' di pescare un nodo p = (0,100)
#     numero di biglietti inseriti a estrazione
def ERGraph(nodeL,p):
    G=graph.Graph() #empty own graph

    for label in nodeL:
        G.addNode(graph.Node(label))
    label=G.nodes.keys()
    for i in range(len(label)):
        for j in range(len(label)):
            a=random.randint(0,10)
            if a<p and i<j:
                G.addDoubleEdge(label[i],label[j])

    return G