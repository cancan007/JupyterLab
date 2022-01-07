#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as  pd
import matplotlib.pyplot as plt


# In[14]:



class CreateGraph():
    
    def __init__(self, p, q):
        self.n = 10
        self.dt = 1
        self.m =2
        self.k = 3
        self.p = p
        self.q = q
        
        self.t_list = []
        self.p_list = []
        self.q_list = []
        
    
    def calculate(self):
        tq = 0
        tp = 0
        t_list = self.t_list
        p_list = self.p_list
        q_list = self.q_list
        n = self.n
        dt = self.dt
        m = self.m
        k = self.k
        p = self.p
        q = self.q
        
        q_list.append(q)
        p_list.append(p)
        t_list.append(0)
        
        for i in range(n):
            if tq == 0:
                tq = q + dt*(p/m)
                tp = p - dt*(k*tq)
                q_list.append(tq)
                p_list.append(tp)
                t_list.append(dt)
            else:
                dt = t_list[-1] + self.dt

                tq = tq + dt*(tp/m)
                tp = tp - dt*(k*tq)
                q_list.append(tq)
                p_list.append(tp)
                t_list.append(dt)
        self.t_list = t_list
        self.q_list = q_list
        self.p_list = p_list
    
    def output_graph(self, w=10, h=8):
        tl = self.t_list
        ql = self.q_list
        pl = self.p_list
        
        fig = plt.figure(figsize=(w, h))
        ax = fig.add_subplot(111)
        x = tl
        y = ql
        ax.scatter(x, y, color='blue', marker='o')
        ax.grid(True)
        ax.set_xlim(0, max(x))
        ax.set_ylim(min(y), max(y))
        ax.set_xlabel('[s]', fontsize=22)
        ax.set_ylabel('q', fontsize=22)
        ax.set_title('Graph of t-q', fontsize=35, color='blue')
        fig.savefig("q-graph.jpg" ,bbox_inches='tight',pad_inches = 0)
        fig.show()
        
        fig = plt.figure(figsize=(w, h))
        ax = fig.add_subplot(111)
        x = tl
        y = pl
        ax.scatter(x, y, color='green', marker='o')
        ax.grid(True)
        ax.set_xlim(0, max(x))
        ax.set_ylim(min(y), max(y))
        ax.set_xlabel('[s]', fontsize=22)
        ax.set_ylabel('p', fontsize=22)
        ax.set_title('Graph of t-p', fontsize=35, color='green')
        fig.savefig("p-graph.jpg" ,bbox_inches='tight',pad_inches = 0)
        fig.show()


# In[16]:


graph = CreateGraph(1.01, 1.02)
graph.calculate()
graph.output_graph()


# In[4]:


#!jupyter nbconvert --to python Yuushiro.ipynb


# In[ ]:




