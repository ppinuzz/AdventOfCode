#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 - Day 3

Created on Sun Jun  7 22:58:10 2026

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

from timeit import default_timer as timer
import numpy as np

#filename = 'D3_test.in'
filename = 'D3.in'

with open(filename, 'r') as file:
    # read as a single string
    data = file.read()

start_time = timer()

def deliver_presents(data):
    houses = {'0;0': 1}
    new_house = ['0', '0']
    for step in data:
        match step:
            case '^':
                new_house = f'{new_house[0]};{int(new_house[1])+1}'
            case '>':
                new_house = f'{int(new_house[0])+1};{new_house[1]}'
            case 'v':
                new_house = f'{new_house[0]};{int(new_house[1])-1}'
            case '<':
                new_house = f'{int(new_house[0])-1};{new_house[1]}'
        if new_house in houses:
            houses[new_house] += 1
        else:
            houses[new_house] = 1
        new_house = new_house.split(';')
    return houses
    

#%% PART 1

houses = deliver_presents(data)

print(f'Houses with at least one present: {len(houses)}')


#%% PART 2

santa = [data[i] for i in range(0, len(data), 2)]
robo_santa = [data[i] for i in range(1, len(data), 2)]

santa_houses = houses = deliver_presents(santa)
robo_houses = deliver_presents(robo_santa)
all_houses = set(santa_houses.keys()).union(set(robo_houses.keys()))
print(f'Houses with at least one present: {len(all_houses)}')

end_time = timer()
elapsed_time = end_time - start_time
print(f'Elapsed time: {elapsed_time:.3f} s')
