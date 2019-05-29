def FastClosestPair(P,S,Pslice):
    l=Pslice[0]
    r=Pslice[1]
    n = r-l
    if n <= 3:
        return SlowClosestPair(P,Pslice)
    else:
        m = (l + r)/2
        PL = (l,m) #bound dx non incluso
        PR = (m,r) #bound dx non incluso
        SL,SR = Split(S,P,PL,PR)
        t = minTuple(FastClosestPair(P,SL,PL),FastClosestPair(P,SR,PR))
        mid = float(P[m].getX()+P[m-1].getX())/2
        minDist=minTuple(t,ClosestPairStrip(P,S,mid,t[0],Pslice))

        return minDist


def SlowClosestPair(P,Pslice):
    l = Pslice[0] 
    r = Pslice[1] 
    minDist = (float("inf"),-1,-1)

    for i in range(l,r-1): 
        for j in range (i+1 ,r): 
            ij = (euclide(P[i],P[j]),i,j)

            if ij[0] < minDist[0]:
                minDist = ij
    return minDist

def euclide(p1,p2):
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    return ((x1-x2)**2+(y1-y2)**2)**0.5
    
#suddivide Y in YL e YR
def Split(S,P,PL,PR):
    SL = []
    SR = []
    for s in S:
        if PL[0] <= s < PL[1]:
            SL.append(s)
        else:
            SR.append(s)
    return SL,SR

def minTuple(t1,t2):
    if t1[0] < t2[0]:
        return t1
    else:
        return t2

def ClosestPairStrip(P,S,mid,d,Pslice):
    S_ = []
    for s in S:
        if abs(P[s].getX()-mid) < d:
            S_.append(s)

    minDist = (float("inf"),-1,-1)

    for u in range(len(S_)-1):
        for v in range(u+1,min(u+6,len(S_))):
            uv = (euclide(P[S_[u]],P[S_[v]]),S_[u],S_[v])
            minDist = minTuple(minDist,uv)

    return minDist
