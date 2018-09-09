''' checking functions for qubit class '''

# pylint: disable=E1101

def qubit_init_check(function):
    ''' check the arguments of initialization function of qubit class '''

    def wrapper(self, alpha, beta):

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
    ''' check the arguments of set_amplitudes function '''

    def wrapper(self, alpha, beta):

        if all(isinstance(elem, (int, float, complex)) for elem in [alpha, beta]):
            if round(abs(alpha) ** 2 + abs(beta) ** 2 - 1, 10) == 0:
                return function(self, alpha, beta)
        
            else:
                raise ValueError('Invalid input! Alpha and beta must statisfy: ' +\
                    '|alpha|\u00b2 + |beta|\u00b2 = 1.')
        
        else:
            raise TypeError('Invalid input! Alpha and beta must be integer, float or complex.')
    
    return wrapper
