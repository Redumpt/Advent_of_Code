# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 13:45:41 2022

CRT = 40 * 6

@author: ghochart
"""

with open('.10.txt') as file:
    signal = file.read().split('\n')
    
cycles = 0
x = 1
signal_strength = 0
final_cycles = 240
fix_cycles = [i for i in range(20,final_cycles + 1,40)]

for mes in signal:
    if cycles > final_cycles:
        break
    if cycles == fix_cycles[0]:
        signal_strength += fix_cycles[0] * x
        fix_cycles.append(fix_cycles.pop(0))
    if mes == 'noop':
        cycles += 1
    else:
        cycles += 1
        if cycles == fix_cycles[0]:
            signal_strength += fix_cycles[0] * x
            fix_cycles.append(fix_cycles.pop(0))
        cycles += 1
        if cycles == fix_cycles[0]:
            signal_strength += fix_cycles[0] * x
            fix_cycles.append(fix_cycles.pop(0))
        x += int(mes.split()[1])

print(signal_strength)

cycles = 1
x = 1
sprit = '###'
sprit_position = '.' * (x-1) + sprit + '.' * (38 - x)
drawing = ''
count = 0
for mes in signal:
    if mes == 'noop':
        drawing += sprit_position[count]
        count += 1
        cycles += 1
    else:
        drawing += sprit_position[count]
        count += 1
        if count > 39:
            count -= 40
            print(drawing)
            drawing = ''
        drawing += sprit_position[count]
        count += 1
        cycles += 2
        x += int(mes.split()[1])
        sprit_position = '.' * (x-1) + sprit + '.' * (38 - x)
    if count > 39:
        count -= 40
        print(drawing)
        drawing = ''
    
        