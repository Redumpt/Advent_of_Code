# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 08:58:07 2022

bored = / 3
round down

monkey throw to other monkey at the end of inspected object

@author: ghochart
"""

import re
import operator

with open('.11.txt') as file:
    monkey_file = list(filter(None,file.read().split('\n')))

 # Operator use to identify action base on str * and +
op = {'+': operator.add,
      '*': operator.mul}
  
 # Create the monkey list to help filtering later on  
r = re.compile('Monkey.*')
monkey_list = list(filter(r.match,monkey_file))
monkeys = {}

 # Add all the element to each monkeys after each ':'
for line in monkey_file:
    if line in monkey_list:
        current_monkey = line.split(':')[0].split()[1]
        monkeys[current_monkey] = []
    else:
        monkeys[current_monkey].append(line.split(':')[1])
      
 # clean the elements for each monkey and reformat
for monkey,values in monkeys.items():
    if type(values[0]) == str:
        monkeys[monkey][0] = [int(x) for x in values[0].split(',')]
        monkeys[monkey][1] = values[1].split()[2:]
        monkeys[monkey][2] = int(values[2].split()[-1])
        monkeys[monkey][3] = values[3].split()[-1]
        monkeys[monkey][4] = values[4].split()[-1]
        monkeys[monkey].append(0)

 # PART 1
# rnd = 20
# relief = 3
# for rounds in range(rnd):
#     for monkey,values in monkeys.items():
#         while values[0]:
#             old = monkeys[monkey][0].pop(0)
#             monkeys[monkey][5] += 1
#             operation = []
#             for x in values[1]:
#                 if x == 'old':
#                     operation.append(old)
#                 elif x in op:
#                     operation.append(x)
#                 else:
#                     operation.append(int(x))
#             new = op[operation[1]](operation[0],operation[2])
#             new = int(new / relief)
#             if new % values[2] == 0:
#                 monkeys[values[3]][0].append(new)
#             else:
#                 monkeys[values[4]][0].append(new)

# all_inspect = []
# for monkey,values in monkeys.items():
#     all_inspect.append(monkeys[monkey][-1])
# all_inspect.sort(reverse=True)

# print(f'Monkey business = {all_inspect[0]*all_inspect[1]}')
    

 # PART 2
rnd = 10000
lcm = 1
for i in monkeys.values():
    lcm *= i[2]
for rounds in range(rnd):
    for monkey,values in monkeys.items():
        while values[0]:
            old = monkeys[monkey][0].pop(0)
            monkeys[monkey][5] += 1
            operation = []
            for x in values[1]:
                if x == 'old':
                    operation.append(old)
                elif x in op:
                    operation.append(x)
                else:
                    operation.append(int(x))
            new = op[operation[1]](operation[0],operation[2]) % lcm           
            if new % values[2] == 0:
                monkeys[values[3]][0].append(new)
            else:
                monkeys[values[4]][0].append(new)
    

all_inspect = []
for monkey,values in monkeys.items():
    all_inspect.append(monkeys[monkey][-1])
all_inspect.sort(reverse=True)

print(f'Monkey business = {all_inspect[0]*all_inspect[1]}')
            


    
        
