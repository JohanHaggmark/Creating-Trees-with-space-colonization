# -*- coding: utf-8 -*-
"""
Created on Thu May 23 20:04:36 2019

@author: canon
"""

import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

class branch():
    def __init__(self, x, x2, y, y2, z, z2):
        self.x = x
        self.y = y
        self.z = z
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.grow_count = 0
        self.grow_x = 0
        self.grow_y = 0
        self.grow_z = 0
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
        ax.plot([self.x,self.x2],[self.y,self.y2],[self.z, self.z2], linewidth=np.sqrt(self.width), color='black')

    def plotLeaf(self):
        leafX = np.random.random(1)*4+self.x2
        leafY = np.random.random(1)*4+self.y2
        leafZ = np.random.random(1)*4+self.z2
        ax.scatter(leafX, leafY, leafZ, color='green', s=10)
#x=[]
#y=[]
#z=[]
x = np.random.random(300)*60
y = np.random.random(300)*60
z = np.random.random(300)*60
#for i in range(1000):
#    x.append(math.sqrt(1000-i)*random.random()*(random.random()*2-1)+15)
#    y.append(math.sqrt(1000-i)*random.random()*(random.random()*2-1)+15)
#    z.append(i/30)

#fig = plt.figure()
ax = plt.figure().add_subplot(111, projection='3d')
#ax.scatter(x,y,z)

branches = [branch(15,15, 15,15, -10,0)]

branches[0].plot()
#plt.scatter(x, y)

maxdist = 30
mindist = 2



for h in range(30):

    for i in range(len(x)-1, 0, -1):
        closest_branch = 0
        dist = 1000
        for j in range(len(branches)):
            temp_dist = np.sqrt((x[i]-branches[j].x2)**2 + (y[i]-branches[j].y2)**2 + (z[i]-branches[j].z2)**2)
            if temp_dist < dist:
                dist = temp_dist
                closest_branch = j
            
        if dist < mindist:
            x = np.delete(x, i)
            y = np.delete(y, i)
            z = np.delete(z, i)
        elif dist < maxdist:
            branches[closest_branch].grow_count += 1
            branches[closest_branch].grow_x += (x[i] - branches[closest_branch].x2)/dist
            branches[closest_branch].grow_y += (y[i] - branches[closest_branch].y2)/dist
            branches[closest_branch].grow_z += (z[i] - branches[closest_branch].z2)/dist
            
    
    for i in range(len(branches)):
        if branches[i].grow_count > 0:
            branches[i].grow_count /= 3
            newBranch = branch(branches[i].x2, branches[i].x2 + branches[i].grow_x/branches[i].grow_count, branches[i].y2, branches[i].y2 + branches[i].grow_y/branches[i].grow_count, branches[i].z2, branches[i].z2 + branches[i].grow_z/branches[i].grow_count )
            branches.append(newBranch)
            branches[i].child.append(newBranch)
            branches[i].grow_count = 0
            branches[i].grow_x = 0    
            branches[i].grow_y = 0 
            branches[i].grow_z = 0 
     
    ax.cla()
    branches[0].updateWidth()  
    for i in range(len(branches)):    
        branches[i].plot()
    #ax.scatter(x,y,z)
   # ax.axis('equal')
    #plt.pause(0.001)

#branches[0].updateWidth()   
        
#plt.clf()
for i in range(len(branches)):    
    branches[i].plot()


ax.axis('equal')
#ax.scatter(x,y,z)






