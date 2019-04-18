from graph import MatrixCompleteGraph
import HK
import randomInsertion

b14 = "burma14"
u22 = "ulysses22"
ds_name = b14

G = MatrixCompleteGraph.createGraphFromTSP(ds_name+".tsp")

circ = randomInsertion.RandomInsertion(G)
print circ 
print randomInsertion.weightCirc(circ,G)

print HK.HKTSP(G)
