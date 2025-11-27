#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2024 - Day 2

Created on Thu Nov 27 22:42:44 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

import numpy as np

#filename = 'D2_test.in'
filename = 'D2.in'

# the number of levels is not constant => cannot use numpy...
#reports = np.loadtxt(filename, dtype=int)
with open(filename, 'r') as file:
    reports = file.readlines()


#%% PUZZLE 1

N_safe = 0
for report in reports:
    # split at spaces, then convert strings to ints (removing trailing \n)
    report = report.split(' ')
    report = [int(level) for level in report]
    report = np.array(report)
    delta = np.diff(report)
    # all-increasing or all-decreasing
    monotonic = (delta > 0).all() | (delta < 0).all()
    small_delta = (abs(delta) >= 1).all() & (abs(delta) <= 3).all()
    safe_report = monotonic & small_delta
    if safe_report:
        N_safe += 1       

print(f'Safe reports: {N_safe}')


#%% PUZZLE 1

N_safe = 0
for report in reports:
    # split at spaces, then convert strings to ints (removing trailing \n)
    report = report.split(' ')
    report = [int(level) for level in report]
    report = np.array(report)
    delta = np.diff(report)
    # all-increasing or all-decreasing
    monotonic = (delta > 0).all() | (delta < 0).all()
    small_delta = (abs(delta) >= 1).all() & (abs(delta) <= 3).all()
    safe_report = monotonic & small_delta
    if safe_report:
        N_safe += 1
    # add Problem Dampener
    else:
        # scenario 1:
        # [1, 3, 2, 4, 5] has delta [2, -1, 2, 1] => one delta < 0, but if
        # the 2nd element (same index as the delta_i < 0) is removed, then the
        # report is [1, 2, 4, 5] and has delta [1, 2, 3] => safe
        # similarly, this holds if all the delta's < 0 but one is > 0
        # => this holds only if ONLY ONE delta has a different sign, otherwise
        # removing one level is not enough to make the report safe
        
        # booleans are like ints
        N_neg = np.sum(delta < 0)
        N_pos = np.sum(delta > 0)
        if N_neg == 1 or N_pos == 1:
            if N_neg == 1:
                idx_bad_level = np.argwhere(delta < 0)
            elif N_pos == 1:
                idx_bad_level = np.argwhere(delta > 0)
            report_cleaned = np.delete(report, idx_bad_level)
            # the report may be safe now => recalculate the deltas to check
            # whether the level increase is not excessive
            delta_cleaned = np.diff(report_cleaned)
            monotonic = (delta_cleaned > 0).all() | (delta_cleaned < 0).all()
            small_delta = (abs(delta_cleaned) >= 1).all() & (abs(delta_cleaned) <= 3).all()
            safe_report = monotonic & small_delta
            if safe_report:
                N_safe += 1
                # the report has been made safe, go to next one
                continue
        
        # scenario 2: 
        # all the delta's are >0 or <0, but they're too big (>3) or too small (<1)
        # BRUTE FORCE METHOD: try removing each element once and check the result
        for j in range(report.shape[0]):
            new_report = np.delete(report, j)
            delta_new = np.diff(new_report)
            # all-increasing or all-decreasing
            monotonic = (delta_new > 0).all() | (delta_new < 0).all()
            small_delta = (abs(delta_new) >= 1).all() & (abs(delta_new) <= 3).all()
            safe_report = monotonic & small_delta
            if safe_report:
                N_safe += 1
                # this report is safe, no need to keep trying 
                break
        
        # if you've reached this point, the report cannot be made safe  

print(f'Safe reports: {N_safe}')
