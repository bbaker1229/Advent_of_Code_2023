#!/usr/bin/env python3

# Define variables
nums = '0123456789'
total = 0

# Read input file
with open('input.txt', 'r') as f:
    for line in f:
        line = list(line)
        value = 0
        # Find the first number in the line
        for i in line:
            if i in nums:
                value = 10 * int(i)
                break
        line.reverse()
        # Find the second number in the line
        for i in line:
            if i in nums:
                value += int(i)
                break
        total += value

# Output data
print(f'The sum of the calibration values is: {total}')
