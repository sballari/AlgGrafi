import random 
import graph

def randomStrategy(G):
    # desc : sceglie un nodo casualmente e lo elimina dal grafo
    # G : grafo su cui effettuare l'attacco
    # tempo : O(len(G.nodes))
    if len(G.nodes) > 0:
        off=random.choice(G.nodes.keys())
        # la scelta non e' a tempo costante in quanto nel nostro codice 
        # le label usate non e' detto siano numeri 
        # incrementali (potrebbero essere stringhe o altro)
        G.subNode(off)

def maxDegreeStrategy(G):
    # desc : sceglie il nodo di grado massimo e lo elimina dal grafo
    # G : grafo su cui effettuare l'attacco
    # tempo : O(len(G.nodes))
    if len(G.nodes) > 0:
        G.subNode(G.get_Max_Degree_Node())
