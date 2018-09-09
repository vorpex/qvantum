''' checking functions for bloch sphere representation '''

# pylint: disable=E1101

import numpy
import qubit

def bloch_coords_check(function):
    ''' check the arguments of bloch_coords function '''

    def wrapper(q):

        if isinstance(q, (qubit.Qubit, qubit.Random_Qubit)):
            return function(q)

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

    def wrapper(u, v, w, xfigsize=None, yfigsize=None, frame_on=None, tight_layout_on=None, \
            style=None, surface_on=None, wireframe_on=None, surface_cmap=None, \
            surface_alpha=None, wireframe_color=None, wireframe_linewidth=None, \
            quiver_color=None, quiver_linewidth=None, quiver_ratio=None, line_color=None, \
            line_linewidth=None, circle_edgecolor=None, circle_facecolor=None, \
            circle_linewidth=None):

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
