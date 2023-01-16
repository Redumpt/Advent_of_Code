# -*- coding: utf-8 -*-
"""
adventofcode.com - Day 13

"""
import ast

with open('.13.txt') as file:
    packages = file.read().split('\n')
    
def check_list(l1, l2):
    if isinstance(l1,list) and isinstance(l2,list):
        r = min([len(l1),len(l2)])
        for i in range(r):
            check = check_list(l1[i], l2[i])
            if check != None:
                return check
        if len(l1) > len(l2):
            return 'Wrong order'
        elif len(l1) < len(l2):
            return 'Right order'
    elif isinstance(l1,list):
        l2 = [l2]
        r = min([len(l1),len(l2)])
        for i in range(r):
            check = check_list(l1[i], l2[i])
            if check != None:
                return check
        if len(l1) > len(l2):
            return 'Wrong order'
        elif len(l1) < len(l2):
            return 'Right order'
    elif isinstance(l2,list):
        l1 = [l1]
        r = min([len(l1),len(l2)])
        for i in range(r):
            check = check_list(l1[i], l2[i])
            if check != None:
                return check
        if len(l1) > len(l2):
            return 'Wrong order'
        elif len(l1) < len(l2):
            return 'Right order'
    else:
        if l1 > l2:
            return 'Wrong order'
        elif l1 < l2:
            return 'Right order'

packages_copy = packages.copy()

right_order = 0
wrong_order = 0
indice = 0
right_indices = 0
while True:
    indice += 1
    # RETREIVE PACKAGES STRING LINES
    string_a = packages_copy[0]
    string_b = packages_copy[1]
    # CONVERT STRING TO LIST USING AST.LITERAL_EVAL()
    list_a = ast.literal_eval(string_a)
    list_b = ast.literal_eval(string_b)
    # Remove 3 first lines (list_a,list_b,None) 
    packages_copy = packages_copy[3:]
    check = check_list(list_a,list_b)
    if check == 'Right order':
        right_order += 1
        right_indices += indice
    else:
        wrong_order += 1
    if len(packages_copy) == 0:
        break

reordered_list = []
packages.append('[[2]]')
packages.append('[[6]]')
for packet in packages:
    if packet == '':
        continue
    else:
        l = ast.literal_eval(packet)
        if reordered_list == []:
            reordered_list.append(l)
        else:
            for i,packet in enumerate(reordered_list):
                check = check_list(l, packet)
                if check == 'Wrong order' and i == len(reordered_list) - 1:
                    reordered_list.append(l)
                elif check == 'Wrong order':
                    continue
                elif check == 'Right order':
                    reordered_list.insert(i,l)
                    break

decoder_key = (reordered_list.index([[2]]) + 1) * (reordered_list.index([[6]]) + 1)

print(f'Number of right order: {right_order}\nIndices: {right_indices}\nDecoder key: {decoder_key}')
        
                
                    



        
                

