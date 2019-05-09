from graph import MatrixCompleteGraph
import time

def HKTSP(G,time_limit=300):
    # G : grafo pesata 
    # time_limit : tempo in secondi massimo di esecuzione prima della terminazione forzata
    # return: tupla distanza soluzione migliore trovata nel tempo limite e tempo di esecuzione

    D = [dict() for i in range(len(G.weight_matrix))] 
    P = [dict() for i in range(len(G.weight_matrix))] 
    S = set(range(0, len(G.weight_matrix)))
    l=[time_limit]
    ret = HKVisit(0, S, G, D, P,l)
    tm=round(time_limit-l[0],2)

    return ret,tm


def HKVisit(v, S, G, D, P,time_limit):
    # v : vertice di arrivo
    # G : grafo pesato delle distanze
    # S : vertici che devo visitare partendo da 0 n-1 -> e' un Set
    
    tm=time.time()
    if len(S) == 1:
        time_limit[0]-=time.time()-tm
        return G.getweight(v, 0) # v in S per ipotesi
    
    if D[v].get(str(S)) != None:
        time_limit[0]-=time.time()-tm
        return D[v][str(S)]

    mindist = None
    minprec = None
    S_ = S.difference({v})  # S=S\{v}
    time_limit[0]-=time.time()-tm
    
    for u in S_:
        
        dist = HKVisit(u, S_, G, D, P,time_limit)+G.getweight(u, v)
        tm=time.time()
        if mindist == None:
            mindist = dist
            minprec = u
        else:
            if dist < mindist:
                mindist = dist
                minprec = u

        time_limit[0]-=time.time()-tm

        if time_limit[0] < 1:
            break
    D[v][str(S)] = mindist
    P[v][str(S)] = minprec
    return mindist