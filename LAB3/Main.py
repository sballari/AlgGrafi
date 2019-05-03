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
optSol = {
    "burma14.tsp" : 3323,
    "ulysses22.tsp": 7013,
    "eil51.tsp": 426,
    "kroD100.tsp":21294,
    "gr229.tsp": 134602,
    "d493.tsp": 35002,
    "dsj1000.tsp": 	18659688
}

mypath="dataset"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
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


for ds_name in onlyfiles:
    print "------------------INIZIO "+ds_name+" ------------"
    G = MatrixCompleteGraph.createGraphFromTSP(ds_name)
    data["index"].append(ds_name)
    
    #HELD-KARP ALGORITHM
    print "esecuzione hk: "+ds_name
    sol,tm= HKTSP(G,120)
    tm=round(tm,3)
    print "costo soluzione: "+str(sol)
    print "tempo esecuzione: "+str(tm)
    errore=str(round(float(sol-optSol[ds_name])/optSol[ds_name]*100,2))+"%"
    print "errore: "+str(errore)
    data["sol_HK"].append(sol)
    data["tempo_HK"].append(tm)
    data["errore_HK"].append(errore)
    
    #RANDOM INSERTION
    print "esecuzione random insertione: "+ds_name
    sol,tm= RandomInsertion(G)
    sol= G.weightCirc(sol)
    tm=round(tm,3)
    print "costo soluzione: "+str(sol)
    print "tempo esecuzione: "+str(tm)
    errore=str(round(float(sol-optSol[ds_name])/optSol[ds_name]*100,2))+"%"
    print "errore: "+str(errore)
    data["sol_r"].append(sol)
    data["tempo_r"].append(tm)
    data["errore_r"].append(errore)
    
    #MST APPROX ALGORITHM
    print "esecuzione MSTApprox: "+ds_name
    sol,tm= MSTApprox.MSTApprox(G)
    sol = G.weightCirc(sol)
    tm=round(tm,3)
    print "costo soluzione: "+str(sol)
    print "tempo esecuzione: "+str(tm)
    errore=str(round(float(sol-optSol[ds_name])/optSol[ds_name]*100,2))+"%"
    print "errore: "+str(errore)
    data["sol_MSTA"].append(sol)
    data["tempo_MSTA"].append(tm)
    data["errore_MSTA"].append(errore)
    

df=pd.DataFrame(data)
df.set_index("index",inplace=True)
print df.to_latex(index=True)



