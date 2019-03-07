import random 
import graph

def randomOffNode(G):
    if len(G.nodes) > 0:
        off=random.choice(G.nodes.keys())
        print 'nodo eliminato: ',off
        G.subNode(off)
    else:
        print 'grafo vuoto'