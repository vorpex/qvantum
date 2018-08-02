''' test '''

import itertools
import math
import numpy
import Qubit

# pylint: disable=E1101
# logging.disable(30)

###########################################################################

# states = list(itertools.product(range(2), repeat=3))
# STATES = []
# for i in range(len(states)):

#     STATES.append(''.join(map(str, states[i])))
# VALUES = [1, 2, 3, 4, 5, 6, 7, 8]
# dict = dict(zip(STATES, VALUES))

# print(dict)

# vector = numpy.array([1, 2, 1, 2, 1, 2, 1, 2])

# i = 0
# for key in dict:

#     dict[key] = vector[i]
#     i = i + 1

# print(dict)

# for item in list(dict.keys()):

#     if item[1] == '0':
#         del dict[item]

# print(list(dict.keys()))

# keys = list(dict.keys())
# KEYS = []
# for key in keys:

#     str1 = key[:2]
#     str2 = key[2 + 1:]
#     print(str1, str2)
#     key = str1 + str2
#     KEYS.append(key)

# print(KEYS)

###########################################################################

# l = numpy.random.choice(['pooh', 'rabbit', 'piglet', 'Christopher'], p=[0.5, 0.1, 0.1, 0.3])
# print(l)

###########################################################################

# print(math.log2(32))

###########################################################################

# d = {}
# print(d)
# d['alma'] = 1
# d['xena'] = 2
# d['korte'] = 3
# print(d)
# d = dict(sorted(d.items()))
# print(d)

# for key in list(d.keys()):

#     if key == 'xena':
#         del d[key]

# print(d)

###########################################################################

# a = 'alma'
# Lista = list(a)
# Lista.pop(2)
# a = ''.join(Lista)
# print(a)

###########################################################################

# M = numpy.matrix([[1 / math.sqrt(2), 1 / math.sqrt(2)], [1 / math.sqrt(2), -1 / math.sqrt(2)]])
# print(M)
# print(M * M)
# print(numpy.linalg.matrix_power(M, 2))

###########################################################################

# states = list(itertools.product(range(2), repeat=len([1, 2, 3])))
# STATES = []
# for i in range(len(states)):

#     STATES.append(''.join(map(str, states[i])))

# print(states)
# print(STATES)

# for STATE in STATES:
    
#     for i in range(len(STATE)):

#         print(STATE[i])

# L = ['000', '001', '010', '011', '100', '101', '111', '110']
# print(L)
# L.sort()
# print(L)
# print(len(L))

###########################################################################

# M = numpy.matrix([
#     [1, 0],
#     [0, -1]
#     ])
# print(M)

# M = numpy.linalg.matrix_power(M, 1)
# print(M)

###########################################################################
