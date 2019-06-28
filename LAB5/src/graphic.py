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
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title of the current axes.
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.savefig("ciao")