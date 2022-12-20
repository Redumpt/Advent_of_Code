# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 13:31:07 2022

@author: ghochart
"""

file1, file2 = '.5_moves.csv','.5_start.csv'

moves_file = open(file1).read().split('\n')
start_file = open(file2).read().split('\n')
moves_file.pop(), start_file.pop()


start_file.reverse()
start = []
for line in start_file:
    temp = [line[idx:idx+3].strip() for idx in range(0, len(line), 4)]
    start.append(temp)    
    
box_org = {}
box_org_2 = {}

for count, row in enumerate(start):
    if count == 0:
        for num in row:
            box_org[num] = []
            box_org_2[num] = []
    else:
        for count, box in enumerate(row):
            if box == '':
                pass
            else: 
                box_org[str(count+1)].append(box)
                box_org_2[str(count+1)].append(box)

for step in moves_file:
    times = int(step.split()[1])
    from_ = step.split()[3]
    to = step.split()[-1]
    count = 0
    while count < times:
        box_org[to].append(box_org[from_].pop())
        count += 1

print('CrateMover 9000')
for values in box_org.values():
    print(values[-1])
    
    

for step in moves_file:
    times = int(step.split()[1])
    from_ = step.split()[3]
    to = step.split()[-1]
    count = 0
    while count < times:
        box_org_2[to].append(box_org_2[from_].pop(-(times - count)))
        count += 1

print('\n\nCrateMover 9001')
for values in box_org_2.values():
    print(values[-1])