''' test circuit on teleportation algorithm '''

import qubit
import register
import gate
import layer
import circuit

q = qubit.Random_Qubit()
q1 = qubit.Qubit(1, 0)
q2 = qubit.Qubit(1, 0)

print(q.show())

r = register.Register([q1, q2])

l0 = layer.Layer([gate.Hadamard(), gate.Gate()])
l1 = layer.Layer([gate.CNOT(0, 1)])

c0 = circuit.Circuit([l0, l1])
c0.run(r)

r.insert_qubit(q, 0)

l2 = layer.Layer([gate.CNOT(0, 1), gate.Gate()])
l3 = layer.Layer([gate.Hadamard(), gate.Gate(), gate.Gate()])

c1 = circuit.Circuit([l2, l3])
c1.run(r)

m0 = r.measure_nth_qubit(0)
m1 = r.measure_nth_qubit(1)

# print(r.show())

XM2 = gate.PauliX()
XM2.power(m1)
ZM1 = gate.PauliZ()
ZM1.power(m0)

l4 = layer.Layer([gate.Gate(), gate.Gate(), XM2])
l5 = layer.Layer([gate.Gate(), gate.Gate(), ZM1])

c2 = circuit.Circuit([l4, l5])
c2.run(r)

# t_coeff = [coeff for coeff in r.get_amplitudes() if coeff != 0]
# Q = qubit.Qubit(t_coeff[0], t_coeff[1])
# print(Q.show())

r.delete_qubit(0)
r.delete_qubit(0)
print(r.show())
