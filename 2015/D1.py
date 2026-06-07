#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 - Day 1

Created on Sun Jun  7 20:45:25 2026

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

from timeit import default_timer as timer

#filename = 'D1_test.in'
filename = 'D1.in'

with open(filename, 'r') as file:
    # read as single string with no '\n'
    data = file.read()
    
start_time = timer()


#%% PART 1

N_up = data.count('(')
N_down = data.count(')')
print(f'Floor: {N_up-N_down}')


#%% PART 2

floor = 0
for i, step in enumerate(data):
    step = 1 if step == '(' else -1
    floor += int(step)
    if floor == -1:
        print(f'Basement reached at step {i+1}')
        break

end_time = timer()
elapsed_time = end_time - start_time
print(f'Elapsed time: {elapsed_time:.3f} s')
