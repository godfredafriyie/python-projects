# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:13:56 2025

@author: Godfred Junior 
"""

import statistics as stats

breeds = ["Poodle", "Bulldog", "Beagle", "Poodle", "Collie", "Poodle", "Beagle"]

breeds = stats.mode(breeds)

print(f"common dog breed is: {breeds}")

