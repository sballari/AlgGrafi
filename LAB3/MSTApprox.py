import primMST
import time

def MSTApprox(G):
    # descr : algoritmo che risolve il problema TSP sul grafo G usando l'albero di copertura minimo di G. La soluzione ottenuta e' 2-approssimata
    # G : grafo pesato
    # ret : tupla contenente il circuito hamiltoniano approssima con il MST e il tempo di esecuzione dell'algoritmo

    tm = time.time()
    mst = primMST.PrimMST(G,0)
    tree = primMST.pi2Tree(mst)
    circ = enumeration(tree,0)
    circ.append(0)
    tm = time.time() - tm
    return circ,tm



def enumeration(tree,v):
    # desc : mette le label in una lista ordinata secondo una visita in profondita'
    # tree : mappa dei successori
    # v : vertice radice
    if (v in tree) == False :
        return [v]
    else : 
        A = [v]
        for c in tree[v] :
            if c != v : 
                A = A+enumeration(tree,c)
        return A

