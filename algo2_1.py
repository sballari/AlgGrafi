#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import random 
import matplotlib.pyplot as plt


# In[2]:


G = nx.Graph()


# ### Numero di vertici

# In[3]:


n=20


# ### Probabilità

# In[4]:


p=10


# ### Creo i vertici

# In[5]:


for i in range(n):
    G.add_node(i)


# ### Creo archi

# In[6]:


for i in range(n):
    for j in range(n):
        a=random.randint(0,100)
        if i!=j and a<p:
            G.add_edge(i,j)


# In[7]:


nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

# In[ ]:




