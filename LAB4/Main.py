from ParserCancerData import ParserCancerData
from FastClosestPair import FastClosestPair
from HierarchicalClustering import Hierarchicalclustering
import random
from Coord import Point
from Circle import *
import time

def get_spaced_colors(n):
    max_value = 16581375 #255**3
    interval = int(max_value / n)
    colors = [hex(I)[2:].zfill(6) for I in range(0, max_value, interval)]
    
    return ["rgb"+str((int(i[:2], 16), int(i[2:4], 16), int(i[4:], 16))) for i in colors]

def getncolors(n):
	space = 255*3//n
	
	colors=[[0,0,0] for i in range(n)]
	for i in range(1,n):
		num = sum(colors[i-1])+space
		for j in range(len(colors[i])):
			if num > 255:
				colors[i][j]=255
				num=num-255
			else:
				colors[i][j]=num
				num =0
	colors = [(color[0],color[1],color[2]) for color in colors]			
	colors = ["rgb"+str(color) for color in colors]
	return colors


def getncolors2(n):
	space = 255//n
	
	colors=[[0,0,0] for i in range(n)]
	for i in range(1,n):
		num = space*i
		for j in range(len(colors[i])):
			colors[i][j]=num

	colors = [(color[0],color[1],color[2]) for color in colors]			
	colors = ["rgb"+str(color) for color in colors]
	return colors

def getncolors3(n):

	colors1 = [[255-i,i,0] for i in range(0,255,5)]
	colors2 = [[0,255-i,i] for i in range(0,255,5)]
	colors3 = [[i,0,255-i] for i in range(0,255,5)]
	colors = colors1+colors2+colors3

	print len(colors)
	chosen_colors=[]
	for c in range(0,len(colors),(len(colors)/n)):
		chosen_colors.append(colors[c])
	colors=chosen_colors
	colors = [(color[0],color[1],color[2]) for color in colors]			
	colors = ["rgb"+str(color) for color in colors]
	random.shuffle(colors)
	return colors


Data = ParserCancerData("unifiedCancerData_3108.csv")

P = sorted(Data,key=lambda x : x.getX())

tm=time.time()
centers,clusters= Hierarchicalclustering(P,15)
print time.time()-tm

colors=get_spaced_colors(len(centers))
colors=getncolors(len(centers))
colors2=getncolors2(len(centers))
colors3=getncolors3(len(centers))

print colors3
draw = drawOnImage()
for i in range (len(centers)):
    draw.drawCircle(centers[i])
    for point in clusters[i]:
        draw.drawLine(centers[i],point,colors3[i])
draw.save()
