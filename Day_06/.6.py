# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:04:24 2022

@author: ghochart
"""

import sys

file = '.6.csv'
buffer = open(file).read().replace('\n','')

# code = []
# code_str = ''
# match = 0
# for char in range(len(buffer)):
#     if len(code) < 4:
#         code.append(buffer[char])
#     else:
#         for count,letter in enumerate(code):
#             if code.count(letter) == 1:
#                 code_str += letter
#                 match += 1
#                 if match == 4:
#                     print(code_str)
#                     print(buffer.find(code_str)+4)
#                     sys.exit()
#             else:
#                 code_str = ''
#                 match = 0
#                 break
#         code.append(buffer[char])
#         code.pop(0)
        

code = []
code_str = ''
match = 0
for char in range(len(buffer)):
    if len(code) < 14:
        code.append(buffer[char])
    else:
        for count,letter in enumerate(code):
            if code.count(letter) == 1:
                code_str += letter
                match += 1
                if match == 14:
                    print(code_str)
                    print(buffer.find(code_str)+14)
                    sys.exit()
            else:
                code_str = ''
                match = 0
                break
        code.append(buffer[char])
        code.pop(0)
                      

    
