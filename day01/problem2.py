#!/usr/bin/env python3

# Define variables
nums = '0123456789'
nums_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
total = 0

# Read input file
with open('input.txt', 'r') as f:
    for line in f:
        value = -1
        # Find the first number in the line
        forward = line
        for i, character in enumerate(forward):
            if character in nums:
                value = 10 * int(character)
            elif character in 'otfsen':
                temp = forward[i:]
                # Since the character is the same as the spelled number check by replacing
                for key, v in nums_dict.items():
                    temp_new = temp.replace(key, v)
                    if temp_new[0] in nums:
                        value = 10 * int(temp_new[0])
                        break
            if value >= 0:
                break  # We have found the value so break
        # Reverse the line
        line = list(line)
        line.reverse()
        line = ''.join(line)
        # Find the second number in the line
        rev = line
        ones_digit = -1
        for i, character in enumerate(rev):
            if character in nums:
                ones_digit = int(character)
            elif character in 'otfsen':
                temp = rev[:i+1]
                temp = list(temp)
                temp.reverse()
                temp = ''.join(temp)
                # Since the character is the same as the spelled number check by replacing
                for key, v in nums_dict.items():
                    temp_new = temp.replace(key, v)
                    if temp_new[0] in nums:
                        ones_digit = int(temp_new[0])
                        break
            if ones_digit >= 0:
                value += ones_digit
                break  # We have found the value so break
        total += value

# Output data
print(f'The sum of the calibration values is: {total}')
