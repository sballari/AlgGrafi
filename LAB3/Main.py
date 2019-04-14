from graph import MatrixCompleteGraph
import HK

b14 = "burma14"
u22 = "ulysses22"
ds_name = b14

G = MatrixCompleteGraph.createGraphFromTSP(ds_name+".tsp")

print HK.HKTSP(G)