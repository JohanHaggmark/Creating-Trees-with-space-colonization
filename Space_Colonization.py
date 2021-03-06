# -*- coding: utf-8 -*-
"""
Created on Thu May 23 20:04:36 2019

@author: canon
"""

import matplotlib.pyplot as plt
import numpy as np
import math

plt.clf()
class branch():
    def __init__(self, x, x2, y, y2):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.grow_count = 0
        self.grow_x = 0
        self.grow_y = 0
        self.width = 1
        self.child = []
    def updateWidth(self):
        width = 0
        for i in range(len(self.child)):
            width += self.child[i].updateWidth()
        if(width > 0):
            self.width = width
        if self.width == 1:
                self.plotLeaf()
        return self.width
    def plot(self):     
        plt.plot([self.x,self.x2],[self.y,self.y2], linewidth=np.sqrt(self.width), color='black')

    def plotLeaf(self):
        leafX = np.random.random(4)*4+self.x2
        leafY = np.random.random(4)*4+self.y2
        plt.scatter(leafX, leafY, color='red', s=10)


branches = [branch(30,30, -3,0)]

branches[0].plot()
plt.scatter(x, y)

maxdist = 10
mindist = 1

x = np.random.random(200)*60
y = np.random.random(200)*60

for h in range(40):

    for i in range(len(x)-1, 0, -1):
        closest_branch = 0
        dist = 1000
        for j in range(len(branches)):
            temp_dist = np.sqrt((x[i]-branches[j].x2)**2 + (y[i]-branches[j].y2)**2)
            if temp_dist < dist:
                dist = temp_dist
                closest_branch = j
            
        if dist < mindist:
            x = np.delete(x, i)
            y = np.delete(y, i)
        elif dist < maxdist:
            branches[closest_branch].grow_count += 1
            branches[closest_branch].grow_x += (x[i] - branches[closest_branch].x2)/dist
            branches[closest_branch].grow_y += (y[i] - branches[closest_branch].y2)/dist
            
    
    for i in range(len(branches)):
        if branches[i].grow_count > 0:
            newBranch = branch(branches[i].x2, branches[i].x2 + branches[i].grow_x/branches[i].grow_count, branches[i].y2, branches[i].y2 + branches[i].grow_y/branches[i].grow_count )
            branches.append(newBranch)
            branches[i].child.append(newBranch)
            branches[i].grow_count = 0
            branches[i].grow_x = 0    
            branches[i].grow_y = 0 
           
plt.clf()
#for i in range(len(branches)):  
branches[0].updateWidth()   
        
#plt.clf()
for i in range(len(branches)):    
    branches[i].plot()
    plt.axis('equal')

plt.scatter(x,y)






