from ParserCancerData import ParserCancerData
from FastClosestPair import Split
import random

#Data = ParserCancerData("unifiedCancerData_212.csv")

Data=[[i,random.randint(0,100),random.randint(0,100)]for i in range(10)]
#print Data

P = sorted(Data,key=lambda x : x[1])
S = sorted(Data,key=lambda x : x[2])
print "S:",S
print "P:",P
l = 0
r = len(P)
m = (l+r)/2

SL,SR = Split(S,P,(0,m),(m,r))
print "SL:",SL
print "SR:",SR