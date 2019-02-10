'''
gate class

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
'''

# pylint: disable=E1101

import check_gate
import numpy
import qubit
import register
import unicodedata

class Gate(object):
    ''' gate on qubit class '''

    def __init__(self):
        ''' initialize gate '''

        self.__gate_name = 'Identity'
        self.__gate_matrix = numpy.matrix([
            [1, 0],
            [0, 1]
            ])

    @check_gate.gate_call_check
    def __call__(self, qr):
        ''' call the gate on qubit '''

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
        ''' getter of name of gate '''

        return self.__gate_name
    
    def get_matrix(self):
        ''' getter of matrix of gate '''

        return self.__gate_matrix

    def get_size(self):
        ''' getter of size of gate's matrix '''

        return self.__gate_matrix.shape[0]
    
    @check_gate.set_name_check
    def set_name(self, name):
        ''' setter of name of gate '''

        self.__gate_name = str(name)

    @check_gate.set_matrix_check
    def set_matrix(self, matrix):
        ''' setter of matrix of gate's matrix '''
    
        self.__gate_matrix = matrix
    
    @check_gate.power_check
    def power(self, power):
        ''' raise the matrix of gate to the given power '''

        self.__gate_matrix = numpy.linalg.matrix_power(self.__gate_matrix, power)

class Hadamard(Gate):
    ''' Hadamard gate class '''

    def __init__(self):
        ''' initialize Hadamard gate '''

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
        ''' setter of name of gate '''

        raise BaseException('Can\'t change the name of object in Hadamard class.')
    
    def set_matrix(self, matrix):
        ''' setter of matrix of Hadamard gate's matrix '''

        raise BaseException('Can\'t change the matrix of object in Hadamard class.')

class SquareNot(Gate):
    ''' Square-Not gate class '''

    def __init__(self):
        ''' initialize Square-Not gate '''

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
        ''' setter of name of gate '''

        raise BaseException('Can\'t change the name of object in SquareNot class.')
    
    def set_matrix(self, matrix):
        ''' setter of matrix of Square-Not gate's matrix '''

        raise BaseException('Can\'t change the matrix of object in SquareNot class.')

class PauliX(Gate):
    ''' Pauli-X gate class '''

    def __init__(self):
        ''' initialize Pauli-X gate '''

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
        ''' setter of name of gate '''

        raise BaseException('Can\'t change the name of object in PauliX class.')
    
    def set_matrix(self, matrix):
        ''' setter of matrix of Pauli-X gate's matrix '''

        raise BaseException('Can\'t change the matrix of object in PauliX class.')

class PauliY(Gate):
    ''' Pauli-Y gate class '''

    def __init__(self):
        ''' initialize Pauli-Y gate '''

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
        ''' setter of name of gate '''

        raise BaseException('Can\'t change the name of object in PauliY class.')
    
    def set_matrix(self, matrix):
        ''' setter of matrix of Pauli-Y gate's matrix '''

        raise BaseException('Can\'t change the matrix of object in PauliY class.')

class PauliZ(Gate):
    ''' Pauli-Z gate class '''

    def __init__(self):
        ''' initialize Pauli-Z gate '''

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
        ''' setter of name of gate '''

        raise BaseException('Can\'t change the name of object in PauliZ class.')
    
    def set_matrix(self, matrix):
        ''' setter of matrix of Pauli-Z gate's matrix '''

        raise BaseException('Can\'t change the matrix of object in PauliZ class.')

class Phase(Gate):
    ''' Phase gate class '''

    def __init__(self):
        ''' initialize Phase gate '''

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
        ''' setter of name of gate '''

        raise BaseException('Can\'t change the name of object in Phase class.')
    
    def set_matrix(self, matrix):
        ''' setter of matrix of Phase gate's matrix '''

        raise BaseException('Can\'t change the matrix of object in Phase class.')

class Pi8(Gate):
    ''' Pi/8 gate class '''

    def __init__(self):
        ''' initialize Pi/8 gate '''

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
        ''' setter of name of gate '''

        raise BaseException('Can\'t change the name of object in Pi8 class.')
    
    def set_matrix(self, matrix):
        ''' setter of matrix of Pi8 gate's matrix '''

        raise BaseException('Can\'t change the matrix of object in Pi8 class.')

class Swap(Gate):
    ''' Swap gate class '''

    def __init__(self):
        ''' initialize Swap gate '''

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
        ''' setter of name of gate '''

        raise BaseException('Can\'t change the name of object in Swap class.')
    
    def set_matrix(self, matrix):
        ''' setter of matrix of Swap gate's matrix '''

        raise BaseException('Can\'t change the matrix of object in Swap class.')

class SquareSwap(Gate):
    ''' Square-Swap gate class '''

    def __init__(self):
        ''' initialize Square-Swap gate '''

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
        ''' setter of name of gate '''

        raise BaseException('Can\'t change the name of object in SquareSwap class.')
    
    def set_matrix(self, matrix):
        ''' setter of matrix of Square-Swap gate's matrix '''

        raise BaseException('Can\'t change the matrix of object in SquareSwap class.')

class CNOT(Gate):
    ''' Controlled-Not gate class '''

    @check_gate.CNOT_check
    def __init__(self, control_qubit, target_qubit):
        ''' initialize Controlled-Not gate '''

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
        ''' setter of name of gate '''
        
        raise BaseException('Can\'t change the name of object in CNOT class.')

    def set_matrix(self, matrix):
        ''' setter of matrix of Controlled-Not gate's matrix '''

        raise BaseException('Can\'t change the matrix of object in CNOT class.')

class ControlledZ(Gate):
    ''' Controlled-Z gate class '''

    def __init__(self):
        ''' initialize Controlled-Z gate '''

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
        ''' setter of name of gate '''
        
        raise BaseException('Can\'t change the name of object in ControlledZ class.')

    def set_matrix(self, matrix):
        ''' setter of matrix of Controlled-Z gate's matrix '''

        raise BaseException('Can\'t change the matrix of object in ControlledZ class.')

class ControlledPhase(Gate):
    ''' Controlled-Phase gate class '''

    def __init__(self):
        ''' initialize Controlled-Phase gate '''

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
        ''' setter of name of gate '''
        
        raise BaseException('Can\'t change the name of object in ControlledPhase class.')

    def set_matrix(self, matrix):
        ''' setter of matrix of Controlled-Phase gate's matrix '''

        raise BaseException('Can\'t change the matrix of object in ControlledPhase class.')

class Ising(Gate):
    ''' Ising gate class '''

    @check_gate.Ising_check
    def __init__(self, phi):
        ''' initialize Ising gate '''

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
        ''' setter of name of gate '''
        
        raise BaseException('Can\'t change the name of object in Ising class.')

    def set_matrix(self, matrix):
        ''' setter of matrix of Ising gate's matrix '''

        raise BaseException('Can\'t change the matrix of object in Ising class.')

class Toffoli(Gate):
    ''' Toffoli gate class '''

    @check_gate.Toffoli_check
    def __init__(self, target_qubit):
        ''' initialize Toffoli gate '''

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
        ''' setter of name of gate '''
        
        raise BaseException('Can\'t change the name of object in Toffoli class.')

    def set_matrix(self, matrix):
        ''' setter of matrix of Toffoli gate's matrix '''

        raise BaseException('Can\'t change the matrix of object in Toffoli class.')

class Fredkin(Gate):
    ''' Fredkin gate class '''

    @check_gate.Fredkin_check
    def __init__(self, control_qubit):
        ''' initialize Fredkin gate '''

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
        ''' setter of name of gate '''
        
        raise BaseException('Can\'t change the name of object in Fredkin class.')

    def set_matrix(self, matrix):
        ''' setter of matrix of Fredkin gate's matrix '''

        raise BaseException('Can\'t change the matrix of object in Fredkin class.')
