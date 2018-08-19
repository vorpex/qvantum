''' test circuit on Grover search algorithm '''

import Qubit
import Register
import Gate
import Layer
import Circuit

import numpy

q0 = Qubit.Qubit(1, 0)
q1 = Qubit.Qubit(1, 0)
q2 = Qubit.Qubit(1, 0)
q3 = Qubit.Qubit(0, 1)

r = Register.Register([q0, q1, q2, q3])
print(r.show())

l0 = Layer.Layer([Gate.Hadamard(), Gate.Hadamard(), Gate.Hadamard(), Gate.Hadamard()])
l1 = Layer.Layer([Gate.Gate(), Gate.PauliX(), Gate.Gate(), Gate.Gate()])

G2 = Gate.Gate()
G2.set_matrix(numpy.matrix([
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

l2 = Layer.Layer([G2])
l3 = Layer.Layer([Gate.Gate(), Gate.PauliX(), Gate.Gate(), Gate.Gate()])
l4 = Layer.Layer([Gate.Hadamard(), Gate.Hadamard(), Gate.Hadamard(), Gate.Gate()])
l5 = Layer.Layer([Gate.PauliX(), Gate.PauliX(), Gate.PauliX(), Gate.Gate()])

G6 = Gate.Gate()
G6.set_matrix(numpy.matrix([
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, -1]
    ]))

l6 = Layer.Layer([G6, Gate.Gate()])
l7 = Layer.Layer([Gate.PauliX(), Gate.PauliX(), Gate.PauliX(), Gate.Gate()])
l8 = Layer.Layer([Gate.Hadamard(), Gate.Hadamard(), Gate.Hadamard(), Gate.Gate()])

c0 = Circuit.Circuit([l0])
c0.run(r)

c1 = Circuit.Circuit([l1, l2, l3, l4, l5, l6, l7, l8])
for i in range(10):

    c1.run(r)

print(r.show())
r.measure_nth_qubit(3)
r.delete_qubit(3)
print(r.show())
