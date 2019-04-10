from graph import MatrixCompleteGraph

def HKTSP(G) :
    D = [dict()] * len(G.weight_matrix)
    P = [dict()] * len(G.weight_matrix)
    S = set(range(0,len(G.weight_matrix)))
    ret = HKVisit(0,S,G,D,P)
    print D
    return ret

def HKVisit(v,S,G,D,P) : 
    # v : vertice di arrivo
    # G : grafo pesato delle distanze
    # S : vertici che devo visitare partendo da 0 n-1 -> e' un Set
    
    if len(S)==1 :
            v_index = S.copy().pop()
            return G.getweight(v_index,0)
    else:
        if D[v].get(str(S)) != None:
            return D[v][str(S)]

        else:
            mindist = None
            minprec = None
            S_=S.difference({v}) # S=S\{v}
            
            for u in S_:
                print (u,S_)
                dist=HKVisit(u,S_,G,D,P)+G.getweight(u,v)
                if mindist == None:
                    mindist = dist
                    minprec = u
                else:
                    if dist < mindist:
                        mindist = dist
                        minprec = u
            D[v][str(S)] = mindist
            P[v][str(S)] = minprec
            return mindist