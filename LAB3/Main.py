from graph import MatrixCompleteGraph
import HK

G = MatrixCompleteGraph.createGraphFromTSP("burma14.tsp")

# G = MatrixCompleteGraph(4)
# G.weight_matrix = [[0,4,1,3],[4,0,2,1],[1,2,0,5],[3,1,5,0]]
print HK.HKTSP(G)