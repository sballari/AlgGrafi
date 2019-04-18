import heap 
import graph


def PrimMST(G,root):
    #G grafo 
    #root : indice del vertice da cui fare partire l'albero

    n = G.getNumberNodes()
    key, pi = keyPiInit(n)  
    
    successori = dict()
    for i in range(n):
        successori[i] = list[]

    #arco minimo che collega v all'albero parziale. 
    #None non c'e' arco per convenzione.

    key[root] = 0 #metto la radice nell'albero parziale
    Q = buildHeap(n,key)
    while Q.isEmpty() == False :
        u = Q.extractMin()
        #trovo l'arco minimo tra u e tutti gli altri nodi 
        for v in range(n): #il grafo e' completo
            if (v!=u):
                if Q.isPresent(v) && G.getweight(u,v) < key[v]:
                    key[v] = G.getweight(u,v)
                    pi[v] = u
                    successori[v].append(u)
                    Q.decreaseKey(v,key[v])
        #endfor
    #endwhile
    
    return successori



 
def keyPiInit(dim):
    key = dict()
    pi = dict()
    for i in range(dim):
        key[i] = None
        pi[i] = None
    return key,pi


def buildHeap(n,keys):
    Q = heap.heap()
    for i in range(n):
        Q.add(i,keys[i])
    return Q
