import random
import graph


def UpaGraph(m,nodesL):
    # desc : Crea un grafo non orientato casuale con numero di 
    #        estrazioni a turno pari a m
    # nodesL : lista delle label dei nodi da usare per costruire il grafo
    # tempo : O(len(nodesL)*m + m^2)
    
    G=graph.NotOrientedGraph() #empty own graph
    for i in nodesL:
        G.addNode(i)

    urn_nodes=[]  
    # inizializzo l'urna  :
    # scelgo m nodi casuali da nodesL e
    # metto dei nodi scelti m-volte nell'urna 
    label = random.sample(G.nodesLabel,m)
    for i in label:
        for j in m:
            urn_nodes.append(label[i])
    

    for node1 in G.nodes:
        Vi= RunTrial(urn_nodes,node1,m) #O(n*m)
        for node2 in Vi: #man mano che pesco creo il grafo
            G.addEdge(node1,node2)
    return G




def RunTrial(urn,node_label,m):
    # desc : estrazione di m nodi casuali
    # urn : urna da cui pescare
    # node_label : label del nodo che effettua l'estrazione
    # m : numero di estrazioni da fare
    # tempo : O(m)

    Vi=[] #nodi pescati
    for i in range(m):
        Vi.append(random.choice(urn))
    urn.append(node_label) #biglietto bianco
    urn+=Vi #amplio l'urna con i cloni, biglietti gialli
    return Vi
