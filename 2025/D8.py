#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025 - Day 8

Created on Mon Dec  8 14:57:16 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

from timeit import default_timer as timer
import numpy as np
import itertools

#filename = 'D8_test.in'
filename = 'D8.in'

with open(filename, 'r') as file:
	# remove trailing '\n' automatically
    data = file.read().splitlines()
data = np.array([line.split(',') for line in data], dtype=int)

start_time = timer()


#%% PUZZLE 1

if filename == 'D8_test.in':
    N_connections = 10
else:
    N_connections = 1000

# build all possible combinations without repetitions:
#   C(n,k) = n!/(k!(n-k)!)
# being couples, k = 2 and C(n,2) = n(n-1)/2
# create couples of row indices, not physical coordinates (easier to handle)
couples = list(itertools.combinations(range(0,data.shape[0]), 2))

dist = np.zeros((len(couples),), dtype=int)
for i, couple in enumerate(couples):
    dist[i] = np.linalg.norm(data[couple[0],:] - data[couple[1],:])

dist = list(dist)
circuits = []
circuits_pts = []
N = 0
while N < N_connections:
    # find couples of closest junction boxes
    idx_min_dist = np.argmin(dist)
    couple = couples[idx_min_dist]
    
    # check if one of the 2 points lies in a circuit
    idx_circ = None
    p1_in_circ = None
    p2_in_circ = None
    merged_circuits = False
    for i, circ in enumerate(circuits):
        if couple[0] in circ:
            p1_in_circ = i
        if couple[1] in circ:
            p2_in_circ = i
            
    if (p1_in_circ is not None) and (p2_in_circ is not None) and (p1_in_circ != p2_in_circ):
        circuits[p1_in_circ].update(circuits[p2_in_circ])
        del circuits[p2_in_circ]
        merged_circuits = True
        circuits_pts[p1_in_circ].update(circuits_pts[p2_in_circ])
        del circuits_pts[p2_in_circ]
    elif p1_in_circ is not None:
        idx_circ = p1_in_circ
    elif p2_in_circ is not None:
        idx_circ = p2_in_circ
    
    if not merged_circuits:
        # one of the points appears in another circuit
        if idx_circ is not None:
            # do nothing if the 2 points are in the same circuit already
            if not (couple[0] in circuits[idx_circ] and couple[1] in circuits[idx_circ]):
                circuits[idx_circ].update([couple[0], couple[1]])
                # all the int() are just to have a more readable output
                circuits_pts[idx_circ].update([(int(data[couple[0],0]),
                                                int(data[couple[0],1]),
                                                int(data[couple[0],2])), 
                                               (int(data[couple[1],0]),
                                                int(data[couple[1],1]),
                                                int(data[couple[1],2]))
                                               ])
        else:
            circuits.append(set([couple[0], couple[1]]))
            # convert ndarray to tuples to add them to the set
            circuits_pts.append(set([(int(data[couple[0],0]),
                                      int(data[couple[0],1]),
                                      int(data[couple[0],2])), 
                                     (int(data[couple[1],0]),
                                      int(data[couple[1],1]),
                                      int(data[couple[1],2]))
                                     ])
                                )
    
    # once you've connected directly two points, remove the couple
    del dist[idx_min_dist]
    del couples[idx_min_dist]
    N += 1

len_circs = [len(circuit) for circuit in circuits]
len_circs.sort()    # in ascending order
try:
    dim_circuits = len_circs[-1] * len_circs[-2] * len_circs[-3]
except:
    dim_circuits = -1

print(f'Product of the 3 largest circuits: {dim_circuits}')

end_time = timer()
elapsed_time = end_time - start_time
print(f'Elapsed time: {elapsed_time:.2f} s')
