import primMST

def MSTApprox(G):
    mst = primMST.PrimMST(G,0)
    tree = primMST.pi2Tree(mst)
    en = enumeration(tree,0)
    en.append(0)
    return en



def enumeration(tree,v):
    #desc mette le label in una lista ordinata per priorita'
    #tree: mappa dei successori
    #v: vertice da esaminare
    #n: numero degli elementi nella lista dei successori
    if (v in tree) == False :
        return [v] # e' una foglia
    else : 
        # v e' in tree -> ha almeno un successore
        A = [v]
        for c in tree[v] :
            if c != v : 
                A = A+enumeration(tree,c)
        return A

def weightCirc(circ,G):
    somma = 0
    for j in range(1, len(circ)):
        i = j-1
        dij = G.getweight(circ[i],circ[j])
        somma += dij
    return somma