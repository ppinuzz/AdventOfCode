#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025 - Day 9

Created on Tue Dec  9 10:26:52 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import itertools

#filename = 'D9_test.in'
filename = 'D9.in'

with open(filename, 'r') as file:
	# remove trailing '\n' automatically
    data = file.read().splitlines()
data = np.array([line.split(',') for line in data], dtype=int)
# for some reason, positions are given as (column, row) => swap them
data = np.column_stack((data[:,1], data[:,0]))


#%% PUZZLE 1

start_time = timer()

# build all possible combinations without repetitions:
#   C(n,k) = n!/(k!(n-k)!)
# being couples, k = 2 and C(n,2) = n(n-1)/2
# create couples of indices, not physical coordinates (easier to handle)
couples = list(itertools.combinations(range(0,data.shape[0]), 2))

areas = np.zeros((len(couples), ), dtype=int)
for i, couple in enumerate(couples):
    delta = data[couple[0],:] - data[couple[1],:]
    # +1 because these are "discrete" coordinates, not continuous
    # (i.e. if 2 corners are at x=1 and x=2, the length is dx=2 tiles, not dx=1)
    areas[i] = np.abs(np.prod(delta+1))
A_max = np.max(areas)

print(f'Largest area: {A_max}')


#%% PUZZLE 2

end_time = timer()
elapsed_time = end_time - start_time
print(f'Elapsed time: {elapsed_time:.2f} s')
