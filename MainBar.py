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
from tqdm import tqdm

sys.setrecursionlimit(10000)

G1 =IOG.IOGraph ('test/as20000102.txt', False)
G2 =IOG.IOGraph ('test/ER0.txt', False)
G3 =IOG.IOGraph ('test/UPA0.txt', False)

G={
    'real': G1,
    'ER': G2,
    'UPA': G3
}

#avg = str(G.avg_degree())
#print "degree DPA: "+str(avg)
#print 'archi:', G.getEdgeNumber()
#print "fine generazione [0..6474]"
# print "fine ER"
dim_CC_maxs=[] #dimensione della componente connessa massima al variare del tempo
keys=[]
index=[]

NumNodes=6474

#simulazione attacco casuale
for g in G:
    for i in tqdm(range(NumNodes),desc=g):
        nodeOff.MaxDegreeOffNode(G[g])
        arrayCC=CC.ConnectedComponets(G[g])
        dim_CC_maxs.append(CC.dim_CC_max(arrayCC))
        index.append(i)
        keys.append(g)
        
df=pd.DataFrame(data={'dim_CC_maxs': dim_CC_maxs,'index': index, 'key': keys})

sns.pairplot(x_vars=["index"], y_vars=["dim_CC_maxs"], data=df, hue="key",plot_kws=dict(s=50), markers="+",height=10)
plt.show()
