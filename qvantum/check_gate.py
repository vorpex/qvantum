''' checking functions for gate class '''

# pylint: disable=E1101

import numpy
from . import qubit
from . import register

def gate_call_check(function):
    ''' check the arguments of call function of gate class '''

    def wrapper(self, qr):

        if isinstance(qr, (qubit.Qubit, qubit.Random_Qubit, register.Register)):
            return function(self, qr)
        
        else:
            raise TypeError('Invalid input! Argument must be qubit or register object.')
    
    return wrapper

def set_name_check(function):
    ''' check the arguments of set_name function '''

    def wrapper(self, name):

        if isinstance(name, str):
            return function(self, name)

        else:
            raise TypeError('Invalid input! Argument must be string.')
    
    return wrapper

def set_matrix_check(function):
    ''' check the arguments of set_matrix function '''

    def wrapper(self, matrix):

        if isinstance(matrix, numpy.ndarray):
            if matrix.shape[0] == matrix.shape[1]:
                id_matrix = numpy.identity(matrix.shape[0])
                rs_matrix = matrix * matrix.conjugate().transpose()
                if numpy.array_equal(rs_matrix.round(10), id_matrix):
                    return function(self, matrix)
            
                else:
                    raise ValueError('Invalid input! Argument must be an unitary matrix.')
        
            else:
                raise ValueError('Invalid input! Argument must be a symmetric matrix.')
        
        else:
            raise TypeError('Invalid input! Argument must be numpy.ndarray.')
    
    return wrapper

def power_check(function):
    ''' check the arguments of power function '''

    def wrapper(self, power):

        if isinstance(power, int):
            return function(self, power)

        else:
            raise TypeError('Invalid input! Argument must be integer.')
    
    return wrapper

def CNOT_check(function):
    ''' check the arguments of CNOT initialization function '''

    def wrapper(self, control_qubit, target_qubit):

        if (control_qubit == 0 and target_qubit == 1) \
            or (control_qubit == 1 and target_qubit == 0):
            return function(self, control_qubit, target_qubit)
        
        else:
            raise ValueError('Invalid input! Use number 0 and 1 to mark the control ' +\
                'and target Qubit. (0, 1): 1st qubit is the control and 2nd is the target. ' +\
                '(1, 0): 2nd qubit is the control and 1st is the target.')
    
    return wrapper

def Ising_check(function):
    ''' check the arguments of Ising initialization function '''

    def wrapper(self, phi):

        if isinstance(phi, (int, float)):
            return function(self, phi)
        
        else:
            raise TypeError('Invalid input! Argument must be integer or float.')
    
    return wrapper

def Toffoli_check(function):
    ''' check the arguments of Toffoli initialization function '''

    def wrapper(self, target_qubit):

        if target_qubit == 0 or target_qubit == 1 or target_qubit == 2:
            return function(self, target_qubit)
        
        else:
            raise ValueError('Invalid input! Use number 0, 1, and 2 to mark the target qubit. ' +\
                '0: 1st qubit is the target. 1: 2nd qubit is the target. 2: 3rd qubit is the ' +\
                'target.')
    
    return wrapper

def Fredkin_check(function):
    ''' check the arguments of Fredkin initialization function '''

    def wrapper(self, control_qubit):

        if control_qubit == 0 or control_qubit == 1 or control_qubit == 2:
            return function(self, control_qubit)
        
        else:
            raise ValueError('Invalid input! Use number 0, 1, and 2 to mark the control qubit. ' +\
            '0: 1st qubit is the control. 1: 2nd qubit is the control. 2: 3rd qubit is the ' +\
            'control.')
    
    return wrapper
