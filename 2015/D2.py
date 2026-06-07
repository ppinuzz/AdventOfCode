#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2015 - Day 2

Created on Sun Jun  7 21:05:17 2026

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

from timeit import default_timer as timer
import numpy as np

filename = 'D2.in'

with open(filename, 'r') as file:
	# remove trailing '\n' automatically
    data = file.read().splitlines()

start_time = timer()

tot = 0
ribbon = 0
vol = 0
for sides in data:
    sides = np.array(sides.split('x'), dtype=int)
    A1 = sides[0] * sides[1]
    A2 = sides[0] * sides[2]
    A3 = sides[2] * sides[1]
    extra = np.min([A1, A2, A3])
    tot += 2*(A1 + A2 + A3) + extra
    vol += np.prod(sides)
    
    sides[np.argmax(sides)] = -1
    short_sides = sides[sides > 0]
    ribbon += 2*(short_sides[1] + short_sides[0])
ribbon += vol

print(f'Square feet of paper: {tot}')
print(f'Feet of ribbon: {ribbon}')

end_time = timer()
elapsed_time = end_time - start_time
print(f'Elapsed time: {elapsed_time:.3f} s')
