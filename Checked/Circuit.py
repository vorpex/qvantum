'''
Circuit class

An instance of the circuit class represents a whole quantum computional process. The circuit is
created by defining the layers which are contained by the given circuit. The order of the layers
refers to that stage which is ran by the given layer. Using the instances of the circuit class the
user can build a quantum algorithm.

The instances of the Circuit class have the following methods:

- __init__()         - initialization method
- get_layer_list()   - getter of the layers in layer list
- get_layer_number() - getter of the number of the layers
- get_nth_layer()    - getter of the n-th layer
- get_circuit_size() - getter of the size of the circuit (equals to the size of the register on 
                       which the layer is usable)
- delete_layer()     - delete layer from circuit
- insert_layer()     - insert layer into circuit
- run()              - run circuit on starting register
'''

# dict(sorted(self.__gate_list.items()))
#   - shall we use that often?
#   - the order is important: how does the dicitonary work?

# pylint: disable=E1101

import Layer
import numpy
import Register

class Circuit(object):
    ''' circuit class '''

    def __init__(self, layer_list):
        ''' initialize circuit '''

        if all(layer_list[0].get_layer_size() == layer_list[i].get_layer_size() \
        for i in range(len(layer_list))):
            RANKS = [i for i in range(len(layer_list))]
            LAYERS = [layer for layer in layer_list]

            self.__layer_list = dict(zip(RANKS, LAYERS))
            self.__layer_list = dict(sorted(self.__layer_list.items()))

        else:
            raise ValueError('Invalid input! Every member in the layer list must have the ' +\
            'same size.')

    def get_layer_list(self):
        ''' getter of the layers in layer list '''

        return self.__layer_list

    def get_layer_number(self):
        ''' getter of the number of the layers '''

        return int(len(self.__layer_list))

    def get_nth_layer(self, nth_layer):
        ''' getter of the n-th layer '''

        return self.__layer_list[nth_layer]
    
    def get_circuit_size(self):
        ''' getter of the size of the circuit (equals to the size of the register on which the 
        layer is usable) '''

        return int(self.__layer_list[0].get_layer_size())

    def delete_layer(self, nr):
        ''' delete layer from circuit '''

        if nr >= 0 and nr <= len(self.__layer_list) - 1:
            for key in list(self.__layer_list.keys()):

                if int(key) == nr:
                    del self.__layer_list[key]

            self.__layer_list = dict(sorted(self.__layer_list.items()))
            RANKS = [i for i in range(len(self.__layer_list))]
            LAYERS = list(self.__layer_list.values())

            self.__layer_list = dict(zip(RANKS, LAYERS))
            self.__layer_list = dict(sorted(self.__layer_list.items()))

        else:
            raise ValueError('Invalid input! Parameter must be greater or equal to 0 and ' +\
            'less or equal to ' + str(len(self.__layer_list) - 1) + '.')

    def insert_layer(self, layer, nr):
        ''' insert layer into circuit '''

        if nr >= 0 and nr <= len(self.__layer_list) \
        and layer.get_layer_size() == self.get_circuit_size():
            self.__layer_list = dict(sorted(self.__layer_list.items()))
            RANKS = [i for i in range(len(self.__layer_list) + 1)]
            VALUES = list(self.__layer_list.values())
            LAYERS = []
            for i in range(len(self.__layer_list) + 1):

                if i < nr:
                    LAYERS.append(VALUES[i])

                elif i == nr:
                    LAYERS.append(layer)

                else:
                    LAYERS.append(VALUES[i - 1])
            
            self.__layer_list = dict(zip(RANKS, LAYERS))
            self.__layer_list = dict(sorted(self.__layer_list.items()))

        else:
            raise ValueError('Invalid input! Layer and Circuit size must be the same. ' +\
            'Parameter must be greater or equal to 0 and less or equal to ' +\
            str(len(self.__layer_list)) + '.')

    def run(self, register):
        ''' run circuit on starting register '''

        if register.get_qubit_nr() == self.get_circuit_size():
            for key in dict(sorted(self.__layer_list.items())):

                vector = numpy.asarray(self.__layer_list[key].get_layer_matrix() * \
                    register.ket()).flatten()
                register.set_amplitudes(vector)

        else:
            raise ValueError('Invalid input! Register must be the same size as the Layers.')
