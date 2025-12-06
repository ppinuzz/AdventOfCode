#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025 - Day 6

Created on Sat Dec  6 11:28:20 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

import numpy as np
from timeit import default_timer as timer

#filename = 'D6_test.in'
filename = 'D6.in'

with open(filename, 'r') as file:
	# remove trailing '\n' automatically
    data = file.read().splitlines()

start_time = timer()

#%% PUZZLE 1

operands = np.zeros((len(data)-1, len(data[0].split())), dtype=int)
for i, line in enumerate(data):
    line = line.split()
    if i < len(data)-1:
        operands[i,:] = np.array(list(map(int, line))) 
    else:
        operators = line.copy()

N = 0
for i, op in enumerate(operators):
    if op == '+' :
        N = N + np.sum(operands[:,i]) 
    else:
        N = N + np.prod(operands[:,i])

print(f'Sum of all operations: {N}') 


#%% PUZZLE 2

# convert list of strings into a matrix of chars
# https://stackoverflow.com/a/9493192/17220538
# (use bytes, not str: https://stackoverflow.com/questions/9476797/#comment68548608_9493192)
data_str_orig = np.array(data[:-1], dtype=bytes)
# view the array (N,) strings as an NxM array of single chars ("S1")
data_str = data_str_orig.view('S1')
# now the entire array is an (N*M, ) array => reshape it
# (the number of rows can be inferred from the original data_str, but the
# number of chars in each string can be determined automatically from the data
# if -1 is passed as 2nd dimension)
data_str = data_str.reshape((data_str_orig.size, -1))
# convert to normal string type
data_str = data_str.astype(str)
# column-wise sum: if the result is the same as the number of rows, then that
# column has only spaces => it's a separator column
#idx_sep_cols = np.squeeze(np.argwhere(np.sum(data_str == ' ', axis=0) == data_str.shape[0]))
numbers = []
num_cols = []
for col in data_str.T:
    # all spaces => separator column
    if (col == ' ').all():
        numbers.append(np.array(num_cols))
        num_cols = []
        continue
    num_cols.append(int(''.join(col).strip()))
# append last column
numbers.append(np.array(num_cols))

N_weird = 0
for i, op in enumerate(operators):
    if op == '+' :
        N_weird = N_weird + np.sum(numbers[i]) 
    else:
        N_weird = N_weird + np.prod(numbers[i])

print(f'Sum of all operations vertically: {N_weird}') 

end_time = timer()
elapsed_time = end_time - start_time
print(f'Elapsed time: {elapsed_time:.2f} s')
