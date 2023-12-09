#!/usr/bin/env python3

# Define variables
card_dict = dict()

# Read input file
with open('input.txt', 'r') as f:
    for line in f:
        # Split the line to find the game number and the different views
        line = line.replace('\n', '')
        gameNumber = int(line.split(':')[0].split(' ')[-1])
        card_dict[gameNumber] = dict()
        winningNumbers = line.split(':')[1].split('|')[0].strip().split(' ')
        winningNumbers = [int(i) for i in winningNumbers if i != '']
        card_dict[gameNumber]['winners'] = winningNumbers
        myNumbers = line.split(':')[1].split('|')[1].strip().split(' ')
        myNumbers = [int(i) for i in myNumbers if i != '']
        card_dict[gameNumber]['myNumbers'] = myNumbers
        temp = list()
        for value in myNumbers:
            if value in winningNumbers:
                temp.append(value)
        card_dict[gameNumber]['score'] = len(temp)
        card_dict[gameNumber]['count'] = 1

for k, _ in card_dict.items():
    card_score = card_dict[k]['score']
    cards_to_update = [i for i in range(k+1, k+card_score+1)]
    for card in cards_to_update:
        card_dict[card]['count'] += card_dict[k]['count']

card_count = 0
for k, _ in card_dict.items():
    card_count += card_dict[k]['count']

# Output data
print(f'The total number of scratchcards is: {card_count}')
# 1093 is too low