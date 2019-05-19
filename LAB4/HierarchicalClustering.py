from FastClosestPair import FastClosestPair 
from Coord import *

# cluster : set di punti
def newCenter(cluster):
    x = 0
    y = 0
    for point in cluster:
        x = x + point.getX() 
        y = y + point.getY()
    x = x / len(cluster)
    y = y / len(cluster)
    return Center(x,y)

# P : [Point]
# k : numero di cluster richiesti

# point : oggetto di tipo Point -> getX,getY
# Cluster : e' un set di Point
# Centers : lista di centroidi -> Centers[i] e' il centroide di Clusters[i]
# cen : oggetto di tipo Center -> getX,getY

def HierarchicalClustering(P,k):
    Clusters = [] 
    for point in P:
        clu = {point}
        Clusters.append(clu) # len(P) clusters, ognuno con 1 singolo punto
    Centers = [Center(0,0) for j in range(len(Clusters))]
    while len(Clusters) > k:
        for index in range(len(Clusters)):
            Centers[index] = newCenter(Clusters[index])
            #print Centers
        closestPoints = FastClosestPair(Centers,Centers,(0,len(Centers)-1))
        index1 = closestPoints[1]
        index2 = closestPoints[2]
        Clusters[index1] = Clusters[index1].union(Clusters[index2])
        Clusters.remove(Clusters[index2])
        Centers.remove(Centers[index2])
    return Clusters
