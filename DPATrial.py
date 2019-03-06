import random
import graph

def DpaGraph(m,nodesL):
    G=graph.Graph() #empty own graph
    for i in nodesL:
        G.addNode(graph.Node(i))

    urn_nodes=[]  #scelta urna iniziale da nodi iniziali
    for i in range(m):
        label=random.choice([i for i in G.nodes])
        urn_nodes.append(label)

    urn_nodes =DPATrial(urn_nodes)

    for node1 in G.nodes:
        Vi= RunTrial(urn_nodes,node1,m)
        for node2 in Vi: #man mano che pesco creo il grafo
            G.addEdge(node1,node2)
    return G

# nodes : urna iniziale 
# setta l'urna con m volte ogni nodo
def DPATrial(nodes):
    V=[]
    for i in range(len(nodes)): #len corrisponde a m
        V+=nodes
    return V

# urn : urna
# nodeLabel : nodo che esegue la pescata
# m : numero di estrazioni da fare
def RunTrial(urn,node_label,m): #estrazione di nodeLabel
    Vi=[] #nodi pescati
    for i in range(m):
        Vi.append(random.choice(urn))
    urn.append(node_label) #biglietto bianco
    urn+=Vi #amplio l'urna con i cloni, biglietti gialli
    return Vi
