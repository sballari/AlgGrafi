import heap 
import graph


def PrimMST(G,root):
    #G grafo 
    #root : indice del vertice da cui fare partire l'albero

    n = G.getNumNodes()
    key, pi = keyPiInit(n,root,G)  

    #arco minimo che collega v all'albero parziale. 
    #None non c'e' arco per convenzione.

    #key[root] = 0 #non serva e' in keypi init
    Q = buildHeap(n,key,root)
    while Q.isEmpty() == False :
        u = Q.extractMin()
        #trovo l'arco minimo tra u e tutti gli altri nodi 
        range_ = range(n)
        range_.remove(u)
        for v in range_: #il grafo e' completo
            if Q.isPresent(v) and G.getweight(u,v) < key[v]:
                key[v] = G.getweight(u,v)
                pi[v] = u
                Q.decreaseKey(v,key[v])
        #endfor
    #endwhile
    
    return pi



 
def keyPiInit(dim,root,G):
    key = dict()
    pi = dict()
    for i in range(dim):
        key[i] = G.getweight(root,i)
        pi[i] = root
    return key,pi


def buildHeap(n,keys,root):
    Q = heap.heap()
    indexs = range(n)
    indexs.remove(root)
    for i in indexs: 
        Q.add(i,keys[i])
    return Q
