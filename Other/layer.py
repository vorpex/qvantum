'''
Layer class

An instance of the layer class represents one stage in a given quantum computional process. The 
layer is created by defining the gates which are contained by the given layer. The order of the 
gates refers to that qubit which is affected by the given gate. Using the instances of the layer 
class the user can build an instance of the circuit class.

The instances of the Layer class have the following methods:

- __init__()         - initialization method
- get_gate_list()    - getter of the matrices of the gates in gate list
- get_gate_nr()      - getter of the matrix of the n-th gate
- get_name_list()    - getter of the names of the gates in gate list
- get_name_nr()      - getter of the name of the n-th gate
- get_layer_matrix() - getter of the result of the Kronecker product of the matrices in gate list
- get_state_size()   - getter of the size of the states on which the layer is usable
- get_layer_size()   - getter of the size of the register on which the layer is usable
- delete_gate()      - delete gate from layer
- insert_gate()      - insert gate into layer
'''

# pylint: disable=E1101

import Gate
import logging
import numpy

class Layer(object):
    ''' layer class '''

    def __init__(self, gate_list):
        ''' initialize layer '''

        if isinstance(gate_list, list) and all(isinstance(g, Gate.Gate) for g in gate_list):
            RANKS = []
            for i in range(len(gate_list)):

                RANKS.append(i + 1)
            
            MATRICES = []
            for gate in gate_list:

                MATRICES.append(gate.get_matrix())

            NAMES = []
            for gate in gate_list:

                NAMES.append(gate.get_name())
                        
            self.__gate_list = dict(zip(RANKS, MATRICES))
            self.__gate_list = dict(sorted(self.__gate_list.items()))

            self.__name_list = dict(zip(RANKS, NAMES))
            self.__name_list = dict(sorted(self.__name_list.items()))
        else:
            logging.warning('Invalid input! Please list of Gates in argument.')

    def get_gate_list(self):
        ''' getter of the matrices of the gates in gate list '''

        return self.__gate_list

    def get_gate_nr(self, nr_gate):
        ''' getter of the matrix of the n-th gate '''

        if isinstance(nr_gate, int) and nr_gate >= 0 and \
        nr_gate <= len(list(self.__gate_list.keys())):
            return self.__gate_list[nr_gate]
        else:
            logging.warning('Invalid input! Argument must be between 1 and ' +\
            str(len(list(self.__gate_list.keys()))))

    def get_name_list(self):
        ''' getter of the names of the gates in gate list '''

        return self.__name_list
    
    def get_name_nr(self, nr_gate):
        ''' getter of the name of the n-th gate '''

        if isinstance(nr_gate, int) and nr_gate >= 0 and \
        nr_gate <= len(list(self.__name_list.keys())):
            return self.__name_list[nr_gate]
        else:
            logging.warning('Invalid input! Argument must be between 1 and ' +\
            str(len(list(self.__name_list.keys()))))

    def get_layer_matrix(self):
        ''' getter of the result of the Kronecker multiplication of the matrices in gate list '''

        M = numpy.identity(self.__gate_list[1].shape[0])
        for i in range(len(self.__gate_list)):

            if i == 0:
                M = M * self.__gate_list[i + 1]
            else:
                M = numpy.kron(M, self.__gate_list[i + 1])

        return M

    def get_state_size(self):
        ''' getter of the size of the states on which the layer is usable '''

        return self.get_layer_matrix().shape[0]
    
    def get_layer_size(self):
        ''' getter of the size of the register on which the layer is usable '''

        return int(numpy.log2(self.get_state_size()))
    
    def delete_gate(self, nr_gate=None):
        ''' delete gate from layer '''

        if nr_gate is None or (isinstance(nr_gate, int) and \
        nr_gate >= 1 and nr_gate <= self.get_layer_size()):
            if nr_gate is None:
                nr_gate = self.get_layer_size()
                logging.warning('Argument is None therefor Gate is going to be deleted from ' +\
                'the end of list.')
            
            for key in list(self.__gate_list.keys()):

                if int(key) == nr_gate:
                    del self.__gate_list[key]

            self.__gate_list = dict(sorted(self.__gate_list.items()))
            RANKS = []
            for i in range(len(list(self.__gate_list.keys()))):

                RANKS.append(i + 1)
            
            MATRICES = list(self.__gate_list.values())
            self.__gate_list = dict(zip(RANKS, MATRICES))
            self.__gate_list = dict(sorted(self.__gate_list.items()))

            for key in list(self.__name_list.keys()):

                if int(key) == nr_gate:
                    del self.__name_list[key]

            self.__name_list = dict(sorted(self.__name_list.items()))
            RANKS = []
            for i in range(len(list(self.__name_list.keys()))):

                RANKS.append(i + 1)
            
            NAMES = list(self.__name_list.values())
            self.__name_list = dict(zip(RANKS, NAMES))
            self.__name_list = dict(sorted(self.__name_list.items()))
        else:
            logging.warning('Invalid input! Argument shall be None or integer between 1 and ' +\
            str(self.get_layer_size()))

    def insert_gate(self, gate, nr_gate=None):
        ''' insert gate into layer '''

        if isinstance(gate, Gate.Gate) and (nr_gate is None or (isinstance(nr_gate, int) and \
        nr_gate >= 1 and nr_gate <= self.get_layer_size() + 1)):
            if nr_gate is None:
                nr_gate = self.get_layer_size() + 1
                logging.warning('Argument is None therefor Gate is going to be instered at ' +\
                'the end of list.')
            
            self.__gate_list = dict(sorted(self.__gate_list.items()))
            RANK = []
            for i in range(len(list(self.__gate_list.keys())) + 1):

                RANK.append(i + 1)
            
            VALUES = list(self.__gate_list.values())
            MATRICES = []
            for i in range(len(list(self.__gate_list.keys())) + 1):

                if i + 1 < nr_gate:
                    MATRICES.append(VALUES[i])
                elif i + 1 == nr_gate:
                    MATRICES.append(gate.get_matrix())
                else:
                    MATRICES.append(VALUES[i - 1])
            
            self.__gate_list = dict(zip(RANK, MATRICES))
            self.__gate_list = dict(sorted(self.__gate_list.items()))

            self.__name_list = dict(sorted(self.__name_list.items()))
            RANK = []
            for i in range(len(list(self.__name_list.keys())) + 1):

                RANK.append(i + 1)
            
            VALUES = list(self.__name_list.values())
            NAMES = []
            for i in range(len(list(self.__name_list.keys())) + 1):

                if i + 1 < nr_gate:
                    NAMES.append(VALUES[i])
                elif i + 1 == nr_gate:
                    NAMES.append(gate.get_name())
                else:
                    NAMES.append(VALUES[i - 1])
            
            self.__name_list = dict(zip(RANK, NAMES))
            self.__name_list = dict(sorted(self.__name_list.items()))
        else:
            logging.warning('Invalid input! Argument shall be a Gate and an integer between 1 ' +\
            'and ' + str(self.get_layer_size() + 1))
