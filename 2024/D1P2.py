#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2024 - Day 1, Puzzle 2

Created on Thu Nov 27 22:31:15 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

import numpy as np

#filename = 'D1_test.in'
filename = 'D1.in'

# by default, they're read as floats, but that buggers me
loc_IDs = np.loadtxt(filename, dtype=int)

sim_score = 0
for ID_sx in loc_IDs[:,0]:
    # booleans are integers => sum of True's evaluates to a sum of 1s
    N = np.sum(loc_IDs[:,1] == ID_sx)
    sim_score = sim_score + ID_sx*N

print(f'Similarity score: {sim_score}')