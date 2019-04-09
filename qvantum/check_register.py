''' checking functions for register class '''

# pylint: disable=E1101

import numpy
from . import qubit

def register_init_check(function):
    """Decorator to check the arguments of initialization function in register class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, qubit_list):
        """Wrapper function for given decorator.
        
        Arguments:
            qubit_list {list} -- List of objects from Qubit or Random_Qubit class
        
        Raises:
            ValueError, TypeError
        """

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
    """Decorator to check the arguments of getting states function in register class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, nth=None):
        """Wrapper function for given decorator.
        
        Keyword Arguments:
            nth {int} -- Number of n-th possible state (default: {None})
        
        Raises:
            TypeError
        """

        if isinstance(nth, int) or nth is None:
            return function(self, nth)

        else:
            raise TypeError('Invalid input! Argument must be integer.')

    return wrapper

def get_amplitudes_check(function):
    """Decorator to check the arguments of getting amplitudes function in register class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, nth=None):
        """Wrapper function for given decorator.
        
        Keyword Arguments:
            nth {int} -- Number of n-th possible amplitude (default: {None})
        
        Raises:
            TypeError
        """

        if isinstance(nth, int) or nth is None:
            return function(self, nth)

        else:
            raise TypeError('Invalid input! Argument must be integer or None type.')

    return wrapper

def set_amplitudes_check(function):
    """Decorator to check the arguments of setting amplitudes function in register class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, amp_list):
        """Wrapper function for given decorator.
        
        Arguments:
            amp_list {list} -- List of int, float or complex objects
        
        Raises:
            ValueError, TypeError
        """

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
    """Decorator to check the arguments of measuring qubit function in register class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, nth):
        """Wrapper function for given decorator.
        
        Arguments:
            nth {int} -- Number of n-th possible qubit
        
        Raises:
            TypeError
        """

        if isinstance(nth, int):
            return function(self, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be integer.')
    
    return wrapper

def delete_qubit_check(function):
    """Decorator to check the arguments of deleting qubit function in register class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, nth):
        """Wrapper function for given decorator.
        
        Arguments:
            nth {int} -- Number of n-th possible qubit
        
        Raises:
            ValueError, TypeError
        """
    
        if isinstance(nth, int):
            return function(self, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be integer.')
    
    return wrapper

def insert_qubit_check(function):
    """Decorator to check the arguments of inserting qubit function in register class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, q, nth):
        """Wrapper function for given decorator.
        
        Arguments:
            q {qubit} -- The qubit to be inserted
            nth {int} -- The index where the qubit is inserted
        
        Raises:
            ValueError, TypeError
        """

        if isinstance(q, (qubit.Qubit, qubit.Random_Qubit)) and isinstance(nth, int):
            return function(self, q, nth)

        else:
            raise TypeError('Invalid input! Argument must a pair of qubit object and integer.')
    
    return wrapper
