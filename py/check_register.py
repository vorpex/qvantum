''' checking functions for register class '''

# pylint: disable=E1101

import numpy
import qubit

def register_init_check(function):
    ''' check the arguments of initialization function of register class '''

    def wrapper(self, qubit_list):

        if isinstance(qubit_list, list) \
            and all(isinstance(elem, (qubit.Qubit, qubit.Random_Qubit)) for elem in qubit_list):
            if len(qubit_list) >= 2:
                return function(self, qubit_list)
            
            else:
                raise ValueError('Invalid input! Qubit list must contain at least 2 qubit ' +\
                    'object.')
        
        else:
            raise TypeError('Invalid input! Argument must be a list of qubit objects.')
    
    return wrapper

def get_states_check(function):
    ''' check the arguments of get_nth_state function '''

    def wrapper(self, nth=None):

        if isinstance(nth, int) or nth is None:
            return function(self, nth)

        else:
            raise TypeError('Invalid input! Argument must be integer.')

    return wrapper

def get_amplitudes_check(function):
    ''' check the arguments of get_amplitudes function '''

    def wrapper(self, nth=None):

        if isinstance(nth, int) or nth is None:
            return function(self, nth)

        else:
            raise TypeError('Invalid input! Argument must be integer or None type.')

    return wrapper

def set_amplitudes_check(function):
    ''' check the arguments of set_amplitudes function '''

    def wrapper(self, amp_list):

        if isinstance(amp_list, list) \
            and all(isinstance(elem, (int, float, complex)) for elem in amp_list):
            if round(numpy.sum(numpy.square(numpy.absolute(amp_list))) - 1, 10) == 0:
                return function(self, amp_list)

            else:
                raise ValueError('Invalid input! The square sum of absolute value of ' +\
                    'amplitudes must be equal to 1.')
        
        else:
            raise TypeError('Invalid input! Argument must be a list of integer, float or ' +\
                'complex numbers.')
    
    return wrapper

def measure_nth_qubit_check(function):
    ''' check the arguments of measure_nth_qubit function '''

    def wrapper(self, nth):

        if isinstance(nth, int):
            return function(self, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be integer.')
    
    return wrapper

def insert_qubit_check(function):
    ''' check the arguments of insert_qubit function '''

    def wrapper(self, q, nth):

        if isinstance(q, (qubit.Qubit, qubit.Random_Qubit)) and isinstance(nth, int):
            return function(self, q, nth)

        else:
            raise TypeError('Invalid input! Argument must a pair of qubit object and integer.')
    
    return wrapper
