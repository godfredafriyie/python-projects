# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 10:22:13 2025

@author: Godfred Junior 
"""

"""Comparing integers using if...else statements and comparison operators."""

print('Enter two integers, and I will tell you the relationships they satisfy.')

# Read first integer
number1 = int(input('Enter first integer: '))

# Read second integer
number2 = int(input('Enter second integer: '))

# condition 1: Check whether the numbers are the same or different
if number1 == number2:
    print(number1, 'is equal to', number2)
else:
    print(number1, 'is not equal to', number2)

# condition 2: Determine which number is smaller or larger
if number1 < number2:
    print(number1, 'is less than', number2)
else:
    print(number1, 'is greater than', number2)

# condition 3: Confirm whether one number is less than or equal to the other, or vice versa
if number1 <= number2:
    print(number1, 'is less than or equal to', number2)
else:
    print(number1, 'is greater than or equal to', number2)
