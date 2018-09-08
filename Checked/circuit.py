'''
circuit class

An instance of circuit class represents a whole quantum computional process. The circuit is
created by defining the layers which are contained by the given circuit. The order of layers
refers to that stage which is ran by the given layer. Using the instances of circuit class the
user can build a quantum algorithm.

The instances of circuit class have the following methods:

- __init__()         - initialization method
- get_layer_list()   - getter of layers in layer list
- get_layer_number() - getter of number of layers
- get_nth_layer()    - getter of n-th layer
- get_circuit_size() - getter of size of circuit (equals to the size of register on 
                       which the layer is usable)
- delete_layer()     - delete layer from circuit
- insert_layer()     - insert layer into circuit
- run()              - run circuit on starting register
'''

# pylint: disable=E1101

import checker
import layer
import numpy
import register

class Circuit(object):
    ''' circuit class '''

    @checker.circuit_init_check
    def __init__(self, layer_list):
        ''' initialize circuit '''

        if all(layer_list[0].get_layer_size() == layer_list[i].get_layer_size() \
            for i in range(len(layer_list))):
            ranks = [i for i in range(len(layer_list))]

            self.__layer_list = dict(zip(ranks, layer_list))
            self.__layer_list = dict(sorted(self.__layer_list.items()))

        else:
            raise ValueError('Invalid input! Every member in the layer list must have the ' +\
                'same size.')

    def get_layer_list(self):
        ''' getter of layers in layer list '''

        return self.__layer_list

    def get_layer_number(self):
        ''' getter of number of layers '''

        return int(len(self.__layer_list))

    @checker.get_nth_layer_check
    def get_nth_layer(self, nth):
        ''' getter of n-th layer '''

        return self.__layer_list[nth]
    
    def get_circuit_size(self):
        ''' getter of size of circuit (equals to the size of register on which the 
        layer is usable) '''

        return int(self.__layer_list[0].get_layer_size())

    @checker.delete_layer_check
    def delete_layer(self, nth):
        ''' delete layer from circuit '''

        for key in list(self.__layer_list.keys()):

            if int(key) == nth:
                del self.__layer_list[key]

        ranks = [i for i in range(len(self.__layer_list))]
        layers = list(self.__layer_list.values())

        self.__layer_list = dict(zip(ranks, layers))
        self.__layer_list = dict(sorted(self.__layer_list.items()))

    @checker.insert_layer_check
    def insert_layer(self, layer, nth):
        ''' insert layer into circuit '''

        if layer.get_layer_size() == self.get_circuit_size():
            ranks = [i for i in range(len(self.__layer_list) + 1)]
            values = list(self.__layer_list.values())
            layers = []
            for i in range(len(self.__layer_list) + 1):

                if i < nth:
                    layers.append(values[i])

                elif i == nth:
                    layers.append(layer)

                else:
                    layers.append(values[i - 1])
            
            self.__layer_list = dict(zip(ranks, layers))
            self.__layer_list = dict(sorted(self.__layer_list.items()))

        else:
            raise ValueError('Invalid input! layer and circuit size must be the same.')

    @checker.run_check
    def run(self, register):
        ''' run circuit on starting register '''

        if register.get_qubit_number() == self.get_circuit_size():
            for key in self.__layer_list:

                vector = numpy.asarray(self.__layer_list[key].get_layer_matrix() * \
                    register.ket()).flatten()
                register.set_amplitudes(vector)

        else:
            raise ValueError('Invalid input! Register must be the same size as the layers.')
