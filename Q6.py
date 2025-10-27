# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:03:39 2025

@author: Godfred Junior
"""

"""Give the correct change using the fewest coins."""

# price of the item
price = float(input("Enter your item price (max $1): "))


while price < 0 or price > 1:
    price = float(input("wrong price, Kindly key in a value between $0 and $1: "))

final_change = round((1 - price) * 100)

quarters = final_change // 25
final_change %= 25  

dimes = final_change // 10  
final_change %= 10  

nickels = final_change // 5 
final_change %= 5  

pennies = final_change

# change
print("\nYour change is:")
if quarters > 0:
    print(quarters, "quarters")
if dimes > 0:
    print(dimes, "dimes")
if nickels > 0:
    print(nickels, "nickels")
if pennies > 0:
    print(pennies, "pennies")
