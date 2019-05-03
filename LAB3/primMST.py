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
        #range_ = range(n)
        #range_.remove(u)
        for v in Q.A: #il grafo e' completo
            if G.getweight(u,v) < key[v]:
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

def pi2Tree(piMap):
    #desc: converte la mappa dei predecessori in un albero classico
    #piMap : mappa dei padri di ogni nodo
    #return : mappa dei successori
    if len(piMap) == 0 : return None
    else: 
        if len(piMap) == 1  :
            el,padre = piMap.popitem()
            return {padre: [el]}
        else:    
            el,padre = piMap.popitem()
            tree = pi2Tree(piMap)
            if padre in tree : tree[padre].append(el)
            else: tree[padre]=[el] 
            return tree


def costPi(piMap,G):
    somma = 0
    for p in piMap:
        el = piMap[p]
        somma += G.getweight(p,el)
    return somma
