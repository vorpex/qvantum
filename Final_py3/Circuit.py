'''
Circuit class

An instance of the circuit class represents a whole quantum computional process. The circuit is
created by defining the layers which are contained by the given circuit. The order of the layers
refers to that stage which is ran by the given layer. Using the instances of the circuit class the
user can build a quantum algorithm.

The instances of the Circuit class have the following methods:

- __init__()         - initialization method
- get_layer_list()   - getter of the layers in layer list
- get_layer_nr()     - getter of the n-th layer
- get_circuit_size() - getter of the size of the circuit
- delete_layer()     - delete layer from circuit
- insert_layer()     - insert layer into circuit
- run()              - run circuit on starting register
'''

# pylint: disable=E1101

import Layer
import logging
import numpy
import Register

class Circuit(object):
    ''' circuit class '''

    def __init__(self, layer_list):
        ''' initialize circuit '''

        if isinstance(layer_list, list) and all(isinstance(l, Layer.Layer) for l in layer_list) \
        and all(layer_list[0].get_layer_size() == layer_list[i].get_layer_size() \
        for i in range(len(layer_list))):
            RANKS = []
            for i in range(len(layer_list)):

                RANKS.append(i + 1)
            
            LAYERS = []
            for layer in layer_list:

                LAYERS.append(layer)
            
            self.__layer_list = dict(zip(RANKS, LAYERS))
            self.__layer_list = dict(sorted(self.__layer_list.items()))

        else:
            logging.warning('Invalid input! Argument must be list of Layer objects with same ' +\
            'size.')

    def get_layer_list(self):
        ''' getter of the layers in layer list '''

        return self.__layer_list

    def get_layer_nr(self, nr_layer):
        ''' getter of the n-th layer '''

        if isinstance(nr_layer, int) and nr_layer >= 1 and nr_layer <= len(self.__layer_list):
            return self.__layer_list[nr_layer]

        else:
            logging.warning('Invalid input! Argument must be between 1 and ' +\
            str(len(self.__layer_list)))
    
    def get_circuit_size(self):
        ''' getter of the size of the circuit '''

        return len(self.__layer_list)

    def delete_layer(self, nr_layer=None):
        ''' delete layer from circuit '''

        if nr_layer is None or (isinstance(nr_layer, int) and \
        nr_layer >= 1 and nr_layer <= self.get_circuit_size()):
            if nr_layer is None:
                nr_layer = self.get_circuit_size()
                logging.warning('Argument is None therefor Layer is going to be deleted from ' +\
                'the end of list.')
            
            for key in list(self.__layer_list.keys()):

                if int(key) == nr_layer:
                    del self.__layer_list[key]

            self.__layer_list = dict(sorted(self.__layer_list.items()))
            RANKS = []
            for i in range(len(self.__layer_list)):

                RANKS.append(i + 1)
            
            LAYERS = list(self.__layer_list.values())
            self.__layer_list = dict(zip(RANKS, LAYERS))
            self.__layer_list = dict(sorted(self.__layer_list.items()))

        else:
            logging.warning('Invalid input! Argument shall be None or integer between 1 and ' +\
            str(self.get_circuit_size()))

    def insert_layer(self, layer, nr_layer=None):
        ''' insert layer into circuit '''

        if isinstance(layer, Layer.Layer) and (nr_layer is None or (isinstance(nr_layer, int) and \
        nr_layer >= 1 and nr_layer <= self.get_circuit_size() + 1)):
            if nr_layer is None:
                nr_layer = self.get_circuit_size() + 1
                logging.warning('Argument is None therefor Layer is going to be instered at ' +\
                'the end of list.')
            
            self.__layer_list = dict(sorted(self.__layer_list.items()))
            RANKS = []
            for i in range(len(self.__layer_list) + 1):

                RANKS.append(i + 1)
            
            VALUES = list(self.__layer_list.values())
            LAYERS = []
            for i in range(len(self.__layer_list) + 1):

                if i + 1 < nr_layer:
                    LAYERS.append(VALUES[i])

                elif i + 1 == nr_layer:
                    LAYERS.append(layer)

                else:
                    LAYERS.append(VALUES[i - 1])
            
            self.__layer_list = dict(zip(RANKS, LAYERS))
            self.__layer_list = dict(sorted(self.__layer_list.items()))

        else:
            logging.warning('Invalid input! Argument shall be a Gate and an integer between 1 ' +\
            'and ' + str(self.get_circuit_size() + 1))

    def run(self, register):
        ''' run circuit on starting register '''

        if isinstance(register, Register.Register) and \
        register.get_qubit_nr() == self.__layer_list[1].get_layer_size():
            for key in dict(sorted(self.__layer_list.items())):

                vector = numpy.asarray(self.__layer_list[key].get_layer_matrix() *\
                register.ket()).flatten()
                register.set_parameters(vector)

        else:
            logging.warning('Invalid input! Argument must be a Register with the same size of ' +\
            'the Layers.')
