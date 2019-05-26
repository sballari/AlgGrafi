from FastClosestPair import * 
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
# cluster : e' un set di Point
# Centers : lista di centroidi -> Centers[i] e' il centroide di clusters[i]
# cen : oggetto di tipo Center -> getX,getY

def Hierarchicalclustering(P,k):
    clusters = [{point} for point in P]
    centerx = [newCenter([point]) for point in P]

    while len(clusters) > k:
        for c in range(len(clusters)):
            centerx[c] = newCenter(clusters[c])
        centery = sorted(centerx,key=lambda y : y.getY())

        closestPoints = FastClosestPair(centerx,centery,(0,len(clusters)))
        print closestPoints,

        
        minDist = (float("inf"),-1,-1)
        for i in range(len(centerx)):
            for j in range(len(centerx)):
                if i < j:
                    ij = (euclide(centerx[i],centerx[j]),i,j)
                    minDist=minTuple(minDist,ij)
        print minDist
        

        index1 = closestPoints[1]
        index2 = closestPoints[2]
        clusters[index1] = clusters[index1].union(clusters[index2])
        clusters.remove(clusters[index2])
        centerx.remove(centerx[index2])
    return centerx,clusters
