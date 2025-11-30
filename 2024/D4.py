#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2024 - Day 4

Created on Sat Nov 29 16:50:31 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

#filename = 'D4_test.in'
filename = 'D4.in'
#filename = 'prova.in'

with open(filename, 'r') as file:
    lines = file.readlines()

# remove whitespaces
lines = [line.strip() for line in lines]

counter_horz = 0
counter_horz_inv = 0
counter_vert = 0
counter_vert_inv = 0
counter_diag_down_dx = 0
counter_diag_down_sx = 0
counter_diag_up_dx = 0
counter_diag_up_sx = 0
N_rows = len(lines)
N_cols = len(lines[0])
for i in range(N_rows):
    for j in range(N_cols):
        letter = lines[i][j]
        # if the letter is X, it might be the beginning of XMAS
        if letter == 'X':
            # look horizontally, if there's room on the line
            # (i.e. if there are at least 3 more letters)
            if j < N_cols-3:
                # next 3 letters
                if lines[i][j+1:j+4] == 'MAS':
                    counter_horz += 1
            # IT TURNS OUT THAT PYTHON WORKS WEIRDLY WITH NEGATIVE SLICING!
            #   x[2:-1:-1]
            # ideally: start at i=2 and decrease by 1 (step -1) until you 
            # reach -1, not including -1, which should create 
            #   x[2] x[1] x[0]
            # BUT for negative steps, Python normalises the indices first:
            # 	start = 2
            #	stop = -1 => normalised to (len(x) + (-1)) = 4
            # so internally it's interpreted as:
            #	x[2:4:-1]
            # and, since 2 < 4 with a negative step, it won't work 
            # => it doesn't throw an error (because the indices are not out-of-bounds), 
            # it simply returns an empty string
            # => DO NOT USE BACKWARD SLICING, BUT REVERSE THE STRING
            # horizontal backward
            if j >= 3:
                # previous 3 letters: SAMX => read from j-3 to j (excluded) is SAM
                if lines[i][j-3:j] == 'SAM':
                    counter_horz_inv += 1
            # vertical downward
            if i < N_rows-3:
                # since this is a list of strings, not a real matrix, I cannot
                # use proper matrix indexing, such as lines[i+1:i+4][j]
                word = [line[j] for line in lines[i+1:i+4]]
                # from ['M', 'A', 'S'] to 'MAS'
                word = ''.join(word)
                if word == 'MAS':
                    counter_vert += 1
            # vertical upward (inverse order)
            if i >= 3:
                word = [line[j] for line in lines[i-3:i]]
                word = ''.join(word)
                if word == 'SAM':
                    counter_vert_inv += 1
            # diagonal downward (left -> right) _|
            if j < N_cols-3 and i < N_rows-3:
                # go down and right
                word = [line[k] for line, k in zip(lines[i+1:i+4], range(j+1, j+4))]
                word = ''.join(word)
                if word == 'MAS':
                    counter_diag_down_dx += 1
            # diagonal downward (right -> left) |_
            if j >= 3 and i < N_rows-3:
                # go down and left
                # while slicing with negative steps is tricky, range() DOES
                # behave as intended: if j==3, then range(2, -1, -1) is 
                # treated as [2, 1, 0]
                word = [line[k] for line, k in zip(lines[i+1:i+4], range(j-1, j-4, -1))]
                word = ''.join(word)
                if word == 'MAS':
                    counter_diag_down_sx += 1
            # diagonal upward (left -> right) ^|
            if j < N_cols-3 and i >= 3:
                # go up and right
                word = [line[k] for line, k in zip(lines[i-3:i], range(j+3, j, -1))]
                word = ''.join(word)
                if word == 'SAM':
                    counter_diag_up_dx += 1
            # diagonal upward (right -> left) |^
            if j >= 3 and i >= 3:
                # go up and left
                word = [line[k] for line, k in zip(lines[i-3:i], range(j-3, j))]
                word = ''.join(word)
                if word == 'SAM':
                    counter_diag_up_sx += 1

counter = counter_horz + counter_horz_inv + counter_vert + counter_vert_inv \
            + counter_diag_down_dx + counter_diag_down_sx \
            + counter_diag_up_dx + counter_diag_up_sx

print('XMAS appears: ')
print(f'\t{counter_horz} horizontal XMAS')
print(f'\t{counter_horz_inv} horizontal backward SAMX')
print(f'\t{counter_vert} vertical downward X/M/A/S')
print(f'\t{counter_vert_inv} vertical upward S/A/M/X')
print(f'\t{counter_diag_down_dx} diagonal downward dx X/M/A/S')
print(f'\t{counter_diag_down_sx} diagonal downward sx X/M/A/S')
print(f'\t{counter_diag_up_dx} diagonal upward dx S/A/M/X')
print(f'\t{counter_diag_up_sx} diagonal upward sx S/A/M/X')
print(f'Total: {counter}')

# =============================================================================
# 2575
# That's not the right answer; your answer is too low. Curiously, it's the right answer for someone else; you might be logged in to the wrong account or just unlucky. In any case, you need to be using your puzzle input. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again.
# =============================================================================

# =============================================================================
# 2622
# That's not the right answer; your answer is too low. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. [Return to Day 4]
# =============================================================================
