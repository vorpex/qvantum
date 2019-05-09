'''teleportation'''

import math
import qvantum

q = qvantum.Random_Qubit()
q1 = qvantum.Qubit(1, 0)
q2 = qvantum.Qubit(1, 0)

r = qvantum.Register([q1, q2])

l0 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
l1 = qvantum.Layer([qvantum.CNOT(0, 1)])

c0 = qvantum.Circuit([l0, l1])
c0.run(r)

r.insert_qubit(q, 0)

l2 = qvantum.Layer([qvantum.CNOT(0, 1), qvantum.Gate()])
l3 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate(), qvantum.Gate()])

c1 = qvantum.Circuit([l2, l3])
c1.run(r)

m0 = r.measure_nth_qubit(0)
m1 = r.measure_nth_qubit(1)

# print(r.show())

XM2 = qvantum.PauliX()
XM2.power(m1)
ZM1 = qvantum.PauliZ()
ZM1.power(m0)

l4 = qvantum.Layer([qvantum.Gate(), qvantum.Gate(), XM2])
l5 = qvantum.Layer([qvantum.Gate(), qvantum.Gate(), ZM1])

c2 = qvantum.Circuit([l4, l5])
c2.run(r)

r.delete_qubit(0)
r.delete_qubit(0)

print(q.show())
print(r.show())
