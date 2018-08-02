''' perform quantum computation '''

# pylint: disable=E1601
import gate_class as gate
import register_class as register
import qubit_class as qubit

##### Bell or EPR states #####
# q1 = qubit.Qubit(1, 0) # [(1, 0); (0, 1)]
# q2 = qubit.Qubit(0, 1) # [(1, 0); (0, 1)]
# r = register.Register(0)
# H = gate.Gate('Hadamard')
# CNOT = gate.Gate('C-NOT')

# r.add_qubit(q1)
# r.add_qubit(q2)
# print r.show()
# q1_new = H.gate_qubit_effect(q1)
# r.replace_qubit(q1_new, 1)
# r.coeffs()
# print r.show()
# CNOT.gate_register_effect(r)
# print r.show()

##### Quantum Teleportation #####
q1 = qubit.Qubit()
q2 = qubit.Qubit(1, 0)
q3 = qubit.Qubit(1, 0)
r = register.Register(0)
H = gate.Gate('Hadamard')
CNOT = gate.Gate('C-NOT')

print q1.show()
r.add_qubit(q2)
r.add_qubit(q3)
q2_new = H.gate_qubit_effect(q2)
r.replace_qubit(q2_new, 1)
r.coeffs()
CNOT.gate_register_effect(r)
print r.show()
r.register.append(r.register[1])
r.register[1] = r.register[0]
r.replace_qubit(q1, 1)
r.coeffs()
print r.show()
