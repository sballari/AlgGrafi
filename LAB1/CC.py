import graph
import random


def ConnectedComponets(G):
    # desc: restituisce una lista di componenti connesse (CC), 
    #       ossia una lista di liste di label di nodi collegate tra loro
    # G : grafo da cui si vuole calcolare le CC
    # tempo : O(|V|+|E|)
    color={}
    for node in G.nodes:
        color[node]='white'
    CC=[]
    for node in G.nodes:
        if color[node] == 'white':
            comp = DFS_visited(G,node,color)
            if len(comp) > 0:
                CC.append(comp)
    return CC

def DFS_visited(G,u,color):
    # desc: attua la ricerca in profondita' a partire dal nodo u percorrendo
    #       archi che portano solo verso nodi bianchi
    # G : grafo non orientato
    # color : dizionario label -> colore
    
    color[u]='gray'
    visited=[]
    for node in G.nodes[u].adj:
        if color[node] == 'white':
            visited+=DFS_visited(G,node,color)
    visited.append(u)
    color[u]='black'
    return visited

def dim_CC_max(CCs):
    # desc : restituisce la dimensione della componente connessa piu' numerosa
    # CCS : lista di componenti connesse
    # tempo : O(len(CCs))
    if(len(CCs) > 0):
        return len(max(CCs, key=lambda coll: len(coll)))
    return 0