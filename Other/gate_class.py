''' gate class '''

# pylint: disable=E1601
import math
import qubit_class as qubit
import register_class as register

class Gate(object):
    ''' pred-defined gate class '''
    def __init__(self, name):
        ''' initialize gate '''
        self.pre_defined_gates = ['Hadamard', 'Pauli-X', 'Pauli-Y', 'Pauli-Z', 'Phase', 'Pi/8', \
        'C-NOT', 'Swap', 'Controlled-Z', 'Controlled-Phase', 'Toffoli', 'Fredkin']
        if isinstance(name, str) and name in self.pre_defined_gates:
            self.name = name
        else:
            print 'To create gate choose an option and try again: ' + self.pre_defined_gates

    def gate_qubit_effect(self, QUBIT):
        ''' call the matching gate on QUBIT '''
        if isinstance(QUBIT, qubit.Qubit):
            if self.name == 'Hadamard':
                return self.hadamard(QUBIT)
            if self.name == 'Pauli-X':
                return self.pauli_x(QUBIT)
            if self.name == 'Pauli-Y':
                return self.pauli_y(QUBIT)
            if self.name == 'Pauli-Z':
                return self.pauli_z(QUBIT)
            if self.name == 'Phase':
                return self.phase(QUBIT)
            if self.name == 'Pi/8':
                return self.pi8(QUBIT)
        else:
            return 'Wrong argument: not in qubit class!'

    def gate_register_effect(self, REGISTER, control=None):
        ''' call the matching gate on REGISTER '''
        if isinstance(REGISTER, register.Register):
            if self.name == 'C-NOT':
                return self.c_not(REGISTER, control)
            if self.name == 'Swap':
                return self.swap(REGISTER)
            if self.name == 'Controlled-Z':
                return self.controlled_z(REGISTER, control)
            if self.name == 'Controlled-Phase':
                return self.controlled_phase(REGISTER, control)
            if self.name == 'Toffoli':
                return self.toffoli(REGISTER, control)
            if self.name == 'Fredkin':
                return self.fredkin(REGISTER, control)
        else:
            return 'Wrong argument: not in register class!'

    def hadamard(self, QUBIT):
        ''' Hadamard gate '''
        alfa_new = (QUBIT.alfa + QUBIT.beta) / math.sqrt(2)
        beta_new = (QUBIT.alfa - QUBIT.beta) / math.sqrt(2)
        QUBIT.alfa = alfa_new
        QUBIT.beta = beta_new
        return QUBIT

    def pauli_x(self, QUBIT):
        ''' Pauli-X gate '''
        alfa_new = QUBIT.beta
        beta_new = QUBIT.alfa
        QUBIT.alfa = alfa_new
        QUBIT.beta = beta_new
        return QUBIT

    def pauli_y(self, QUBIT):
        ''' Pauli-Y gate '''
        alfa_new = QUBIT.beta * complex(0, -1)
        beta_new = QUBIT.alfa * complex(0, 1)
        QUBIT.alfa = alfa_new
        QUBIT.beta = beta_new
        return QUBIT

    def pauli_z(self, QUBIT):
        ''' Pauli-Z gate '''
        alfa_new = QUBIT.alfa
        beta_new = QUBIT.beta * -1
        QUBIT.alfa = alfa_new
        QUBIT.beta = beta_new
        return QUBIT

    def phase(self, QUBIT):
        ''' Phase gate '''
        alfa_new = QUBIT.alfa
        beta_new = QUBIT.beta * complex(0, 1)
        QUBIT.alfa = alfa_new
        QUBIT.beta = beta_new
        return QUBIT

    def pi8(self, QUBIT):
        ''' Pi/8 gate '''
        alfa_new = QUBIT.alfa
        beta_new = QUBIT.beta * complex(math.cos(math.pi/4), math.sin(math.pi/4))
        QUBIT.alfa = alfa_new
        QUBIT.beta = beta_new
        return QUBIT

    def c_not(self, REGISTER, control=None):
        ''' C-NOT gate '''
        if control is None:
            control = 1

        if len(REGISTER.coeffs_list) != 2 ** len(REGISTER.register):
            REGISTER.coeffs()
        else:
            pass

        if control == 1:
            flip1 = REGISTER.coeffs_list[3]
            flip2 = REGISTER.coeffs_list[2]
            REGISTER.replace_coeff(flip1, 3)
            REGISTER.replace_coeff(flip2, 4)
        else:
            flip1 = REGISTER.coeffs_list[1]
            flip2 = REGISTER.coeffs_list[3]
            REGISTER.replace_coeff(flip1, 4)
            REGISTER.replace_coeff(flip2, 2)

        return REGISTER

    def swap(self, REGISTER):
        ''' Swap gate '''
        if len(REGISTER.coeffs_list) != 2 ** len(REGISTER.register):
            REGISTER.coeffs()
        else:
            pass

        flip1 = REGISTER.coeffs_list[2]
        flip2 = REGISTER.coeffs_list[1]
        REGISTER.replace_coeff(flip1, 2)
        REGISTER.replace_coeff(flip2, 3)
        return REGISTER

    def controlled_z(self, REGISTER, control=None):
        ''' C-NOT gate '''
        if control is None:
            control = 1

        if len(REGISTER.coeffs_list) != 2 ** len(REGISTER.register):
            REGISTER.coeffs()
        else:
            pass

        if control == 1:
            flip1 = REGISTER.coeffs_list[3] * -1
            REGISTER.replace_coeff(flip1, 4)
        else:
            flip1 = REGISTER.coeffs_list[1] * -1
            REGISTER.replace_coeff(flip1, 2)

        return REGISTER

    def controlled_phase(self, REGISTER, control=None):
        ''' C-NOT gate '''
        if control is None:
            control = 1

        if len(REGISTER.coeffs_list) != 2 ** len(REGISTER.register):
            REGISTER.coeffs()
        else:
            pass

        if control == 1:
            flip1 = REGISTER.coeffs_list[3] * complex(0, 1)
            REGISTER.replace_coeff(flip1, 4)
        else:
            flip1 = REGISTER.coeffs_list[1] * complex(0, 1)
            REGISTER.replace_coeff(flip1, 2)

        return REGISTER

    def toffoli(self, REGISTER, control=None):
        ''' Toffoli gate '''
        if control is None:
            control = 3

        if len(REGISTER.coeffs_list) != 2 ** len(REGISTER.register):
            REGISTER.coeffs()
        else:
            pass

        if control == 3:
            flip1 = REGISTER.coeffs_list[6]
            flip2 = REGISTER.coeffs_list[7]
            REGISTER.replace_coeff(flip1, 8)
            REGISTER.replace_coeff(flip2, 7)
        elif control == 1:
            flip1 = REGISTER.coeffs_list[3]
            flip2 = REGISTER.coeffs_list[7]
            REGISTER.replace_coeff(flip1, 8)
            REGISTER.replace_coeff(flip2, 4)
        else:
            flip1 = REGISTER.coeffs_list[5]
            flip2 = REGISTER.coeffs_list[7]
            REGISTER.replace_coeff(flip1, 8)
            REGISTER.replace_coeff(flip2, 6)

        return REGISTER

    def fredkin(self, REGISTER, control=None):
        ''' Toffoli gate '''
        if control is None:
            control = 1

        if len(REGISTER.coeffs_list) != 2 ** len(REGISTER.register):
            REGISTER.coeffs()
        else:
            pass

        if control == 1:
            flip1 = REGISTER.coeffs_list[5]
            flip2 = REGISTER.coeffs_list[6]
            REGISTER.replace_coeff(flip1, 7)
            REGISTER.replace_coeff(flip2, 6)
        elif control == 2:
            flip1 = REGISTER.coeffs_list[3]
            flip2 = REGISTER.coeffs_list[6]
            REGISTER.replace_coeff(flip1, 7)
            REGISTER.replace_coeff(flip2, 4)
        else:
            flip1 = REGISTER.coeffs_list[3]
            flip2 = REGISTER.coeffs_list[5]
            REGISTER.replace_coeff(flip1, 6)
            REGISTER.replace_coeff(flip2, 4)

        return REGISTER

# H = Gate('Hadamard')
# q = qubit.Qubit(0, 1)
# print q.show()
# H.gate_qubit_effect(q)
# print q.show()

# X = Gate('Pauli-X')
# q = qubit.Qubit()
# print q.show()
# X.gate_qubit_effect(q)
# print q.show()

# Y = Gate('Pauli-Y')
# q = qubit.Qubit(1, 0)
# print q.show()
# Y.gate_qubit_effect(q)
# print q.show()

# Z = Gate('Pauli-Z')
# q = qubit.Qubit()
# print q.show()
# Z.gate_qubit_effect(q)
# print q.show()

# S = Gate('Phase')
# q = qubit.Qubit(1/math.sqrt(2), 1/math.sqrt(2))
# print q.show()
# S.gate_qubit_effect(q)
# print q.show()

# T = Gate('Pi/8')
# q = qubit.Qubit(0, 1)
# print q.show()
# T.gate_qubit_effect(q)
# print q.show()

# CNOT = Gate('C-NOT')
# r = register.Register(0)
# r.add_qubit(qubit.Qubit(1/math.sqrt(2), 1/math.sqrt(2)))
# r.add_qubit(qubit.Qubit(1, 0))
# print r.show()
# CNOT.gate_register_effect(r)
# print r.show()

# SWAP = Gate('Swap')
# r = register.Register(2)
# print r.show()
# SWAP.gate_register_effect(r)
# print r.show()

##### C-NOT vs Swap - TEST1 #####
# CNOT = Gate('C-NOT')
# r = register.Register(0)
# r.add_qubit(qubit.Qubit(1, 0))
# r.add_qubit(qubit.Qubit(0, 1))
# print r.show()
# CNOT.gate_register_effect(r, 1)
# print r.show()
# CNOT.gate_register_effect(r, 2)
# print r.show()
# CNOT.gate_register_effect(r, 1)
# print r.show()
# print '\n'

# SWAP = Gate('Swap')
# r = register.Register(0)
# r.add_qubit(qubit.Qubit(1, 0))
# r.add_qubit(qubit.Qubit(0, 1))
# print r.show()
# SWAP.gate_register_effect(r)
# print r.show()
##### TEST1 #####

##### C-NOT vs Swap - TEST2 #####
# q1 = qubit.Qubit()
# q2 = qubit.Qubit()

# CNOT = Gate('C-NOT')
# r = register.Register(0)
# r.add_qubit(q1)
# r.add_qubit(q2)
# print r.show()
# CNOT.gate_register_effect(r, 1)
# print r.show()
# CNOT.gate_register_effect(r, 2)
# print r.show()
# CNOT.gate_register_effect(r, 1)
# print r.show()
# print '\n'

# SWAP = Gate('Swap')
# r = register.Register(0)
# r.add_qubit(q1)
# r.add_qubit(q2)
# print r.show()
# SWAP.gate_register_effect(r)
# print r.show()
##### TEST2 #####

# q1 = qubit.Qubit()
# q2 = qubit.Qubit()

# CZ = Gate('Controlled-Z')
# r = register.Register(0)
# r.add_qubit(q1)
# r.add_qubit(q2)
# print r.show()
# CZ.gate_register_effect(r, 1)
# print r.show()

# CZ = Gate('Controlled-Z')
# r = register.Register(0)
# r.add_qubit(q1)
# r.add_qubit(q2)
# print r.show()
# CZ.gate_register_effect(r, 2)
# print r.show()

# q1 = qubit.Qubit()
# q2 = qubit.Qubit()

# CP = Gate('Controlled-Phase')
# r = register.Register(0)
# r.add_qubit(q1)
# r.add_qubit(q2)
# print r.show()
# CP.gate_register_effect(r, 1)
# print r.show()

# CP = Gate('Controlled-Phase')
# r = register.Register(0)
# r.add_qubit(q1)
# r.add_qubit(q2)
# print r.show()
# CP.gate_register_effect(r, 2)
# print r.show()

# q1 = qubit.Qubit()
# q2 = qubit.Qubit()
# q3 = qubit.Qubit()

# TOFF = Gate('Toffoli')
# r = register.Register(0)
# r.add_qubit(q1)
# r.add_qubit(q2)
# r.add_qubit(q3)
# print r.show()
# TOFF.gate_register_effect(r, 3)
# print r.show()

# TOFF = Gate('Toffoli')
# r = register.Register(0)
# r.add_qubit(q1)
# r.add_qubit(q2)
# r.add_qubit(q3)
# print r.show()
# TOFF.gate_register_effect(r, 2)
# print r.show()

# TOFF = Gate('Toffoli')
# r = register.Register(0)
# r.add_qubit(q1)
# r.add_qubit(q2)
# r.add_qubit(q3)
# print r.show()
# TOFF.gate_register_effect(r, 1)
# print r.show()

# q1 = qubit.Qubit()
# q2 = qubit.Qubit()
# q3 = qubit.Qubit()

# FRED = Gate('Fredkin')
# r = register.Register(0)
# r.add_qubit(q1)
# r.add_qubit(q2)
# r.add_qubit(q3)
# print r.show()
# FRED.gate_register_effect(r, 1)
# print r.show()

# FRED = Gate('Fredkin')
# r = register.Register(0)
# r.add_qubit(q1)
# r.add_qubit(q2)
# r.add_qubit(q3)
# print r.show()
# FRED.gate_register_effect(r, 2)
# print r.show()

# FRED = Gate('Fredkin')
# r = register.Register(0)
# r.add_qubit(q1)
# r.add_qubit(q2)
# r.add_qubit(q3)
# print r.show()
# FRED.gate_register_effect(r, 3)
# print r.show()
