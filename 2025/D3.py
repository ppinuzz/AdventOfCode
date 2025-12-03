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