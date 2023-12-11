#!/usr/bin/env python3

class Seed:
    def __init__(self, number):
        seed_dict = {
            'seed': number,
            'soil': number,
            'fertilizer': number,
            'water': number,
            'light': number,
            'temperature': number,
            'humidity': number,
            'location': number,
        }
        self.info = seed_dict

# Read input file
with open('input.txt', 'r') as f:
    for line in f:
        if line.startswith('seeds'):
            seedline = line.split(':')[1].split()
            seeds = list()
            for seedNumber in seedline:
                seeds.append(Seed(int(seedNumber)))
        if line.find('map') >= 0:
            sourceStr = line.split(' ')[0].split('-')[0]
            destinationStr = line.split(' ')[0].split('-')[-1]
            for seed in seeds:
                seed.info[destinationStr] = seed.info[sourceStr]
        if line[0].isdigit():
            line = line.replace('\n', '')
            dest_start = int(line.split(' ')[0])
            source_start = int(line.split(' ')[1])
            range_len = int(line.split(' ')[2])
            for seed in seeds:
                sourceValue = seed.info[sourceStr]
                if (sourceValue >= source_start) and (sourceValue < (source_start + range_len)):
                    delta = sourceValue - source_start
                    seed.info[destinationStr] = dest_start + delta

# Find the min location value
min_value = 999999999999999999999999
for seed in seeds:
    value = seed.info['location']
    if value < min_value:
        min_value = value

# Output data
print(f'The min location value is: {min_value}')
  