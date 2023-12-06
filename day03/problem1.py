#!/usr/bin/env python3

# Define variables
symbols = '=+-#*/&@%$'
null_value = '.'
numbers = '0123456789'
row = 0

# Define helper functions
def number_locations(map, tup_loc, max_rows, max_cols, numbers):
    row = tup_loc[0]
    col = tup_loc[1]
    num_list = list()
    for i in [row - 1, row, row + 1]:
        for j in [col - 1, col, col + 1]:
            if (i >= 0) and (i < max_rows):
                if (j >= 0) and (j < max_cols):
                    if map[i][j] in numbers:
                        num_list.append((i, j))
    return num_list

def find_number_from_location(map, tup_loc, max_cols, numbers):
    row = tup_loc[0]
    col = tup_loc[1]
    val = map[row][col]
    left = col
    while ((left - 1) >= 0) and (map[row][left - 1] in numbers):
        val = map[row][left - 1] + val
        left -= 1
    right = col
    while ((right + 1) < max_cols) and (map[row][right + 1] in numbers):
        val = val + map[row][right + 1]
        right += 1
    return {(row, left): int(val)}

map = list()
symbol_locations = list()
with open('input.txt', 'r') as f:
    for line in f:
        line = list(line.replace('\n', ''))
        col_cnt = len(line)
        for i in range(col_cnt):
            if line[i] in symbols:
                symbol_locations.append((row, i))
        map.append(line)
        row += 1

parts = dict()
for loc in symbol_locations:
    number_list = number_locations(map, loc, row, col_cnt, numbers)
    for item in number_list:
        num = find_number_from_location(map, item, col_cnt, numbers)
        for k, v in num.items():
            parts[k] = v

total = 0
for _, v in parts.items():
    total += v

# Output data
print(f'The sum of the part numbers is: {total}')
