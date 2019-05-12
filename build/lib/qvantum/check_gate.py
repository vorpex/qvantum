'''checking functions for gate class'''

# pylint: disable=E1101, W1401

import numpy
from . import qubit
from . import register

def gate_call_check(function):
    """Decorator to check the arguments of call function in gate class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, qr):
        """Method which makes possible to call a gate on a qubit or a register. The only 
        restriction is that the size of the gate and the size of the qubit or regsiter must be 
        equal to each other.
        
        Arguments:
            qr {Qubit, Register} -- The qubit or register which the gate is called on
        
        Raises:
            ValueError, TypeError
        
        Examples:
            >>> import qvantum
            >>>
            >>> q = qvantum.Random_Qubit()
            >>> q.show()
            '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
            >>> qvantum.Hadamard()(q)
            >>> q.show()
            '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'
        """

        if isinstance(qr, (qubit.Qubit, qubit.Random_Qubit, register.Register)):
            return function(self, qr)
        
        else:
            raise TypeError('Invalid input! Argument must be qubit or register object.')
    
    return wrapper

def set_name_check(function):
    """Decorator to check the arguments of setting name function.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, name):
        """Method to set a new name for the gate.
        
        Arguments:
            name {str} -- Name of the gate to be set
        
        Raises:
            TypeError
        
        Examples:
            >>> import qvantum
            >>> g = qvantum.Gate()
            >>> g.get_name()
            'Identity'
            >>> g.set_name('shoe')
            >>> g.get_name()
            'shoe'
        """

        if isinstance(name, str):
            return function(self, name)

        else:
            raise TypeError('Invalid input! Argument must be string.')
    
    return wrapper

def set_matrix_check(function):
    """Decorator to check the arguments of setting matrix function.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, matrix):
        """Method to set a new unitary matrix for the gate. If matrix is not unitary then an error 
        is raised.
        
        Arguments:
            matrix {numpy.ndarray} -- Matrix of the gate to be set
        
        Raises:
            ValueError, TypeError
        
        Examples:
            >>> import numpy
            >>> import qvantum
            >>>
            >>> g = qvantum.Gate()
            >>> g.get_matrix()
            matrix([[1, 0],
                    [0, 1]])
            >>> g.set_matrix(numpy.matrix([
                    [1 / numpy.sqrt(2), 1 / numpy.sqrt(2)],
                    [1 / numpy.sqrt(2), -1 / numpy.sqrt(2)]
                    ])
                )
            >>> g.get_matrix()
            matrix([[ 0.70710678,  0.70710678],
                    [ 0.70710678, -0.70710678]])
        """

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
    """Decorator to check the arguments of raising a matrix to the given power function.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, power):
        """Method to raise the unitary matrix of the gate to the given power and overwrites the 
        original matrix of the gate with the results matrix.
        
        Arguments:
            power {int} -- The power which the gate is raised on
        
        Raises:
            TypeError
        
        Examples:
            >>> import qvantum
            >>>
            >>> t = qvantum.Toffoli()
            >>> t.get_matrix()
            matrix([[1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0]])
            >>> t.power(2)
            >>> t.get_matrix()
            matrix([[1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1]])
        """

        if isinstance(power, int):
            return function(self, power)

        else:
            raise TypeError('Invalid input! Argument must be integer.')
    
    return wrapper

def CNOT_check(function):
    """Decorator to check the arguments of calling Controlled-Not gate.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, control_qubit, target_qubit):
        """Method to initialize Controlled-Not gate.

        Arguments:
            control_qubit {int} -- Possible values: 0 or 1
            target_qubit {int} -- Possible values: 0 or 1
        
        Raises:
            ValueError

        Examples:
            >>> import qvantum
            >>>
            >>> h = qvantum.CNOT(1, 0)
        """

        if (control_qubit == 0 and target_qubit == 1) \
            or (control_qubit == 1 and target_qubit == 0):
            return function(self, control_qubit, target_qubit)
        
        else:
            raise ValueError('Invalid input! Use number 0 and 1 to mark the control ' +\
                'and target Qubit. (0, 1): 1st qubit is the control and 2nd is the target. ' +\
                '(1, 0): 2nd qubit is the control and 1st is the target.')
    
    return wrapper

def Ising_check(function):
    """Decorator to check the arguments of calling Ising gate.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, phi):
        """Method to initialize Ising gate.

        Arguments:
            phi {int, float} -- The used angle
        
        Raises:
            TypeError

        Examples:
            >>> import qvantum
            >>>
            >>> h = qvantum.Ising(1)
        """

        if isinstance(phi, (int, float)):
            return function(self, phi)
        
        else:
            raise TypeError('Invalid input! Argument must be integer or float.')
    
    return wrapper

def Toffoli_check(function):
    """Decorator to check the arguments of calling Toffoli gate.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, target_qubit):
        """Method to initialize Toffoli gate.

        Arguments:
            target_qubit {Qubit} -- Possible values: 0, 1 or 2
        
        Raises:
            ValueError

        Examples:
            >>> import qvantum
            >>>
            >>> h = qvantum.Toffoli(0)
        """

        if target_qubit == 0 or target_qubit == 1 or target_qubit == 2:
            return function(self, target_qubit)
        
        else:
            raise ValueError('Invalid input! Use number 0, 1, and 2 to mark the target qubit. ' +\
                '0: 1st qubit is the target. 1: 2nd qubit is the target. 2: 3rd qubit is the ' +\
                'target.')
    
    return wrapper

def Fredkin_check(function):
    """Decorator to check the arguments of calling Fredkin gate.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, control_qubit):
        """Method to initialize Fredkin gate.

        Arguments:
            control_qubit {Qubit} -- Possible values: 0, 1 or 2
        
        Raises:
            ValueError

        Examples:
            >>> import qvantum
            >>>
            >>> h = qvantum.Fredkin(2)
        """

        if control_qubit == 0 or control_qubit == 1 or control_qubit == 2:
            return function(self, control_qubit)
        
        else:
            raise ValueError('Invalid input! Use number 0, 1, and 2 to mark the control qubit. ' +\
            '0: 1st qubit is the control. 1: 2nd qubit is the control. 2: 3rd qubit is the ' +\
            'control.')
    
    return wrapper
