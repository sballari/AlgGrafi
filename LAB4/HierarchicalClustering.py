from FastClosestPair import FastClosestPair
from Coord import Point,Center
from utility import newCenter,euclide

def binarySearchNewCenterP(p,P,l,r):
    #desc: esegue una ricerca binaria per trovare la posizione in cui inserire il nuovo centroide rispetto S
    #tempo: O(log(n))

    if l + 1 == r:
        return l 
    else:
        m = (l + r)/2
        if p.getX() < P[m].getX():
            return binarySearchNewCenterP(p,P,l,m)
        if p.getX() >= P[m].getX():
            return binarySearchNewCenterP(p,P,m,r)

def binarySearchNewCenterS(p,P,S,l,r):
    #desc: esegue una ricerca binaria per trovare la posizione in cui inserire il nuovo centroide rispetto S
    #tempo: O(log(n))

    if l + 1 == r:
        return l 
    else:
        m = (l + r)/2
        if p.getY() < P[S[m]].getY():
            return binarySearchNewCenterS(p,P,S,l,m)
        if p.getY() >= P[S[m]].getY():
            return binarySearchNewCenterS(p,P,S,m,r)

def binarySearchS(p,P,S,l,r):
    #desc: esegue una ricerca binaria per trovare la posizione del punto p nell'intervallo [l,r] in S
    #tempo: O(log(n))
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
        


def CalculateNewPS(P,S,clusters,center1,center2,count):
    #desc: elimina i centroidi center1 center2, inserisce il nuovo centroide e aggiorna gli array
    #tempo: O(n)
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

def Hierarchicalclustering(P,k,kmin=0,kmax=0):
    #desc: algoritmo per il calcolo di k centroidi
    #P: insieme di punti
    #k: numero di cluster finali
    #tempo: O(n^2 log(n)) con n=len(P)

    clusters = [{point} for point in P]
    centerx = [newCenter([P[p]],p) for p in range(len(P))]
    tmp = [(centerx[center],center) for center in range(len(centerx))]
    tmp = sorted(tmp,key=lambda y : y[0].getY())
    centery = [v[1] for v in tmp]

    counter = 0
    while len(centerx) > k:	

        closestPoints = FastClosestPair(centerx,centery,(0,len(clusters))) # (d,i,j) con i,j indici di centerx
        
        index1 = min(closestPoints[1],closestPoints[2])
        index2 = max(closestPoints[1],closestPoints[2])

        CalculateNewPS(centerx,centery,clusters,index1,index2,counter)
        counter+=1

    return centerx,clusters
