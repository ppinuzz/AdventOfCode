#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2024 - Day 1, Puzzle 1

Created on Thu Nov 27 22:19:10 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

import numpy as np

#filename = 'D1_test.in'
filename = 'D1.in'


loc_IDs = np.loadtxt(filename)
N = loc_IDs.shape[0]
# convert to list to make it modifyable in real time
IDs_sx = [int(loc_IDs[i,0]) for i in range(N)]
IDs_dx = [int(loc_IDs[i,1]) for i in range(N)]

dist = 0
for i in range(N):
    idx_min_sx = np.argmin(IDs_sx)
    idx_min_dx = np.argmin(IDs_dx)
    dist = dist + abs(IDs_sx[idx_min_sx] - IDs_dx[idx_min_dx])
    # remove used location IDs
    IDs_sx.pop(idx_min_sx)
    IDs_dx.pop(idx_min_dx)

print(f'Total distance: {dist}')