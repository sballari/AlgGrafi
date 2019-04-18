import primMST

def tspMST(G):
    succ_mst = primMST.PrimMST(G,0) 
    indexEnumerationMap = enumeration(succ_mst,0,1,dict())


def enumeration(succ,index,next_n,enumeration):
    # tree : nodo -> [nodo]
    enumerarion[index] = next_n
    for s in succ[index]
        enumeration(succ,s,next_n+1,enumeration)
    return 
    
    
    