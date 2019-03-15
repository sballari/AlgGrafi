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
G1.plotGraph()

