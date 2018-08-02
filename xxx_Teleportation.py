''' test circuit on teleportation algorithm '''

import Qubit
import Register
import Gate
import Layer
import Circuit

import logging

logging.disable(30)

q = Qubit.Qubit()
q1 = Qubit.Qubit(1, 0)
q2 = Qubit.Qubit(1, 0)

print(q.show())

r = Register.Register([q1, q2])

l1 = Layer.Layer([Gate.Hadamard(), Gate.Gate()])
l2 = Layer.Layer([Gate.CNOT(1, 2)])

c1 = Circuit.Circuit([l1, l2])
c1.run(r)

r.insert_qubit(q, 1)

l3 = Layer.Layer([Gate.CNOT(1, 2), Gate.Gate()])
l4 = Layer.Layer([Gate.Hadamard(), Gate.Gate(), Gate.Gate()])

c2 = Circuit.Circuit([l3, l4])
c2.run(r)

m1 = r.measure(1)
m2 = r.measure(2)

# print(r.show())

XM2 = Gate.PauliX()
XM2.power(m2)
ZM1 = Gate.PauliZ()
ZM1.power(m1)

# 1. solution #####################################################################################
# 219. line in Register: del self.__state_vector[item]

# Q = Qubit.Qubit(r.get_parameters()[0], r.get_parameters()[1])

# XM2(Q)
# ZM1(Q)

# print(Q.show())

# 2. solution #####################################################################################
# 219. line in Register: self.__state_vector[item] = 0

l5 = Layer.Layer([Gate.Gate(), Gate.Gate(), XM2])
l6 = Layer.Layer([Gate.Gate(), Gate.Gate(), ZM1])

c3 = Circuit.Circuit([l5, l6])
c3.run(r)

r.delete_qubit(1)
r.delete_qubit(1)
print(r.show())
