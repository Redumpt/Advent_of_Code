# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:07:46 2022

@author: ghochart
"""

file = '.4.csv'
cleanup = open(file).read().replace('"','').split('\n')
cleanup.pop()
list_in_count = 0
overlap_count = 0

for section in cleanup:
    temp = []
    for group in section.split(','):
        left, right = group[:group.find('-')], group[group.find('-') + 1:]
        temp.append(int(left))
        temp.append(int(right))
    if (temp[0] >= temp[2] and temp[1] <= temp[3]) or (temp[2] >= temp[0] and temp[3] <= temp[1]):
        list_in_count += 1
    
for section in cleanup:
    temp = []
    for group in section.split(','):
        left, right = group[:group.find('-')], group[group.find('-') + 1:]
        temp.append(int(left))
        temp.append(int(right))
    if (temp[2] <= temp[0] <= temp[3]) or (temp[2] <= temp[1] <= temp[3]):
        overlap_count += 1
        continue
    elif (temp[0] <= temp[2] <= temp[1]) or (temp[0] <= temp[3] <= temp[1]):
        overlap_count += 1

print(list_in_count)
print(overlap_count)