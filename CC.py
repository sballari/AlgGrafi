import graph
import random

def ConnectedComponets(G):
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
    color[u]='gray'
    visited=[]
    for node in G.nodes[u].adj:
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