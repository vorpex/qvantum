''' test measuring quantum entanglement '''

import qubit
import register
import gate
import layer
import circuit

import math

# q0 = qubit.Qubit(0, 1)
# q1 = qubit.Qubit(0, 1)

# r = register.Register([q0, q1])

# l0 = layer.Layer([Gate.Hadamard(), Gate.Gate()])
# l1 = layer.Layer([Gate.CNOT(0, 1)])
# l2 = layer.Layer([Gate.CNOT(1, 0)])

# c = circuit.Circuit([l0, l1, l2])
# c.run(r)

# print(r.show())
# r.measure_nth_qubit(1)
# print(r.show())

###################################################################################################

q0 = qubit.Qubit(0, 1)
q1 = qubit.Qubit(-1 / math.sqrt(2), 1 / math.sqrt(2))

r = register.Register([q0, q1])

print(r.show())
