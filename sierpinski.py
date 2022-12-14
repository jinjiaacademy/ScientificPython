# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 22:01:39 2022

@author: Jinjia Liu

Code a Sierpinski Triangle
"""
import numpy as np
import matplotlib.pyplot as plt

N = 10000

# Initialize x and y vectors
sx = np.zeros(N)
sy = np.zeros(N)

for i in range(1, N):
    # generate a random number {1, 2, 3}
    k = np.random.randint(1, 4)
    
    # update the x and y points
    sx[i] = sx[i-1]/2 + k - 1
    sy[i] = sy[i-1]/2
    if k == 2:
        sy[i] += 2
        
plt.plot(sx, sy, 'k.', markersize=1)
plt.title('Sierpinski Triangle')
plt.axis('off')
plt.show()
