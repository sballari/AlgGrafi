from Coord import *
import random

def newCenter(cluster):
    x = 0
    y = 0
    for point in cluster:
        x = x + point.getX() 
        y = y + point.getY()
    x = x / len(cluster)
    y = y / len(cluster)
    return Center(x,y) 

def euclide(p1,p2):
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def partition(P,centers):
    clusters=[[] for center in centers]
    minDist=(float("inf"),-1)
    for p in P:
        for center in range(len(centers)):
            dist = euclide(p,centers[center])
            if minDist[0] > dist:
                minDist = (dist,center)
        clusters[minDist[1]].append(p)
    return clusters
def kmeans(P,k,q):
    centers=random.sample(P, k)

    while q > 0:
        clusters = partition(P,centers)
        print clusters
        for c in range(len(clusters)):
            centers[c]=newCenter(clusters[c])
    
    return centers,clusters