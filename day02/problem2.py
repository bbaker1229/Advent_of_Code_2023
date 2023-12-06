#!/usr/bin/env python3

# Define variables
total = 0

# Read input file
with open('input.txt', 'r') as f:
    for line in f:
        # Split the line to find the game number and the different views
        line = line.replace('\n', '')
        redMax = 0
        greenMax = 0
        blueMax = 0
        line = line.split(':')
        viewList = line[1].split(';')
        # For each view determine the number of each color seen and compare to the max seen in the game
        for view in viewList:
            view = view.split(',')
            for color in view:
                if color.endswith('red'):
                    color = int(color.replace('red', ''))
                    if color > redMax:
                        redMax = color
                elif color.endswith('green'):
                    color = int(color.replace('green', ''))
                    if color > greenMax:
                        greenMax = color
                elif color.endswith('blue'):
                    color = int(color.replace('blue', ''))
                    if color > blueMax:
                        blueMax = color
        # Determine the power of the game and add to the total
        gamePower = redMax * greenMax * blueMax
        total += gamePower

# Output data
print(f'The sum of the powers is: {total}')
