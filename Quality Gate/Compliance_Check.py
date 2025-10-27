# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:08:27 2025

@author: Godfred Junior 
"""

import numpy as np
import statistics as stats

# data sample with 100 as outlier
data = [15, 17, 18, 19, 20, 23, 100]


mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data)  

# Display results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
