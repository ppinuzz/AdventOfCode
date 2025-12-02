#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025 - Day 2

Created on Tue Dec  2 09:39:38 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

import numpy as np
from sympy import divisors
from re import findall

#filename = 'D2_test.in'
filename = 'D2.in'

with open(filename, 'r') as file:
    # only 1 line of data: readlines() creates a ['myline'], readline() reads
    # only the 1st line 'myline'
    data = file.readline()

ranges = data.split(',')
# split each string '11-22' to ['11', '22'], the apply int() to convert
ranges = [list(map(int, range_i.split('-'))) for range_i in ranges]
invalid_ID = []
for range_i in ranges:
    # list of IDs in between the 2 limits
    # (+1 to include last value)
    IDs = list(map(str, range(range_i[0], range_i[1]+1)))
    for ID in IDs:
# =============================================================================
#         # a string can split in equal pieces of N different lengths, where the 
#         # lengths are the divisors of the number
#         # (exclude 1)
#         div = list(divisors(len(ID)))[1:]
#         for N in div:
#             # split string into pieces of length len(ID)/N
#             # https://stackoverflow.com/a/9477447/17220538
#             L = int(len(ID)/N)
#             pieces = findall('.'*L, ID)
#             # pick the non-repeating pieces converting to a set: if now len = 1,
#             # then there are only repeated digits => invalid ID
#             uniques = set(pieces)
#             if len(uniques) == 1:
#                 invalid_ID.append(ID)
#                 break
# =============================================================================
        # if you can't split the string in groups of digits repeated twice,
        # then the ID won't be invalid
        if len(ID) % 2 != 0:
            continue
        # split string into pieces of length len(ID)/N
        #             # https://stackoverflow.com/a/9477447/17220538
        #             L = int(int(len(ID)/N))
        L = int(len(ID) / 2)
        pieces = findall('.'*L, ID)
        # pick the non-repeating pieces converting to a set: if now len = 1,
        # then there are only repeated digits => invalid ID
        uniques = set(pieces)
        if len(uniques) == 1:
            invalid_ID.append(ID)

sum_invalid = np.sum(np.array(list(map(int, invalid_ID))))
print(f'Sum of invalid IDs: {sum_invalid}')