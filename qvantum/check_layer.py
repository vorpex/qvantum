'''checking functions for layer class'''

# pylint: disable=E1101, W1401

from . import gate

def layer_init_check(function):
    """Decorator to check the arguments of initialization function in layer class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, gate_list):
        """Method to initialize an instance of the Layer class. The argument must be a list of 
        objects in the Gate class or in an inherited class such as: Hadamard, SquareNot, PauliX, 
        PauliY, PauliZ, Phase, Pi8, Swap, SquareSwap, CNOT, ControlledZ, ControlledPhase, Ising, 
        Toffoli, Fredkin.
        
        Arguments:
            gate_list {list} -- List of objects from Gate class
        
        Raises:
            TypeError
        
        Examples:
            >>> import qvantum
            >>>
            >>> l1 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
            >>> l1.get_gate_list()
            OrderedDict([(0, <qvantum.gate.Hadamard at 0x1ae588c2d68>), (1, <qvantum.gate.Gate at 0x1ae56a08a20>)])
            >>> l2 = qvantum.Layer([qvantum.PauliX()])
            >>> l2.get_layer_matrix()
            matrix([[0., 1.],
                    [1., 0.]])
        """

        if isinstance(gate_list, list) and all(isinstance(elem, (gate.Gate, gate.Hadamard, \
            gate.SquareNot, gate.PauliX, gate.PauliY, gate.PauliZ, gate.Phase, gate.Pi8, \
            gate.Swap, gate.SquareSwap, gate.CNOT, gate.ControlledZ, gate.ControlledPhase, \
            gate.Ising, gate.Toffoli, gate.Fredkin)) for elem in gate_list):
            return function(self, gate_list)
        
        else:
            raise TypeError('Invalid input! Argument must be a list of gate objects.')
    
    return wrapper

def get_nth_gate_check(function):
    """Decorator to check the arguments of getting nth gate function.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, nth):
        """Method to return the n-th gate in the current Layer object. The parameter must be 
        between 0 and the actual number of the gates.
        
        Arguments:
            nth {int} -- Number of n-th possible gate
        
        Raises:
            TypeError
        
        Examples:
            >>> import qvantum
            >>>
            >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
            >>> l.get_nth_gate(0)
            <qvantum.gate.Hadamard at 0x1ae588c2d68>
            >>> l.get_nth_gate(1)
            <qvantum.gate.Gate at 0x1ae56a08a20>
            >>> l.get_nth_gate(2)
            ---------------------------------------------------------------------------
            KeyError                                  Traceback (most recent call last)
            <ipython-input-18-5075d5884ea2> in <module>
            ----> 1 l1.get_nth_gate(2)

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_layer.py in wrapper(self, nth)
                27 
                28         if isinstance(nth, int):
            ---> 29             return function(self, nth)
                30 
                31         else:

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\layer.py in get_nth_gate(self, nth)
                53         ''' getter of n-th gate '''
                54 
            ---> 55         return self.__gate_list[nth]
                56 
                57     def get_layer_matrix(self):

            KeyError: 2
        """

        if isinstance(nth, int):
            return function(self, nth)

        else:
            raise TypeError('Invalid input! Argument must be integer.')
    
    return wrapper


def delete_gate_check(function):
    """Decorator to check the arguments of deleting gate function.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, nth):
        """Method to delete the n-th gate from the current Layer object. The parameter must be 
        equal to or bigger than 0 and less than the actual size of the Layer.
        
        Arguments:
            nth {int} -- Number of n-th possible gate
        
        Raises:
            ValueError, TypeError
        
        Examples:
            >>> import qvantum
            >>>
            >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate(), qvantum.PauliX()])
            >>> l.get_gate_list()
            OrderedDict([(0, <qvantum.gate.Hadamard at 0x1ae59262ba8>), (1, <qvantum.gate.Gate at 0x1ae58146ba8>), (2, <qvantum.gate.PauliX at 0x1ae59262d30>)])
            >>> l.delete_gate(3)
            ---------------------------------------------------------------------------
            ValueError                                Traceback (most recent call last)
            <ipython-input-24-9e9f639d1d88> in <module>
            ----> 1 l.delete_gate(3)

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_layer.py in wrapper(self, nth)
                41 
                42         if isinstance(nth, int):
            ---> 43             return function(self, nth)
                44 
                45         else:

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\layer.py in delete_gate(self, nth)
                98         else:
                99             raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +\
            --> 100                 'less or equal to ' + str(len(self.__gate_list) - 1) + '.')
                101 
                102     @check_layer.insert_gate_check

            ValueError: Invalid input! Argument must be greater or equal to 0 and less or equal to 2.
            >>> l.delete_gate(0)
            >>> l.get_gate_list()
            OrderedDict([(0, <qvantum.gate.Gate at 0x1cff211fda0>), (1, <qvantum.gate.PauliX at 0x1cff3f5f4a8>)])
        """

        if isinstance(nth, int):
            return function(self, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be integer.')
    
    return wrapper

def insert_gate_check(function):
    """Decorator to check the arguments of inserting gate function.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, g, nth):
        """Method to insert a Gate object into the n-th place in the current Layer object. The 
        first parameter must be a Gate object or an object in an inherited class such as: 
        Hadamard, SquareNot, PauliX, PauliY, PauliZ, Phase, Pi8, Swap, SquareSwap, CNOT, 
        ControlledZ, ControlledPhase, Ising, Toffoli, Fredkin. The second parameter must be equal 
        to or bigger than 0 and equal to or less than the actual size of the Layer.
        
        Arguments:
            g {gate} -- The gate to be inserted
            nth {int} -- The index where the gate is inserted
        
        Raises:
            ValueError, TypeError
        
        Examples:
            >>> import qvantum
            >>>
            >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate(), qvantum.PauliX()])
            >>> l.get_gate_list()
            OrderedDict([(0, <qvantum.gate.Hadamard at 0x1ae59262ba8>), (1, <qvantum.gate.Gate at 0x1ae58146ba8>), (2, <qvantum.gate.PauliX at 0x1ae59262d30>)])
            >>> l.insert_gate(qvantum.PauliY(), 4)
            ---------------------------------------------------------------------------
            ValueError                                Traceback (most recent call last)
            <ipython-input-32-16da0a14a92d> in <module>
            ----> 1 l.insert_gate(qvantum.PauliY(), 4)

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_layer.py in wrapper(self, g, nth)
                57             gate.ControlledZ, gate.ControlledPhase, gate.Ising, gate.Toffoli, gate.Fredkin)) \
                58             and isinstance(nth, int):
            ---> 59             return function(self, g, nth)
                60 
                61         else:

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\layer.py in insert_gate(self, g, nth)
                123         else:
                124             raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +\
            --> 125                 'less or equal to ' + str(len(self.__gate_list)) + '.')

            ValueError: Invalid input! Argument must be greater or equal to 0 and less or equal to 2.
            >>> l.insert_gate(qvantum.PauliY(), 1)
            >>> l.get_gate_list()
            OrderedDict([(0, <qvantum.gate.Hadamard at 0x1ae59266470>),
                         (1, <qvantum.gate.PauliY at 0x1ae5923d400>),
                         (2, <qvantum.gate.Gate at 0x1ae59266438>),
                         (3, <qvantum.gate.PauliX at 0x1ae59266390>)])
            >>> l.insert_gate(qvantum.PauliY(), 4)
            >>> l.get_gate_list()
            OrderedDict([(0, <qvantum.gate.Hadamard at 0x1ae59266470>),
                         (1, <qvantum.gate.PauliY at 0x1ae5923d400>),
                         (2, <qvantum.gate.Gate at 0x1ae59266438>),
                         (3, <qvantum.gate.PauliX at 0x1ae59266390>),
                         (4, <qvantum.gate.PauliY at 0x1ae59266400>)])
        """

        if isinstance(g, (gate.Gate, gate.Hadamard, gate.SquareNot, gate.PauliX, gate.PauliY, \
            gate.PauliZ, gate.Phase, gate.Pi8, gate.Swap, gate.SquareSwap, gate.CNOT, \
            gate.ControlledZ, gate.ControlledPhase, gate.Ising, gate.Toffoli, gate.Fredkin)) \
            and isinstance(nth, int):
            return function(self, g, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be a pair of gate object and integer.')
    
    return wrapper
