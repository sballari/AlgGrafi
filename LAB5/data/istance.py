
nfile = "istance.csv"

f = open(nfile,"a")

#Domanda 1

pop = [250,2000,5000,15000,50000,100000]
for p in pop:
    f.write("1"+","+str(p)+",50,100"+","+"10"+"\n")

#Domanda 2 
for k in range(10,101):
    f.write("2"+","+"-999"+","+str(k)+","+"100"+","+"10"+"\n")


#Domanda 3 
#for it in range(10,1001):
#    f.write("3"+","+"-999"+","+"50"+","+str(it)+","+"20"+"\n")

#Domanda 4
for cutoff in range(0,38183,50):
    f.write("4"+","+"-999"+","+"50"+","+"100"+","+str(cutoff)+"\n")

f.close()