#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025 - Day 7

Created on Sun Dec  7 12:07:37 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

import numpy as np
from timeit import default_timer as timer

#filename = 'D7_test.in'
filename = 'D7.in'

with open(filename, 'r') as file:
	# remove trailing '\n' automatically
    data = file.read().splitlines()

start_time = timer()

# convert list of strings to a matrix of chars
# https://stackoverflow.com/a/9493192/17220538
# (use bytes, not str: https://stackoverflow.com/questions/9476797/#comment68548608_9493192)
data = np.array(data[:-1], dtype=bytes)
# view the array (N,) strings as an NxM array of single chars ("S1")
# now the entire array is an (N*M, ) array => reshape it
# (the number of rows can be inferred from the original data_str, but the
# number of chars in each string can be determined automatically from the data
# if -1 is passed as 2nd dimension)
# and reconvert to a normal string type
data = data.view('S1').reshape((data.size, -1)).astype(str)

# starting point
N = 0
idx_beam = np.argwhere(data[0,:] == 'S')[0]
print(''.join(data[0,:]))
for line in data[1:]:
    for idx in idx_beam:
        if line[idx] == '.':
            line[idx] = '|'
        elif line[idx] == '^':
            line[[idx-1, idx+1]] = '|'
            N += 1
    idx_beam = np.atleast_1d(np.squeeze(np.argwhere(line == '|')))
    print(''.join(line))

print(f'Beam split {N} times')

end_time = timer()
elapsed_time = end_time - start_time
print(f'Elapsed time: {elapsed_time:.2f} s')
