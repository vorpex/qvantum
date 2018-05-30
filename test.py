''' test '''

import itertools
import math
import numpy
import Qubit

# pylint: disable=E1101

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

dict = {}
print(dict)
dict['alma'] = 1
dict['xena'] = 2
dict['korte'] = 3
print(sorted(dict))
