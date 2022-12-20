# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 08:34:44 2022

A = rock = X
B = paper = Y
C = scissors = Z

Score = rock:1, paper:2, scissors:3
        win:6, draw:3, lose:0

@author: ghochart
"""

file = '.2.csv'
rps_strategy = open(file).read().split('\n')

rps_points = {'X':1, 'Y':2, 'Z':3, 'A':1, 'B':2, 'C':3}
win_loss_part_1 = {'A X':3,
                   'A Y':6,
                   'A Z':0,
                   'B X':0,
                   'B Y':3,
                   'B Z':6,
                   'C X':6,
                   'C Y':0,
                   'C Z':3}
total_points_part_1 = 0

for round in rps_strategy:
    if round == '':
        continue
    else:    
        round_score = win_loss_part_1[round]
        rps_score = rps_points[round[-1]]
        total_points_part_1 += round_score + rps_score
print(f'Total point part 1 = {total_points_part_1}')

win_loss_part_2 = {'A X':(0,'C'),
                   'A Y':(3,'A'),
                   'A Z':(6,'B'),
                   'B X':(0,'A'),
                   'B Y':(3,'B'),
                   'B Z':(6,'C'),
                   'C X':(0,'B'),
                   'C Y':(3,'C'),
                   'C Z':(6,'A')}

total_points_part_2 = 0

for round in rps_strategy:
    if round == '':
        continue
    else:    
        round_score = win_loss_part_2[round][0]
        rps_score = rps_points[win_loss_part_2[round][1]]
        total_points_part_2 += round_score + rps_score
print(f'Total point part 2 = {total_points_part_2}')
