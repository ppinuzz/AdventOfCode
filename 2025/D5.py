#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025 - Day 5

Created on Fri Dec  5 09:03:34 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

from timeit import default_timer as timer
import numpy as np

filename = 'D5_test.in'
#filename = 'D5.in'

with open(filename, 'r') as file:
	# remove trailing '\n' automatically
    data = file.read().splitlines()

start_time = timer()


#%% PUZZLE 1

good_IDs = []
products = []
for i, line in enumerate(data):
    if line:
        ID1, ID2 = line.split('-')
        ID_range = [int(ID1), int(ID2)]
        good_IDs.append(ID_range)
    else:
        products = list(map(int, data[i+1:]))
        break

N_good = 0
for ID in products:
    for IDrange in good_IDs:
        if ID >= IDrange[0] and ID <= IDrange[1]:
            N_good += 1
            # move to next ID once you've established this is safe
            break

print(f'Number of safe items: {N_good}')


#%% PUZZLE 2

good_IDs.append([3, 7])
good_IDs.append([4, 8])
good_IDs.append([4, 6])
good_IDs.append([5, 9])

good_IDs = np.array(good_IDs)
MAX = np.max(good_IDs)
# sentinel value
SENT = MAX + 1
ranges_safe = []
range_i = None
while np.sum(good_IDs == SENT) < good_IDs.size:
    # 1st value is the minimum of the possible 1st points (i.e. 1st column)
    ID_1 = np.min(good_IDs[:,0])
    idx_1 = (good_IDs[:,0] == ID_1)
    # if there are more occurrences of the same left limit, choose the one with the
    # highest right limit...
    max_dx = np.max(good_IDs[idx_1,1])
    idx_highest_1 = np.argwhere(good_IDs[:,1] == max_dx)[0][0]
    # ... and then select its right limit
    ID_2 = good_IDs[idx_highest_1,1]
    if range_i is not None and ID_1 > range_i[1]:
        ranges_safe.append(range_i)
    if range_i is not None:
        if ID_1 < range_i[1] and ID_2 > range_i[1]:
            range_i[1] = ID_2
        else:
            range_i = [ID_1, ID_2]
    else:
        range_i = [ID_1, ID_2]
    # "remove" all the values you've either used to create the range, or discarded
    # (e.g. if you have more ranges with the same left limit, only the range with 
    # the highest right limit is useful; all the others are included in it)
    good_IDs[idx_1,:] = SENT
    
    
    
    # now the biggest valid ID is range_i[1] and all the values below it are:
    #   - useless if they appear in the 2nd column: if all the values in between
    #   ID_1 and ID_2 are safe, all the intervals ending in something < ID_2 are
    # already included => remove those lines entirely
    good_IDs[good_IDs[:,1]<=range_i[1], :] = SENT
    
    # check among those having left <= range_i[2]: choose the one with the biggest
    # right value => overlapping ranges => expand the range
    idx_smaller_1 = np.squeeze(np.argwhere(good_IDs[:,0] <= range_i[1]))
    if idx_smaller_1.size > 0:
        # and choose the one with the highest right value
        max_dx = np.max(good_IDs[idx_smaller_1,1])
        idx_smaller_highest_1 = np.squeeze(np.argwhere(good_IDs[:,1] == max_dx))
        # once you have it, substitute the 2md range element
        range_i[1] = max_dx
        good_IDs[idx_smaller_1,:] = SENT
ranges_safe.append(range_i)

ranges_safe = np.array(ranges_safe)
N = np.sum(np.diff(ranges_safe) + 1)


print(f'Number of safe IDs: {N}')

# 328879328518241: too low
# 348388785848227: too low
# 355500779999935: too low

end_time = timer()
elapsed_time = end_time - start_time
print(f'Elapsed time: {elapsed_time:.2f} s')