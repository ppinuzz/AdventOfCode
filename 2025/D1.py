#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025 - Day 1

Created on Mon Dec  1 09:20:22 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

import numpy as np

#filename = 'D1_test.in'
filename = 'D1.in'


#%% PUZZLE 1

moves = [] 
with open(filename, 'r') as file:
    for line in file:
        line = line.replace('R', '+')
        line = line.replace('L','-')
        moves.append(int(line)) 

moves = np.array(moves) 

# dial starts at position 50 from text 
dial = 50
dial_positions = []
for i, N in enumerate(moves):
    dial = dial + N
    
    # 98 + 3 = 101 => 1 on the dial
    # remove 99 (i.e. 1 full turn) to get 2, then remove 1 to account for the
    # 0 position
    # repeat until dial is < 99 (i.e. remove an integer number of full turns)
    if dial > 0:
        while dial > 99:
            dial = (dial - 99) - 1
    # 2 - 4 = -2 => 98 on the dial
    # add one full turn to convert -2 to the range [0,99], then add 1 to 
    # account for the 0 position
    elif dial < 0:
        while dial < 0:
            dial = (dial + 99) + 1
    
    dial_positions.append(dial)

dial_positions = np.array(dial_positions)
# True's are integer 1s
password = np.sum(dial_positions == 0)

print(f'Password: {password}') 

