# -*- coding: utf-8 -*-
"""
adventofcode.com - Day 15

"""

import regex as re

def spread(signal, row):
    r = signal[4]
    x = signal[0]
    y = signal[1]
    dis = abs(row - y)
    force = r-dis
    minimum = x - force
    maximum = x + force
    if y < row and y + r >= row:
        return [minimum,maximum]
    elif y > row and y - r <= row:
        return [minimum,maximum]
    elif y == row:
        return [minimum,maximum]
    else:
        return 0

with open('.15.txt') as file:
    signals = file.read().split('\n')
    #  FROM 'Sensor at x=1, y=2: closest beacon is at x=3, y=4' TO [1,2,3,4]
    signals = [[int(s) for s in re.findall('[-]?[0-9]+', signal)] for signal in signals]
    # add the range of signal: FROM [1,2,3,4] TO [1,2,3,4,4] => 1-3=2, 2-4=2, 2+2=4
    signals = [signal+[abs(signal[0]-signal[2])+abs(signal[1]-signal[3])] for signal in signals]
    max_range = max([signal[3] for signal in signals])


row = 2000000

x_beacon = set()
for signal in signals:
    if signal[3] == row:
        x_beacon.add(signal[2])

forces = set()    
for signal in signals:
    force = spread(signal,row)
    if force != 0:
        for r in range(force[0],force[1]+1):
            forces.add(r)
            
result = len(forces) - len(x_beacon)

print(f'{result} cannot contain a beacon on y={row}')

min_ = 0
max_ = 4000000

for x in range(min_,max_+1):
    row = x            
    forces = []
    zone = []
    count = 0
    for signal in signals:
        force = spread(signal,row)
        if force != 0:
            if (force[0] < min_ and force[1] < min_) or (force[0] > max_ and force[1] > max_) :
                continue
            else:
                if force[0] < min_:
                    force[0] = min_
                if force[1] > max_:
                    force[1] = max_
            forces.append(force)
            
    forces.sort()
    for f in forces:
        if zone:
            if f[0] < zone[count][1] and f[1] > zone[count][1]:
                zone[count][1] = f[1]
            elif f[0] >= zone[count][1]:
                if f[0] == zone[count][1] or f[0] == zone[count][1]+1:
                    zone[count][1] = f[1]
                else:
                    zone.append(f)
                    count += 1
        else:
            zone.append(f)     
    
    if len(zone) > 1:
        result = (zone[0][1]+1) * 4000000 + row
        
print(f'Part 2 result = {result}')
