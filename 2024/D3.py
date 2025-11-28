#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2024 - Day 2

Created on Fri Nov 28 21:03:39 2025

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

#filename = 'D3_test.in'
filename = 'D3.in'

# char in the valid command, e.g. mul(124,3)
valid_char = ['m', 'u', 'l', '(', ',', ')']

with open(filename, 'r') as file:
    memory = file.readlines()


#%% PUZZLE 1

commands = []
for line in memory:
    num_length = 0
    reading_command = False
    reading_number = False
    # once you have the line, loop through it until you find the 1st char of
    # the command (i.e. 'm', which is stored in valid_car[0])
    i = 0
    # the command will be stored here
    command_temp = []
    for char in line:
        if char == valid_char[i]:
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
        elif reading_command:
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
        # found a whole command!
        if i == len(valid_char):
            commands.append(command_temp)
            command_temp = []
            i = 0
            reading_command = False
            reading_number = False
            num_length = 0

# now that you have all of the commands, evaluate them => easy: extract the 
# digits and multiply them
result = 0
for command in commands:
    N_1 = ''
    N_2 = ''
    # start by putting the digits into the 1st number
    reading_first_num = True
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
                result = result + int(N_1) * int(N_2)

print(f'Valid commands found: {len(commands)}')
print(f'Total sum: {result}')


#%% PUZZLE 2
