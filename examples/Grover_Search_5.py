'''grover search 5'''

import numpy
import qvantum

q0 = qvantum.Qubit(1, 0)
q1 = qvantum.Qubit(1, 0)
q2 = qvantum.Qubit(1, 0)
q3 = qvantum.Qubit(0, 1)

r = qvantum.Register([q0, q1, q2, q3])
r.show()

l0 = qvantum.Layer([qvantum.Hadamard(), qvantum.Hadamard(), qvantum.Hadamard(), qvantum.Hadamard()])
l1 = qvantum.Layer([qvantum.Gate(), qvantum.PauliX(), qvantum.Gate(), qvantum.Gate()])

g2 = qvantum.Gate()
g2.set_matrix(numpy.matrix([
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
	]))

l2 = qvantum.Layer([g2])
l3 = qvantum.Layer([qvantum.Gate(), qvantum.PauliX(), qvantum.Gate(), qvantum.Gate()])
l4 = qvantum.Layer([qvantum.Hadamard(), qvantum.Hadamard(), qvantum.Hadamard(), qvantum.Gate()])
l5 = qvantum.Layer([qvantum.PauliX(), qvantum.PauliX(), qvantum.PauliX(), qvantum.Gate()])

g6 = qvantum.Gate()
g6.set_matrix(numpy.matrix([
	[1, 0, 0, 0, 0, 0, 0, 0],
	[0, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 0],
	[0, 0, 0, 0, 0, 0, 0, -1]
	]))

l6 = qvantum.Layer([g6, qvantum.Gate()])
l7 = qvantum.Layer([qvantum.PauliX(), qvantum.PauliX(), qvantum.PauliX(), qvantum.Gate()])
l8 = qvantum.Layer([qvantum.Hadamard(), qvantum.Hadamard(), qvantum.Hadamard(), qvantum.Gate()])

c = qvantum.Circuit([l0, l1, l2, l3, l4, l5, l6, l7, l8])
c.run(r)

r.show()
r.measure_nth_qubit(3)
r.delete_qubit(3)
r.show()
