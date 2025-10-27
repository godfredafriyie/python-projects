# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:55:38 2025

@author: Godfred Junior 
"""

import statistics

data = [20,50,50,10,30,40,40,70,80,60,90]

#mean
mean = statistics.mean(data)

#mode 
mode = statistics.mode(data) 

#median 
median = statistics.median(data)

print("Mean:", mean)
print ("Mode:", mode) 
print("Median:", median)


