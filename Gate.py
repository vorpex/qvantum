'''
Gate class

Short summary

The instances of the Gate class have the following methods:

- __init__() - initialization method
- ...
'''

'''
Replacement:

    - Python2: super(Hadamard, self), super(PauliX, self), ... etc.
    - Python3: super()
'''

import logging
import math
import numpy
import Qubit
import unicodedata

class Gate(object):
    ''' gate class '''

    def __init__(self):
        ''' initialize gate '''

        self.__gate_name = 'Identity'
        self.__gate_matrix = numpy.matrix([[1, 0], [0, 1]])

    def __call__(self, qubit):
        ''' call the gate on qubit '''

        if isinstance(qubit, Qubit.Qubit):
            vector = self.__gate_matrix * qubit.ket()
            qubit.set_parameters(vector.item(0), vector.item(1))

            return qubit
        
        else:
            logging.warning('Invalid input! Not in Qubit class. ' +\
            'Please use instance of Qubit class.')

    def get_name(self):
        ''' getter of the name of the gate '''

        return self.__gate_name
    
    def get_matrix(self):
        ''' getter of the matrix of the gate '''

        return self.__gate_matrix

    def get_size(self):
        ''' getter of the size of the gate's matrix '''

        return self.__gate_matrix.shape[0]
    
    def set_name(self, name):
        ''' setter of the name of the gate '''

        self.__gate_name = str(name)

    def set_matrix(self, matrix):
        ''' setter of the matrix of the gate's matrix '''
    
        if isinstance(matrix, numpy.ndarray):
            if matrix.shape[0] == matrix.shape[1]:
                IDENTITY = numpy.identity(matrix.shape[0])
                MATRIX = matrix * matrix.conjugate().transpose()
                if numpy.array_equal(MATRIX.round(10), IDENTITY):
                    self.__gate_matrix = matrix

                else:
                    logging.warning('The matrix is not unitary. Please use a unitary matrix!')
            
            else:
                logging.warning('Invalid input! Matrix is not symmetric. ' +\
                'Please use symmetric matrix.')

        else:
           logging.warning('Invalid input! Not numpy matrix. Please use numpy.ndarray.') 

    def unitary_check(self):
        ''' checking if the matrix of the gate is unitary '''

        IDENTITY = numpy.identity(self.__gate_matrix.shape[0])
        MATRIX = self.__gate_matrix * self.__gate_matrix.conjugate().transpose()
        if numpy.array_equal(MATRIX.round(10), IDENTITY):
            print('The matrix is unitary.')
            return 1
        
        else:
            logging.warning('The matrix is not unitary. Please use a unitary matrix!')
            return 0

class Hadamard(Gate):
    ''' Hadamard gate class '''

    def __init__(self):
        ''' initialize Hadamard gate '''

        Gate.__init__(self)
        super().set_name('Hadamard')
        super().set_matrix(numpy.matrix([
            [1 / math.sqrt(2), 1 / math.sqrt(2)], \
            [1 / math.sqrt(2), -1 / math.sqrt(2)]
            ]))
    
    def set_name(self, name):
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Hadamard gate's matrix '''

        pass

class PauliX(Gate):
    ''' Pauli-X gate class '''

    def __init__(self):
        ''' initialize Pauli-X gate '''

        Gate.__init__(self)
        super().set_name('Pauli-X')
        super().set_matrix(numpy.matrix([
            [0, 1], \
            [1, 0]
            ]))
    
    def set_name(self, name):
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Hadamard gate's matrix '''

        pass

class PauliY(Gate):
    ''' Pauli-Y gate class '''

    def __init__(self):
        ''' initialize Pauli-Y gate '''

        Gate.__init__(self)
        super().set_name('Pauli-Y')
        super().set_matrix(numpy.matrix([
            [0, complex(0, -1)], \
            [complex(0, 1), 0]
            ]))
    
    def set_name(self, name):
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Hadamard gate's matrix '''

        pass

class PauliZ(Gate):
    ''' Pauli-Z gate class '''

    def __init__(self):
        ''' initialize Pauli-Z gate '''

        Gate.__init__(self)
        super().set_name('Pauli-Z')
        super().set_matrix(numpy.matrix([
            [1, 0], \
            [0, -1]
            ]))
    
    def set_name(self, name):
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Hadamard gate's matrix '''

        pass

class Phase(Gate):
    ''' Phase gate class '''

    def __init__(self):
        ''' initialize Phase gate '''

        Gate.__init__(self)
        super().set_name('Phase')
        super().set_matrix(numpy.matrix([
            [1, 0], \
            [0, complex(0, 1)]
            ]))
    
    def set_name(self, name):
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Hadamard gate's matrix '''

        pass

class Pi8(Gate):
    ''' Pi/8 gate class '''

    def __init__(self):
        ''' initialize Pi/8 gate '''

        Gate.__init__(self)
        super().set_name(unicodedata.lookup('GREEK SMALL LETTER PI') + '/8')
        super().set_matrix(numpy.matrix([
            [1, 0], \
            [0, complex(math.cos(math.pi/4), math.sin(math.pi/4))]
            ]))
    
    def set_name(self, name):
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Hadamard gate's matrix '''

        pass

class CNOT(Gate):
    ''' Controlled-Not gate class '''

    def __init__(self):
        ''' initialize Controlled-Not gate '''

        Gate.__init__(self)
        super().set_name('Controlled-Not')
        super().set_matrix(numpy.matrix([
            [1, 0, 0, 0], \
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
            ]))
    
    def __call__(self, control_qubit, target_qubit):
        ''' call the gate on qubit '''

        if isinstance(control_qubit, Qubit.Qubit) and isinstance(target_qubit, Qubit.Qubit):
            coeff_list = []
            for i in range(control_qubit.ket().shape[0]):

                for j in range(target_qubit.ket().shape[0]):

                    coeff_list.append(control_qubit.ket()[i] * target_qubit.ket()[j])
            
            state = numpy.array(coeff_list)
            state.shape = (control_qubit.ket().shape[0] + target_qubit.ket().shape[0], 1)
            state = self.get_matrix() * state

            return state
        
        else:
            logging.warning('Invalid input! Not in Qubit class. ' +\
            'Please use instances of Qubit class.')
    
    def set_name(self, name):
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Hadamard gate's matrix '''

        pass

q = Qubit.Qubit(1, 0)
Hadamard()(q)
print(q.show())
print(Hadamard().get_name())

print('\n')

H = Hadamard()
print(H.get_name())
H.set_name('Test')
print(H.get_name())
print(H.get_size())

print('\n')

print(Pi8().get_name())

print('\n')

q1 = Qubit.Qubit(0, 1)
q2 = Qubit.Qubit(1 / math.sqrt(2), -1 / math.sqrt(2))
print(CNOT()(q1, q2))
