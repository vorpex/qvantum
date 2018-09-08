''' checker functions '''

# pylint: disable=E1101

import gate
import layer
import numpy
import qubit
import register

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

def bloch_coords_check(function):
    ''' check the arguments of bloch_coords function '''

    def wrapper(qubit):

        if isinstance(qubit, (qubit.Qubit, qubit.Random_Qubit)):
            return function(qubit)
                
        else:
            raise TypeError('Invalid input! Argument must be instance of qubit class.')
    
    return wrapper

def bloch_qubit_check(function):
    ''' check the arguments of bloch_qubit function '''

    def wrapper(u, v, w):

        if all(isinstance(elem, (int, float)) for elem in [u, v, w]):
            if round(u ** 2 + v ** 2 + w ** 2 - 1, 10) == 0:
                return function(u, v, w)
        
            else:
                raise ValueError('Invalid input! u, v and w must statisfy: ' +\
                    'u\u00b2 + v\u00b2 + w\u00b2 = 1.')
        
        else:
            raise TypeError('Invalid input! u, v, and w must be integer or float.')
    
    return wrapper

def bloch_sphere_plot_check(function):
    ''' check the arguments of bloch_sphere_plot function '''

    def wrapper(u, v, w, xfigsize, yfigsize, frame_on, tight_layout_on, \
            style, surface_on, wireframe_on, surface_cmap, surface_alpha, \
            wireframe_color, wireframe_linewidth, quiver_color, quiver_linewidth, \
            quiver_ratio, line_color, line_linewidth, circle_edgecolor, \
            circle_facecolor, circle_linewidth):

        if all(isinstance(elem, (int, float)) for elem in [u, v, w]):
            if round(u ** 2 + v ** 2 + w ** 2 - 1, 10) == 0:
                return function(u, v, w, xfigsize, yfigsize, frame_on, tight_layout_on, \
                    style, surface_on, wireframe_on, surface_cmap, surface_alpha, \
                    wireframe_color, wireframe_linewidth, quiver_color, quiver_linewidth, \
                    quiver_ratio, line_color, line_linewidth, circle_edgecolor, \
                    circle_facecolor, circle_linewidth)
        
            else:
                raise ValueError('Invalid input! u, v and w must statisfy: ' +\
                    'u\u00b2 + v\u00b2 + w\u00b2 = 1.')
        
        else:
            raise TypeError('Invalid input! u, v, and w must be integer or float.')
    
    return wrapper

def phase_test_check(function):
    ''' check the arguments of phase_test function '''

    def wrapper(c1, c2):

        if all(isinstance(elem, complex) for elem in [c1, c2]):
            return function(c1, c2)
        
        else:
            raise TypeError('Invalid input! c1 and c2 must be complex.')
    
    return wrapper

def register_init_check(function):
    ''' check the arguments of initialization function of register class '''

    def wrapper(self, qubit_list):

        if isinstance(qubit_list, list) \
            and all(isinstance(elem, qubit.Qubit) for elem in qubit_list):
            if len(qubit_list) >= 2:
                return function(self, qubit_list)
            
            else:
                raise ValueError('Invalid input! Qubit list must contain at least 2 qubit ' +\
                    'object.')
        
        else:
            raise TypeError('Invalid input! Argument must be a list of qubit objects.')
    
    return wrapper

def get_nth_state_check(function):
    ''' check the arguments of get_nth_state function '''

    def wrapper(self, nth):

        if isinstance(nth, int):
            return function(self, nth)

        else:
            raise TypeError('Invalid input! Argument must be integer.')

    return wrapper

def get_amplitudes_check(function):
    ''' check the arguments of get_amplitudes function '''

    def wrapper(self, nth):

        if isinstance(nth, (int, None)):
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
                raise ValueError('Invalid input! The square sum of absolute value of amplitudes ' +\
                    'must be equal to 1.')
        
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

    def wrapper(self, qubit, nth):

        if isinstance(qubit, qubit.Qubit) and isinstance(nth, int):
            return function(self, qubit, nth)

        else:
            raise TypeError('Invalid input! Argument must a pair of qubit object and integer.')
    
    return wrapper

def gate_call_check(function):
    ''' check the arguments of call function of gate class '''

    def wrapper(self, qr):

        if isinstance(qr, (qubit.Qubit, register.Register)):
            return function(self, qr)
        
        else:
            raise TypeError('Invalid input! Argument must be qubit or register object.')
    
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

    def wrapper(self, gate, nth):

        if isinstance(gate, gate.Gate) and isinstance(nth, int):
            return function(self, gate, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be a pair of gate object and integer.')
    
    return wrapper

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

    def wrapper(self, layer, nth):

        if isinstance(layer, layer.Layer) and isinstance(nth, int):
            return function(self, layer, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be a pair of layer object and integer.')
    
    return wrapper

def run_check(function):
    ''' check the arguments of run function '''

    def wrapper(self, register):

        if isinstance(register, register.Register):
            return function(self, register)
        
        else:
            raise TypeError('Invalid input! Argument must be a register object.')
    
    return wrapper
