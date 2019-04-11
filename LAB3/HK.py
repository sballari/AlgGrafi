from graph import MatrixCompleteGraph


def HKTSP(G):
    D = [dict() for i in range(len(G.weight_matrix))] 
    P = [dict() for i in range(len(G.weight_matrix))] 
    S = set(range(0, len(G.weight_matrix)))
    ret = HKVisit(0, S, G, D, P)
    return ret


def HKVisit(v, S, G, D, P):
    # v : vertice di arrivo
    # G : grafo pesato delle distanze
    # S : vertici che devo visitare partendo da 0 n-1 -> e' un Set

    if len(S) == 1:
        return G.getweight(v, 0) # v in S per ipotesi
    else:
        if D[v].get(str(S)) != None:
            return D[v][str(S)]

        else:
            mindist = None
            minprec = None
            S_ = S.difference({v})  # S=S\{v}

            for u in S_:
                dist = HKVisit(u, S_, G, D, P)+G.getweight(u, v)
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