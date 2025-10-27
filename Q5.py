# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 11:06:23 2025

@author: Godfred Junior
"""


smallest_value = float('inf')
second_smallest_value = float('inf')

# Ask the user to key 10 numbers
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))

    if num < smallest_value:
        second_smallest_value = smallest_value
        smallest = num
    
    elif num < second_smallest_value:
        second_smallest_value= num

# Showing the two smallest numbers
print("Smallest number:", smallest_value)
print("Second smallest number:", second_smallest_value)
