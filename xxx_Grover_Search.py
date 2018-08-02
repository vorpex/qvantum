''' test circuit on Grover search algorithm '''

import Qubit
import Register
import Gate
import Layer
import Circuit

import logging
import numpy

logging.disable(30)

q1 = Qubit.Qubit(1, 0)
q2 = Qubit.Qubit(1, 0)
q3 = Qubit.Qubit(1, 0)
q4 = Qubit.Qubit(0, 1)

r = Register.Register([q1, q2, q3, q4])
print(r.show())

l1 = Layer.Layer([Gate.Hadamard(), Gate.Hadamard(), Gate.Hadamard(), Gate.Hadamard()])
l2 = Layer.Layer([Gate.Gate(), Gate.PauliX(), Gate.Gate(), Gate.Gate()])

G3 = Gate.GateR()
G3.set_matrix(numpy.matrix([
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

l3 = Layer.Layer([G3])
l4 = Layer.Layer([Gate.Gate(), Gate.PauliX(), Gate.Gate(), Gate.Gate()])
l5 = Layer.Layer([Gate.Hadamard(), Gate.Hadamard(), Gate.Hadamard(), Gate.Gate()])
l6 = Layer.Layer([Gate.PauliX(), Gate.PauliX(), Gate.PauliX(), Gate.Gate()])

G7 = Gate.GateR()
G7.set_matrix(numpy.matrix([
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, -1]
    ]))

l7 = Layer.Layer([G7, Gate.Gate()])
l8 = Layer.Layer([Gate.PauliX(), Gate.PauliX(), Gate.PauliX(), Gate.Gate()])
l9 = Layer.Layer([Gate.Hadamard(), Gate.Hadamard(), Gate.Hadamard(), Gate.Gate()])

c = Circuit.Circuit([l1, l2, l3, l4, l5, l6, l7, l8, l9])
c.run(r)

print(r.show())
r.measure(4)
r.delete_qubit(4)
print(r.show())
