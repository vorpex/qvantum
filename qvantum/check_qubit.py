''' checking functions for qubit class '''

# pylint: disable=E1101, W1401

def qubit_init_check(function):
    """Decorator to check the arguments of initialization function in qubit class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, alpha, beta):
        """Wrapper function for given decorator.
        
        Arguments:
            alpha {int, float, complex} -- Amplitude or probability of being in state 0
            beta {int, float, complex} -- Amplitude or probability of being in state 1
        
        Raises:
            ValueError, TypeError
        """

        if all(isinstance(elem, (int, float, complex)) for elem in [alpha, beta]):
            if round(abs(alpha) ** 2 + abs(beta) ** 2 - 1, 10) == 0:
                return function(self, alpha, beta)
        
            else:
                raise ValueError('Invalid input! Alpha and beta must statisfy: ' +\
                    '|alpha|\u00b2 + |beta|\u00b2 = 1.')
        
        else:
            raise TypeError('Invalid input! Alpha and beta must be integer, float or complex.')
    
    return wrapper

def set_amplitudes_check(function):
    """Decorator to check the arguments of setting new amplitudes function in qubit class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, alpha, beta):
        """Wrapper function for given decorator.
        
        Arguments:
            alpha {int, float, complex} -- Amplitude or probability of being in state 0
            beta {int, float, complex} -- Amplitude or probability of being in state 1
        
        Raises:
            ValueError, TypeError
        """

        if all(isinstance(elem, (int, float, complex)) for elem in [alpha, beta]):
            if round(abs(alpha) ** 2 + abs(beta) ** 2 - 1, 10) == 0:
                return function(self, alpha, beta)
        
            else:
                raise ValueError('Invalid input! Alpha and beta must statisfy: ' +\
                    '|alpha|\u00b2 + |beta|\u00b2 = 1.')
        
        else:
            raise TypeError('Invalid input! Alpha and beta must be integer, float or complex.')
    
    return wrapper
