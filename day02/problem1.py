#!/usr/bin/env python3

# Define variables
redLimit = 12
greenLimit = 13
blueLimit = 14
total = 0

# Read input file
with open('input.txt', 'r') as f:
    for line in f:
        # Split the line to find the game number and the different views
        line = line.replace('\n', '')
        failFlag = False
        line = line.split(':')
        gameNumber = int(line[0][5:])
        viewList = line[1].split(';')
        # For each view determine the number of each color seen and compare to the max
        for view in viewList:
            view = view.split(',')
            for color in view:
                if color.endswith('red'):
                    color = int(color.replace('red', ''))
                    if color > redLimit:
                        failFlag = True
                elif color.endswith('green'):
                    color = int(color.replace('green', ''))
                    if color > greenLimit:
                        failFlag = True
                elif color.endswith('blue'):
                    color = int(color.replace('blue', ''))
                    if color > blueLimit:
                        failFlag = True
                if failFlag:
                    break
            if failFlag:
                break
        # If we did not exceed the max then add this game number to the total
        if not failFlag:
            total += gameNumber

# Output data
print(f'The sum of the possible games is: {total}')
