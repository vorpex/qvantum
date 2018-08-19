''' test circuit on teleportation algorithm '''

import Qubit
import Register
import Gate
import Layer
import Circuit

q = Qubit.Random_Qubit()
q1 = Qubit.Qubit(1, 0)
q2 = Qubit.Qubit(1, 0)

print(q.show())

r = Register.Register([q1, q2])

l0 = Layer.Layer([Gate.Hadamard(), Gate.Gate()])
l1 = Layer.Layer([Gate.CNOT(0, 1)])

c0 = Circuit.Circuit([l0, l1])
c0.run(r)

r.insert_qubit(q, 0)

l2 = Layer.Layer([Gate.CNOT(0, 1), Gate.Gate()])
l3 = Layer.Layer([Gate.Hadamard(), Gate.Gate(), Gate.Gate()])

c1 = Circuit.Circuit([l2, l3])
c1.run(r)

m0 = r.measure_nth_qubit(0)
m1 = r.measure_nth_qubit(1)

# print(r.show())

XM2 = Gate.PauliX()
XM2.power(m1)
ZM1 = Gate.PauliZ()
ZM1.power(m0)

l4 = Layer.Layer([Gate.Gate(), Gate.Gate(), XM2])
l5 = Layer.Layer([Gate.Gate(), Gate.Gate(), ZM1])

c2 = Circuit.Circuit([l4, l5])
c2.run(r)

r.delete_qubit(0)
r.delete_qubit(0)
print(r.show())
