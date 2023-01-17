# -*- coding: utf-8 -*-
"""
adventofcode.com - Day 14

"""

from ast import literal_eval as le

def show_cave(cave_shape): #  Show the map as a text
    shape = ''
    for y in cave_shape:
        for x in y:
            shape += x
        shape += '\n'
    return print(shape)

with open('.14.txt') as file:
    cave = file.read().split('\n')
    #  From ['475,65 -> 475,60'] to [[475,65],[475,60]]
    cave_rock = [[le('[' + i + ']') for i in line] for line in [line.split(' -> ') for line in cave]]
    #  Asserting Min and Max of coordinate
    min_x = min([min([coord[0] for coord in line]) for line in cave_rock]) - 5
    max_x = max([max([coord[0] for coord in line]) for line in cave_rock]) + 5
    min_y = 0
    max_y = max([max([coord[1] for coord in line]) for line in cave_rock]) + 2
    #  Cave creating base on Min and Max coordinate
    cave_shape = [['.' for x in range(max_x - min_x + 1)] for y in range(max_y - min_y + 1)]

#  From [[475,10],[475,12],[477,12]] to [[475,10],[475,11],[475,12],[476,12],[477,12]]
#  From cave_shape = ['.','.','.'] to ['#','#','.']
for l,line in enumerate(cave_rock):
    ext = []
    for i,rock in enumerate(line):
        if i == len(line) - 1:
            continue
        elif line[i][0] != line[i+1][0]:
            r = line[i+1][0] - line[i][0]
            if r > 0:
                count = 1
                while count <= r - 1:
                    ext.append([rock[0]+count,rock[1]])
                    count += 1
            else:
                count = -1
                while count >= r + 1:
                    ext.append([rock[0]+count,rock[1]])
                    count -= 1
        elif line[i][1] != line[i+1][1]:
            r = line[i+1][1] - line[i][1]
            if r > 0:
                count = 1
                while count <= r - 1:
                    ext.append([rock[0],rock[1]+count])
                    count += 1
            else:
                count = -1
                while count >= r + 1:
                    ext.append([rock[0],rock[1]+count])
                    count -= 1
    cave_rock[l] = cave_rock[l] + ext
    for box in cave_rock[l]:
        if cave_shape[box[1] - min_y][box[0] - min_x] == '.':
            cave_shape[box[1] - min_y][box[0] - min_x] = '#'

sand_start = [500,0]
sand_unit = 0

while True:
    
    sand_position = [sand_start[0]-min_x, sand_start[1]-min_y] # Start of the sand
    
    while True:
        if sand_position[1] > max_y - 1:
            break
        elif cave_shape[sand_position[1]+1][sand_position[0]] == '.':
            sand_position = [sand_position[0],sand_position[1]+1]
            continue
        elif cave_shape[sand_position[1]+1][sand_position[0]-1] == '.':
            sand_position = [sand_position[0]-1,sand_position[1]+1]
            continue
        elif cave_shape[sand_position[1]+1][sand_position[0]+1] == '.':
            sand_position = [sand_position[0]+1,sand_position[1]+1]
            continue
        else:
            cave_shape[sand_position[1]][sand_position[0]] = 'o'
            sand_unit += 1
            break
    if sand_position[1] > max_y - 1:
        break

sand_unit_bottom = sand_unit

while True:
    
    sand_position = [sand_start[0]-min_x, sand_start[1]-min_y] # Start of the sand
    
    while True:
        if cave_shape[sand_start[1]-min_y][sand_start[0]-min_x] == 'o':
            break
        elif sand_position[1] == max_y - 1:
            cave_shape[sand_position[1]][sand_position[0]] = 'o'
            sand_unit_bottom += 1
            break
        elif sand_position[0] == (max_x - min_x) - 1 or sand_position[0] == 1:
            cave_shape[sand_position[1]][sand_position[0]] = 'o'
            sand_unit_bottom += 1
            break
        elif cave_shape[sand_position[1]+1][sand_position[0]] == '.':
            sand_position = [sand_position[0],sand_position[1]+1]
            continue
        elif cave_shape[sand_position[1]+1][sand_position[0]-1] == '.':
            sand_position = [sand_position[0]-1,sand_position[1]+1]
            continue
        elif cave_shape[sand_position[1]+1][sand_position[0]+1] == '.':
            sand_position = [sand_position[0]+1,sand_position[1]+1]
            continue
        else:
            cave_shape[sand_position[1]][sand_position[0]] = 'o'
            sand_unit_bottom += 1
            break
    if cave_shape[sand_start[1]-min_y][sand_start[0]-min_x] == 'o':
        break

count_left = 0
count_right = 0
for line in cave_shape:
    if line[1] == 'o':
        count_left += 1
    if line[-2] == 'o':
        count_right += 1

for i in range(count_left):
    sand_unit_bottom += i
    
for i in range(count_right):
    sand_unit_bottom += i
    
print(f'Sand unit part 1: {sand_unit}\nSand unit part 2: {sand_unit_bottom}')
    
        

    
    

                

    
            
        
