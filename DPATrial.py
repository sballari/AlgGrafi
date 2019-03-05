import random

class DPATrial:
    def __init__(self,nodes):
        self.num=len(nodes)
        self.nodeNumbers=[]
        for i in range(self.num):
            self.nodeNumbers+=[i for i in nodes]
    def RunTrial(self,node_label):
        Vi=[]
        for i in range(self.num):
            Vi.append(random.choice(self.nodeNumbers))
        self.nodeNumbers.append(node_label)
        self.nodeNumbers+=Vi
        return Vi
