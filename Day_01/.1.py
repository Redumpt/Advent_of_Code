# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 08:34:44 2022

@author: ghochart
"""

file = '.1.csv'

cal_list = open(file).read().split(sep='\n')
total_cal = 0
max_cal = 0
max_cal_list = []

for cal in cal_list:
    if cal == '':
        if total_cal > max_cal:
            max_cal_list.append(total_cal)
            max_cal = total_cal
            total_cal = 0
        else:
            max_cal_list.append(total_cal)
            total_cal = 0
    else:
        total_cal += int(cal)
        
print(f'maximum calories carried = {max_cal}')   
max_cal_list.sort(reverse=True)
print(f'Total of top 3 maximum calories = {sum(max_cal_list[0:3])}')
