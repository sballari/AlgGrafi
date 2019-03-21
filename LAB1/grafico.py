import graph
import random
import UPA
import ER 
import nodeOff
import CC
import networkx as nx
import time
import pandas as pd
import matplotlib.pyplot as plt
import sys
import seaborn as sns
from tqdm import tqdm

sys.setrecursionlimit(10000)

G1 =graph.NotOrientedGraph.inputGraph ('ER0.txt')
G1.plotGraph()
