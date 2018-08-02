''' test measuring quantum entanglement '''

import Qubit
import Register
import Gate
import Layer
import Circuit

import logging
import math

logging.disable(30)

# q1 = Qubit.Qubit(0, 1)
# q2 = Qubit.Qubit(0, 1)

# r = Register.Register([q1, q2])

# l1 = Layer.Layer([Gate.Hadamard(), Gate.Gate()])
# l2 = Layer.Layer([Gate.CNOT(1, 2)])
# l3 = Layer.Layer([Gate.CNOT(2, 1)])

# c = Circuit.Circuit([l1, l2, l3])
# c.run(r)

# print(r.show())
# r.measure(2)
# r.delete_qubit(2)
# print(r.show())

###################################################################################################

q1 = Qubit.Qubit(0, 1)
q2 = Qubit.Qubit(-1 / math.sqrt(2), 1 / math.sqrt(2))

r = Register.Register([q1, q2])

print(r.show())
r.delete_qubit(2)
print(r.show())
