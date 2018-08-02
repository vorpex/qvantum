'''
Register class

"A quantum register is a system comprising multiple qubits[1] and is the quantum analog of the 
classical processor register. An n size quantum register is a quantum system comprising n qubits.
The Hilbert space, H, in which the data stored in a quantum register is:
    
    H = H(n-1) × H(n-2) × ... × H(0)."

via Wikipedia: https://en.wikipedia.org/wiki/Quantum_register

The instances of the Register class have the following methods:

- __init__()       - initialize register
# - get_coeff_list() - getter of the coefficients of the Qubits
- get_state_nr()   - getter of the number of the possible states
- get_qubit_nr()   - getter of the number of qubits in the register
- get_parameters() - getter of the parameters
- set_parameters() - setter of the parameters
- check()          - check if the square sum of the absolute values of the elements of the state 
                     vector equals to 1
- show()           - register representation
- measure()        - measure the qubit(s) of the register
- ket()            - return the ket vector of the register
- bra()            - return the bra vector of the register
- delete_qubit()   - delete qubit from register
- insert_qubit()   - insert qubit into register
'''

# pylint: disable=E1101

import itertools
import logging
import math
import numpy
import random
import Qubit
import unicodedata

class Register(object):
    ''' register class '''

    def __init__(self, qubit_list=None, qubit_nr=None):
        ''' initialize register '''

        if (qubit_list is None and qubit_nr is None) or \
        (qubit_list is None and isinstance(qubit_nr, int) and qubit_nr >= 2) or \
        (qubit_nr is None and all(isinstance(q, Qubit.Qubit) for q in qubit_list) and \
        isinstance(qubit_list, list) and len(qubit_list) >= 2):
            if qubit_list is None and qubit_nr is None:
                logging.warning('Due to empty argument random Register of 3 Qubits was created.')
                qubit_list = [Qubit.Qubit(), Qubit.Qubit(), Qubit.Qubit()]
            
            if qubit_list is None and qubit_nr is not None:
                logging.warning('Nr of desired Qubits was given. Random Register created.')
                qubit_list = []
                for i in range(qubit_nr):

                    qubit_list.append(Qubit.Qubit())
            
            self.__coeff_list = []
            for qubit in qubit_list:

                self.__coeff_list.append([qubit.get_alpha(), qubit.get_beta()])

            states = list(itertools.product(range(2), repeat=len(qubit_list)))
            STATES = []
            for i in range(len(states)):

                STATES.append(''.join(map(str, states[i])))

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
            logging.warning('Invalid input! Please use no arguments or list of Qubits ' +\
            'or the number of desired Qubits (at least 2).')

    # def get_coeff_list(self):
    #     ''' getter of the coefficients of the Qubits '''

    #     return self.__coeff_list
    
    def get_state_nr(self):
        ''' getter of the number of the possible states '''

        return int(len(list(self.__state_vector.keys())))
    
    def get_qubit_nr(self):
        ''' getter of the number of qubits in the register '''

        return int(math.log2(self.get_state_nr()))
    
    def get_states(self, nr_state=None):
        ''' getter of the states '''

        if nr_state is None:
            return list(self.__state_vector.keys())

        elif isinstance(nr_state, int) and nr_state >= 1 and nr_state <= self.get_state_nr():
            return list(self.__state_vector.keys())[nr_state - 1]

        else:
            logging.warning('Invalid input! Argument shall be None or integer between 1 and ' +\
            str(self.get_state_nr()))

    def get_parameters(self, nr_state=None):
        ''' getter of the parameters '''

        if nr_state is None:
            return list(self.__state_vector.values())

        elif isinstance(nr_state, int) and nr_state >= 1 and nr_state <= self.get_state_nr():
            return list(self.__state_vector.values())[nr_state - 1]

        else:
            logging.warning('Invalid input! Argument shall be None or integer between 1 and ' +\
            str(self.get_state_nr()))
    
    def set_parameters(self, coeff_list):
        ''' setter of the parameters '''

        if len(coeff_list) == self.get_state_nr() \
        and isinstance(coeff_list, numpy.ndarray) \
        and round(numpy.sum(numpy.square(numpy.absolute(coeff_list))) - 1, 10) == 0:

            # self.__coeff_list = coeff_list

            i = 0
            self.__state_vector = dict(sorted(self.__state_vector.items()))
            for key in self.__state_vector:

                self.__state_vector[key] = coeff_list[i]
                i = i + 1

        else:
            logging.warning('Invalid input! Please use numpy.ndarray as argument. Length of ' +\
            'array has to be ' + str(self.get_state_nr()) + '. Make sure' +\
            ' that the absolute square sum of the coefficients equals to 1. Register remained ' +\
            'the same.')
    
    def check(self):
        ''' check if the square sum of the absolute values of the elements of the state vector 
        equals to 1 '''

        state_vector = numpy.array(list(self.__state_vector.values()))
        if round(numpy.sum(numpy.square(numpy.absolute(state_vector))) - 1, 10) == 0:
            return 1

        else:
            return round(numpy.sum(numpy.square(numpy.absolute(state_vector))), 10)

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

    def measure(self, nr_qubit=None):
        ''' measure the qubit(s) of the register '''

        if nr_qubit is None:
            RESULT = numpy.random.choice(list(self.__state_vector.keys()), \
            p=list(numpy.square(numpy.absolute(numpy.array(list(self.__state_vector.values()))))))
            for key in self.__state_vector:

                if key == RESULT:
                    self.__state_vector[key] = 1

                else:
                    self.__state_vector[key] = 0
            
            logging.warning('No Qubit was specified, whole register is measured.')
            # print('|' + RESULT + '>')
            return int(RESULT)

        elif isinstance(nr_qubit, int) \
        and nr_qubit >= 1 and nr_qubit <= self.get_qubit_nr():
            result0 = []
            for key in self.__state_vector:

                if key[nr_qubit - 1] == '0':
                    result0.append(self.__state_vector[key])
            
            prob0 = numpy.sum(numpy.square(numpy.absolute(numpy.array(result0))))
            RESULT = numpy.random.choice([0, 1], p=[prob0, 1 - prob0])
            
            for item in list(self.__state_vector.keys()):

                if item[nr_qubit - 1] != str(RESULT):
                    self.__state_vector[item] = 0
            
            renorm = numpy.sum(numpy.square(numpy.absolute(numpy.array(\
                list(self.__state_vector.values())))))
            self.__state_vector = dict(sorted(self.__state_vector.items()))
            for key in self.__state_vector:

                self.__state_vector[key] = self.__state_vector[key] / math.sqrt(renorm)

            # print('|' + str(RESULT) + '>')
            return int(RESULT)

        else:
            logging.warning('Invalid input! Argument shall be None or integer between 1 and ' +\
            str(self.get_qubit_nr()))
    
    def ket(self):
        ''' return the ket vector of the register '''

        ket = numpy.array(list(self.__state_vector.values()))
        ket.shape = (len(ket), 1)
        return ket

    def bra(self):
        ''' return the bra vector of the register '''

        bra = self.ket().transpose()
        return bra
    
    def delete_qubit(self, nr_qubit=None):
        ''' delete qubit from register '''

        if nr_qubit is None or (isinstance(nr_qubit, int) \
        and nr_qubit >= 1 and nr_qubit <= self.get_qubit_nr()):
            if nr_qubit is None:
                nr_qubit = self.get_qubit_nr()
                logging.warning('Argument is None therefor Qubit is going to be deleted from ' +\
                'the end of list.')
            
            self.__state_vector = dict(sorted(self.__state_vector.items()))
            KEYS =[]
            for key in self.__state_vector:

                list_key = list(key)
                list_key.pop(nr_qubit - 1)
                KEYS.append(''.join(list_key))
            
            VALUES = list(self.__state_vector.values())
            
            self.__state_vector = {}
            for i in range(len(KEYS)):

                if KEYS[i] not in list(self.__state_vector.keys()):
                    self.__state_vector[KEYS[i]] = VALUES[i]

                else:
                    self.__state_vector[KEYS[i]] = self.__state_vector[KEYS[i]] + VALUES[i]

            self.__state_vector = dict(sorted(self.__state_vector.items()))
            for key in self.__state_vector:

                if self.__coeff_list[nr_qubit - 1][0] == -1 * self.__coeff_list[nr_qubit - 1][1]:
                    self.__state_vector[key] = 1
                # Qubit.Qubit(-1 / math.sqrt(2), 1 / math.sqrt(2)) causes problem
                else:
                    self.__state_vector[key] = self.__state_vector[key] / \
                    (self.__coeff_list[nr_qubit - 1][0] + self.__coeff_list[nr_qubit - 1][1])

        else:
            logging.warning('Invalid input! Argument shall be None or integer between 1 and ' +\
            str(self.get_qubit_nr()))
    
    def insert_qubit(self, qubit=None, nr_qubit=None):
        ''' insert qubit into register '''

        if (qubit is None and nr_qubit is None) or \
        (qubit is None and isinstance(nr_qubit, int) \
        and nr_qubit >= 1 and nr_qubit <= self.get_qubit_nr() + 1) or \
        (isinstance(qubit, Qubit.Qubit) and nr_qubit is None) or \
        (isinstance(qubit, Qubit.Qubit) and isinstance(nr_qubit, int) \
        and nr_qubit >= 1 and nr_qubit <= self.get_qubit_nr() + 1):
            if qubit is None:
                qubit = Qubit.Qubit()
                logging.warning('Argument for Qubit is None therefor random Qubit is going to ' +\
                'be inserted.')
            
            if nr_qubit is None:
                nr_qubit = self.get_qubit_nr() + 1
                logging.warning('Argument is None therefor Qubit is going to be inserted at ' +\
                'the end of list.')
            
            qubit_keys = ['0', '1']
            qubit_values = [qubit.get_alpha(), qubit.get_beta()]
            self.__state_vector = dict(sorted(self.__state_vector.items()))
            keys = list(self.__state_vector.keys())
            values = list(self.__state_vector.values())
            state_dict = {}
            for i in range(self.get_state_nr()):
                for j in range(2):

                    state_dict[keys[i][:nr_qubit - 1] + qubit_keys[j] + keys[i][nr_qubit - 1:]] = \
                    values[i] * qubit_values[j]
            
            state_dict = dict(sorted(state_dict.items()))

            STATE_DICT = {}
            for key in state_dict:
                
                STATE_DICT[key] = state_dict[key]
            
            STATE_DICT = dict(sorted(STATE_DICT.items()))
            self.__state_vector = STATE_DICT

        else:
            logging.warning('Invalid input! Argument shall be None or integer between 1 and ' +\
            str(self.get_qubit_nr() + 1))
