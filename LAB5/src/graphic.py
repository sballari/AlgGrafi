import matplotlib.pyplot as plt

fname = "result.csv"
f=open(fname,'r')
data=f.read()
data=data.split('\n')

for nl in range(len(data)-1):
    line=data[nl].split(' ')
    for l in range(len(line)):
        line[l]=int(line[l])
    data[nl]=line
data.pop()

graphic = [[] for i in range(4)]
for d in data:
    graphic[d[0]-1].append(d)


#domanda 1
pop = [d[1] for d in graphic[0]]
par0 = [d[5] for d in graphic[0]]
seq0 = [d[6] for d in graphic[0]]

# line 1 points
x1 = pop
y1 = par0
# plotting the line 1 points 
plt.plot(x1, y1, label = "parallel")
# line 2 points
x2 = pop
y2 = seq0
# plotting the line 2 points 
plt.plot(x2, y2, label = "sequential")
plt.xlabel('x - population')
# Set the y axis label of the current axis.
plt.ylabel('y - time ms')
# Set a title of the current axes.
plt.title('Domanda 1 ')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.savefig("domanda1")
plt.clf()

#domanda 2
clu = [d[2] for d in graphic[1]]
par1 = [d[5] for d in graphic[1]]
seq1 = [d[6] for d in graphic[1]]

# line 1 points
x1 = clu
y1 = par1
# plotting the line 1 points 
plt.plot(x1, y1, label = "parallel")
# line 2 points
x2 = clu
y2 = seq1
# plotting the line 2 points 
plt.plot(x2, y2, label = "sequential")
plt.xlabel('x - cluster')
# Set the y axis label of the current axis.
plt.ylabel('y - time ms')
# Set a title of the current axes.
plt.title('Domanda 2')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.savefig("domanda2")

plt.clf()

#domanda 3
it = [d[3] for d in graphic[2]]
par2 = [d[5] for d in graphic[2]]
seq2 = [d[6] for d in graphic[2]]

# line 1 points
x1 = it
y1 = par2
# plotting the line 1 points 
plt.plot(x1, y1, label = "parallel")
# line 2 points
x2 = it
y2 = seq2
# plotting the line 2 points 
plt.plot(x2, y2, label = "sequential")
plt.xlabel('x - iteration')
# Set the y axis label of the current axis.
plt.ylabel('y - time ms')
# Set a title of the current axes.
plt.title('Domanda 3')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.savefig("domanda3")
plt.clf()

#domanda 4
cutoff = [d[4] for d in graphic[3]]
par3 = [d[5] for d in graphic[3]]
seq3 = [d[6] for d in graphic[3]]

# line 1 points
x1 = cutoff
y1 = par3
# plotting the line 1 points 
plt.plot(x1, y1, label = "parallel")
# line 2 points

# plotting the line 2 points 
plt.xlabel('x - cutoff')
# Set the y axis label of the current axis.
plt.ylabel('y - time ms')
# Set a title of the current axes.
plt.title('Domanda 4')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.savefig("domanda4")
plt.clf()

import numpy as np
from scipy.interpolate import interp1d

fig, ax = plt.subplots()
ax.scatter(x1,y1, s=5, c="crimson")

f = interp1d(x1, y1, kind='cubic')
xdens = np.linspace(0, 39000, num=400)
ydens = f(xdens)

ax.plot(xdens, ydens, label="interpolation")
ax.legend()
ax2 = ax.twinx()
yderiv =  np.diff(ydens)/np.diff(xdens)
ax2.plot(xdens[:-1],yderiv, color="C2", label="derivative")

ax2.legend()
plt.show()