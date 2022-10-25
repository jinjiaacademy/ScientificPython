# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:18:44 2022

@author: Jinjia Liu
"""

x = int(input("Enter the first side length: "))
y = int(input("Enter the second side length: "))
z = int(input("Enter the third side length: "))

if x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2:
    print("It's a real Pythagorean triplets.")
else:
    print("No, it's not a real Pythagorean triplets.")