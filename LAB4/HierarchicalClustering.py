from FastClosestPair import * 
from Coord import *
from tqdm import tqdm

def binarySearchNewCenterP(p,P,l,r):
    if l + 1 == r:
        return l 
    else:
        m = (l + r)/2
        if p.getX() < P[m].getX():
            return binarySearchNewCenterP(p,P,l,m)
        if p.getX() >= P[m].getX():
            return binarySearchNewCenterP(p,P,m,r)

def binarySearchNewCenterS(p,P,S,l,r):
    if l + 1 == r:
        return l 
    else:
        m = (l + r)/2
        if p.getY() < P[S[m]].getY():
            return binarySearchNewCenterS(p,P,S,l,m)
        if p.getY() >= P[S[m]].getY():
            return binarySearchNewCenterS(p,P,S,m,r)

def binarySearchS(p,P,S,l,r):
    if l + 1 == r:
        return l 
    else:
        m = (l + r)/2
        if p.getY() < P[S[m]].getY():
            return binarySearchS(p,P,S,l,m)
        if p.getY() > P[S[m]].getY():
            return binarySearchS(p,P,S,m,r)
        i=m-1
        found = -1
        while found==-1 and P[S[i]].getY() == p.getY() and i >= l:
            if p.idcenter == P[S[i]].idcenter:
                found = i
            i=i-1
        if found == -1:
            i = m
            while found == -1 and P[S[i]].getY() == p.getY() and i < r:

                if p.idcenter == P[S[i]].idcenter:
                    found = i
                i=i+1

        return found
        

# cluster : set di punti
def newCenter(cluster,idcenter):
    x = 0
    y = 0
    for point in cluster:
        x = x + point.getX() 
        y = y + point.getY()
    x = x / len(cluster)
    y = y / len(cluster)
    return Center(x,y,idcenter) 

def CalculateNewPS(P,S,clusters,center1,center2,count):
    new_cluster = clusters[center1].union(clusters[center2])
    new_center = newCenter(new_cluster,len(P)+count)

    yy1=binarySearchS(P[center1],P,S,0,len(S))
    yy2=binarySearchS(P[center2],P,S,0,len(S))

    y1=min(yy1,yy2)
    y2=max(yy1,yy2)

    x_center = binarySearchNewCenterP(new_center,P,center1,center2)
    y_center = binarySearchNewCenterS(new_center,P,S,y1,y2)

    s=0
    while s < len(S)-1:
        if s == y_center:
            S[s]=x_center
        else:
            if y1 <= s < y_center:
                S[s]=S[s+1]
            
            if s >= y2:
                S[s]=S[s+1]

            if center1 < S[s] <=x_center or S[s]> center2:
                S[s]=S[s]-1
        s=s+1
    S.pop()

    p=0
    while p < len(P)-1:
        if p == x_center:
            P[p]=new_center
            clusters[p]=new_cluster 
        else:
            if center1 <= p < x_center:
                P[p]=P[p+1]
                clusters[p]=clusters[p+1]
            
            if p >= center2:
                P[p]=P[p+1]
                clusters[p]=clusters[p+1]

        p=p+1
    P.pop()
    clusters.pop()

# P : [Point]
# k : numero di cluster richiesti

# point : oggetto di tipo Point -> getX,getY
# cluster : e' un set di Point
# Centers : lista di centroidi -> Centers[i] e' il centroide di clusters[i]
# cen : oggetto di tipo Center -> getX,getY

def Hierarchicalclustering(P,k):
    clusters = [{point} for point in P]
    centerx = [newCenter([P[p]],p) for p in range(len(P))]
    tmp = [(centerx[center],center) for center in range(len(centerx))]
    tmp = sorted(tmp,key=lambda y : y[0].getY())
    centery = [v[1] for v in tmp]

    counter = 0

    for z in tqdm(range(k,len(P))):

        closestPoints = FastClosestPair(centerx,centery,(0,len(clusters))) # (d,i,j) con i,j indici di centerx
        """
        print closestPoints,
        
        minDist = (float("inf"),-1,-1)
        for i in range(len(centerx)):
            for j in range(len(centerx)):
                if i < j:
                    ij = (euclide(centerx[i],centerx[j]),i,j)
                    minDist=minTuple(minDist,ij)
        print minDist
        """

        index1 = min(closestPoints[1],closestPoints[2])
        index2 = max(closestPoints[1],closestPoints[2])
        
        CalculateNewPS(centerx,centery,clusters,index1,index2,counter)
        counter+=1

    return centerx,clusters
