'''layer class'''

# pylint: disable=E1101, W1401

from . import check_layer
import collections
import numpy

class Layer(object):
    """layer class

    An instance of layer class represents one stage in a given quantum computional process. The 
    layer is created by defining the gates which are contained by the given layer. The order of 
    gates refers to that qubit which is affected by the given gate. Using the instances of layer 
    class the user can build an instance of circuit class.

    The instances of layer class have the following methods:

    - __init__()         - initialization method
    - get_gate_list()    - getter of gates in gate list
    - get_gate_number()  - getter of number of gates
    - get_nth_gate()     - getter of n-th gate
    - get_layer_matrix() - getter of result of Kronecker product of matrices in gate list
    - get_matrix_size()  - getter of size of layer matrix (equals to the size of states on 
                        which the layer is usable)
    - get_layer_size()   - getter of size of layer (equals to the size of register on 
                        which the layer is usable)
    - delete_gate()      - delete gate from layer
    - insert_gate()      - insert gate into layer
    """

    @check_layer.layer_init_check
    def __init__(self, gate_list):
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

        ranks = [i for i in range(len(gate_list))]   

        self.__gate_list = collections.OrderedDict(zip(ranks, gate_list))

    def get_gate_list(self):
        """Method to return the gates which are contained by the current Layer object.

        Examples:
            >>> import qvantum
            >>>
            >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
            >>> l.get_gate_list()
            OrderedDict([(0, <qvantum.gate.Hadamard at 0x1ae588c2d68>), (1, <qvantum.gate.Gate at 0x1ae56a08a20>)])
        """

        return self.__gate_list

    def get_gate_number(self):
        """Method to return the number of the gates which are contained by the current Layer object.

        Examples:
            >>> import qvantum
            >>>
            >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
            >>> l.get_gate_number()
            2
        """

        return int(len(self.__gate_list))

    @check_layer.get_nth_gate_check
    def get_nth_gate(self, nth):
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

        return self.__gate_list[nth]

    def get_layer_matrix(self):
        """Method to return the result of the Kronecker multiplication of the gates’ matrices 
        which are contained by the current Layer object. When the Layer is applied on a Register 
        during one step of a calculation the state vector of the Register is multiplied by this 
        matrix.

        Examples:
            >>> import qvantum
            >>>
            >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
            >>> l.get_layer_matrix()
            matrix([[ 0.70710678,  0.        ,  0.70710678,  0.        ],
                    [ 0.        ,  0.70710678,  0.        ,  0.70710678],
                    [ 0.70710678,  0.        , -0.70710678, -0.        ],
                    [ 0.        ,  0.70710678, -0.        , -0.70710678]])
        """

        m = numpy.identity(self.__gate_list[0].get_matrix().shape[0])
        for i in range(len(self.__gate_list)):

            if i == 0:
                m = m * self.__gate_list[i].get_matrix()

            else:
                m = numpy.kron(m, self.__gate_list[i].get_matrix())

        return m

    def get_matrix_size(self):
        """Method to return the size of the matrix of the current Layer object.

        Examples:
            >>> import qvantum
            >>>
            >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
            >>> l.get_layer_matrix()
            matrix([[ 0.70710678,  0.        ,  0.70710678,  0.        ],
                    [ 0.        ,  0.70710678,  0.        ,  0.70710678],
                    [ 0.70710678,  0.        , -0.70710678, -0.        ],
                    [ 0.        ,  0.70710678, -0.        , -0.70710678]])
            >>> l.get_matrix_size()
            4
        """

        return int(self.get_layer_matrix().shape[0])
    
    def get_layer_size(self):
        """Method to return the size of the current Layer object. Remember, it’s not the size 
        of the matrix of the current Layer object but the size of a Register object which the 
        Layer can be applied on.

        Examples:
            >>> import qvantum
            >>>
            >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
            >>> l.get_layer_matrix()
            matrix([[ 0.70710678,  0.        ,  0.70710678,  0.        ],
                    [ 0.        ,  0.70710678,  0.        ,  0.70710678],
                    [ 0.70710678,  0.        , -0.70710678, -0.        ],
                    [ 0.        ,  0.70710678, -0.        , -0.70710678]])
            >>> l.get_matrix_size()
            4
            >>> l.get_layer_size()
            2
        """

        return int(numpy.log2(self.get_matrix_size()))

    @check_layer.delete_gate_check
    def delete_gate(self, nth):
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

        if nth >= 0 and nth <= len(self.__gate_list) - 1:
            gl = self.__gate_list.copy()
            for key in gl:

                if int(key) == nth:
                    del self.__gate_list[nth]

            ranks = [i for i in range(len(self.__gate_list))]            
            gates = list(self.__gate_list.values())

            self.__gate_list = collections.OrderedDict(zip(ranks, gates))
        
        else:
            raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +\
                'less or equal to ' + str(len(self.__gate_list) - 1) + '.')

    @check_layer.insert_gate_check
    def insert_gate(self, g, nth):
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

        if nth >= 0 and nth <= len(self.__gate_list):
            ranks = [i for i in range(len(self.__gate_list) + 1)]            
            values = list(self.__gate_list.values())
            gates = []
            for i in range(len(self.__gate_list) + 1):

                if i < nth:
                    gates.append(values[i])

                elif i == nth:
                    gates.append(g)

                else:
                    gates.append(values[i - 1])
            
            self.__gate_list = collections.OrderedDict(zip(ranks, gates))
        
        else:
            raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +\
                'less or equal to ' + str(len(self.__gate_list)) + '.')
