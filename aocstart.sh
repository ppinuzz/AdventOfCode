#/usr/bin/bash

# get today's day number
# 1) date +%d	outputs day of the mont with 2 digits (e.g. 03)
# 2) pass to sed to remove leading 0, if present
# 3) s/.../.../ = "substitute what's in 1st /.../ with what's in 2nd /.../"
#	^	start of the line
#	0*	any number of 0s
#	since the 2nd /.../ is empty, this replaces all the leading 0s with nothing
day_number=$(date +%d | sed 's/^0*//')
year=$(date +%Y)
# full date string like 'Mon Dec  1 09:20:22 2025'
today=$(date +"%a %b %e %H:%M:%S %Y")

# crate year directory, if it doesn't exist already
mkdir -p "${year}"
python_file="${year}/D${day_number}.py"
input_file="${year}/D${day_number}.in"
test_file="${year}/D${day_number}_test.in"

if [[ -e "${python_file}" ]]; then
	echo "File ${python_file} already exists! Skipping creation..."
	exit 1
else
	# <<EOF 	everything from EOF to the line containing EOF will be treated as 
	# as input to cat (i.e. it will be printed to file here)
	cat > "${python_file}" <<EOF
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025 - Day ${day_number}

Created on ${today}

@author: Andrea Pinardi <andreapinardi319@gmail.com>
"""

filename = 'D${day_number}_test.in'
#filename = 'D${day_number}.in'

with open(filename, 'r') as file:
	# remove trailing '\n' automatically
    data = file.read().splitlines()
EOF
	echo "Created ${python_file}, ${input_file} and ${test_file}"
	# bad trick to create new files
	touch "${input_file}"
	touch "${test_file}"
fi