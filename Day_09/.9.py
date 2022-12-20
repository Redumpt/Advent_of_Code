# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:47:32 2022

a = [i+p for i,p in zip(x,y)]

@author: ghochart
"""

with open('.9.txt') as file:
    moves = file.read().split('\n')


move = {'L': [-1,0],
        'R': [1,0],
        'U': [0,1],
        'D': [0,-1]}

knots = [[0,0] for i in range(10)]
recorded_coordonate = set()

for step in moves:
    d,s = step.split()
    for count in range(int(s)):
        for idx, knot in enumerate(knots):
            if idx == 0:
                knots[idx] = [d+h for d,h in zip(move[d],knots[idx])]
                continue
            gap = [h-t for h,t in zip(knots[idx-1],knots[idx])]
            if (-1 <= gap[0] <= 1) and (-1 <= gap[1] <= 1):
                pass
            else:
                if gap[0] == 0 or gap[1] == 0:
                    knots[idx] = [int(t+(g*0.5)) for t,g in zip(knots[idx],gap)]
                else:
                    knots[idx] = [int(t+(g/2)) if abs(g) == 2 else t+g for t,g in zip(knots[idx],gap)]                
            if idx == len(knots)-1:
                recorded_coordonate.add(tuple(knots[idx]))
        
print(len(recorded_coordonate))

file.close()