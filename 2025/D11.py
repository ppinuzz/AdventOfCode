#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025 - Day 11

Created on Thu Dec 11 09:50:01 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

from timeit import default_timer as timer

#filename = 'D11_test.in'
filename = 'D11.in'

with open(filename, 'r') as file:
	# remove trailing '\n' automatically
    data = file.read().splitlines()

devices = {}
for line in data:
    # remove the :
    line = line.replace(':', '')
    tokens = line.split(' ')
    devices[tokens[0]] = list(tokens[1:])


#%% PUZZLE 1

start_time = timer()

def look_for_out(devices, device):
    for dev in devices[device]:
        # base case: you've reached the exit => keep track by incrementing the 
        # counter
        if dev == 'out':
            look_for_out.counter += 1
        else:
            look_for_out(devices, dev)

look_for_out.counter = 0
look_for_out(devices, 'you')

print(f'Number of paths: {look_for_out.counter}')

end_time = timer()
elapsed_time = end_time - start_time
print(f'Elapsed time: {elapsed_time:.2f} s')
