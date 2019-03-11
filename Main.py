import graph
import random
import DPATrial as DPA
import ER 
import nodeOff
import CC
import networkx as nx
import input_graph as IOG
import time
import pandas as pd
import matplotlib.pyplot as plt
import sys
import seaborn as sns
plot_kws={"s": 3}
sys.setrecursionlimit(10000)
rangeL = [i for i in range(6474)]
#G1 =IOG.IOGraph ('as20000102.txt', False)
G2 = ER.ERNotOrientedGraph(rangeL, 0.0006)
#G3 = DPA.DpaGraph(2,rangeL)

G={
#    'real': G1,
    'ER': G2
#    'UPA': G3
}

nodes=0

#avg = str(G.avg_degree())
#print "degree DPA: "+str(avg)
#print 'archi:', G.getEdgeNumber()
#print "fine generazione [0..6474]"
# print "fine ER"
dim_CC_maxs=[] #dimensione della componente connessa massima al variare del tempo
keys=[]
index=[]
tm=time.time()
#simulazione attacco casuale
while nodes < len(rangeL):
    nodes=nodes+1
    for g in G:
        print len(G[g].nodesLabel),
        nodeOff.MaxDegreeOffNode(G[g])
        arrayCC=CC.ConnectedComponets(G[g])
        dim_CC_maxs.append(CC.dim_CC_max(arrayCC))
        index.append(nodes)
        keys.append(g)
    print ''
print time.time()-tm

df=pd.DataFrame(data={'dim_CC_maxs': dim_CC_maxs,'index': index, 'key': keys})

sns.pairplot(x_vars=["index"], y_vars=["dim_CC_maxs"], data=df, hue="key",plot_kws=dict(s=50), markers="+",height=10)
plt.show()
