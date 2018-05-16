'''
Gate class

Short summary

The instances of the Gate class have the following methods:

- __init__() - initialization method
- ...
'''

import logging
import math
import numpy
import Qubit

class Gate(object):
    ''' gate class '''

    def __init__(self):
        ''' initialize gate '''

        self.__gate_name = 'Identity'
        self.__gate_matrix = numpy.matrix([[1, 0], [0, 1]])
        self.__gate_size = self.__gate_matrix.shape

    def get_name(self):
        ''' getter of the name of the gate '''

        return self.__gate_name
    
    def get_matrix(self):
        ''' getter of the matrix of the gate '''

        return self.__gate_matrix

    def get_size(self):
        ''' getter of the size of the gate's matrix '''

        return self.__gate_size
    
    def set_name(self, name):
        ''' setter of the name of the gate '''

        self.__gate_name = str(name)

    def set_matrix(self, matrix):
        ''' setter of the matrix of the gate's matrix '''
    
        if isinstance(matrix, (numpy.ndarray)):
            if matrix.shape[0] == matrix.shape[1]:
                self.__gate_matrix = matrix
            
            else:
                logging.warning('Invalid input! Matrix is not symmetric. ' +\
                'Please use symmetric matrix.')

        else:
           logging.warning('Invalid input! Not numpy matrix. Please use numpy.ndarray.') 

    # def unitary_check(self):
    #     ''' checking if the matrix of the gate is unitary '''

        # get the size of the matrix (M) - n
        # create n-dimensional identity matrix
        # create conjugate transponate of M
        # create M * M*^T and check if it is equal to identity matrix
        # inform user about the result of the test

    def affect(self, qubit):
        ''' call the gate on qubit '''

        if isinstance(qubit, Qubit.Qubit):
            vector = self.__gate_matrix * qubit.ket()
            qubit.set_parameters(vector[0], vector[1])

            return qubit
        
        else:
            logging.warning('Invalid input! Not in Qubit class. Please use instance of Qubit class.')

class H(Gate):
    ''' pre-defined Hadamard gate class '''

    def __init__(self):
        ''' call H as a function '''

        Gate.__init__(self)
        self.set_name('Hadamard')
        # return self.affect(qubit)

print(H().get_name())
