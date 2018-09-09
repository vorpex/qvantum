''' test measuring quantum entanglement '''

import Qubit
import Register
import Gate
import Layer
import Circuit

import math

# q0 = Qubit.Qubit(0, 1)
# q1 = Qubit.Qubit(0, 1)

# r = Register.Register([q0, q1])

# l0 = Layer.Layer([Gate.Hadamard(), Gate.Gate()])
# l1 = Layer.Layer([Gate.CNOT(0, 1)])
# l2 = Layer.Layer([Gate.CNOT(1, 0)])

# c = Circuit.Circuit([l0, l1, l2])
# c.run(r)

# print(r.show())
# r.measure_nth_qubit(1)
# r.delete_qubit(1)
# print(r.show())

###################################################################################################

q0 = Qubit.Qubit(0, 1)
q1 = Qubit.Qubit(-1 / math.sqrt(2), 1 / math.sqrt(2))

r = Register.Register([q0, q1])

print(r.show())
r.delete_qubit(1)
print(r.show())
