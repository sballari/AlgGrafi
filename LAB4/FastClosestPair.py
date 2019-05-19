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
        t = min(FastClosestPair(P,SL,PL),FastClosestPair(P,SR,PR))
        mid = 0.5 * (P[m].getX()+P[m+1].getX())
        return minTuple(t,ClosestPairStrip(S,mid,t[0]))


def SlowClosestPair(P,Pslice):
    l = Pslice[0] #1
    r = Pslice[1] #3
    minI = -1 
    minJ = -1
    minD = float("inf")
    for i in range(l,r-1): #(1,2)
        for j in range (i+1,r): #(2,3)
            d = euclide(P[i],P[j])
            if d < minD:
                minD = d
                minI = i
                minJ = j
    return (minD,minI,minJ)

def euclide(p1,p2):
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    return ((x1-x2)**2+(y1-y2)**2)**0.5
    
# suddivide Y in YL e YR
def Split(S,P,PL,PR):
    SL = []
    SR = []
    for s in S:
        if binarySearch(s,P,PL) == True:
            SL.append(s)
        else:
            SR.append(s)
    return SL,SR


def binarySearch(s,P,Pslice):
    l=Pslice[0]
    r=Pslice[1]
    if l + 1 == r: 
        return s.getX() == P[l].getX() and s.getY() == P[l].getY()

    else:
        m = (l + r)/2
        if s.getX() < P[m].getX():
            return binarySearch(s,P,(l,m))
        if s.getX() > P[m].getX():
            return binarySearch(s,P,(m,r))
        i=m-1
        found = False
        while P[i].getX() == s.getX() and i >= l and found!=True:
            if s.getY() == P[i].getY():
                found = True
            i=i-1
        if found != True:
            i = m
            while P[i].getX() == s.getX() and i < r and found!=True:
                if s.getY() == P[i].getY():
                    found = True
                i=i+1
        return found

def minTuple(t1,t2):
    if t1[0] < t2[0]:
        return t1
    else:
        return t2

def ClosestPairStrip(S,mid,d):
    S_ = []
    for i in range(len(S)):
        if abs(S[i].getX()-mid) < d:
            s_ = (i,S[i])
            S_.append(s_)
    minDist = (float("inf"),-1,-1)
    for u in range(len(S_)-1):
        for v in range(u+1,min(u+6,len(S_))):
            uv = (euclide(S_[u][1],S_[v][1]),S_[u][0],S_[v][0])
            minDist = minTuple(minDist,uv)
    return minDist
