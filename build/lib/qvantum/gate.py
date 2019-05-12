'''gate class'''

# pylint: disable=E1101, W1401

from . import check_gate
import numpy
from . import qubit
from . import register
import unicodedata

class Gate(object):
    """gate class

    "In quantum computing and specifically the quantum circuit model of computation, a quantum logic
    gate is a basic quantum circuit operating on a small number of qubits. They are the building blocks
    of quantum circuits, like classical logic gates are for conventional digital circuits.

    Quantum logic gates are represented by unitary matrices. The most common quantum gates operate on
    spaces of one or two qubits, just like the common classical logic gates operate on one or two bits.
    As matrices, quantum gates can be described by 2^n x 2^n sized unitary matrices, where n is the
    number of qubits that the gate act on. The variables that the gates act upon, the quantum states,
    are vectors in 2^n complex dimensions, where n again is the number of qubits of variable:
    The base vectors are the possible outcomes if measured, and a quantum state is a linear combination
    of outcomes."

    via Wikipedia: https://en.wikipedia.org/wiki/Quantum_logic_gate

    The instances of gate class have the following methods:

    - __init__()      - initialization method
    - __call__()      - call method
    - get_name()      - getter of name of gate
    - get_matrix()    - getter of matrix of gate
    - get_size()      - getter of size of matrix of gate
    - set_name()      - setter of name of gate
    - set_matrix()    - setter of matrix of gate
    - power()         - raise the matrix of gate to the given power
    """

    def __init__(self):
        """Method to initialize a 2x2 sized identity matrix. Every identity matrix is a unitary 
        matrix as well.

        Examples:
            >>> import qvantum
            >>>
            >>> g = qvantum.Gate()
            >>> g.get_name()
            'Identity'
            >>> g.get_matrix()
            matrix([[1, 0],
                    [0, 1]])
            >>> g.get_size()
            2
        """

        self.__gate_name = 'Identity'
        self.__gate_matrix = numpy.matrix([
            [1, 0],
            [0, 1]
            ])

    @check_gate.gate_call_check
    def __call__(self, qr):
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

        if isinstance(qr, (qubit.Qubit, qubit.Random_Qubit)) and self.get_size() == 2:
            vector = self.__gate_matrix * qr.ket()
            qr.set_amplitudes(vector.item(0), vector.item(1))
        
        elif isinstance(qr, register.Register) and self.get_size() == qr.get_state_number():
            vector = numpy.asarray(self.__gate_matrix * qr.ket()).flatten()
            qr.set_amplitudes(list(vector))
        
        else:
            raise ValueError('Invalid input! Use qubit or register as input with the same size ' +\
                'as the gate size.')

    def get_name(self):
        """Method to return the unitary matrix of the gate.

        Examples:
            >>> import qvantum
            >>>
            >>> c = qvantum.CNOT(0, 1)
            >>> c.get_name()
            'Controlled-Not'
        """

        return self.__gate_name
    
    def get_matrix(self):
        """Method to return the unitary matrix of the gate.

        Examples:
            >>> import qvantum
            >>>
            >>> c = qvantum.CNOT(0, 1)
            >>> c.get_matrix()
            matrix([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 1],
                    [0, 0, 1, 0]])
        """

        return self.__gate_matrix

    def get_size(self):
        """Method to retun the size of the unitary matrix of the gate.

        Examples:
            >>> import qvantum
            >>>
            >>> c = qvantum.CNOT(0, 1)
            >>> c.get_size()
            4
        """

        return self.__gate_matrix.shape[0]
    
    @check_gate.set_name_check
    def set_name(self, name):
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

        self.__gate_name = str(name)

    @check_gate.set_matrix_check
    def set_matrix(self, matrix):
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
    
        self.__gate_matrix = matrix
    
    @check_gate.power_check
    def power(self, power):
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

        self.__gate_matrix = numpy.linalg.matrix_power(self.__gate_matrix, power)

class Hadamard(Gate):
    """This class is an inherited class from the Gate class. It’s the implementation of the 
    Hadamard gate. Its unitary matrix:

    """

    def __init__(self):
        """Method to initialize Hadamard gate.

        Examples:
            >>> import qvantum
            >>>
            >>> h = qvantum.Hadamard()
        """

        Gate.__init__(self)
        # super().set_name('Hadamard')
        # super().set_matrix(numpy.matrix([
        #     [1 / numpy.sqrt(2), 1 / numpy.sqrt(2)],
        #     [1 / numpy.sqrt(2), -1 / numpy.sqrt(2)]
        #     ]))
        super(Hadamard, self).set_name('Hadamard')
        super(Hadamard, self).set_matrix(numpy.matrix([
            [1 / numpy.sqrt(2), 1 / numpy.sqrt(2)],
            [1 / numpy.sqrt(2), -1 / numpy.sqrt(2)]
            ]))
    
    def set_name(self, name):
        """Setter of name of Hadamard gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the name of object in Hadamard class.')
    
    def set_matrix(self, matrix):
        """Setter of matrix of Hadamard gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the matrix of object in Hadamard class.')

class SquareNot(Gate):
    """This class is an inherited class from the Gate class. It’s the implementation of the 
    Square-Not gate. Its unitary matrix:
    
    """

    def __init__(self):
        """Method to initialize Square-Not gate.

        Examples:
            >>> import qvantum
            >>>
            >>> h = qvantum.SquareNot()
        """

        Gate.__init__(self)
        # super().set_name('Square-Not')
        # super().set_matrix(numpy.matrix([
        #     [1 + complex(0, 1), 1 - complex(0, 1)],
        #     [1 - complex(0, 1), 1 + complex(0, 1)]
        #     ]))
        super(SquareNot, self).set_name('Square-Not')
        super(SquareNot, self).set_matrix(numpy.matrix([
            [1 + complex(0, 1), 1 - complex(0, 1)],
            [1 - complex(0, 1), 1 + complex(0, 1)]
            ]))
    
    def set_name(self, name):
        """Setter of name of Square-Not gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the name of object in SquareNot class.')
    
    def set_matrix(self, matrix):
        """Setter of matrix of Square-Not gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the matrix of object in SquareNot class.')

class PauliX(Gate):
    """This class is an inherited class from the Gate class. It’s the implementation of the 
    Pauli-X gate. Its unitary matrix:
    
    """

    def __init__(self):
        """Method to initialize Pauli-X gate.

        Examples:
            >>> import qvantum
            >>>
            >>> h = qvantum.PauliX()
        """

        Gate.__init__(self)
        # super().set_name('Pauli-X')
        # super().set_matrix(numpy.matrix([
        #     [0, 1],
        #     [1, 0]
        #     ]))
        super(PauliX, self).set_name('Pauli-X')
        super(PauliX, self).set_matrix(numpy.matrix([
            [0, 1],
            [1, 0]
            ]))
    
    def set_name(self, name):
        """Setter of name of Pauli-X gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the name of object in PauliX class.')
    
    def set_matrix(self, matrix):
        """Setter of matrix of Pauli-X gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the matrix of object in PauliX class.')

class PauliY(Gate):
    """This class is an inherited class from the Gate class. It’s the implementation of the 
    Pauli-Y gate. Its unitary matrix:
    
    """

    def __init__(self):
        """Method to initialize Pauli-Y gate.

        Examples:
            >>> import qvantum
            >>>
            >>> h = qvantum.PauliY()
        """

        Gate.__init__(self)
        # super().set_name('Pauli-Y')
        # super().set_matrix(numpy.matrix([
        #     [0, complex(0, -1)],
        #     [complex(0, 1), 0]
        #     ]))
        super(PauliY, self).set_name('Pauli-Y')
        super(PauliY, self).set_matrix(numpy.matrix([
            [0, complex(0, -1)],
            [complex(0, 1), 0]
            ]))
    
    def set_name(self, name):
        """Setter of name of Pauli-Y gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the name of object in PauliY class.')
    
    def set_matrix(self, matrix):
        """Setter of matrix of Pauli-Y gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the matrix of object in PauliY class.')

class PauliZ(Gate):
    """This class is an inherited class from the Gate class. It’s the implementation of the 
    Pauli-Z gate. Its unitary matrix:
    
    """

    def __init__(self):
        """Method to initialize Pauli-Z gate.

        Examples:
            >>> import qvantum
            >>>
            >>> h = qvantum.PauliZ()
        """

        Gate.__init__(self)
        # super().set_name('Pauli-Z')
        # super().set_matrix(numpy.matrix([
        #     [1, 0],
        #     [0, -1]
        #     ]))
        super(PauliZ, self).set_name('Pauli-Z')
        super(PauliZ, self).set_matrix(numpy.matrix([
            [1, 0],
            [0, -1]
            ]))
    
    def set_name(self, name):
        """Setter of name of Pauli-Z gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the name of object in PauliZ class.')
    
    def set_matrix(self, matrix):
        """Setter of matrix of Pauli-Z gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the matrix of object in PauliZ class.')

class Phase(Gate):
    """This class is an inherited class from the Gate class. It’s the implementation of the 
    Phase gate. Its unitary matrix:
    
    """

    def __init__(self):
        """Method to initialize Phase gate.

        Examples:
            >>> import qvantum
            >>>
            >>> h = qvantum.Phase()
        """

        Gate.__init__(self)
        # super().set_name('Phase')
        # super().set_matrix(numpy.matrix([
        #     [1, 0],
        #     [0, complex(0, 1)]
        #     ]))
        super(Phase, self).set_name('Phase')
        super(Phase, self).set_matrix(numpy.matrix([
            [1, 0],
            [0, complex(0, 1)]
            ]))
    
    def set_name(self, name):
        """Setter of name of Phase gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the name of object in Phase class.')
    
    def set_matrix(self, matrix):
        """Setter of matrix of Phase gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the matrix of object in Phase class.')

class Pi8(Gate):
    """This class is an inherited class from the Gate class. It’s the implementation of the 
    Pi/8 gate. Its unitary matrix:
    
    """

    def __init__(self):
        """Method to initialize Pi/8 gate.

        Examples:
            >>> import qvantum
            >>>
            >>> h = qvantum.Pi8()
        """

        Gate.__init__(self)
        # super().set_name(unicodedata.lookup('GREEK SMALL LETTER PI') + '/8')
        # super().set_matrix(numpy.matrix([
        #     [1, 0],
        #     [0, complex(numpy.cos(numpy.pi/4), numpy.sin(numpy.pi/4))]
        #     ]))
        super(Pi8, self).set_name(unicodedata.lookup('GREEK SMALL LETTER PI') + '/8')
        super(Pi8, self).set_matrix(numpy.matrix([
            [1, 0],
            [0, complex(numpy.cos(numpy.pi/4), numpy.sin(numpy.pi/4))]
            ]))
    
    def set_name(self, name):
        """Setter of name of Pi/8 gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the name of object in Pi8 class.')
    
    def set_matrix(self, matrix):
        """Setter of matrix of Pi/8 gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the matrix of object in Pi8 class.')

class Swap(Gate):
    """This class is an inherited class from the Gate class. It’s the implementation of the 
    Swap gate. Its unitary matrix:
    
    """

    def __init__(self):
        """Method to initialize Swap gate.

        Examples:
            >>> import qvantum
            >>>
            >>> h = qvantum.Swap()
        """

        Gate.__init__(self)
        # super().set_name('Swap')
        # super().set_matrix(numpy.matrix([
        #     [1, 0, 0, 0],
        #     [0, 0, 1, 0],
        #     [0, 1, 0, 0],
        #     [0, 0, 0, 1]
        #     ]))
        super(Swap, self).set_name('Swap')
        super(Swap, self).set_matrix(numpy.matrix([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
            ]))
    
    def set_name(self, name):
        """Setter of name of Swap gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the name of object in Swap class.')
    
    def set_matrix(self, matrix):
        """Setter of matrix of Swap gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the matrix of object in Swap class.')

class SquareSwap(Gate):
    """This class is an inherited class from the Gate class. It’s the implementation of the 
    Square-Swap gate. Its unitary matrix:
    
    """

    def __init__(self):
        """Method to initialize Square-Swap gate.

        Examples:
            >>> import qvantum
            >>>
            >>> h = qvantum.SquareSwap()
        """

        Gate.__init__(self)
        # super().set_name('Square-Swap')
        # super().set_matrix(numpy.matrix([
        #     [1, 0, 0, 0],
        #     [0, (1 + complex(0, 1)) / 2, (1 - complex(0, 1)) / 2, 0],
        #     [0, (1 - complex(0, 1)) / 2, (1 + complex(0, 1)) / 2, 0],
        #     [0, 0, 0, 1]
        #     ]))
        super(SquareSwap, self).set_name('Square-Swap')
        super(SquareSwap, self).set_matrix(numpy.matrix([
            [1, 0, 0, 0],
            [0, (1 + complex(0, 1)) / 2, (1 - complex(0, 1)) / 2, 0],
            [0, (1 - complex(0, 1)) / 2, (1 + complex(0, 1)) / 2, 0],
            [0, 0, 0, 1]
            ]))
    
    def set_name(self, name):
        """Setter of name of Square-Swap gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the name of object in SquareSwap class.')
    
    def set_matrix(self, matrix):
        """Setter of matrix of Square-Swap gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the matrix of object in SquareSwap class.')

class CNOT(Gate):
    """This class is an inherited class from the Gate class. It’s the implementation of the 
    Controlled-Not gate. It’s called on 2 qubits. The parameters determine which one is the 
    control and the target – (0, 1) or (1, 0). Its unitary matrix:
    
    """

    @check_gate.CNOT_check
    def __init__(self, control_qubit, target_qubit):
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

        Gate.__init__(self)
        # super().set_name('Controlled-Not')
        super(CNOT, self).set_name('Controlled-Not')
        if control_qubit == 0 and target_qubit == 1:
            # super().set_matrix(numpy.matrix([
            # [1, 0, 0, 0],
            # [0, 1, 0, 0],
            # [0, 0, 0, 1],
            # [0, 0, 1, 0]
            # ]))
            super(CNOT, self).set_matrix(numpy.matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
            ]))

        else:
            # super().set_matrix(numpy.matrix([
            # [1, 0, 0, 0],
            # [0, 0, 0, 1],
            # [0, 0, 1, 0],
            # [0, 1, 0, 0]
            # ]))
            super(CNOT, self).set_matrix(numpy.matrix([
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0]
            ]))

    def set_name(self, name):
        """Setter of name of Controlled-Not gate. Always raises BaseException.

        Raises:
            BaseException
        """
        
        raise BaseException('Can\'t change the name of object in CNOT class.')

    def set_matrix(self, matrix):
        """Setter of matrix of Controlled-Not gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the matrix of object in CNOT class.')

class ControlledZ(Gate):
    """This class is an inherited class from the Gate class. It’s the implementation of the 
    Controlled-Z gate. Its unitary matrix:
    
    """

    def __init__(self):
        """Method to initialize Controlled-Z gate.

        Examples:
            >>> import qvantum
            >>>
            >>> h = qvantum.ControlledZ()
        """

        Gate.__init__(self)
        # super().set_name('Controlled-Z')
        # super().set_matrix(numpy.matrix([
        #     [1, 0, 0, 0],
        #     [0, 1, 0, 0],
        #     [0, 0, 1, 0],
        #     [0, 0, 0, -1]
        #     ]))
        super(ControlledZ, self).set_name('Controlled-Z')
        super(ControlledZ, self).set_matrix(numpy.matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, -1]
            ]))

    def set_name(self, name):
        """Setter of name of Controlled-Z gate. Always raises BaseException.

        Raises:
            BaseException
        """
        
        raise BaseException('Can\'t change the name of object in ControlledZ class.')

    def set_matrix(self, matrix):
        """Setter of matrix of Controlled-Z gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the matrix of object in ControlledZ class.')

class ControlledPhase(Gate):
    """This class is an inherited class from the Gate class. It’s the implementation of the 
    Controlled-Phase gate. Its unitary matrix:
    
    """

    def __init__(self):
        """Method to initialize Controlled-Phase gate.

        Examples:
            >>> import qvantum
            >>>
            >>> h = qvantum.ControlledPhase()
        """

        Gate.__init__(self)
        # super().set_name('Controlled-Phase')
        # super().set_matrix(numpy.matrix([
        #     [1, 0, 0, 0],
        #     [0, 1, 0, 0],
        #     [0, 0, 1, 0],
        #     [0, 0, 0, complex(0, 1)]
        #     ]))
        super(ControlledPhase, self).set_name('Controlled-Phase')
        super(ControlledPhase, self).set_matrix(numpy.matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, complex(0, 1)]
            ]))

    def set_name(self, name):
        """Setter of name of Controlled-Phase gate. Always raises BaseException.

        Raises:
            BaseException
        """
        
        raise BaseException('Can\'t change the name of object in ControlledPhase class.')

    def set_matrix(self, matrix):
        """Setter of matrix of Controlled-Phase gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the matrix of object in ControlledPhase class.')

class Ising(Gate):
    """This class is an inherited class from the Gate class. It’s the implementation of the 
    Ising gate. Its unitary matrix:
    
    """

    @check_gate.Ising_check
    def __init__(self, phi):
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

        Gate.__init__(self)
        # super().set_name('Ising')
        # super().set_matrix(numpy.matrix([
        #     [1, 0, 0, complex(0, -1) * complex(numpy.cos(phi), numpy.sin(phi))],
        #     [0, 1, complex(0, -1), 0],
        #     [0, complex(0, -1), 1, 0],
        #     [complex(0, -1) * complex(numpy.cos(-1 * phi), numpy.sin(-1 * phi)), 0, 0, 1]
        #     ]))
        super(Ising, self).set_name('Ising')
        super(Ising, self).set_matrix(numpy.matrix([
            [1, 0, 0, complex(0, -1) * complex(numpy.cos(phi), numpy.sin(phi))],
            [0, 1, complex(0, -1), 0],
            [0, complex(0, -1), 1, 0],
            [complex(0, -1) * complex(numpy.cos(-1 * phi), numpy.sin(-1 * phi)), 0, 0, 1]
            ]))

    def set_name(self, name):
        """Setter of name of Ising gate. Always raises BaseException.

        Raises:
            BaseException
        """
        
        raise BaseException('Can\'t change the name of object in Ising class.')

    def set_matrix(self, matrix):
        """Setter of matrix of Ising gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the matrix of object in Ising class.')

class Toffoli(Gate):
    """This class is an inherited class from the Gate class. It’s the implementation of the 
    Toffoli gate. It’s called on 3 qubits. The parameters determine which one is the target 
    qubit – 0, 1 or 2.Its unitary matrix:
    
    """

    @check_gate.Toffoli_check
    def __init__(self, target_qubit):
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

        Gate.__init__(self)
        # super().set_name('Toffoli')
        super(Toffoli, self).set_name('Toffoli')
        if target_qubit == 2:
            # super().set_matrix(numpy.matrix([
            #     [1, 0, 0, 0, 0, 0, 0, 0],
            #     [0, 1, 0, 0, 0, 0, 0, 0],
            #     [0, 0, 1, 0, 0, 0, 0, 0],
            #     [0, 0, 0, 1, 0, 0, 0, 0],
            #     [0, 0, 0, 0, 1, 0, 0, 0],
            #     [0, 0, 0, 0, 0, 1, 0, 0],
            #     [0, 0, 0, 0, 0, 0, 0, 1],
            #     [0, 0, 0, 0, 0, 0, 1, 0]
            #     ]))
            super(Toffoli, self).set_matrix(numpy.matrix([
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0]
                ]))

        elif target_qubit == 1:
            # super().set_matrix(numpy.matrix([
            #     [1, 0, 0, 0, 0, 0, 0, 0],
            #     [0, 1, 0, 0, 0, 0, 0, 0],
            #     [0, 0, 1, 0, 0, 0, 0, 0],
            #     [0, 0, 0, 1, 0, 0, 0, 0],
            #     [0, 0, 0, 0, 1, 0, 0, 0],
            #     [0, 0, 0, 0, 0, 0, 0, 1],
            #     [0, 0, 0, 0, 0, 0, 1, 0],
            #     [0, 0, 0, 0, 0, 1, 0, 0]
            #     ]))
            super(Toffoli, self).set_matrix(numpy.matrix([
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0]
                ]))

        else:
            # super().set_matrix(numpy.matrix([
            #     [1, 0, 0, 0, 0, 0, 0, 0],
            #     [0, 1, 0, 0, 0, 0, 0, 0],
            #     [0, 0, 1, 0, 0, 0, 0, 0],
            #     [0, 0, 0, 0, 0, 0, 0, 1],
            #     [0, 0, 0, 0, 1, 0, 0, 0],
            #     [0, 0, 0, 0, 0, 1, 0, 0],
            #     [0, 0, 0, 0, 0, 0, 1, 0],
            #     [0, 0, 0, 1, 0, 0, 0, 0]
            #     ]))
            super(Toffoli, self).set_matrix(numpy.matrix([
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 0]
                ]))

    def set_name(self, name):
        """Setter of name of Toffoli gate. Always raises BaseException.

        Raises:
            BaseException
        """
        
        raise BaseException('Can\'t change the name of object in Toffoli class.')

    def set_matrix(self, matrix):
        """Setter of matrix of Toffoli gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the matrix of object in Toffoli class.')

class Fredkin(Gate):
    """This class is an inherited class from the Gate class. It’s the implementation of the 
    Fredkin gate. It’s called on 3 qubits. The parameters determine which one is the control 
    qubit – 0, 1 or 2.Its unitary matrix:
    
    """

    @check_gate.Fredkin_check
    def __init__(self, control_qubit):
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

        Gate.__init__(self)
        # super().set_name('Fredkin')
        super(Fredkin, self).set_name('Fredkin')
        if control_qubit == 0:
            # super().set_matrix(numpy.matrix([
            #     [1, 0, 0, 0, 0, 0, 0, 0],
            #     [0, 1, 0, 0, 0, 0, 0, 0],
            #     [0, 0, 1, 0, 0, 0, 0, 0],
            #     [0, 0, 0, 1, 0, 0, 0, 0],
            #     [0, 0, 0, 0, 1, 0, 0, 0],
            #     [0, 0, 0, 0, 0, 0, 1, 0],
            #     [0, 0, 0, 0, 0, 1, 0, 0],
            #     [0, 0, 0, 0, 0, 0, 0, 1]
            #     ]))
            super(Fredkin, self).set_matrix(numpy.matrix([
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1]
                ]))

        elif control_qubit == 1:
            # super().set_matrix(numpy.matrix([
            #     [1, 0, 0, 0, 0, 0, 0, 0],
            #     [0, 1, 0, 0, 0, 0, 0, 0],
            #     [0, 0, 1, 0, 0, 0, 0, 0],
            #     [0, 0, 0, 0, 0, 0, 1, 0],
            #     [0, 0, 0, 0, 1, 0, 0, 0],
            #     [0, 0, 0, 0, 0, 1, 0, 0],
            #     [0, 0, 0, 1, 0, 0, 0, 0],
            #     [0, 0, 0, 0, 0, 0, 0, 1]
            #     ]))
            super(Fredkin, self).set_matrix(numpy.matrix([
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1]
                ]))

        else:
            # super().set_matrix(numpy.matrix([
            #     [1, 0, 0, 0, 0, 0, 0, 0],
            #     [0, 1, 0, 0, 0, 0, 0, 0],
            #     [0, 0, 1, 0, 0, 0, 0, 0],
            #     [0, 0, 0, 0, 0, 1, 0, 0],
            #     [0, 0, 0, 0, 1, 0, 0, 0],
            #     [0, 0, 0, 1, 0, 0, 0, 0],
            #     [0, 0, 0, 0, 0, 0, 1, 0],
            #     [0, 0, 0, 0, 0, 0, 0, 1]
            #     ]))
            super(Fredkin, self).set_matrix(numpy.matrix([
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1]
                ]))

    def set_name(self, name):
        """Setter of name of Fredkin gate. Always raises BaseException.

        Raises:
            BaseException
        """
        
        raise BaseException('Can\'t change the name of object in Fredkin class.')

    def set_matrix(self, matrix):
        """Setter of matrix of Fredkin gate. Always raises BaseException.

        Raises:
            BaseException
        """

        raise BaseException('Can\'t change the matrix of object in Fredkin class.')
