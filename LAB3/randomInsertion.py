import graph
import random

def RandomInsertion(G):
    circParz = [0]
    nodi_non_usati = range(1,G.getNumNodes())
    
    minimo = 1
    for i in range(1,G.getNumNodes()):
        if G.getweight(0,i) < G.getweight(0,minimo):
            minimo = i
    nodi_non_usati.pop(minimo-1)
    circParz.append(minimo)
    circParz.append(0)
    
    while len(nodi_non_usati) != 0 : 
        rint = random.randint(0,len(nodi_non_usati)-1)
        k = nodi_non_usati[rint]
        if rint == len(nodi_non_usati)-1:
            nodi_non_usati.pop()
        else:
            nodi_non_usati[rint] = nodi_non_usati.pop()

        minimaC = (0,1)
        for j in range(1,len(circParz)): 
            i= j-1
            djk = G.getweight(circParz[j],k)
            dik = G.getweight(circParz[i],k)
            dij = G.getweight(circParz[i],circParz[j])
            delta = djk + dik - dij
            if delta < G.getweight(circParz[minimaC[0]], circParz[minimaC[1]]):
                minimaC = (i,j)
        circParz.insert(minimaC[1],k)

    return circParz

def weightCirc(circ,G):
    somma = 0
    for j in range(1, len(circ)):
        i = j-1
        dij = G.getweight(circ[i],circ[j])
        somma += dij
    return somma



        




