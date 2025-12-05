#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025 - Day 5

Created on Fri Dec  5 09:03:34 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

#filename = 'D5_test.in'
filename = 'D5.in'

with open(filename, 'r') as file:
	# remove trailing '\n' automatically
    data = file.read().splitlines()

good_IDs = [] 
products = [] 
for i, line in enumerate(data):
    if line:
        ID1, ID2 = line.split('-')
        ID_range = [int(ID1), int(ID2)]
        good_IDs.append(ID_range)
    else:
        products = list(map(int, data[i+1:])) 
        break

N_good = 0
for ID in products:
    for IDrange in good_IDs:
        if ID >= IDrange[0] and ID <= IDrange[1]:
            N_good += 1
            # move to next ID once you've established this is safe
            break

print(f'Number of safe items: {N_good}')