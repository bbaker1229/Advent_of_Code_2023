#!/usr/bin/env python3

# Define variables
total_score = 0

# Read input file
with open('input.txt', 'r') as f:
    for line in f:
        # Split the line to find the game number and the different views
        line = line.replace('\n', '')
        gameNumber = int(line.split(':')[0].split(' ')[-1])
        winningNumbers = line.split(':')[1].split('|')[0].strip().split(' ')
        winningNumbers = [int(i) for i in winningNumbers if i != '']
        myNumbers = line.split(':')[1].split('|')[1].strip().split(' ')
        myNumbers = [int(i) for i in myNumbers if i != '']
        temp = list()
        score = 0
        for value in myNumbers:
            if value in winningNumbers:
                temp.append(value)
                if score == 0:
                    score = 1
                else:
                    score *= 2
        total_score += score
    
# Output data
print(f'The total score is: {total_score}')
        