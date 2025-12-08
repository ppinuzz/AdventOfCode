#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025 - Day 4

Created on Thu Dec  4 09:12:16 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

from timeit import default_timer as timer

#filename = 'D4_test.in'
filename = 'D4.in'

with open(filename, 'r') as file:
    data = file.read().splitlines()

start_time = timer()


#%% PUZZLE 1

N_valid = 0
for i, line in enumerate(data):
    for j, pos in enumerate(line):
        neighbours = []
        if pos == '.':
            continue
        else:
            if i > 0:
                neighbours.append(data[i-1][j])
                if j > 0:
                    neighbours.append(data[i-1][j-1])
                if j < len(line)-1:
                    neighbours.append(data[i-1][j+1])
            if i < len(data)-1:
                neighbours.append(data[i+1][j])
                if j > 0:
                    neighbours.append(data[i+1][j-1])
                if j < len(line)-1:
                    neighbours.append(data[i+1][j+1])
            if j > 0:
                neighbours.append(data[i][j-1])
            if j < len(line)-1:
                neighbours.append(data[i][j+1])
            N_rolls_adj = neighbours.count('@')
            if N_rolls_adj < 4:
                N_valid += 1

print(f'Accessible rolls of paper: {N_valid}')


#%% PUZZLE 2

N_valid = 0
data_temp = data.copy()

roll_removed = 0
while True:
    N_valid = 0
    accessible = []
    for i, line in enumerate(data_temp):
        for j, pos in enumerate(line):
            neighbours = []
            if pos == '.':
                continue
            else:
                if i > 0:
                    neighbours.append(data_temp[i-1][j])
                    if j > 0:
                        neighbours.append(data_temp[i-1][j-1])
                    if j < len(line)-1:
                        neighbours.append(data_temp[i-1][j+1])
                if i < len(data)-1:
                    neighbours.append(data_temp[i+1][j])
                    if j > 0:
                        neighbours.append(data_temp[i+1][j-1])
                    if j < len(line)-1:
                        neighbours.append(data_temp[i+1][j+1])
                if j > 0:
                    neighbours.append(data_temp[i][j-1])
                if j < len(line)-1:
                    neighbours.append(data_temp[i][j+1])
                N_rolls_adj = neighbours.count('@')
                if N_rolls_adj < 4:
                    N_valid += 1
                    accessible.append([i,j])
    roll_removed = roll_removed + N_valid
    if N_valid == 0:
        break
    # remove roll once it has been accessed
    for roll in accessible:
        i = roll[0]
        j = roll[1]
        data_temp[i] = data_temp[i][0:j] + '.' + data_temp[i][j+1:]

print(f'Rolls of paper removed: {roll_removed}')

end_time = timer()
elapsed_time = end_time - start_time
print(f'Elapsed time: {elapsed_time:.2f} s')
