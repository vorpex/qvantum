'''
Gate class

"In quantum computing and specifically the quantum circuit model of computation, a quantum logic
gate is a basic quantum circuit operating on a small number of qubits. They are the building blocks
of quantum circuits, like classical logic gates are for conventional digital circuits.

Quantum logic gates are represented by unitary matrices. The most common quantum gates operate on
spaces of one or two qubits, just like the common classical logic gates operate on one or two bits.
As matrices, quantum gates can be described by 2^n x 2^n sized unitary matrices, where n is the
number of qubits that the gate act on. The variables that the gates act upon, the quantum states,
are vectors in 2^n complex dimensions, where n again is the number of qubits of the variable:
The base vectors are the possible outcomes if measured, and a quantum state is a linear combination
of these outcomes."

via Wikipedia: https://en.wikipedia.org/wiki/Quantum_logic_gate

The instances of the Gate class have the following methods:

- __init__()      - initialization method
- __call__()      - call method
- get_name()      - getter of the name of the gate
- get_matrix()    - getter of the matrix of the gate
- get_size()      - getter of the size of the matrix of the gate
- set_name()      - setter of the name of the gate
- set_matrix()    - setter of the matrix of the gate
- unitary_check() - method to check whether the matrix of the gate is unitary or not
- power()         - raise the matrix of the gate to the given power
'''

# pylint: disable=E1101

import math
import numpy
import Qubit
import Register
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

    def __call__(self, qr):
        ''' call the gate on qubit '''

        if isinstance(qr, Qubit.Qubit) and self.get_size() == 2:
            vector = self.__gate_matrix * qr.ket()
            qr.set_amplitudes(vector.item(0), vector.item(1))
        
        elif isinstance(qr, Register.Register) and self.get_size() == qr.get_state_number():
            vector = numpy.asarray(self.__gate_matrix * qr.ket()).flatten()
            qr.set_amplitudes(vector)
        
        else:
            raise ValueError('Invalid input! Use Qubit or Register as input with the same size ' +\
            'as the gate')

    def get_name(self):
        ''' getter of the name of the gate '''

        return self.__gate_name
    
    def get_matrix(self):
        ''' getter of the matrix of the gate '''

        return self.__gate_matrix

    def get_size(self):
        ''' getter of the size of the gate's matrix '''

        return self.__gate_matrix.shape[0]
    
    def set_name(self, name):
        ''' setter of the name of the gate '''

        self.__gate_name = str(name)

    def set_matrix(self, matrix):
        ''' setter of the matrix of the gate's matrix '''
    
        if matrix.shape[0] == matrix.shape[1]:
            IDENTITY = numpy.identity(matrix.shape[0])
            MATRIX = matrix * matrix.conjugate().transpose()
            if numpy.array_equal(MATRIX.round(10), IDENTITY):
                self.__gate_matrix = matrix

            else:
                raise ValueError('Invalid input! Matrix is not unitary. ' +\
                'Please use an unitary matrix.')
        
        else:
            raise ValueError('Invalid input! Please use symmetric matrix.')

    def unitary_check(self):
        ''' checking if the matrix of the gate is unitary '''

        IDENTITY = numpy.identity(self.__gate_matrix.shape[0])
        MATRIX = self.__gate_matrix * self.__gate_matrix.conjugate().transpose()
        if numpy.array_equal(MATRIX.round(10), IDENTITY):
            return 1
        
        else:
            return 0
    
    def power(self, power):
        ''' raise the matrix of the gate to the given power '''

        self.__gate_matrix = numpy.linalg.matrix_power(self.__gate_matrix, power)

class Hadamard(Gate):
    ''' Hadamard gate class '''

    def __init__(self):
        ''' initialize Hadamard gate '''

        Gate.__init__(self)
        # super().set_name('Hadamard')
        # super().set_matrix(numpy.matrix([
        #     [1 / math.sqrt(2), 1 / math.sqrt(2)],
        #     [1 / math.sqrt(2), -1 / math.sqrt(2)]
        #     ]))
        super(Hadamard, self).set_name('Hadamard')
        super(Hadamard, self).set_matrix(numpy.matrix([
            [1 / math.sqrt(2), 1 / math.sqrt(2)],
            [1 / math.sqrt(2), -1 / math.sqrt(2)]
            ]))
    
    def set_name(self, name):
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Hadamard gate's matrix '''

        pass

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
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Square-Not gate's matrix '''

        pass

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
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Pauli-X gate's matrix '''

        pass

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
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Pauli-Y gate's matrix '''

        pass

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
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Pauli-Z gate's matrix '''

        pass

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
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Phase gate's matrix '''

        pass

class Pi8(Gate):
    ''' Pi/8 gate class '''

    def __init__(self):
        ''' initialize Pi/8 gate '''

        Gate.__init__(self)
        # super().set_name(unicodedata.lookup('GREEK SMALL LETTER PI') + '/8')
        # super().set_matrix(numpy.matrix([
        #     [1, 0],
        #     [0, complex(math.cos(math.pi/4), math.sin(math.pi/4))]
        #     ]))
        super(Pi8, self).set_name(unicodedata.lookup('GREEK SMALL LETTER PI') + '/8')
        super(Pi8, self).set_matrix(numpy.matrix([
            [1, 0],
            [0, complex(math.cos(math.pi/4), math.sin(math.pi/4))]
            ]))
    
    def set_name(self, name):
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Pi8 gate's matrix '''

        pass

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
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Swap gate's matrix '''

        pass

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
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Square-Swap gate's matrix '''

        pass

class CNOT(Gate):
    ''' Controlled-Not gate class '''

    def __init__(self, control_qubit, target_qubit):
        ''' initialize Controlled-Not gate '''

        if (control_qubit == 0 and target_qubit == 1) \
        or (control_qubit == 1 and target_qubit == 0):
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

        else:
            raise ValueError('Invalid input! Use number 0 and 1 to mark the control ' +\
            'and target Qubit. (0, 1): 1st Qubit is the control and 2nd is the target. ' +\
            '(1, 0): 2nd Qubit is the control and 1st is the target.')

    def set_name(self, name):
        ''' setter of the name of the gate '''
        
        pass

    def set_matrix(self, matrix):
        ''' setter of the matrix of the Controlled-Not gate's matrix '''

        pass

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
        ''' setter of the name of the gate '''
        
        pass

    def set_matrix(self, matrix):
        ''' setter of the matrix of the Controlled-Z gate's matrix '''

        pass

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
        ''' setter of the name of the gate '''
        
        pass

    def set_matrix(self, matrix):
        ''' setter of the matrix of the Controlled-Phase gate's matrix '''

        pass

class Ising(Gate):
    ''' Ising gate class '''

    def __init__(self, phi):
        ''' initialize Ising gate '''

        Gate.__init__(self)
        # super().set_name('Ising')
        # super().set_matrix(numpy.matrix([
        #     [1, 0, 0, complex(0, -1) * complex(math.cos(phi), math.sin(phi))],
        #     [0, 1, complex(0, -1), 0],
        #     [0, complex(0, -1), 1, 0],
        #     [complex(0, -1) * complex(math.cos(-1 * phi), math.sin(-1 * phi)), 0, 0, 1]
        #     ]))
        super(Ising, self).set_name('Ising')
        super(Ising, self).set_matrix(numpy.matrix([
            [1, 0, 0, complex(0, -1) * complex(math.cos(phi), math.sin(phi))],
            [0, 1, complex(0, -1), 0],
            [0, complex(0, -1), 1, 0],
            [complex(0, -1) * complex(math.cos(-1 * phi), math.sin(-1 * phi)), 0, 0, 1]
            ]))

    def set_name(self, name):
        ''' setter of the name of the gate '''
        
        pass

    def set_matrix(self, matrix):
        ''' setter of the matrix of the Ising gate's matrix '''

        pass

class Toffoli(Gate):
    ''' Toffoli gate class '''

    def __init__(self, target_qubit):
        ''' initialize Toffoli gate '''

        if target_qubit == 0 or target_qubit == 1 or target_qubit == 2:
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

        else:
            raise ValueError('Invalid input! Use number 0, 1, and 2 to mark the target Qubit. ' +\
            '0: 1st Qubit is the target. 1: 2nd Qubit is the target. 2: 3rd Qubit is the target.')

    def set_name(self, name):
        ''' setter of the name of the gate '''
        
        pass

    def set_matrix(self, matrix):
        ''' setter of the matrix of the Toffoli gate's matrix '''

        pass

class Fredkin(Gate):
    ''' Fredkin gate class '''

    def __init__(self, control_qubit):
        ''' initialize Fredkin gate '''

        if control_qubit == 0 or control_qubit == 1 or control_qubit == 2:
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

        else:
            raise ValueError('Invalid input! Use number 0, 1, and 2 to mark the control Qubit. ' +\
            '0: 1st Qubit is the control. 1: 2nd Qubit is the control. ' +\
            '2: 3rd Qubit is the control.')

    def set_name(self, name):
        ''' setter of the name of the gate '''
        
        pass

    def set_matrix(self, matrix):
        ''' setter of the matrix of the Fredkin gate's matrix '''

        pass
