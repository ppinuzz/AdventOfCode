#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025 - Day 4

Created on Thu Dec  4 09:12:16 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

#filename = 'D4_test.in'
filename = 'D4.in'

with open(filename, 'r') as file:
    data = file.read().splitlines()

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