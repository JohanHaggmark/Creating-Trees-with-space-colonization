# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:00:34 2019

@author: Johan
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
import random

x = []
y = []
z = []
for i in range(1000):
    x.append(math.sqrt(1000-i)*random.random()*(random.random()*2-1)+15)
    y.append(math.sqrt(1000-i)*random.random()*(random.random()*2-1)+15)
    z.append(i/30)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z)