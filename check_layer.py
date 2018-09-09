''' checking functions for layer class '''

# pylint: disable=E1101

import gate

def layer_init_check(function):
    ''' check the arguments of initialization function of layer class '''

    def wrapper(self, gate_list):

        if isinstance(gate_list, list) and all(isinstance(elem, gate.Gate) for elem in gate_list):
            return function(self, gate_list)
        
        else:
            raise TypeError('Invalid input! Argument must be a list of gate objects.')
    
    return wrapper

def get_nth_gate_check(function):
    ''' check the arguments of get_nth_gate function '''

    def wrapper(self, nth):

        if isinstance(nth, int):
            return function(self, nth)

        else:
            raise TypeError('Invalid input! Argument must be integer.')
    
    return wrapper


def delete_gate_check(function):
    ''' check the arguments of delete_gate function '''

    def wrapper(self, nth):

        if isinstance(nth, int):
            return function(self, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be integer.')
    
    return wrapper

def insert_gate_check(function):
    ''' check the arguments of insert_gate function '''

    def wrapper(self, g, nth):

        if isinstance(g, gate.Gate) and isinstance(nth, int):
            return function(self, g, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be a pair of gate object and integer.')
    
    return wrapper
