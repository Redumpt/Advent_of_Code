# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 15:10:20 2022

E = z
S = a

a_z = higher

@author: ghochart
"""
def mount():
    with open('.12.txt') as file:
        mountain = file.read().split('\n')
    for y,row in enumerate(mountain):
        mountain[y] = [letter for letter in mountain[y]]
        for x,box in enumerate(mountain[y]):
            if 'S' == box:
                start = [y,x]
                mountain[y][x] = 'a'
            elif 'E' == box:
                end = [y,x]
                mountain[y][x] = 'z'
    return mountain,start,end        

def mp(check,p,m):
    if check == 'up':
        if p[0] == 0:
            return False
        actual = ord(m[p[0]][p[1]])
        up = ord(m[p[0]-1][p[1]])
        return actual + 1 >= up
    elif check == 'down':
        if p[0] == len(m)-1:
            return False
        actual = ord(m[p[0]][p[1]])
        down = ord(m[p[0]+1][p[1]])
        return actual + 1 >= down
    elif check == 'right':
        if p[1] == len(m[0])-1:
            return False
        actual = ord(m[p[0]][p[1]])
        right = ord(m[p[0]][p[1]+1])
        return actual + 1 >= right
    elif check == 'left':
        if p[1] == 0:
            return False
        actual = ord(m[p[0]][p[1]])
        left = ord(m[p[0]][p[1]-1])
        return actual + 1 >= left

mountain,position,end = mount()    

# while True:
#     if mp('a') + 1 <= mp('up') :
        
        
        
        
        
        
        
        
    