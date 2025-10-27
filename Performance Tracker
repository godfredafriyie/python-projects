# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 09:59:00 2025

@author: Godfred Junior 
"""

"""Using nested control statements to analyze examination results with input validation."""


# Initialize variables
passes = 0  # Number of students who passed

# Process the input for 15 students
for student in range(15):
    while True:
        try:
            # Get the user input
            result = int(input('Enter result (1=pass, 2=fail): '))

            # Validating of the input 
            if result in (1, 2):
                break  
            else:
                print("Invalid input. Please enter 1 for pass or 2 for fail.")
        except ValueError:
            print("Invalid input. Please enter a numeric value (1 or 2).")

    if result == 1:
        passes += 1  

failures = 15 - passes  

print('Passed:', passes)
print('Failed:', failures)

if passes > 9:
    print('Bonus to instructor!')

