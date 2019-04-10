from graph import MatrixCompleteGraph
Gs = []
Gs.append ( MatrixCompleteGraph.createGraphFromTSP("d493.tsp"))  #file0
Gs.append ( MatrixCompleteGraph.createGraphFromTSP("burma14.tsp")) #file1
Gs.append ( MatrixCompleteGraph.createGraphFromTSP("dsj1000.tsp")) #file2
Gs.append ( MatrixCompleteGraph.createGraphFromTSP("eil51.tsp")) #file3
Gs.append ( MatrixCompleteGraph.createGraphFromTSP("gr229.tsp")) #file4
Gs.append ( MatrixCompleteGraph.createGraphFromTSP("kroD100.tsp")) #file5
Gs.append ( MatrixCompleteGraph.createGraphFromTSP("ulysses22.tsp")) #file6

i=0
for g in Gs :
    print "file "+ str(i)
    print (g.weight_matrix)
    i+=1
