# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 09:20:23 2022

@author: ghochart
"""
import string

file = '.3.csv'
rucksack = open(file).read().split('\n')

a_z = {}
for count,letter in enumerate(list(string.ascii_letters)):
    a_z[letter] = count + 1
    
priorities_points = 0
for compartiment in rucksack:
    if compartiment == '':
        continue
    else:
        length = int(len(compartiment) / 2)
        left = compartiment[:length]
        right = compartiment[length:]
        for obj in left:
            if obj in right:
                priorities_points += a_z[obj]
                break
        
print(f'Priorities sum = {priorities_points}')

count = 0
groups = []
badge_points = 0

for group in rucksack:
    if count == 3:
        count = 0
        for obj in groups[0]:
            if obj in groups[1] and obj in groups[2]:
                badge_points += a_z[obj]
                break
        groups.clear()            
    groups.append(group)
    count += 1
        
print(f'badge sum = {badge_points}')
        