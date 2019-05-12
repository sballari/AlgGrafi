
# P : lista dei punti -> [[id_contea, x_val, y_val, population, risk]]
# k : numero di cluster richiesti

def HierarchicalClustering(P,k):
    # n = len(P)
    C = []
    for point in P:
        C.append({point})
    while len(C) > k:
        
