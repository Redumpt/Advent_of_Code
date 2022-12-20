# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:37:41 2022

@author: ghochart
"""

file = '.7.csv'
system = open(file).read().split('\n')
system.pop()

directories = []
files = []
for count, com in enumerate(system):
    if '$ ls' in com:
        total = 0
        control = count + 1
        layer = 1
        while True:
            if control >= len(system):
                break
            if layer == 0:
                break
            elif '$ cd ..' in system[control]:
                layer -= 1
                control += 1
            elif '$ cd' in system[control]:
                layer += 1
                control += 1
            elif 'dir ' in system[control]:
                control += 1
            elif '$ ls' in system[control]:
                control += 1
            else:
                total += int(system[control].split()[0])
                control += 1
        directories.append((system[count-1],total))
        

total_under_100000 = 0
for directory in directories:
    if int(directory[1]) <= 100000:
        total_under_100000 += int(directory[1])

print(total_under_100000)
print(f'Space left = {70000000 - directories[0][1]}')
print(f'Need to free {30000000 - (70000000 - directories[0][1])}')

free_space_needed = 30000000 - (70000000 - directories[0][1])

diff = None
for num in directories:
    if diff == None:
        diff = num[1] - free_space_needed 
        folder = num
        print(diff)
    elif (num[1] - free_space_needed) > 0 and (num[1] - free_space_needed) < diff:
        diff = num[1] - free_space_needed 
        folder = num
print(diff)
print(folder)