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
    return (float((x1-x2)**2+(y1-y2)**2))**0.5

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