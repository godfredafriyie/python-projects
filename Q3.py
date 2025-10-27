# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 10:31:35 2025

@author: Godfred Junior 
"""

#user enters a 5 digit no. 
user_int = input("key in your 5 digit no.: ") 

#ensuring a valid input from the user 
while not (user_int.isdigit() and len(user_int) == 5): 
    user_int = input("Wrong!Kindly enter exactly 5 digits: ")
    
#loop
for single_digit in user_int:
   print(single_digit, end='  ') 
print()  

