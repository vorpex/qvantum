''' checking functions for circuit class '''

# pylint: disable=E1101

import layer
import register

def circuit_init_check(function):
    ''' check the arguments of initialization function of circuit class '''

    def wrapper(self, layer_list):

        if isinstance(layer_list, list) \
            and all(isinstance(elem, layer.Layer) for elem in layer_list):
            return function(self, layer_list)
        
        else:
            raise TypeError('Invalid input! Argument must be a list of layer objects.')
    
    return wrapper

def get_nth_layer_check(function):
    ''' check the arguments of get_nth_layer function '''

    def wrapper(self, nth):

        if isinstance(nth, int):
            return function(self, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be integer.')
    
    return wrapper

def delete_layer_check(function):
    ''' check the arguments of delete_layer function '''

    def wrapper(self, nth):

        if isinstance(nth, int):
            return function(self, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be integer.')
    
    return wrapper

def insert_layer_check(function):
    ''' check the arguments of insert_layer function '''

    def wrapper(self, l, nth):

        if isinstance(l, layer.Layer) and isinstance(nth, int):
            return function(self, l, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be a pair of layer object and integer.')
    
    return wrapper

def run_check(function):
    ''' check the arguments of run function '''

    def wrapper(self, r):

        if isinstance(r, register.Register):
            return function(self, r)
        
        else:
            raise TypeError('Invalid input! Argument must be a register object.')
    
    return wrapper
