# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:31:04 2025

@author: Godfred Junior
"""


# first Pattern 
for i in range(1, 7):
    print('*' * i)
print()  

# Second Pattern 
for i in range(6, 0, -1):
    print('*' * i)
print()

# Third Pattern 
for i in range(6, 0, -1):
    print(' ' * (6 - i) + '*' * i)
print()  

# Fourth Pattern 
for i in range(1, 7):
    print(' ' * (6 - i) + '*' * i)
