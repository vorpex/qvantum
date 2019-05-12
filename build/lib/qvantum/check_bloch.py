'''checking functions for bloch sphere representation'''

# pylint: disable=E1101, W1401

from . import qubit

def bloch_coords_check(function):
    """Decorator to check the arguments of qubit-to-bloch-coords function.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(q):
        """This function calculates the coordinates of the Bloch representation from the state vector 
        of a Qubit object.
    
        Arguments:
            q {qubit} -- Instance of Qubit class or Random_Qubit class
        
        Raises:
            TypeError
        
        Examples:
            >>> import qvantum
            >>>
            >>> q = qvantum.Random_Qubit()
            >>> q.show()
            '|Ψ> = (-0.5879-0.7251i)|0> + (0.3522-0.0674i)|1>'
            >>> qvantum.bloch_coords(q)
            (-0.31632342351128423, 0.5899599386821074, 0.7428908146479567)
        """

        if isinstance(q, (qubit.Qubit, qubit.Random_Qubit)):
            return function(q)

        else:
            raise TypeError('Invalid input! Argument must be instance of qubit class.')
    
    return wrapper

def bloch_qubit_check(function):
    """Decorator to check the arguments of bloch-coords-to-qubit function.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(u, v, w):
        """This function calculates the state vector of a Qubit object from the given Bloch 
        coordinates.
        
        Arguments:
            u {int, float} -- 1st coordinate of Bloch representation
            v {int, float} -- 2nd coordinate of Bloch representation
            w {int, float} -- 3rd coordinate of Bloch representation
        
        Raises:
            ValueError, TypeError
        
        Examples:
            >>> import math
            >>> import qvantum
            >>>
            >>> u = 0
            >>> v = 1 / math.sqrt(2)
            >>> w = 1 / math.sqrt(2)
            >>> qvantum.bloch_qubit(u, v, w).show()
            '|Ψ> = (0.9239+0.0000i)|0> + (0.0000+0.3827i)|1>'
        """

        if all(isinstance(elem, (int, float)) for elem in [u, v, w]):
            if round(u ** 2 + v ** 2 + w ** 2 - 1, 10) == 0:
                return function(u, v, w)
        
            else:
                raise ValueError('Invalid input! u, v and w must satisfy: ' +\
                    'u\u00b2 + v\u00b2 + w\u00b2 = 1.')
        
        else:
            raise TypeError('Invalid input! u, v, and w must be integer or float.')
    
    return wrapper

def bloch_sphere_plot_check(function):
    """Decorator to check the arguments of plotting bloch sphere function.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(u, v, w, xfigsize=15, yfigsize=7.5, frame_on=False, tight_layout_on=False, \
            style='dark_background', surface_on=True, wireframe_on=True, surface_cmap='Blues_r', \
            surface_alpha=0.3, wireframe_color='#d3d3d3', wireframe_linewidth=0.075, \
            quiver_color='#ffffff', quiver_linewidth=1.5, quiver_ratio=0.1, line_color='#d3d3d3', \
            line_linewidth=0.3, circle_edgecolor='#d3d3d3', circle_facecolor='none', \
            circle_linewidth=0.3):
        """This function visualizes the qubit using its bloch coordinates and the matplotlib module.
    
        Arguments:
            u {int, float} -- 1st coordinate of Bloch representation
            v {int, float} -- 2nd coordinate of Bloch representation
            w {int, float} -- 3rd coordinate of Bloch representation
        
        Keyword Arguments:
            xfigsize {int, float} -- X size of figure (default: {15})
            yfigsize {int, float} -- Y size of figure (default: {7.5})
            frame_on {bool} -- Frame (default: {False})
            tight_layout_on {bool} -- Tight layout (default: {False})
            style {str} -- Style (default: {'dark_background'})
            surface_on {bool} -- Surface (default: {True})
            wireframe_on {bool} -- Wireframe (default: {True})
            surface_cmap {str} -- Surface cmap (default: {'Blues_r'})
            surface_alpha {int, float} -- Surface alpha (default: {0.3})
            wireframe_color {str} -- Wireframe color (default: {'#d3d3d3'})
            wireframe_linewidth {int, float} -- Width of wireframe line (default: {0.075})
            quiver_color {str} -- Quiver color (default: {'#ffffff'})
            quiver_linewidth {int, float} -- Width of quiver line (default: {1.5})
            quiver_ratio {int, float} -- Quiver ratio (default: {0.1})
            line_color {str} -- Line color (default: {'#d3d3d3'})
            line_linewidth {int, float} -- Width of line (default: {0.3})
            circle_edgecolor {str} -- Edge color of circle (default: {'#d3d3d3'})
            circle_facecolor {str} -- Face color of circle (default: {'none'})
            circle_linewidth {int, float} -- Width of circle line (default: {0.3})
        
        Raises:
            ValueError, TypeError
        
        Examples:
            >>> import qvantum
            >>>
            >>> q = qvantum.Random_Qubit()
            >>> q.show()
            '|Ψ> = (0.6257-0.4027i)|0> + (-0.5114+0.4299i)|1>'
            >>> u = qvantum.bloch_coords(q)[0]
            >>> v = qvantum.bloch_coords(q)[1]
            >>> w = qvantum.bloch_coords(q)[2]
            >>> qvantum.bloch_sphere_plot(u, v, w)
        """

        if all(isinstance(elem, (int, float)) for elem in [u, v, w]):
            if round(u ** 2 + v ** 2 + w ** 2 - 1, 10) == 0:
                return function(u, v, w, xfigsize, yfigsize, frame_on, tight_layout_on, \
                    style, surface_on, wireframe_on, surface_cmap, surface_alpha, \
                    wireframe_color, wireframe_linewidth, quiver_color, quiver_linewidth, \
                    quiver_ratio, line_color, line_linewidth, circle_edgecolor, \
                    circle_facecolor, circle_linewidth)
        
            else:
                raise ValueError('Invalid input! u, v and w must satisfy: ' +\
                    'u\u00b2 + v\u00b2 + w\u00b2 = 1.')
        
        else:
            raise TypeError('Invalid input! u, v, and w must be integer or float.')
    
    return wrapper

def phase_test_check(function):
    """Decorator to check the arguments of phase testing function.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(c1, c2):
        """Computes the phase between two complex number.
    
        Arguments:
            c1 {complex} -- 1st complex number
            c2 {complex} -- 2nd complex number
        
        Raises:
            TypeError
        
        Examples:
            >>> import qvantum
            >>>
            >>> q1 = qvantum.Random_Qubit()
            >>> q1.show()
            '|Ψ> = (0.6615-0.4616i)|0> + (0.5513-0.2132i)|1>'
            >>> q2 = qvantum.Random_Qubit()
            >>> q2.show()
            '|Ψ> = (-0.2091-0.3620i)|0> + (-0.3893+0.8208i)|1>'
            >>> qvantum.phase_test(q1.get_alpha(), q2.get_alpha())
            0.08522011231864535
            >>> qvantum.phase_test(q1.get_beta(), q2.get_beta())
            -0.7255489587145547
        """

        if all(isinstance(elem, complex) for elem in [c1, c2]):
            return function(c1, c2)
        
        else:
            raise TypeError('Invalid input! c1 and c2 must be complex.')
    
    return wrapper
