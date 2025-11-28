#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2024 - Day 2

Created on Fri Nov 28 21:03:39 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

import numpy as np

#filename = 'D3_test_1.in'
#filename = 'D3_test_2.in'
filename = 'D3.in'

# char in the valid command, e.g. mul(124,3)
valid_char = ['m', 'u', 'l', '(', ',', ')']
chars_cond = [['d', 'o', '(', ')'], ['d', 'o', 'n', "'", 't', '(', ')']]

with open(filename, 'r') as file:
    memory = file.readlines()


commands = []
for line in memory:
    num_length = 0
    reading_command = False
    reading_number = False
    reading_cond_statement = False
    reading_dont = False
    # once you have the line, loop through it until you find the 1st char of
    # the command (i.e. 'm', which is stored in valid_car[0])
    i = 0
    # same, but for the conditional statement
    j = 0
    # the command will be stored here
    command_temp = []
    for char in line:
        if char == valid_char[i] and not reading_cond_statement:
            command_temp.append(char)
            # move to the next char in the command (e.g. 'u', if you've found
            # the first 'm')
            i += 1
            # if True, you're reading a potential command
            reading_command = True
            # if you've been reading a number, reset the length counter
            if reading_number:
                num_length = 0
                reading_number = False
        # if you've detected a sequence that could be a command, but this new
        # character is not a valid char OR an integer of 1-3 digits, then 
        # discard the content of the command and restart from the 1st valid
        # char (i.e. from 'm')
        elif reading_command and not reading_cond_statement:
            # if you're reading a potential command and you're here:
            #   - you might have read a char which is not valid (e.g. x)
            #       => start from scratch
            #   - you might have found a number => check if its length is 1-3
            #   digits
            if char.isdigit() and num_length < 3:
                command_temp.append(char)
                num_length += 1
                # now you're reading a number
                reading_number = True
            else:
                # if not a digit, it's an invalid char or it's a too long number
                i = 0
                reading_command = False
                reading_number = False
                command_temp = []
                num_length = 0
        # if you've reached this point and i == 6 (last valid char), then you've
        # found a whole command and you've just read the last char
        if i == len(valid_char):
            commands.append(command_temp)
            command_temp = []
            i = 0
            reading_command = False
            reading_number = False
            num_length = 0
            # move directly to next char, to skip the next instruction
            continue
        
        if not reading_command:
            # if you've reached this point, the char is not in the command, but
            # it might be in a conditional statement
            # both do() and don't() share the initial 'do', you can check either
            # SHORT CIRCUIT EVALUATION: before cheking for char in do(), if 
            # j >= 3 it won't be possible, since do() has j=0-3 => do not try
            # to evaluate char == chars_cond[0][j], as j will be out-of-bounds
            if j < 4 and char == chars_cond[0][j]:
                command_temp.append(char)
                j += 1
                reading_cond_statement = True
            # if the char is not in do(), it might be in don't()
            elif char == chars_cond[1][j]:
                command_temp.append(char)
                j += 1
                reading_cond_statement = True
                reading_dont = True
            else:
                # or it might not be in both
                command_temp = []
                j = 0
                reading_cond_statement = False
                reading_dont = False
        # if j = 4 and you're reading do(), or j = 7 and you're reading
        # don't(), then you've found an entire conditional statement!
        if (j == len(chars_cond[0]) and not reading_dont) or (j == len(chars_cond[1]) and reading_dont):
            commands.append(command_temp)
            command_temp = []
            j = 0
            reading_cond_statement = False
            reading_dont = False
        

# now that you have all of the commands, evaluate them
mults = []
for command in commands:
    N_1 = ''
    N_2 = ''
    # start by putting the digits into the 1st number
    reading_first_num = True
    # if you've found a do() or don't() statement 
    # put a dummy value and skip to the next command
    whole_command = ''.join(command)
    if whole_command == 'do()':
        mults.append(+np.inf)
        continue
    elif whole_command == "don't()":
        mults.append(-np.inf)
        continue
    for char in command:
        if char.isdigit():
            # concatenate strings, do not append them into a list
            if reading_first_num:
                N_1 += char
            else:
                N_2 += char
        else:
            # if this is not a digit, then it's either a letter/(), or the ','
            # separating the 2 operands => if it's a comma, then the 1st number
            # is completed
            if char == ',':
                reading_first_num = False
            # if you've reached the ')', then you have both numbers!
            elif char == ')':
                mult = int(N_1) * int(N_2)
                mults.append(mult)

result = 0
# at the beginning, mul() is enable => don't skip the multiplication results
skip_mults = False
for mult in mults:
    # if you find +Inf, that's a do => keep reading next mults
    if mult == +np.inf:
        skip_mults = False
        # (skip to next value because this is just a placeholder)
        continue
    # if it's -Inf, it's a don't() => start skipping
    elif mult == -np.inf:
        skip_mults = True
        continue
    
    if not skip_mults:
        result = result + mult
    
print(f'Valid commands found: {len(commands)}')
print(f'Total sum: {result}')
