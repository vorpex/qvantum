'''
register class

"A quantum register is a system comprising multiple qubits[1] and is the quantum analog of the 
classical processor register. An n size quantum register is a quantum system comprising n qubits.
The Hilbert space, H, in which the data stored in a quantum register is:
    
    H = H(n-1) × H(n-2) × ... × H(0)."

via Wikipedia: https://en.wikipedia.org/wiki/Quantum_register

The instances of the register class have the following methods:

- __init__()          - initialize register
- get_coeff_list()    - getter of coefficients of qubits
- get_state_number()  - getter of number of possible states
- get_qubit_number()  - getter of number of qubits in the register
- get_nth_state()     - getter of n-th state
- get_amplitudes()    - getter of amplitudes
- set_amplitudes()    - setter of amplitudes
- show()              - register representation
- measure_register()  - measure the whole register
- measure_nth_qubit() - measure the n-th qubit
- ket()               - return the ket vector of register
- bra()               - return the bra vector of register
- insert_qubit()      - insert qubit into register
'''

# pylint: disable=E1101

import checker
import itertools
import math
import numpy
import random
import qubit
import unicodedata

class Register(object):
    ''' register class '''

    @checker.register_init_check
    def __init__(self, qubit_list):
        ''' initialize register '''

        self.__coeff_list = [[qubit.get_alpha(), qubit.get_beta()] for qubit in qubit_list]

        states_list = list(itertools.product(range(2), repeat=len(qubit_list)))
        states = [''.join(map(str, states_list[i])) for i in range(len(states_list))]
        states.sort()
        coeffs = []
        for state in states:

            product = 1
            for i in range(len(state)):
                
                if state[i] == '0':
                    product = product * qubit_list[i].get_alpha()

                else:
                    product = product * qubit_list[i].get_beta()

            coeffs.append(product)

        self.__state_vector = dict(zip(states, coeffs))
        self.__state_vector = dict(sorted(self.__state_vector.items()))

    def get_coeff_list(self):
        ''' getter of the coefficients of the qubits '''

        return self.__coeff_list
    
    def get_state_number(self):
        ''' getter of the number of the possible states '''

        return int(len(self.__state_vector))
    
    def get_qubit_number(self):
        ''' getter of the number of qubits in the register '''

        return int(math.log2(self.get_state_number()))

    @checker.get_nth_state_check
    def get_nth_state(self, nth):
        ''' getter of the n-th state '''

        return list(self.__state_vector.keys())[nth]

    @checker.get_amplitudes_check
    def get_amplitudes(self, nth=None):
        ''' getter of the amplitudes '''

        if nth is None:
            return list(self.__state_vector.values())

        else:
            return list(self.__state_vector.values())[nth]
    
    @checker.set_amplitudes_check
    def set_amplitudes(self, amp_list):
        ''' setter of the amplitudes '''

        if len(amp_list) == self.get_state_number():
            i = 0
            for key in self.__state_vector:

                self.__state_vector[key] = amp_list[i]
                i = i + 1

            self.__state_vector = dict(sorted(self.__state_vector.items()))

        else:
            raise ValueError('Invalid input! The amplitudes list must be the same size as the ' +\
                'number of the possible states.')

    def show(self):
        ''' register representation '''

        keys = list(self.__state_vector.keys())
        values = list(self.__state_vector.values())
        state_string = '|' + unicodedata.lookup('GREEK CAPITAL LETTER PSI') + '> ='
        
        for i in range(len(keys)):

            state_string = state_string + ' ' + '({0:.4f}{1}{2:.4f}i)'.format(values[i].real, \
            '+-'[values[i].imag < 0], abs(values[i].imag)) + '|' + keys[i] + '> +'
        
        state_string = state_string[:-2]

        return state_string

    def measure_register(self):
        ''' measure whole register '''

        result = numpy.random.choice(list(self.__state_vector.keys()), \
            p=list(numpy.square(numpy.absolute(numpy.array(list(self.__state_vector.values()))))))
        for key in self.__state_vector:

            if key == result:
                self.__state_vector[key] = 1

            else:
                self.__state_vector[key] = 0

        self.__state_vector = dict(sorted(self.__state_vector.items()))
        return result
    
    @checker.measure_nth_qubit_check
    def measure_nth_qubit(self, nth):
        ''' measure the n-th qubit '''

        result0 = []
        for key in self.__state_vector:

            if key[nth] == '0':
                result0.append(self.__state_vector[key])
        
        prob0 = numpy.sum(numpy.square(numpy.absolute(numpy.array(result0))))
        result = numpy.random.choice([0, 1], p=[prob0, 1 - prob0])
        
        for item in list(self.__state_vector.keys()):

            if item[nth] != str(result):
                self.__state_vector[item] = 0
        
        renorm = numpy.sum(numpy.square(numpy.absolute(numpy.array( \
            list(self.__state_vector.values())))))
    
        for key in self.__state_vector:

            self.__state_vector[key] = self.__state_vector[key] / math.sqrt(renorm)

        self.__state_vector = dict(sorted(self.__state_vector.items()))
        return int(result)
    
    def ket(self):
        ''' return the ket vector of the register '''

        ket = numpy.array(list(self.__state_vector.values()))
        ket.shape = (len(ket), 1)
        return ket

    def bra(self):
        ''' return the bra vector of the register '''

        bra = self.ket().transpose()
        return bra
    
    @checker.insert_qubit_check
    def insert_qubit(self, qubit, nth):
        ''' insert qubit into register '''

        qubit_keys = ['0', '1']
        qubit_values = [qubit.get_alpha(), qubit.get_beta()]
        keys = list(self.__state_vector.keys())
        values = list(self.__state_vector.values())
        state_dict = {}
        for i in range(self.get_state_number()):
            for j in range(2):

                state_dict[keys[i][:nth] + qubit_keys[j] + keys[i][nth:]] = \
                    values[i] * qubit_values[j]
        
        state_dict = dict(sorted(state_dict.items()))
        self.__state_vector = state_dict
