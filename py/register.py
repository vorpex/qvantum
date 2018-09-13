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
- get_states()        - getter of states
- get_amplitudes()    - getter of amplitudes
- set_amplitudes()    - setter of amplitudes
- show()              - register representation
- measure_register()  - measure the whole register
- measure_nth_qubit() - measure the n-th qubit
- ket()               - return the ket vector of register
- bra()               - return the bra vector of register
- delete_qubit()      - delete qubit from register
- insert_qubit()      - insert qubit into register
'''

# pylint: disable=E1101

import check_register
import itertools
import math
import numpy
import unicodedata

class Register(object):
    ''' register class '''

    @check_register.register_init_check
    def __init__(self, qubit_list):
        ''' initialize register '''

        self.__coeff_list = [[q.get_alpha(), q.get_beta()] for q in qubit_list]

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

    @check_register.get_states_check
    def get_states(self, nth=None):
        ''' getter of the states '''

        if nth is None:
            return list(self.__state_vector.keys())
        
        else:
            return list(self.__state_vector.keys())[nth]

    @check_register.get_amplitudes_check
    def get_amplitudes(self, nth=None):
        ''' getter of the amplitudes '''

        if nth is None:
            return list(self.__state_vector.values())

        else:
            return list(self.__state_vector.values())[nth]
    
    @check_register.set_amplitudes_check
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
                'number of possible states.')

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
    
    @check_register.measure_nth_qubit_check
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

    @check_register.delete_qubit_check
    def delete_qubit(self, nth):
        ''' delete qubit from register '''

        if nth >= 0 and nth <= self.get_qubit_number() - 1:
            keys =[]
            for key in self.__state_vector:

                list_key = list(key)
                list_key.pop(nth)
                keys.append(''.join(list_key))
            
            values = list(self.__state_vector.values())
            
            self.__state_vector = {}
            for i in range(len(keys)):

                if keys[i] not in list(self.__state_vector.keys()):
                    self.__state_vector[keys[i]] = values[i]

                else:
                    self.__state_vector[keys[i]] = self.__state_vector[keys[i]] + values[i]

            self.__state_vector = dict(sorted(self.__state_vector.items()))
            for elem in self.__state_vector:

                if self.__coeff_list[nth][0] == -1 * self.__coeff_list[nth][1]:
                    self.__state_vector[elem] = 1
                # qubit.Qubit(-1 / math.sqrt(2), 1 / math.sqrt(2)) causes problem
                else:
                    self.__state_vector[elem] = self.__state_vector[elem] / \
                        (self.__coeff_list[nth][0] + self.__coeff_list[nth][1])

        else:
            raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +\
                'less or equal to ' + str(self.get_qubit_number() - 1) + '.')
    
    @check_register.insert_qubit_check
    def insert_qubit(self, q, nth):
        ''' insert qubit into register '''

        if nth >= 0 and nth <= self.get_qubit_number():
            qubit_keys = ['0', '1']
            qubit_values = [q.get_alpha(), q.get_beta()]
            keys = list(self.__state_vector.keys())
            values = list(self.__state_vector.values())
            state_dict = {}
            for i in range(self.get_state_number()):
                for j in range(2):

                    state_dict[keys[i][:nth] + qubit_keys[j] + keys[i][nth:]] = \
                        values[i] * qubit_values[j]
            
            self.__state_vector = dict(sorted(state_dict.items()))
        
        else:
            raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +\
                'less or equal to ' + str(self.get_qubit_number()) + '.')
