'''
Layer class

An instance of the layer class represents one stage in a given quantum computional process. The 
layer is created by defining the gates which are contained by the given layer. The order of the 
gates refers to that qubit which is affected by the given gate. Using the instances of the layer 
class the user can build an instance of the circuit class.

The instances of the Layer class have the following methods:

- __init__()         - initialization method
- get_gate_list()    - getter of the gates in gate list
- get_gate_number()  - getter of the number of the gates
- get_nth_gate()     - getter of the n-th gate
- get_layer_matrix() - getter of the result of the Kronecker product of the matrices in gate list
- get_matrix_size()  - getter of the size of the layer matrix (equals to the size of the states on 
                       which the layer is usable)
- get_layer_size()   - getter of the size of the layer (equals to the size of the register on 
                       which the layer is usable)
- delete_gate()      - delete gate from layer
- insert_gate()      - insert gate into layer
'''

# dict(sorted(self.__gate_list.items()))
#   - shall we use that often?
#   - the order is important: how does the dicitonary work?

# pylint: disable=E1101

import Gate
import numpy

class Layer(object):
    ''' layer class '''

    def __init__(self, gate_list):
        ''' initialize layer '''

        RANKS = [i for i in range(len(gate_list))]   
        GATES = [gate for gate in gate_list]

        self.__gate_list = dict(zip(RANKS, GATES))
        self.__gate_list = dict(sorted(self.__gate_list.items()))

    def get_gate_list(self):
        ''' getter of the gates in gate list '''

        return self.__gate_list

    def get_gate_number(self):
        ''' getter of the number of the gates '''

        return int(len(self.__gate_list))

    def get_nth_gate(self, nth_gate):
        ''' getter of the n-th gate '''

        return self.__gate_list[nth_gate]

    def get_layer_matrix(self):
        ''' getter of the result of the Kronecker multiplication of the matrices in gate list '''

        M = numpy.identity(self.__gate_list[0].get_matrix().shape[0])
        for i in range(len(self.__gate_list)):

            if i == 0:
                M = M * self.__gate_list[i].get_matrix()

            else:
                M = numpy.kron(M, self.__gate_list[i].get_matrix())

        return M

    def get_matrix_size(self):
        ''' getter of the size of the layer matrix (equals to the size of the states on which the 
        layer is usable) '''

        return int(self.get_layer_matrix().shape[0])
    
    def get_layer_size(self):
        ''' getter of the size of the layer (equals to the size of the register on which the 
        layer is usable) '''

        return int(numpy.log2(self.get_matrix_size()))
    
    def delete_gate(self, nr):
        ''' delete gate from layer '''

        if nr >= 0 and nr <= len(self.__gate_list) - 1:
            for key in list(self.__gate_list.keys()):

                if int(key) == nr:
                    del self.__gate_list[key]

            self.__gate_list = dict(sorted(self.__gate_list.items()))
            RANKS = [i for i in range(len(self.__gate_list))]            
            GATES = list(self.__gate_list.values())

            self.__gate_list = dict(zip(RANKS, GATES))
            self.__gate_list = dict(sorted(self.__gate_list.items()))
        
        else:
            raise ValueError('Invalid input! Parameter must be greater or equal to 0 and ' +\
            'less or equal to ' + str(len(self.__gate_list) - 1) + '.')

    def insert_gate(self, gate, nr):
        ''' insert gate into layer '''

        if nr >= 0 and nr <= len(self.__gate_list):        
            self.__gate_list = dict(sorted(self.__gate_list.items()))
            RANKS = [i for i in range(len(self.__gate_list) + 1)]            
            VALUES = list(self.__gate_list.values())
            GATES = []
            for i in range(len(self.__gate_list) + 1):

                if i < nr:
                    GATES.append(VALUES[i])

                elif i == nr:
                    GATES.append(gate)

                else:
                    GATES.append(VALUES[i - 1])
            
            self.__gate_list = dict(zip(RANKS, GATES))
            self.__gate_list = dict(sorted(self.__gate_list.items()))

        else:
            raise ValueError('Invalid input! Parameter must be greater or equal to 0 and ' +\
            'less or equal to ' + str(len(self.__gate_list)) + '.')
