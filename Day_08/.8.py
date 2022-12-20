# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 08:17:59 2022

@author: ghochart
"""

file = '.8.txt'
tree_map = open(file).read().split('\n')
visible_tree = 0
max_scenic = 0

for count, row in enumerate(tree_map):
    for sub_count, tree in enumerate(row):
        coordonate = [sub_count, count]
        left_visible = True
        right_visible = True
        up_visible = True
        down_visible = True
        left_scenic = 0
        right_scenic = 0
        up_scenic = 0
        down_scenic = 0
        
        while coordonate[0] > 0:
            coordonate[0] -= 1
            left_scenic += 1
            if int(tree) <= int(tree_map[count][coordonate[0]]):
                left_visible = False
                break
            
        coordonate = [sub_count, count]
        while coordonate[0] < len(row)-1:
            coordonate[0] += 1
            right_scenic += 1
            if int(tree) <= int(tree_map[count][coordonate[0]]):
                right_visible = False
                break
        
        coordonate = [sub_count, count]
        while coordonate[1] > 0:
            coordonate[1] -= 1
            up_scenic += 1
            if int(tree) <= int(tree_map[coordonate[1]][sub_count]):
                up_visible = False
                break    
        
        coordonate = [sub_count, count]
        while coordonate[1] < len(tree_map)-1:
            coordonate[1] += 1
            down_scenic += 1
            if int(tree) <= int(tree_map[coordonate[1]][sub_count]):
                down_visible = False
                break
            
        if left_visible == True or right_visible == True or up_visible == True or down_visible == True:
            visible_tree += 1
        
        total_scenic = left_scenic * right_scenic * up_scenic * down_scenic
        if total_scenic > max_scenic:
            max_scenic = total_scenic
            
        

print(visible_tree)
print(max_scenic)