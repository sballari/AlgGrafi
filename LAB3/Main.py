from graph import MatrixCompleteGraph
from HK import HKTSP
from randomInsertion import RandomInsertion
import MSTApprox
import primMST
import pandas as pd
from os import listdir
from os.path import isfile, join
from sys import setrecursionlimit
from pandas.compat import OrderedDict

setrecursionlimit(10000)

f=open("dataset/data_opt.csv","r")
s=f.read()
s=s.split("\n")
optSol=[i.split() for i in s]

data = OrderedDict()

data["index"] = []

data["sol_HK"] = []
data["tempo_HK"] = []
data["errore_HK"] = []

data["sol_r"] = []
data["tempo_r"] = []
data["errore_r"] = [] 

data["sol_MSTA"] = []
data["tempo_MSTA"] = []
data["errore_MSTA"] = []

for ds_name, opt_sol in optSol:
    print "------------------INIZIO "+ds_name+" ------------"
    G = MatrixCompleteGraph.createGraphFromTSP(ds_name)
    data["index"].append(ds_name)
    
    #HELD-KARP ALGORITHM
    print "esecuzione hk: "+ds_name
    sol,tm= HKTSP(G,120)
    tm='%.2E' % tm
    print "costo soluzione: "+str(sol)
    print "tempo esecuzione: "+str(tm)
    errore=round(float(sol-int(opt_sol))/int(opt_sol)*100,2)
    print "errore: "+str(errore)
    data["sol_HK"].append(sol)
    data["tempo_HK"].append(tm)
    data["errore_HK"].append(errore)
    
    #RANDOM INSERTION
    print "esecuzione random insertion: "+ds_name
    sol,tm= RandomInsertion(G)
    sol= G.weightCirc(sol)
    tm='%.2E' % tm
    print "costo soluzione: "+str(sol)
    print "tempo esecuzione: "+str(tm)
    errore=round(float(sol-int(opt_sol))/int(opt_sol)*100,2)
    print "errore: "+str(errore)
    data["sol_r"].append(sol)
    data["tempo_r"].append(tm)
    data["errore_r"].append(errore)
    
    #MST APPROX ALGORITHM
    print "esecuzione MSTApprox: "+ds_name
    sol,tm= MSTApprox.MSTApprox(G)
    sol = G.weightCirc(sol)
    tm='%.2E' % tm
    print "costo soluzione: "+str(sol)
    print "tempo esecuzione: "+str(tm)
    errore=round(float(sol-int(opt_sol))/int(opt_sol)*100,2)
    print "errore: "+str(errore)
    data["sol_MSTA"].append(sol)
    data["tempo_MSTA"].append(tm)
    data["errore_MSTA"].append(errore)
    

df=pd.DataFrame(data)
df.set_index("index",inplace=True)
with open('relazione/mytable.tex', 'w') as tf:
     tf.write(df.to_latex(index=True))






