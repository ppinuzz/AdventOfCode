#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025 - Day 3

Created on Wed Dec  3 09:51:52 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

import numpy as np

#filename = 'D3_test.in'
filename = 'D3.in'

with open(filename, 'r') as file:
    data = file.readlines()

banks = []
for bank in data:
    # remove trailing \n
    bank = bank.strip()
    temp = [int(jolt) for jolt in bank]
    banks.append(np.array(temp))


#%% PUZZLE 1

jolts = []
for bank in banks:
    idx_max = np.argmax(bank)
    if idx_max < (bank.shape[0]-1):
        max_1 = np.max(bank)
        # once you have max, the next digit must be after that to have the max joltage 
        max_2 = np.max(bank[idx_max+1:])
    else:
        # if the max digit is the last one, look for the 2nd largest digits 
        # to have the biggest number
        bank_nomax = bank.copy()
        max_2 = bank[idx_max]
        # sentinel value
        bank_nomax[idx_max] = -1
        max_1 = np.max(bank_nomax)
    jolt = max_1*10 + max_2
    jolts.append(jolt)

jolts = np.array(jolts)
tot_jolt = np.sum(jolts)

print(f'Total joltage output: {tot_jolt}') 


#%% PUZZLE 2

jolts = []
for bank in banks:
    bank_temp = bank.copy()
    # find max value and check whether there are at least other 11 digits
    # after it to create a 12-digits number
    # set to false to start the loop
    enough_digits = False
    
    jolt = []
    for n_digit in range(12):
        digit_found = False
        bank_temp2 = bank_temp.copy()
        while not digit_found:
            max_num = np.max(bank_temp2)
            idx_max = np.argmax(bank_temp2)
            N_digits_dx = bank_temp.shape[0] - (idx_max + 1)
            # check whether there are enough digits to the right of the max to 
            # create a new joltage
            if N_digits_dx < (12-(n_digit+1)):
                # temporary remove the max value you've found
                bank_temp2[idx_max] = -1
                digit_found = False
            else:
                digit_found = True
        jolt.append(str(max_num))
        # replace all values to the left of the max (and the max) with dummies
        bank_temp[0:idx_max+1] = -1
    # from ['2', '3', '4'] to '234'
    jolt = int(''.join(jolt))
    jolts.append(jolt)

jolts = np.array(jolts)
tot_jolt = np.sum(jolts)

print(f'Total joltage output: {tot_jolt}')

# 3121910778619 => too low
