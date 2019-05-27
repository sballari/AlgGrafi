from FastClosestPair import * 
from Coord import *

def insertP(ls, n): 
    index = -1
    # Searching for the position 
    for i in range(len(ls)): 
        if ls[i].getX() > n.getX(): 
            index = i 
            break

    if index == -1:
        ls.append(n)
        return ls,len(ls)-1
    else:
        new_list = ls[:index] + [n] + ls[index:]
        return new_list,index

def insertS(ls, n): 
    index = -1
    for i in range(len(ls)): 
        if ls[i].getY() > n.getY(): 
            index = i 
            break

    if index == -1:
        ls.append(n)
        return ls,len(ls)-1
    else:
        new_list = ls[:index] + [n] + ls[index:]
        return new_list,index

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
        print "**********************************************************"
        print len(centerx),len(centery),len(clusters)
        for c_index in range(len(clusters)):
            print c_index, [str(c) for c in clusters[c_index]], str(centerx[c_index])

        closestPoints = FastClosestPair(centerx,centery,(0,len(clusters)))

        print closestPoints,

        minDist = (float("inf"),-1,-1)
        for i in range(len(centerx)):
            for j in range(len(centerx)):
                if i < j:
                    ij = (euclide(centerx[i],centerx[j]),i,j)
                    minDist=minTuple(minDist,ij)
        print minDist

        if closestPoints[0] != minDist[0]:
            print "qualcosa non vaaaa"
            break

        index1 = closestPoints[1]
        index2 = closestPoints[2]
        """
        print closestPoints[0],index1,index2
        print len(centerx),len(centery),len(clusters)
        """
        centerx1 = centerx[index1]
        centery1 = centerx[index1]
        cluster1 = clusters[index1]

        centerx2 = centerx[index2]
        centery2 = centerx[index2]
        cluster2 = clusters[index2]
        """
        print euclide(centerx1,centerx2 )
        for c_index in range(len(clusters)):
            print c_index, [str(c) for c in clusters[c_index]], str(centerx[c_index])
        """
        clusters.remove(cluster1)
        clusters.remove(cluster2)

        centerx.remove(centerx1)
        centerx.remove(centerx2)

        centery.remove(centery1)
        centery.remove(centery2)
        """
        print ""
        for c_index in range(len(clusters)):
            print c_index, [str(c) for c in clusters[c_index]], str(centerx[c_index])
        print ""
        print len(centerx),len(centery),len(clusters)
        """
        new_clusters = cluster1.union(cluster2)

        new_center = newCenter(new_clusters)

        centery,index=insertS(centery, new_center)
        centerx,index = insertP(centerx, new_center)
        clusters.insert(index, new_clusters)
        """
        print len(centerx),len(centery),len(clusters)

        for c_index in range(len(clusters)):
            print c_index, [str(c) for c in clusters[c_index]], str(centerx[c_index])
        for c in centerx:
            print c,
        print ""
        for c in centery:
            print c,
        print ""
        """
    return centerx,clusters
