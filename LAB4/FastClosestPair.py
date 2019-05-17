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
        mid = 0.5 * (P[m][1]+P[m+1][1])
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
    return ((p1[1]-p2[1])**2+(p1[2]-p2[2])**2)**0.5
    
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
        return s[0] == P[l][0]
    else:
        m = (l + r)/2
        if s[1] < P[m][1]:
            return binarySearch(s,P,(l,m))
        if s[1] > P[m][1]:
            return binarySearch(s,P,(m,r))
        i=m-1
        found = False
        while P[i][1] == s[1] and i >= l and found!=True:
            if s[0] == P[i][0]:
                found = True
            i=i-1
        if found != True:
            i = m
            while P[i][1] == s[1] and i < r and found!=True:
                if s[0] == P[i][0]:
                    found = True
                i=i+1
        return found   

def minTuple(t1,t2):
    if t1[0]< t2[0]:
        return t1
    else:
        return t2

def ClosestPairStrip(S,mid,d):
    S_ = []
    for s in S:
        if abs(s[1]-mid) < d:
            S_.append(s)
    minDist = (float("inf"),-1,-1)
    for u in range(len(S_)-1):
        for v in range(u+1,min(u+6,len(S_))):
            uv = (euclide(S_[u],S_[v]),S_[u],S_[v])
            minDist = minTuple(minDist,uv)
    return minDist