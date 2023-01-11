# -*- coding: utf-8 -*-
"""

adventofcode.com 2022 - Day 12


notes:
    
E = z
S = a

a_z = higher

"""
def mount():  # Load the mountain file as mountain[row][column]
    with open('.12.txt') as file:
        mountain = file.read().split('\n')  # turn each row text to list   
    dict_m = {}
    for y,row in enumerate(mountain):
        mountain[y] = [letter for letter in mountain[y]]
        for x,box in enumerate(mountain[y]):  # record / replace starting and ending point and convert letters to numbers
            if 'S' == box:
                start = [y,x]
                mountain[y][x] = 'a'
            elif 'E' == box:
                end = [y,x]
                mountain[y][x] = 'z'
            level = ord(mountain[y][x]) - 97
            dict_m[str([y,x])] = {'loc':[y,x],'level':level,'min_steps':None}
    mountain = dict_m
    return mountain,start,end


  # PART 1

mountain,position,end = mount()
step = 0
mountain[str(position)]['min_steps'] = step
list_position = None
new_position = []

while True:
    step += 1   
    if list_position == None:
        list_position = [position]
    elif len(new_position) == 0:
        break
    else:
        list_position = new_position.copy()
        new_position.clear()       
    for pos in list_position:
        pos_check = mountain[str(pos)]['loc']
        level_check = mountain[str(pos)]['level'] + 1
        # UP
        pos_up = [pos_check[0]-1,pos_check[1]]
        if str(pos_up) in mountain:
            if mountain[str(pos_up)]['level'] <= level_check:
                if mountain[str(pos_up)]['min_steps'] == None or mountain[str(pos_up)]['min_steps'] > step:
                    mountain[str(pos_up)]['min_steps'] = step
                    new_position.append(pos_up)
        # RIGHT
        pos_right = [pos_check[0],pos_check[1]+1]
        if str(pos_right) in mountain:
            if mountain[str(pos_right)]['level'] <= level_check:
                if mountain[str(pos_right)]['min_steps'] == None or mountain[str(pos_right)]['min_steps'] > step:
                    mountain[str(pos_right)]['min_steps'] = step
                    new_position.append(pos_right)
        # DOWN
        pos_down = [pos_check[0]+1,pos_check[1]]
        if str(pos_down) in mountain:
            if mountain[str(pos_down)]['level'] <= level_check:
                if mountain[str(pos_down)]['min_steps'] == None or mountain[str(pos_down)]['min_steps'] > step:
                    mountain[str(pos_down)]['min_steps'] = step
                    new_position.append(pos_down)    
        # LEFT
        pos_left = [pos_check[0],pos_check[1]-1]
        if str(pos_left) in mountain:
            if mountain[str(pos_left)]['level'] <= level_check:
                if mountain[str(pos_left)]['min_steps'] == None or mountain[str(pos_left)]['min_steps'] > step:
                    mountain[str(pos_left)]['min_steps'] = step
                    new_position.append(pos_left)
                
print(mountain[str(end)])


  # PART 2

list_a_level = []
for i in mountain.values():
    if i['level'] == 0:
        list_a_level.append(i)
steps_taken = []
        
for start in list_a_level:
    
    mountain,position,end = mount()
    position = start['loc']
    step = 0
    mountain[str(position)]['min_steps'] = step
    list_position = None
    new_position = []
    
    while True:
        step += 1   
        if list_position == None:
            list_position = [position]
        elif len(new_position) == 0:
            break
        else:
            list_position = new_position.copy()
            new_position.clear()       
        for pos in list_position:
            pos_check = mountain[str(pos)]['loc']
            level_check = mountain[str(pos)]['level'] + 1
            # UP
            pos_up = [pos_check[0]-1,pos_check[1]]
            if str(pos_up) in mountain:
                if mountain[str(pos_up)]['level'] <= level_check:
                    if mountain[str(pos_up)]['min_steps'] == None or mountain[str(pos_up)]['min_steps'] > step:
                        mountain[str(pos_up)]['min_steps'] = step
                        new_position.append(pos_up)
            # RIGHT
            pos_right = [pos_check[0],pos_check[1]+1]
            if str(pos_right) in mountain:
                if mountain[str(pos_right)]['level'] <= level_check:
                    if mountain[str(pos_right)]['min_steps'] == None or mountain[str(pos_right)]['min_steps'] > step:
                        mountain[str(pos_right)]['min_steps'] = step
                        new_position.append(pos_right)
            # DOWN
            pos_down = [pos_check[0]+1,pos_check[1]]
            if str(pos_down) in mountain:
                if mountain[str(pos_down)]['level'] <= level_check:
                    if mountain[str(pos_down)]['min_steps'] == None or mountain[str(pos_down)]['min_steps'] > step:
                        mountain[str(pos_down)]['min_steps'] = step
                        new_position.append(pos_down)    
            # LEFT
            pos_left = [pos_check[0],pos_check[1]-1]
            if str(pos_left) in mountain:
                if mountain[str(pos_left)]['level'] <= level_check:
                    if mountain[str(pos_left)]['min_steps'] == None or mountain[str(pos_left)]['min_steps'] > step:
                        mountain[str(pos_left)]['min_steps'] = step
                        new_position.append(pos_left)
    
    if mountain[str(end)]['min_steps'] != None:
        steps_taken.append(mountain[str(end)]['min_steps'])
    

print(min(steps_taken))
        
        
        
        
        
        
        
        
    
