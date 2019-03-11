import graph
import random

# return: lista di liste in cui ogni sottolista contiene le label di una componente connessa
# del grafo iniziale
def ConnectedComponets(G):
    color={}
    for node in G.nodes:
        color[node]='white'
    CC=[]
    for node in G.nodes:
        if len(G.nodes[G.maxDegree].adj_out) < len(G.nodes[node].adj_out):
            G.maxDegree=node.label
        if color[node] == 'white':
            comp = DFS_visited(G,node,color)
            if len(comp) > 0:
                CC.append(comp)
    return CC

def DFS_visited(G,u,color):
    color[u]='gray'
    visited=[]
    for node in G.nodes[u].adj_out:
        if color[node] == 'white':
            visited+=DFS_visited(G,node,color)
    visited.append(u)
    color[u]='black'
    return visited

def resilienza(CC):
    if(len(CC) > 0):
        Cmax=len(max(CC, key=lambda coll: len(coll)))
        V=sum([len(i) for i in CC])
        return float(Cmax)/V
    return 0    

def dim_CC_max(CCs):
    if(len(CCs) > 0):
        return len(max(CCs, key=lambda coll: len(coll)))
    return 0   