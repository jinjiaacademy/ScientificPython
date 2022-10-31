# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 17:17:59 2022

@author: Jinjia Liu
"""
import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# plt.subplot(2, 1, 1)
# plt.plot(np.random.randn(10))
# 
# plt.subplot(2, 1, 2)
# plt.plot(np.random.randn(10))
# 
# for i in range(9):
#     plt.subplot(3, 3, i+1)
#     plt.plot(np.random.randn(7))
# =============================================================================

# =============================================================================
# fig, ax = plt.subplots(3, 1, figsize=(2, 9))
# 
# x = np.arange(10)
# ax[0].plot(x, x**2, 'b')
# ax[1].plot(x, np.sqrt(x), 'r')
# ax[2].plot(x, x, 'g')
# =============================================================================

# =============================================================================
# fig, ax = plt.subplots(2, 2)
# 
# ax[0, 0].plot(np.random.randn(4, 4))
# ax[0, 1].plot(np.random.randn(4, 4))
# ax[1, 0].plot(np.random.randn(4, 4))
# ax[1, 1].plot(np.random.randn(4, 4))
# =============================================================================

# =============================================================================
# fig, ax = plt.subplots(3, 3)
# 
# rows = [0, 1, 2]
# cols = [0, 1, 2]
# 
# mtx = [(row, col) for row in rows for col in cols]
# 
# for row, col in mtx:
#     ax[row, col].plot(np.random.randn(4,4))
# =============================================================================

# =============================================================================
# x = np.linspace(-3, 3, 101)
# 
# plt.plot(x, x, label='y=x')
# plt.plot(x, x**2, label='y=x**2')
# plt.plot(x, x**3, label='y=x**3')
# 
# plt.xlabel('x')
# plt.ylabel('y=f(x)')
# plt.xlim([x[0], x[-1]])
# plt.ylim([-10, 10])
# plt.title('A really awesome plot!')
# 
# plt.gca().set_aspect(1/plt.gca().get_data_ratio())
# plt.legend()
# 
# =============================================================================

# =============================================================================
# x = np.linspace(0, 10, 100)
# 
# for i in np.linspace(0, 1, 50):
#     plt.plot(x, x**i, color=[i/2, 0, i])
#     
# plt.show()
# =============================================================================
