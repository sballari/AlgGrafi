import graph
import random
import DPATrial as DPA
import ER 
import nodeOff
import CC
import time
import pandas as pd
import matplotlib.pyplot as plt



def IOGraph(file,isDirected):

    f=open(file,'r')
    s = f.read()
    s=s.split('\n')
    for i in range(len(s)):
        s[i]=s[i].split('\t')
    
    if isDirected :
        G = graph.NotOrientedGraph() 
    else:
        G = graph.OrientedGraph()

    for i in range(len(s)-1):
        G.addEdge(s[i][0],s[i][1])
    
    return G