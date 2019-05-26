from FastClosestPair import * 
from Coord import *

def insertP(list, n): 
    index =0
    # Searching for the position 
    for i in range(len(list)): 
        if list[i].getX() > n.getX(): 
            index = i 
            break

      
    # Inserting n in the list 
    new_list = list[:index] + [n] + list[index:]
    return new_list,index+1

def insertS(list, n): 
    index = 0
    for i in range(len(list)): 
        if list[i].getY() > n.getY(): 
            index = i 
            break
      
    # Inserting n in the list 
    new_list = list[:index] + [n] + list[index:]
    return new_list,index+1

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
    centery = sorted(centerx,key=lambda y : y.getY())

    while len(clusters) > k:

        closestPoints = FastClosestPair(centerx,centery,(0,len(clusters)))
        print "----------------------------------"

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
        print closestPoints[0],index1,index2
        print len(centerx),len(centery),len(clusters)

        centerx1 = centerx[index1]
        centery1 = centerx[index1]
        cluster1 = clusters[index1]

        centerx2 = centerx[index2]
        centery2 = centerx[index2]
        cluster2 = clusters[index2]

        print cluster1,cluster2

        clusters.remove(cluster1)
        clusters.remove(cluster2)

        centerx.remove(centerx1)
        centerx.remove(centerx2)

        centery.remove(centery1)
        centery.remove(centery2)

        print len(centerx),len(centery),len(clusters)

        new_clusters = cluster1.union(cluster2)

        new_center = newCenter(new_clusters)

        centery,index=insertS(centery, new_center)
        centerx,index = insertP(centerx, new_center)
        clusters.insert(index, new_clusters)
        print len(centerx),len(centery),len(clusters)

    return centerx,clusters
