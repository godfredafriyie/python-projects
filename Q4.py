# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 10:47:55 2025

@author: Godfred Junior 
"""

#piggy bank

piggy_savings= 0  

# Continue adding money until the total reaches or exceeds $500
while piggy_savings <= 500:
    try:
        # Asking the user how much to add
        deposit = float(input("Hello piggy bank user! Enter your prefered amount to add: "))

        if deposit < 0:
            print("Sorry, Negative amounts are not allowed. Please enter a positive value.")
            continue  

# total savings
        piggy_savings += deposit
        print(f"Current balance: ${piggy_savings:.2f}") 

    except ValueError:
        print("Invalid input. Please enter a numerical amount.")

# Final message for limit
print("Congrats! You have reached the $500 limit.")