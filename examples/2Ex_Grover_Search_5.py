''' test circuit on Grover search algorithm '''

import qubit
import register
import gate
import layer
import circuit

import numpy

q0 = qubit.Qubit(1, 0)
q1 = qubit.Qubit(1, 0)
q2 = qubit.Qubit(1, 0)
q3 = qubit.Qubit(0, 1)

r = register.Register([q0, q1, q2, q3])
print(r.show())

l0 = layer.Layer([gate.Hadamard(), gate.Hadamard(), gate.Hadamard(), gate.Hadamard()])
l1 = layer.Layer([gate.Gate(), gate.PauliX(), gate.Gate(), gate.Gate()])

G2 = gate.Gate()
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

l2 = layer.Layer([G2])
l3 = layer.Layer([gate.Gate(), gate.PauliX(), gate.Gate(), gate.Gate()])
l4 = layer.Layer([gate.Hadamard(), gate.Hadamard(), gate.Hadamard(), gate.Gate()])
l5 = layer.Layer([gate.PauliX(), gate.PauliX(), gate.PauliX(), gate.Gate()])

G6 = gate.Gate()
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

l6 = layer.Layer([G6, gate.Gate()])
l7 = layer.Layer([gate.PauliX(), gate.PauliX(), gate.PauliX(), gate.Gate()])
l8 = layer.Layer([gate.Hadamard(), gate.Hadamard(), gate.Hadamard(), gate.Gate()])

c = circuit.Circuit([l0, l1, l2, l3, l4, l5, l6, l7, l8])
c.run(r)

print(r.show())
r.measure_nth_qubit(3)
r.delete_qubit(3)
print(r.show())
