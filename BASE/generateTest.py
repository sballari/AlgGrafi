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
rangeL = [i for i in range(6474)]
for i in range(5):
    G=DPA.DpaGraph(2,rangeL)
    G.writeOnFile('test/UPA'+str(i))

for i in range(5):
    G=ER.ERNotOrientedGraph(rangeL, 0.0006)
    G.writeOnFile('test/ER'+str(i))