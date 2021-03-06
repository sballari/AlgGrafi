from Coord import Center
import random
from utility import newCenter,errore_distorsione,euclide

def partition(P,centers):
    #desc: crea i cluster
    #P: punti da inserire nei cluster
    #centers: centroidi
    #tempo: O(len(P)*len(centers))
    clusters=[[] for center in centers]
    for p in P:
        minDist=(float("inf"),-1)
        for center in range(len(centers)):
            dist = euclide(p,centers[center])

            if minDist[0] > dist:
                minDist = (dist,center)
        clusters[minDist[1]].append(p)
    return clusters
    
def kmeans(centers,P,k,q):
    #desc: algoritmo per la divisione dei punti in cluster.
    #centers: centri iniziali
    #P: punti da clusterizzare
    #k: numero di cluster
    #q: numero di interazioni dell'algoritmo
    #tempo: O(q*k*len(P)+k)

    centers= [Center(center.getX(),center.getY()) for center in centers]
    
    while q > 0:
        clusters = partition(P,centers)
        for c in range(len(clusters)):
            centers[c]=newCenter(clusters[c]) if len(clusters[c]) > 0 else centers[c]
        q=q-1
    return centers,clusters