# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:38:24 2022

@author: Jinjia Liu
"""

# Input two numbers from the user
firstNum = float(input('Input the first number: '))
secondNum = float(input('Input the second number: '))
product = firstNum * secondNum

# Create a dictionary with keys 'firstNum', 'secondNum', 'product'

D = {}
D['firstNum'] = firstNum
D['secondNum'] = secondNum
D['product'] = product

print(' ')
print(D)