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

import logging
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

    def __call__(self, qubit):
        ''' call the gate on qubit '''

        if isinstance(qubit, Qubit.Qubit) and self.__gate_matrix.shape[0] == 2:
            vector = self.__gate_matrix * qubit.ket()
            qubit.set_parameters(vector.item(0), vector.item(1))
        
        else:
            logging.warning('Invalid input! Not in Qubit class. ' +\
            'Please use instance of Qubit class.')

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
    
        if isinstance(matrix, numpy.ndarray):
            if matrix.shape[0] == matrix.shape[1]:
                IDENTITY = numpy.identity(matrix.shape[0])
                MATRIX = matrix * matrix.conjugate().transpose()
                if numpy.array_equal(MATRIX.round(10), IDENTITY):
                    self.__gate_matrix = matrix

                else:
                    logging.warning('The matrix is not unitary! Please use a unitary matrix.')
            
            else:
                logging.warning('Invalid input! Matrix is not symmetric. ' +\
                'Please use symmetric matrix.')

        else:
           logging.warning('Invalid input! Not numpy matrix. Please use numpy.ndarray.') 

    def unitary_check(self):
        ''' checking if the matrix of the gate is unitary '''

        IDENTITY = numpy.identity(self.__gate_matrix.shape[0])
        MATRIX = self.__gate_matrix * self.__gate_matrix.conjugate().transpose()
        if numpy.array_equal(MATRIX.round(10), IDENTITY):
            print('The matrix is unitary.')
            return 1
        
        else:
            logging.warning('The matrix is not unitary! Please use a unitary matrix.')
            return 0

    def power(self, power):
        ''' raise the matrix of the gate to the given power '''

        if isinstance(power, int):
            self.__gate_matrix = numpy.linalg.matrix_power(self.__gate_matrix, power)

        else:
            logging.warning('Invalid input! The power must be the type of integer.')

class GateR(Gate):
    ''' gate on register class '''

    def __init__(self):
        ''' initialize gate '''

        Gate.__init__(self)
        super(GateR, self).set_matrix(numpy.matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
            ]))
    
    def __call__(self, register):
        ''' call the gate on register '''

        if isinstance(register, Register.Register) and \
        register.get_state_nr() == self.get_size():
            vector = numpy.asarray(self.get_matrix() * register.ket()).flatten()
            register.set_parameters(vector)

        else:
            logging.warning('Invalid input! User object of Register class as argument. ' +\
            'Size of Register and Gate must be equal.')

class Hadamard(Gate):
    ''' Hadamard gate class '''

    def __init__(self):
        ''' initialize Hadamard gate '''

        Gate.__init__(self)
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
        super(Swap, self).set_name('Swap')
        super(Swap, self).set_matrix(numpy.matrix([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
            ]))
    
    def __call__(self, register):
        ''' call the gate on register '''

        if isinstance(register, Register.Register) and register.get_qubit_nr() == 2:
            vector = numpy.asarray(self.get_matrix() * register.ket()).flatten()
            register.set_parameters(vector)

        else:
            logging.warning('Invalid input! Argument must be Register of two Qubits.')
    
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
        super(SquareSwap, self).set_name('Square-Swap')
        super(SquareSwap, self).set_matrix(numpy.matrix([
            [1, 0, 0, 0],
            [0, (1 + complex(0, 1)) / 2, (1 - complex(0, 1)) / 2, 0],
            [0, (1 - complex(0, 1)) / 2, (1 + complex(0, 1)) / 2, 0],
            [0, 0, 0, 1]
            ]))
    
    def __call__(self, register):
        ''' call the gate on register '''

        if isinstance(register, Register.Register) and register.get_qubit_nr() == 2:
            vector = numpy.asarray(self.get_matrix() * register.ket()).flatten()
            register.set_parameters(vector)

        else:
            logging.warning('Invalid input! Argument must be Register of two Qubits.')
    
    def set_name(self, name):
        ''' setter of the name of the gate '''

        pass
    
    def set_matrix(self, matrix):
        ''' setter of the matrix of the Square-Swap gate's matrix '''

        pass

class CNOT(Gate):
    ''' Controlled-Not gate class '''

    def __init__(self, control_qubit=None, target_qubit=None):
        ''' initialize Controlled-Not gate '''

        if (control_qubit == 1 and target_qubit == 2) or \
        (control_qubit == 2 and target_qubit == 1) or \
        (control_qubit == None and target_qubit == None):
            if control_qubit is None and target_qubit is None:
                control_qubit = 1
                target_qubit = 2
                logging.warning('Control and target Qubit are None then the 1st is the control ' +\
                'and the 2nd is the target.')

            else:
                pass

            Gate.__init__(self)
            super(CNOT, self).set_name('Controlled-Not')
            if control_qubit == 1 and target_qubit == 2:
                super(CNOT, self).set_matrix(numpy.matrix([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 1],
                [0, 0, 1, 0]
                ]))

            else:
                super(CNOT, self).set_matrix(numpy.matrix([
                [1, 0, 0, 0],
                [0, 0, 0, 1],
                [0, 0, 1, 0],
                [0, 1, 0, 0]
                ]))

        else:
            logging.warning('Invalid input! Use number 1, 2 (or both None) to mark the control ' +\
            'and target Qubit.')

    def __call__(self, register):
        ''' call the gate on register '''

        if isinstance(register, Register.Register) and register.get_qubit_nr() == 2:            
            vector = numpy.asarray(self.get_matrix() * register.ket()).flatten()
            register.set_parameters(vector)

        else:
            logging.warning('Invalid input! Argument must be Register of two Qubits.')

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
        super(ControlledZ, self).set_name('Controlled-Z')
        super(ControlledZ, self).set_matrix(numpy.matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, -1]
            ]))

    def __call__(self, register):
        ''' call the gate on register '''

        if isinstance(register, Register.Register) and register.get_qubit_nr() == 2:            
            vector = numpy.asarray(self.get_matrix() * register.ket()).flatten()
            register.set_parameters(vector)

        else:
            logging.warning('Invalid input! Argument must be Register of two Qubits.')

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
        super(ControlledPhase, self).set_name('Controlled-Phase')
        super(ControlledPhase, self).set_matrix(numpy.matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, complex(0, 1)]
            ]))

    def __call__(self, register):
        ''' call the gate on register '''

        if isinstance(register, Register.Register) and register.get_qubit_nr() == 2:            
            vector = numpy.asarray(self.get_matrix() * register.ket()).flatten()
            register.set_parameters(vector)

        else:
            logging.warning('Invalid input! Argument must be Register of two Qubits.')

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

        if isinstance(phi, (int, long, float)):
            Gate.__init__(self)
            super(Ising, self).set_name('Ising')
            super(Ising, self).set_matrix(numpy.matrix([
                [1, 0, 0, complex(0, -1) * complex(math.cos(phi), math.sin(phi))],
                [0, 1, complex(0, -1), 0],
                [0, complex(0, -1), 1, 0],
                [complex(0, -1) * complex(math.cos(-1 * phi), math.sin(-1 * phi)), 0, 0, 1]
                ]))

        else:
            logging.warning('Invalid input! Give the phase as argument in radian. ' +\
            'Use int, long or float type.')

    def __call__(self, register):
        ''' call the gate on register '''

        if isinstance(register, Register.Register) and register.get_qubit_nr() == 2:            
            vector = numpy.asarray(self.get_matrix() * register.ket()).flatten()
            register.set_parameters(vector)

        else:
            logging.warning('Invalid input! Argument must be Register of two Qubits.')

    def set_name(self, name):
        ''' setter of the name of the gate '''
        
        pass

    def set_matrix(self, matrix):
        ''' setter of the matrix of the Ising gate's matrix '''

        pass

class Toffoli(Gate):
    ''' Toffoli gate class '''

    def __init__(self, target_qubit=None):
        ''' initialize Toffoli gate '''

        if target_qubit is None or \
        target_qubit == 1 or target_qubit == 2 or target_qubit == 3:
            if target_qubit is None:
                target_qubit = 3
                logging.warning('Target Qubit is None then the 1st and 2nd are ' +\
                'the controls and the 3rd is the target.')

            else:
                pass

            Gate.__init__(self)
            super(Toffoli, self).set_name('Toffoli')
            if target_qubit == 3:
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

            elif target_qubit == 2:
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
            logging.warning('Invalid input! Use number 1, 2, 3 (or None) to mark the ' +\
            'target Qubit.')

    def __call__(self, register):
        ''' call the gate on register '''

        if isinstance(register, Register.Register) and register.get_qubit_nr() == 3:            
            vector = numpy.asarray(self.get_matrix() * register.ket()).flatten()
            register.set_parameters(vector)

        else:
            logging.warning('Invalid input! Argument must be Register of three Qubits.')

    def set_name(self, name):
        ''' setter of the name of the gate '''
        
        pass

    def set_matrix(self, matrix):
        ''' setter of the matrix of the Toffoli gate's matrix '''

        pass

class Fredkin(Gate):
    ''' Fredkin gate class '''

    def __init__(self, control_qubit=None):
        ''' initialize Fredkin gate '''

        if control_qubit is None or \
        control_qubit == 1 or control_qubit == 2 or control_qubit == 3:
            if control_qubit is None:
                control_qubit = 1
                logging.warning('Control Qubit is None then the 2nd and 3rd are ' +\
                'the targets and the 1st is the control.')

            else:
                pass

            Gate.__init__(self)
            super(Fredkin, self).set_name('Fredkin')
            if control_qubit == 1:
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

            elif control_qubit == 2:
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
            logging.warning('Invalid input! Use number 1, 2, 3 (or None) to mark the ' +\
            'control Qubit.')

    def __call__(self, register):
        ''' call the gate on register '''

        if isinstance(register, Register.Register) and register.get_qubit_nr() == 3:            
            vector = numpy.asarray(self.get_matrix() * register.ket()).flatten()
            register.set_parameters(vector)

        else:
            logging.warning('Invalid input! Argument must be Register of three Qubits.')

    def set_name(self, name):
        ''' setter of the name of the gate '''
        
        pass

    def set_matrix(self, matrix):
        ''' setter of the matrix of the Fredkin gate's matrix '''

        pass
