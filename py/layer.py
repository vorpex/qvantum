'''
layer class

An instance of layer class represents one stage in a given quantum computional process. The 
layer is created by defining the gates which are contained by the given layer. The order of 
gates refers to that qubit which is affected by the given gate. Using the instances of layer 
class the user can build an instance of circuit class.

The instances of layer class have the following methods:

- __init__()         - initialization method
- get_gate_list()    - getter of gates in gate list
- get_gate_number()  - getter of number of gates
- get_nth_gate()     - getter of n-th gate
- get_layer_matrix() - getter of result of Kronecker product of matrices in gate list
- get_matrix_size()  - getter of size of layer matrix (equals to the size of states on 
                       which the layer is usable)
- get_layer_size()   - getter of size of layer (equals to the size of register on 
                       which the layer is usable)
- delete_gate()      - delete gate from layer
- insert_gate()      - insert gate into layer
'''

# pylint: disable=E1101

import check_layer
import numpy

class Layer(object):
    ''' layer class '''

    @check_layer.layer_init_check
    def __init__(self, gate_list):
        ''' initialize layer '''

        ranks = [i for i in range(len(gate_list))]   

        self.__gate_list = dict(zip(ranks, gate_list))
        self.__gate_list = dict(sorted(self.__gate_list.items()))

    def get_gate_list(self):
        ''' getter of gates in gate list '''

        return self.__gate_list

    def get_gate_number(self):
        ''' getter of number of gates '''

        return int(len(self.__gate_list))

    @check_layer.get_nth_gate_check
    def get_nth_gate(self, nth):
        ''' getter of n-th gate '''

        return self.__gate_list[nth]

    def get_layer_matrix(self):
        ''' getter of result of Kronecker multiplication of matrices in gate list '''

        m = numpy.identity(self.__gate_list[0].get_matrix().shape[0])
        for i in range(len(self.__gate_list)):

            if i == 0:
                m = m * self.__gate_list[i].get_matrix()

            else:
                m = numpy.kron(m, self.__gate_list[i].get_matrix())

        return m

    def get_matrix_size(self):
        ''' getter of size of layer matrix (equals to the size of states on which the 
        layer is usable) '''

        return int(self.get_layer_matrix().shape[0])
    
    def get_layer_size(self):
        ''' getter of size of layer (equals to the size of register on which the 
        layer is usable) '''

        return int(numpy.log(self.get_matrix_size(), 2))

    @check_layer.delete_gate_check
    def delete_gate(self, nth):
        ''' delete gate from layer '''

        if nth >= 0 and nth <= len(self.__gate_list) - 1:
            for key in list(self.__gate_list.keys()):

                if int(key) == nth:
                    del self.__gate_list[nth]

            self.__gate_list = dict(sorted(self.__gate_list.items()))

            ranks = [i for i in range(len(self.__gate_list))]            
            gates = list(self.__gate_list.values())

            self.__gate_list = dict(zip(ranks, gates))
            self.__gate_list = dict(sorted(self.__gate_list.items()))
        
        else:
            raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +\
                'less or equal to ' + str(len(self.__gate_list) - 1) + '.')

    @check_layer.insert_gate_check
    def insert_gate(self, g, nth):
        ''' insert gate into layer '''

        if nth >= 0 and nth <= len(self.__gate_list):
            ranks = [i for i in range(len(self.__gate_list) + 1)]            
            values = list(self.__gate_list.values())
            gates = []
            for i in range(len(self.__gate_list) + 1):

                if i < nth:
                    gates.append(values[i])

                elif i == nth:
                    gates.append(g)

                else:
                    gates.append(values[i - 1])
            
            self.__gate_list = dict(zip(ranks, gates))
            self.__gate_list = dict(sorted(self.__gate_list.items()))
        
        else:
            raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +\
                'less or equal to ' + str(len(self.__gate_list)) + '.')
