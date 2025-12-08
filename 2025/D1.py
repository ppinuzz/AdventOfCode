#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025 - Day 1

Created on Mon Dec  1 09:20:22 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

from timeit import default_timer as timer
import numpy as np

#filename = 'D1_test.in'
filename = 'D1.in'


moves = [] 
with open(filename, 'r') as file:
    for line in file:
        line = line.replace('R', '+')
        line = line.replace('L','-')
        moves.append(int(line)) 

moves = np.array(moves) 

start_time = timer()

# dial starts at position 50 from text 
dial = 50
dial_positions = [50]
N_zeros = 0
for i, N in enumerate(moves):
    N_turns = 0
    dial = dial + N
    
# =============================================================================
#     if dial > 0:
#         # number of full turns in positive direction
#         N_turns = np.floor(dial / 100)
#     elif dial < 0:
#         N_turns = np.ceil(-dial / 100)
# =============================================================================
    
    # 98 + 3 = 101 => 1 on the dial
    # remove 100 (i.e. 1 full turn) to get 1
    # repeat until dial is < 99 (i.e. remove an integer number of full turns)
    if dial > 0:
        while dial > 99:
            dial = dial - 100
            N_turns += 1
    # 2 - 4 = -2 => 98 on the dial
    # add one full turn to convert -2 to the range [0,99]
    elif dial < 0:
        while dial < 0:
            dial = dial + 100
            N_turns += 1
    
    # possible cases:
    # 1) start 0, end at > 0
    #       A) 0 --(+30)-->  30 < 99  => 0 turn OK
    #       B) 0 --(+130)--> 130 > 99 => 130-100=30 < 99 => 1 turn OK
    #   N_zeros = N_turns
    # 2) start from 0, end at < 0
    #       A) 0 --(-30)-->  -30 < 0   => -30+100=70 > 0 => (1-1) = 0 turn OK
    #       B) 0 --(-130)--> -130 < 99 => -130+200=70 > 0 => (2-1) = 1 turn OK
    #   N_zeros = N_turns - 1
    # 3) start from >0, end at 0
    #       A) 10 --(-10)--> 0 < 99    => 0 turn OK
    #       B) 10 --(-110)--> 100 > 99 => 100-100=0 < 99 => 1 turn OK
    #       C) 10 --(+190)--> 200 > 99 => 200-200=0 < 99 => (2-1) turn OK 
    #   N_zeros = N_turns   if N < 0
    #   N_zeros = N_turns-1 if N > 0
    
    dial_positions.append(dial)
    
    # edge cases where the number of turns does not coincides with the 
    # number of times the dial is passing through 0
    if (dial == 0 and N < 0):           # 3C)
        N_zeros = N_zeros + N_turns
    elif dial == 0:                     # 3A, 3B
        N_zeros = N_zeros + (N_turns - 1)
    elif (dial_positions[-2] == 0 and (dial_positions[-2]+N < 0)):  # 2A, 2B
        N_zeros = N_zeros + (N_turns - 1)
    else:
        N_zeros = N_zeros + N_turns
    
    

dial_positions = np.array(dial_positions)
# True's are integer 1s
password = np.sum(dial_positions == 0)

N_zeros = N_zeros + password

print(f'Password 1: {password}') 
print(f'Password 2: {N_zeros}') 

end_time = timer()
elapsed_time = end_time - start_time
print(f'Elapsed time: {elapsed_time:.2f} s')
