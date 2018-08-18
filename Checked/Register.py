'''
Register class

"A quantum register is a system comprising multiple qubits[1] and is the quantum analog of the 
classical processor register. An n size quantum register is a quantum system comprising n qubits.
The Hilbert space, H, in which the data stored in a quantum register is:
    
    H = H(n-1) × H(n-2) × ... × H(0)."

via Wikipedia: https://en.wikipedia.org/wiki/Quantum_register

The instances of the Register class have the following methods:

- __init__()          - initialize register
- get_coeff_list()    - getter of the coefficients of the qubits
- get_state_number()  - getter of the number of the possible states
- get_qubit_number()  - getter of the number of qubits in the register
- get_nth_state()     - getter of the n-th state
- get_amplitudes()    - getter of the amplitudes
- set_amplitudes()    - setter of the amplitudes
- check()             - check if the square sum of the absolute values of the elements of the state 
                        vector equals to 1
- show()              - register representation
- measure_register()  - measure whole register
- measure_nth_qubit() - measure the n-th qubit
- ket()               - return the ket vector of the register
- bra()               - return the bra vector of the register
- delete_qubit()      - delete qubit from register
- insert_qubit()      - insert qubit into register
'''

# dict(sorted(self.__gate_list.items()))
#   - shall we use that often?
#   - the order is important: how does the dicitonary work?

# pylint: disable=E1101

import itertools
import math
import numpy
import random
import Qubit
import unicodedata

class Register(object):
    ''' register class '''

    def __init__(self, qubit_list):
        ''' initialize register '''

        if len(qubit_list) >= 2:            
            self.__coeff_list = [[qubit.get_alpha(), qubit.get_beta()] for qubit in qubit_list]

            states = list(itertools.product(range(2), repeat=len(qubit_list)))
            STATES = [''.join(map(str, states[i])) for i in range(len(states))]
            STATES.sort()
            COEFFS = []
            for STATE in STATES:

                product = 1
                for i in range(len(STATE)):
                    
                    if STATE[i] == '0':
                        product = product * qubit_list[i].get_alpha()

                    else:
                        product = product * qubit_list[i].get_beta()

                COEFFS.append(product)

            self.__state_vector = dict(zip(STATES, COEFFS))
            self.__state_vector = dict(sorted(self.__state_vector.items()))

        else:
            raise ValueError('Invalid input! Qubit list must contain at least 2 Qubit.')

    def get_coeff_list(self):
        ''' getter of the coefficients of the qubits '''

        return self.__coeff_list
    
    def get_state_number(self):
        ''' getter of the number of the possible states '''

        return int(len(self.__state_vector))
    
    def get_qubit_number(self):
        ''' getter of the number of qubits in the register '''

        return int(math.log2(self.get_state_nr()))
    
    def get_nth_state(self, nth):
        ''' getter of the n-th state '''

        return list(self.__state_vector.keys())[nth]

    def get_amplitudes(self, nth=None):
        ''' getter of the amplitudes '''

        if nth is None:
            return list(self.__state_vector.values())

        else:
            return list(self.__state_vector.values())[nth]
    
    def set_amplitudes(self, amp_list):
        ''' setter of the amplitudes '''

        if len(amp_list) == self.get_state_nr() \
        and round(numpy.sum(numpy.square(numpy.absolute(amp_list))) - 1, 10) == 0:
            i = 0
            self.__state_vector = dict(sorted(self.__state_vector.items()))
            for key in self.__state_vector:

                self.__state_vector[key] = amp_list[i]
                i = i + 1

        else:
            raise ValueError('Invalid input! The amplitudes list must be the same size as the ' +\
            'number of the possible states and the square sum of the absolute value of the ' +\
            'amplitudes must be equal to 1.')
    
    def check(self):
        ''' check if the square sum of the absolute values of the elements of the state vector 
        equals to 1 '''

        state_vector = numpy.array(list(self.__state_vector.values()))
        if round(numpy.sum(numpy.square(numpy.absolute(state_vector))) - 1, 10) == 0:
            return 1

        else:
            return 0

    def show(self):
        ''' register representation '''

        KEYS = list(self.__state_vector.keys())
        VALUES = list(self.__state_vector.values())
        state_string = '|' + unicodedata.lookup('GREEK CAPITAL LETTER PSI') + '> ='
        
        for i in range(len(KEYS)):

            state_string = state_string + ' ' + '({0:.4f}{1}{2:.4f}i)'.format(VALUES[i].real, \
            '+-'[VALUES[i].imag < 0], abs(VALUES[i].imag)) + '|' + KEYS[i] + '> +'
        
        state_string = state_string[:-2]

        return state_string

    def measure_register(self):
        ''' measure whole register '''

        RESULT = numpy.random.choice(list(self.__state_vector.keys()), \
            p=list(numpy.square(numpy.absolute(numpy.array(list(self.__state_vector.values()))))))
        for key in self.__state_vector:

            if key == RESULT:
                self.__state_vector[key] = 1

            else:
                self.__state_vector[key] = 0

        # print('|' + RESULT + '>')
        return int(RESULT)
    
    def measure_nth_qubit(self, nth):
        ''' measure the n-th qubit '''

        result0 = []
        for key in self.__state_vector:

            if key[nth] == '0':
                result0.append(self.__state_vector[key])
        
        prob0 = numpy.sum(numpy.square(numpy.absolute(numpy.array(result0))))
        RESULT = numpy.random.choice([0, 1], p=[prob0, 1 - prob0])
        
        for item in list(self.__state_vector.keys()):

            if item[nth] != str(RESULT):
                self.__state_vector[item] = 0
        
        renorm = numpy.sum(numpy.square(numpy.absolute(numpy.array( \
            list(self.__state_vector.values())))))
        self.__state_vector = dict(sorted(self.__state_vector.items()))
        for key in self.__state_vector:

            self.__state_vector[key] = self.__state_vector[key] / math.sqrt(renorm)

        # print('|' + str(RESULT) + '>')
        return int(RESULT)
    
    def ket(self):
        ''' return the ket vector of the register '''

        ket = numpy.array(list(self.__state_vector.values()))
        ket.shape = (len(ket), 1)
        return ket

    def bra(self):
        ''' return the bra vector of the register '''

        bra = self.ket().transpose()
        return bra
    
    # def delete_qubit(self, nr_qubit=None):
    #     ''' delete qubit from register '''

    #     if nr_qubit is None or (isinstance(nr_qubit, int) \
    #     and nr_qubit >= 1 and nr_qubit <= self.get_qubit_nr()):
    #         if nr_qubit is None:
    #             nr_qubit = self.get_qubit_nr()
    #             logging.warning('Argument is None therefor Qubit is going to be deleted from ' +\
    #             'the end of list.')
            
    #         self.__state_vector = dict(sorted(self.__state_vector.items()))
    #         KEYS =[]
    #         for key in self.__state_vector:

    #             list_key = list(key)
    #             list_key.pop(nr_qubit - 1)
    #             KEYS.append(''.join(list_key))
            
    #         VALUES = list(self.__state_vector.values())
            
    #         self.__state_vector = {}
    #         for i in range(len(KEYS)):

    #             if KEYS[i] not in list(self.__state_vector.keys()):
    #                 self.__state_vector[KEYS[i]] = VALUES[i]

    #             else:
    #                 self.__state_vector[KEYS[i]] = self.__state_vector[KEYS[i]] + VALUES[i]

    #         self.__state_vector = dict(sorted(self.__state_vector.items()))
    #         for key in self.__state_vector:

    #             if self.__coeff_list[nr_qubit - 1][0] == -1 * self.__coeff_list[nr_qubit - 1][1]:
    #                 self.__state_vector[key] = 1
    #             # Qubit.Qubit(-1 / math.sqrt(2), 1 / math.sqrt(2)) causes problem
    #             else:
    #                 self.__state_vector[key] = self.__state_vector[key] / \
    #                 (self.__coeff_list[nr_qubit - 1][0] + self.__coeff_list[nr_qubit - 1][1])

    #     else:
    #         logging.warning('Invalid input! Argument shall be None or integer between 1 and ' +\
    #         str(self.get_qubit_nr()))
    
    def insert_qubit(self, qubit, nr):
        ''' insert qubit into register '''

        if nr >= 0 and nr <= self.get_qubit_number():
            qubit_keys = ['0', '1']
            qubit_values = [qubit.get_alpha(), qubit.get_beta()]
            self.__state_vector = dict(sorted(self.__state_vector.items()))
            keys = list(self.__state_vector.keys())
            values = list(self.__state_vector.values())
            state_dict = {}
            for i in range(self.get_state_nr()):
                for j in range(2):

                    state_dict[keys[i][:nr] + qubit_keys[j] + keys[i][nr:]] = \
                        values[i] * qubit_values[j]
            
            state_dict = dict(sorted(state_dict.items()))

            STATE_DICT = {}
            for key in state_dict:
                
                STATE_DICT[key] = state_dict[key]
            
            STATE_DICT = dict(sorted(STATE_DICT.items()))
            self.__state_vector = STATE_DICT

        else:
            raise ValueError('Invalid input! Parameter must be greater or equal to 0 and ' +\
            'less or equal to ' + str(self.get_qubit_number()) + '.')
