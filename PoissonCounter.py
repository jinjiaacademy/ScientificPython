# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 10:30:12 2022

@author: Jinjia Liu
"""

# =============================================================================
# Exercise: Make a Poisson-like counter.
# parameter lambda. positive number (10)
# start at 1, multiply by random number uniform([0, 1])
# target number is smaller than exp(-lambda)
# count the number of iterations until target < exp(-lambda)
# =============================================================================

import numpy as np

def poissonCounter(lambdaN):
    target = 1
    count = 0
    
    while target >= np.exp(-lambdaN):
        target *= np.random.uniform(0, 1)
        # print(f'target = {target}')
        count += 1
        
    return count    

p = np.zeros(100)

for i in range(100):
    p[i] = poissonCounter(10)

print(p) 