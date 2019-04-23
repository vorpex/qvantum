# qvantum.bloch module

**`def qvantum.bloch.__init__()`**

Initialize self.  See help(type(self)) for accurate signature.
**`def qvantum.bloch.bloch_coords()`**

This function calculates the coordinates of the Bloch representation from the state vector 
of a Qubit object.
    
**Arguments:**

    q {qubit} -- Instance of Qubit class or Random_Qubit class

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (-0.5879-0.7251i)|0> + (0.3522-0.0674i)|1>'
    >>> qvantum.bloch_coords(q)
    (-0.31632342351128423, 0.5899599386821074, 0.7428908146479567)

**`def qvantum.bloch.bloch_qubit()`**

This function calculates the state vector of a Qubit object from the given Bloch 
coordinates.

**Arguments:**

u {int, float} -- 1st coordinate of Bloch representation
v {int, float} -- 2nd coordinate of Bloch representation
w {int, float} -- 3rd coordinate of Bloch representation

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import math
    >>> import qvantum
    >>>
    >>> u = 0
    >>> v = 1 / math.sqrt(2)
    >>> w = 1 / math.sqrt(2)
    >>> qvantum.bloch_qubit(u, v, w).show()
    '|Ψ> = (0.9239+0.0000i)|0> + (0.0000+0.3827i)|1>'

**`def qvantum.bloch.bloch_sphere_plot()`**

This function visualizes the qubit using its bloch coordinates and the matplotlib module.
    
**Arguments:**
    u {int, float} -- 1st coordinate of Bloch representation
    v {int, float} -- 2nd coordinate of Bloch representation
    w {int, float} -- 3rd coordinate of Bloch representation

**Keyword Arguments:**
    xfigsize {int, float} -- X size of figure (default: {15})
    yfigsize {int, float} -- Y size of figure (default: {7.5})
    frame_on {bool} -- Frame (default: {False})
    tight_layout_on {bool} -- Tight layout (default: {False})
    style {str} -- Style (default: {'dark_background'})
    surface_on {bool} -- Surface (default: {True})
    wireframe_on {bool} -- Wireframe (default: {True})
    surface_cmap {str} -- Surface cmap (default: {'Blues_r'})
    surface_alpha {int, float} -- Surface alpha (default: {0.3})
    wireframe_color {str} -- Wireframe color (default: {'#d3d3d3'})
    wireframe_linewidth {int, float} -- Width of wireframe line (default: {0.075})
    quiver_color {str} -- Quiver color (default: {'#ffffff'})
    quiver_linewidth {int, float} -- Width of quiver line (default: {1.5})
    quiver_ratio {int, float} -- Quiver ratio (default: {0.1})
    line_color {str} -- Line color (default: {'#d3d3d3'})
    line_linewidth {int, float} -- Width of line (default: {0.3})
    circle_edgecolor {str} -- Edge color of circle (default: {'#d3d3d3'})
    circle_facecolor {str} -- Face color of circle (default: {'none'})
    circle_linewidth {int, float} -- Width of circle line (default: {0.3})

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6257-0.4027i)|0> + (-0.5114+0.4299i)|1>'
    >>> u = qvantum.bloch_coords(q)[0]
    >>> v = qvantum.bloch_coords(q)[1]
    >>> w = qvantum.bloch_coords(q)[2]
    >>> qvantum.bloch_sphere_plot(u, v, w)

**`def qvantum.bloch.phase_test()`**

Computes the phase between two complex number.
    
**Arguments:**
    c1 {complex} -- 1st complex number
    c2 {complex} -- 2nd complex number

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q1.show()
    '|Ψ> = (0.6615-0.4616i)|0> + (0.5513-0.2132i)|1>'
    >>> q2 = qvantum.Random_Qubit()
    >>> q2.show()
    '|Ψ> = (-0.2091-0.3620i)|0> + (-0.3893+0.8208i)|1>'
    >>> qvantum.phase_test(q1.get_alpha(), q2.get_alpha())
    0.08522011231864535
    >>> qvantum.phase_test(q1.get_beta(), q2.get_beta())
    -0.7255489587145547

# qvantum.check_bloch module

**`def qvantum.check_bloch.__init__()`**

Initialize self.  See help(type(self)) for accurate signature.
**`def qvantum.check_bloch.bloch_coords_check()`**

Decorator to check the arguments of qubit-to-bloch-coords function.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_bloch.bloch_qubit_check()`**

Decorator to check the arguments of bloch-coords-to-qubit function.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_bloch.bloch_sphere_plot_check()`**

Decorator to check the arguments of plotting bloch sphere function.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_bloch.phase_test_check()`**

Decorator to check the arguments of phase testing function.
    
**Arguments:**
function {} -- The tested function
    
# qvantum.check_circuit module

**`def qvantum.check_circuit.__init__()`**

Initialize self.  See help(type(self)) for accurate signature.
**`def qvantum.check_circuit.circuit_init_check()`**

Decorator to check the arguments of initialization function in circuit class.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_circuit.delete_layer_check()`**

Decorator to check the arguments of deleting layer function.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_circuit.get_nth_layer_check()`**

Decorator to check the arguments of getting nth layer function.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_circuit.insert_layer_check()`**

Decorator to check the arguments of inserting layer function.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_circuit.run_check()`**

Decorator to check the arguments of running circuit function.
    
**Arguments:**
function {} -- The tested function
    
# qvantum.check_gate module

**`def qvantum.check_gate.CNOT_check()`**

Decorator to check the arguments of calling Controlled-Not gate.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_gate.Fredkin_check()`**

Decorator to check the arguments of calling Fredkin gate.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_gate.Ising_check()`**

Decorator to check the arguments of calling Ising gate.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_gate.Toffoli_check()`**

Decorator to check the arguments of calling Toffoli gate.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_gate.__init__()`**

Initialize self.  See help(type(self)) for accurate signature.
**`def qvantum.check_gate.gate_call_check()`**

Decorator to check the arguments of call function in gate class.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_gate.power_check()`**

Decorator to check the arguments of raising a matrix to the given power function.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_gate.set_matrix_check()`**

Decorator to check the arguments of setting matrix function.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_gate.set_name_check()`**

Decorator to check the arguments of setting name function.
    
**Arguments:**
function {} -- The tested function
    
# qvantum.check_layer module

**`def qvantum.check_layer.__init__()`**

Initialize self.  See help(type(self)) for accurate signature.
**`def qvantum.check_layer.delete_gate_check()`**

Decorator to check the arguments of deleting gate function.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_layer.get_nth_gate_check()`**

Decorator to check the arguments of getting nth gate function.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_layer.insert_gate_check()`**

Decorator to check the arguments of inserting gate function.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_layer.layer_init_check()`**

Decorator to check the arguments of initialization function in layer class.
    
**Arguments:**
function {} -- The tested function
    
# qvantum.check_qubit module

**`def qvantum.check_qubit.__init__()`**

Initialize self.  See help(type(self)) for accurate signature.
**`def qvantum.check_qubit.qubit_init_check()`**

Decorator to check the arguments of initialization function in qubit class.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_qubit.set_amplitudes_check()`**

Decorator to check the arguments of setting new amplitudes function in qubit class.
    
**Arguments:**
function {} -- The tested function
    
# qvantum.check_register module

**`def qvantum.check_register.__init__()`**

Initialize self.  See help(type(self)) for accurate signature.
**`def qvantum.check_register.delete_qubit_check()`**

Decorator to check the arguments of deleting qubit function in register class.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_register.get_amplitudes_check()`**

Decorator to check the arguments of getting amplitudes function in register class.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_register.get_states_check()`**

Decorator to check the arguments of getting states function in register class.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_register.insert_qubit_check()`**

Decorator to check the arguments of inserting qubit function in register class.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_register.measure_nth_qubit_check()`**

Decorator to check the arguments of measuring qubit function in register class.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_register.register_init_check()`**

Decorator to check the arguments of initialization function in register class.
    
**Arguments:**
function {} -- The tested function
    
**`def qvantum.check_register.set_amplitudes_check()`**

Decorator to check the arguments of setting amplitudes function in register class.
    
**Arguments:**
function {} -- The tested function
    
# qvantum.circuit module

**`def qvantum.circuit.__init__()`**

Initialize self.  See help(type(self)) for accurate signature.
**`class qvantum.circuit.Circuit`**

circuit class

    An instance of circuit class represents a whole quantum computional process. The circuit is
    created by defining the layers which are contained by the given circuit. The order of layers
    refers to that stage which is ran by the given layer. Using the instances of circuit class the
    user can build a quantum algorithm.

    The instances of circuit class have the following methods:

    - __init__() - initialization method
    - get_layer_list()   - getter of layers in layer list
    - get_layer_number() - getter of number of layers
    - get_nth_layer()    - getter of n-th layer
    - get_circuit_size() - getter of size of circuit (equals to the size of register on which the layer is usable)
    - delete_layer()     - delete layer from circuit
    - insert_layer()     - insert layer into circuit
    - run()      		 - run circuit on starting register
    
**`def qvantum.circuit.Circuit.__call__()`**

Call self as a function.
**`def qvantum.circuit.Circuit.__init__()`**

Method to initialize an instance of the Circuit class. The argument must be a list of objects in the Layer class with the same size.

**Arguments:**
    layer_list {list} -- List of objects from Layer class

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> l1 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l2 = qvantum.Layer([qvantum.PauliY(), qvantum.PauliX()])
    >>> c = qvantum.Circuit([l1, l2])
    >>> c.get_layer_list()
    OrderedDict([(0, <qvantum.layer.Layer at 0x27b474c2cf8>), (1, <qvantum.layer.Layer at 0x27b47bf2198>)])
    >>> c.get_nth_layer(0)
    <qvantum.layer.Layer at 0x27b474c2cf8>

**`def qvantum.circuit.Circuit.delete_layer()`**

Method to delete the n-th layer from the current Circuit object. The parameter must 
be equal to or bigger than 0 and less than the actual number of the layers in the Circuit.

**Arguments:**
    nth {int} -- Number of layer to be deleted

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> l1 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l2 = qvantum.Layer([qvantum.CNOT(1, 0)])
    >>> c = qvantum.Circuit([l1, l2])
    >>> c.get_layer_list()
    OrderedDict([(0, <qvantum.layer.Layer at 0x27b47e65630>), (1, <qvantum.layer.Layer at 0x27b47e65cc0>)])
    >>> c.delete_layer(2)
    ---------------------------------------------------------------------------
    ValueErrorTraceback (most recent call last)
    <ipython-input-23-2ef6caf8af8a> in <module>
    ----> 1 c.delete_layer(2)

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_circuit.py in wrapper(self, nth)
39 
40 if isinstance(nth, int):
    ---> 41     return function(self, nth)
42 
43 else:

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\circuit.py in delete_layer(self, nth)
82 else:
83     raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +    ---> 84 'less or equal to ' + str(len(self.__layer_list) - 1) + '.')
85 
86     @check_circuit.insert_layer_check

    ValueError: Invalid input! Argument must be greater or equal to 0 and less or equal to 1.
    >>> c.delete_layer(0)
    >>> c.get_layer_list()
    OrderedDict([(0, <qvantum.layer.Layer at 0x27b47e65cc0>)])

**`def qvantum.circuit.Circuit.get_circuit_size()`**

Method to return the size of the current Circuit object. It’s the size of the 
Register object which the Circuit can be applied on.

**Examples:**

    >>> import qvantum
    >>>
    >>> l1 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l2 = qvantum.Layer([qvantum.CNOT(1, 0)])
    >>> c = qvantum.Circuit([l1, l2])
    >>> c.get_layer_list()
    OrderedDict([(0, <qvantum.layer.Layer at 0x27b47e65630>), (1, <qvantum.layer.Layer at 0x27b47e65cc0>)])
    >>> c.get_circuit_size()
    2

**`def qvantum.circuit.Circuit.get_layer_list()`**

Method to return the layers which are contained by the current Circuit object.

**Examples:**

    >>> import qvantum
    >>>
    >>> l1 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l2 = qvantum.Layer([qvantum.PauliY(), qvantum.PauliX()])
    >>> c = qvantum.Circuit([l1, l2])
    >>> c.get_layer_list()
    OrderedDict([(0, <qvantum.layer.Layer at 0x27b474c2cf8>), (1, <qvantum.layer.Layer at 0x27b47bf2198>)])

**`def qvantum.circuit.Circuit.get_layer_number()`**

Method returnd the number of the layers which are contained by the current Circuit object.

**Examples:**

    >>> import qvantum
    >>>
    >>> l1 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l2 = qvantum.Layer([qvantum.PauliY(), qvantum.PauliX()])
    >>> c = qvantum.Circuit([l1, l2])
    >>> c.get_layer_list()
    OrderedDict([(0, <qvantum.layer.Layer at 0x27b474c2cf8>), (1, <qvantum.layer.Layer at 0x27b47bf2198>)])
    >>> c.get_layer_number()
    2

**`def qvantum.circuit.Circuit.get_nth_layer()`**

Method to return the n-th layer in the current Circuit object. The parameter must be 
between 0 and the actual number of the layers.

**Arguments:**
    nth {int} -- Number of nth possible layer

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> l1 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l2 = qvantum.Layer([qvantum.PauliY(), qvantum.PauliX()])
    >>> c = qvantum.Circuit([l1, l2])
    >>> c.get_layer_list()
    OrderedDict([(0, <qvantum.layer.Layer at 0x27b474c2cf8>), (1, <qvantum.layer.Layer at 0x27b47bf2198>)])
    >>> c.get_nth_layer(1)
    <qvantum.layer.Layer at 0x27b47bf2198>
    >>> c.get_nth_layer(2)
    ---------------------------------------------------------------------------
    KeyError  Traceback (most recent call last)
    <ipython-input-16-a2c18bd79e3d> in <module>
    ----> 1 c.get_nth_layer(2)

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_circuit.py in wrapper(self, nth)
26 
27 if isinstance(nth, int):
    ---> 28     return function(self, nth)
29 
30 else:

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\circuit.py in get_nth_layer(self, nth)
57 ''' getter of n-th layer '''
58 
    ---> 59 return self.__layer_list[nth]
60 
61     def get_circuit_size(self):

    KeyError: 2

**`def qvantum.circuit.Circuit.insert_layer()`**

Method to insert a Layer object into the n-th place in the current Circuit object. The 
first parameter must be a Layer object while the second parameter must be equal to or 
bigger than 0 and equal to or less than the actual size of the layers in the Circuit. The 
size of the Layer object must be equal to the size of the already used Layers in the 
Circuit.

**Arguments:**
    l {layer} -- Layer to be inserted
    nth {int} -- Index where the layer to be inserted

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> l1 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l2 = qvantum.Layer([qvantum.CNOT(1, 0)])
    >>> c = qvantum.Circuit([l1, l2])
    >>> c.get_layer_list()
    OrderedDict([(0, <qvantum.layer.Layer at 0x27b47de9898>), (1, <qvantum.layer.Layer at 0x27b47de9550>)])
    >>> l3 = qvantum.Layer([qvantum.Swap()])
    >>> c.insert_layer(3)
    ---------------------------------------------------------------------------
    ValueErrorTraceback (most recent call last)
    <ipython-input-31-3fd723aee9a2> in <module>
    ----> 1 c.insert_layer(l3, 3)

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_circuit.py in wrapper(self, l, nth)
52 
53 if isinstance(l, layer.Layer) and isinstance(nth, int):
    ---> 54     return function(self, l, nth)
55 
56 else:

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\circuit.py in insert_layer(self, l, nth)
109     raise ValueError('Invalid input! Layer and circuit size must be the same. ' +110 'Argument must be greater or equal to 0 and less or equal to ' +    --> 111 str(len(self.__layer_list)) + '.')
112 
113     @check_circuit.run_check

    ValueError: Invalid input! Layer and circuit size must be the same. Argument must be greater or equal to 0 and less or equal to 2.
    >>> c.insert_layer(l3, 1)
    >>> c.get_layer_list()
    OrderedDict([(0, <qvantum.layer.Layer at 0x27b47de9898>), (1, <qvantum.layer.Layer at 0x27b47e5dc50>), (2, <qvantum.layer.Layer at 0x27b47de9550>)])

**`def qvantum.circuit.Circuit.run()`**

Method to perform the computational process on a Register object as input and returns 
the result. The size of the Register object and the size of the Circuit object must be 
equal.

**Arguments:**
    r {register} -- Register which the circuit is applied on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q2 = qvantum.Random_Qubit()
    >>> r = qvantum.Register([q1, q2])
    >>> r.show()
    '|Ψ> = (-0.8867+0.1861i)|00> + (-0.2437-0.1838i)|01> + (0.2726+0.0534i)|10> + (0.0469+0.0810i)|11>'
    >>> l1 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l2 = qvantum.Layer([qvantum.CNOT(1, 0)])
    >>> c = qvantum.Circuit([l1, l2])
    >>> c.run(r)
    >>> r.show()
    '|Ψ> = (-0.4342+0.1693i)|00> + (-0.2054-0.1873i)|01> + (-0.8198+0.0938i)|10> + (-0.1392-0.0727i)|11>'

# qvantum.gate module

**`def qvantum.gate.__init__()`**

Initialize self.  See help(type(self)) for accurate signature.
**`class qvantum.gate.CNOT`**

This class is an inherited class from the Gate class. It’s the implementation of the 
    Controlled-Not gate. It’s called on 2 qubits. The parameters determine which one is the 
    control and the target – (0, 1) or (1, 0). Its unitary matrix:
    
    
**`def qvantum.gate.CNOT.__call__()`**

Method which makes possible to call a gate on a qubit or a register. The only 
restriction is that the size of the gate and the size of the qubit or regsiter must be 
equal to each other.

**Arguments:**
    qr {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

**`def qvantum.gate.CNOT.__init__()`**

Method to initialize Controlled-Not gate.

**Arguments:**
    control_qubit {int} -- Possible values: 0 or 1
    target_qubit {int} -- Possible values: 0 or 1

**Raises:**
    ValueError

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.CNOT(1, 0)

**`def qvantum.gate.CNOT.get_matrix()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_matrix()
    matrix([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]])

**`def qvantum.gate.CNOT.get_name()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

**`def qvantum.gate.CNOT.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

**`def qvantum.gate.CNOT.power()`**

Method to raise the unitary matrix of the gate to the given power and overwrites the 
original matrix of the gate with the results matrix.

**Arguments:**
    power {int} -- The power which the gate is raised on

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> t = qvantum.Toffoli()
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]])
    >>> t.power(2)
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])

**`def qvantum.gate.CNOT.set_matrix()`**

Setter of matrix of Controlled-Not gate. Always raises BaseException.

**Raises:**
    BaseException

**`def qvantum.gate.CNOT.set_name()`**

Setter of name of Controlled-Not gate. Always raises BaseException.

**Raises:**
    BaseException

**`class qvantum.gate.ControlledPhase`**

This class is an inherited class from the Gate class. It’s the implementation of the 
    Controlled-Phase gate. Its unitary matrix:
    
    
**`def qvantum.gate.ControlledPhase.__call__()`**

Method which makes possible to call a gate on a qubit or a register. The only 
restriction is that the size of the gate and the size of the qubit or regsiter must be 
equal to each other.

**Arguments:**
    qr {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

**`def qvantum.gate.ControlledPhase.__init__()`**

Method to initialize Controlled-Phase gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.ControlledPhase()

**`def qvantum.gate.ControlledPhase.get_matrix()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_matrix()
    matrix([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]])

**`def qvantum.gate.ControlledPhase.get_name()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

**`def qvantum.gate.ControlledPhase.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

**`def qvantum.gate.ControlledPhase.power()`**

Method to raise the unitary matrix of the gate to the given power and overwrites the 
original matrix of the gate with the results matrix.

**Arguments:**
    power {int} -- The power which the gate is raised on

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> t = qvantum.Toffoli()
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]])
    >>> t.power(2)
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])

**`def qvantum.gate.ControlledPhase.set_matrix()`**

Setter of matrix of Controlled-Phase gate. Always raises BaseException.

**Raises:**
    BaseException

**`def qvantum.gate.ControlledPhase.set_name()`**

Setter of name of Controlled-Phase gate. Always raises BaseException.

**Raises:**
    BaseException

**`class qvantum.gate.ControlledZ`**

This class is an inherited class from the Gate class. It’s the implementation of the 
    Controlled-Z gate. Its unitary matrix:
    
    
**`def qvantum.gate.ControlledZ.__call__()`**

Method which makes possible to call a gate on a qubit or a register. The only 
restriction is that the size of the gate and the size of the qubit or regsiter must be 
equal to each other.

**Arguments:**
    qr {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

**`def qvantum.gate.ControlledZ.__init__()`**

Method to initialize Controlled-Z gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.ControlledZ()

**`def qvantum.gate.ControlledZ.get_matrix()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_matrix()
    matrix([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]])

**`def qvantum.gate.ControlledZ.get_name()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

**`def qvantum.gate.ControlledZ.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

**`def qvantum.gate.ControlledZ.power()`**

Method to raise the unitary matrix of the gate to the given power and overwrites the 
original matrix of the gate with the results matrix.

**Arguments:**
    power {int} -- The power which the gate is raised on

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> t = qvantum.Toffoli()
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]])
    >>> t.power(2)
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])

**`def qvantum.gate.ControlledZ.set_matrix()`**

Setter of matrix of Controlled-Z gate. Always raises BaseException.

**Raises:**
    BaseException

**`def qvantum.gate.ControlledZ.set_name()`**

Setter of name of Controlled-Z gate. Always raises BaseException.

**Raises:**
    BaseException

**`class qvantum.gate.Fredkin`**

This class is an inherited class from the Gate class. It’s the implementation of the 
    Fredkin gate. It’s called on 3 qubits. The parameters determine which one is the control 
    qubit – 0, 1 or 2.Its unitary matrix:
    
    
**`def qvantum.gate.Fredkin.__call__()`**

Method which makes possible to call a gate on a qubit or a register. The only 
restriction is that the size of the gate and the size of the qubit or regsiter must be 
equal to each other.

**Arguments:**
    qr {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

**`def qvantum.gate.Fredkin.__init__()`**

Method to initialize Fredkin gate.

**Arguments:**
    control_qubit {Qubit} -- Possible values: 0, 1 or 2

**Raises:**
    ValueError

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.Fredkin(2)

**`def qvantum.gate.Fredkin.get_matrix()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_matrix()
    matrix([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]])

**`def qvantum.gate.Fredkin.get_name()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

**`def qvantum.gate.Fredkin.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

**`def qvantum.gate.Fredkin.power()`**

Method to raise the unitary matrix of the gate to the given power and overwrites the 
original matrix of the gate with the results matrix.

**Arguments:**
    power {int} -- The power which the gate is raised on

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> t = qvantum.Toffoli()
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]])
    >>> t.power(2)
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])

**`def qvantum.gate.Fredkin.set_matrix()`**

Setter of matrix of Fredkin gate. Always raises BaseException.

**Raises:**
    BaseException

**`def qvantum.gate.Fredkin.set_name()`**

Setter of name of Fredkin gate. Always raises BaseException.

**Raises:**
    BaseException

**`class qvantum.gate.Gate`**

gate class

    "In quantum computing and specifically the quantum circuit model of computation, a quantum logic
    gate is a basic quantum circuit operating on a small number of qubits. They are the building blocks
    of quantum circuits, like classical logic gates are for conventional digital circuits.

    Quantum logic gates are represented by unitary matrices. The most common quantum gates operate on
    spaces of one or two qubits, just like the common classical logic gates operate on one or two bits.
    As matrices, quantum gates can be described by 2^n x 2^n sized unitary matrices, where n is the
    number of qubits that the gate act on. The variables that the gates act upon, the quantum states,
    are vectors in 2^n complex dimensions, where n again is the number of qubits of variable:
    The base vectors are the possible outcomes if measured, and a quantum state is a linear combination
    of outcomes."

    via Wikipedia: https://en.wikipedia.org/wiki/Quantum_logic_gate

    The instances of gate class have the following methods:

    - __init__()      - initialization method
    - __call__()      - call method
    - get_name()      - getter of name of gate
    - get_matrix()    - getter of matrix of gate
    - get_size()      - getter of size of matrix of gate
    - set_name()      - setter of name of gate
    - set_matrix()    - setter of matrix of gate
    - power() - raise the matrix of gate to the given power
    
**`def qvantum.gate.Gate.__call__()`**

Method which makes possible to call a gate on a qubit or a register. The only 
restriction is that the size of the gate and the size of the qubit or regsiter must be 
equal to each other.

**Arguments:**
    qr {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

**`def qvantum.gate.Gate.__init__()`**

Method to initialize a 2x2 sized identity matrix. Every identity matrix is a unitary 
matrix as well.

**Examples:**

    >>> import qvantum
    >>>
    >>> g = qvantum.Gate()
    >>> g.get_name()
    'Identity'
    >>> g.get_matrix()
    matrix([[1, 0],
    [0, 1]])
    >>> g.get_size()
    2

**`def qvantum.gate.Gate.get_matrix()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_matrix()
    matrix([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]])

**`def qvantum.gate.Gate.get_name()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

**`def qvantum.gate.Gate.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

**`def qvantum.gate.Gate.power()`**

Method to raise the unitary matrix of the gate to the given power and overwrites the 
original matrix of the gate with the results matrix.

**Arguments:**
    power {int} -- The power which the gate is raised on

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> t = qvantum.Toffoli()
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]])
    >>> t.power(2)
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])

**`def qvantum.gate.Gate.set_matrix()`**

Method to set a new unitary matrix for the gate. If matrix is not unitary then an error 
is raised.

**Arguments:**
    matrix {numpy.ndarray} -- Matrix of the gate to be set

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import numpy
    >>> import qvantum
    >>>
    >>> g = qvantum.Gate()
    >>> g.get_matrix()
    matrix([[1, 0],
    [0, 1]])
    >>> g.set_matrix(numpy.matrix([
    [1 / numpy.sqrt(2), 1 / numpy.sqrt(2)],
    [1 / numpy.sqrt(2), -1 / numpy.sqrt(2)]
    ])
)
    >>> g.get_matrix()
    matrix([[ 0.70710678,  0.70710678],
    [ 0.70710678, -0.70710678]])

**`def qvantum.gate.Gate.set_name()`**

Method to set a new name for the gate.

**Arguments:**
    name {str} -- Name of the gate to be set

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>> g = qvantum.Gate()
    >>> g.get_name()
    'Identity'
    >>> g.set_name('shoe')
    >>> g.get_name()
    'shoe'

**`class qvantum.gate.Hadamard`**

This class is an inherited class from the Gate class. It’s the implementation of the 
    Hadamard gate. Its unitary matrix:

    
**`def qvantum.gate.Hadamard.__call__()`**

Method which makes possible to call a gate on a qubit or a register. The only 
restriction is that the size of the gate and the size of the qubit or regsiter must be 
equal to each other.

**Arguments:**
    qr {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

**`def qvantum.gate.Hadamard.__init__()`**

Method to initialize Hadamard gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.Hadamard()

**`def qvantum.gate.Hadamard.get_matrix()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_matrix()
    matrix([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]])

**`def qvantum.gate.Hadamard.get_name()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

**`def qvantum.gate.Hadamard.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

**`def qvantum.gate.Hadamard.power()`**

Method to raise the unitary matrix of the gate to the given power and overwrites the 
original matrix of the gate with the results matrix.

**Arguments:**
    power {int} -- The power which the gate is raised on

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> t = qvantum.Toffoli()
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]])
    >>> t.power(2)
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])

**`def qvantum.gate.Hadamard.set_matrix()`**

Setter of matrix of Hadamard gate. Always raises BaseException.

**Raises:**
    BaseException

**`def qvantum.gate.Hadamard.set_name()`**

Setter of name of Hadamard gate. Always raises BaseException.

**Raises:**
    BaseException

**`class qvantum.gate.Ising`**

This class is an inherited class from the Gate class. It’s the implementation of the 
    Ising gate. Its unitary matrix:
    
    
**`def qvantum.gate.Ising.__call__()`**

Method which makes possible to call a gate on a qubit or a register. The only 
restriction is that the size of the gate and the size of the qubit or regsiter must be 
equal to each other.

**Arguments:**
    qr {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

**`def qvantum.gate.Ising.__init__()`**

Method to initialize Ising gate.

**Arguments:**
    phi {int, float} -- The used angle

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.Ising(1)

**`def qvantum.gate.Ising.get_matrix()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_matrix()
    matrix([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]])

**`def qvantum.gate.Ising.get_name()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

**`def qvantum.gate.Ising.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

**`def qvantum.gate.Ising.power()`**

Method to raise the unitary matrix of the gate to the given power and overwrites the 
original matrix of the gate with the results matrix.

**Arguments:**
    power {int} -- The power which the gate is raised on

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> t = qvantum.Toffoli()
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]])
    >>> t.power(2)
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])

**`def qvantum.gate.Ising.set_matrix()`**

Setter of matrix of Ising gate. Always raises BaseException.

**Raises:**
    BaseException

**`def qvantum.gate.Ising.set_name()`**

Setter of name of Ising gate. Always raises BaseException.

**Raises:**
    BaseException

**`class qvantum.gate.PauliX`**

This class is an inherited class from the Gate class. It’s the implementation of the 
    Pauli-X gate. Its unitary matrix:
    
    
**`def qvantum.gate.PauliX.__call__()`**

Method which makes possible to call a gate on a qubit or a register. The only 
restriction is that the size of the gate and the size of the qubit or regsiter must be 
equal to each other.

**Arguments:**
    qr {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

**`def qvantum.gate.PauliX.__init__()`**

Method to initialize Pauli-X gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.PauliX()

**`def qvantum.gate.PauliX.get_matrix()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_matrix()
    matrix([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]])

**`def qvantum.gate.PauliX.get_name()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

**`def qvantum.gate.PauliX.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

**`def qvantum.gate.PauliX.power()`**

Method to raise the unitary matrix of the gate to the given power and overwrites the 
original matrix of the gate with the results matrix.

**Arguments:**
    power {int} -- The power which the gate is raised on

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> t = qvantum.Toffoli()
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]])
    >>> t.power(2)
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])

**`def qvantum.gate.PauliX.set_matrix()`**

Setter of matrix of Pauli-X gate. Always raises BaseException.

**Raises:**
    BaseException

**`def qvantum.gate.PauliX.set_name()`**

Setter of name of Pauli-X gate. Always raises BaseException.

**Raises:**
    BaseException

**`class qvantum.gate.PauliY`**

This class is an inherited class from the Gate class. It’s the implementation of the 
    Pauli-Y gate. Its unitary matrix:
    
    
**`def qvantum.gate.PauliY.__call__()`**

Method which makes possible to call a gate on a qubit or a register. The only 
restriction is that the size of the gate and the size of the qubit or regsiter must be 
equal to each other.

**Arguments:**
    qr {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

**`def qvantum.gate.PauliY.__init__()`**

Method to initialize Pauli-Y gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.PauliY()

**`def qvantum.gate.PauliY.get_matrix()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_matrix()
    matrix([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]])

**`def qvantum.gate.PauliY.get_name()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

**`def qvantum.gate.PauliY.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

**`def qvantum.gate.PauliY.power()`**

Method to raise the unitary matrix of the gate to the given power and overwrites the 
original matrix of the gate with the results matrix.

**Arguments:**
    power {int} -- The power which the gate is raised on

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> t = qvantum.Toffoli()
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]])
    >>> t.power(2)
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])

**`def qvantum.gate.PauliY.set_matrix()`**

Setter of matrix of Pauli-Y gate. Always raises BaseException.

**Raises:**
    BaseException

**`def qvantum.gate.PauliY.set_name()`**

Setter of name of Pauli-Y gate. Always raises BaseException.

**Raises:**
    BaseException

**`class qvantum.gate.PauliZ`**

This class is an inherited class from the Gate class. It’s the implementation of the 
    Pauli-Z gate. Its unitary matrix:
    
    
**`def qvantum.gate.PauliZ.__call__()`**

Method which makes possible to call a gate on a qubit or a register. The only 
restriction is that the size of the gate and the size of the qubit or regsiter must be 
equal to each other.

**Arguments:**
    qr {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

**`def qvantum.gate.PauliZ.__init__()`**

Method to initialize Pauli-Z gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.PauliZ()

**`def qvantum.gate.PauliZ.get_matrix()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_matrix()
    matrix([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]])

**`def qvantum.gate.PauliZ.get_name()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

**`def qvantum.gate.PauliZ.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

**`def qvantum.gate.PauliZ.power()`**

Method to raise the unitary matrix of the gate to the given power and overwrites the 
original matrix of the gate with the results matrix.

**Arguments:**
    power {int} -- The power which the gate is raised on

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> t = qvantum.Toffoli()
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]])
    >>> t.power(2)
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])

**`def qvantum.gate.PauliZ.set_matrix()`**

Setter of matrix of Pauli-Z gate. Always raises BaseException.

**Raises:**
    BaseException

**`def qvantum.gate.PauliZ.set_name()`**

Setter of name of Pauli-Z gate. Always raises BaseException.

**Raises:**
    BaseException

**`class qvantum.gate.Phase`**

This class is an inherited class from the Gate class. It’s the implementation of the 
    Phase gate. Its unitary matrix:
    
    
**`def qvantum.gate.Phase.__call__()`**

Method which makes possible to call a gate on a qubit or a register. The only 
restriction is that the size of the gate and the size of the qubit or regsiter must be 
equal to each other.

**Arguments:**
    qr {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

**`def qvantum.gate.Phase.__init__()`**

Method to initialize Phase gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.Phase()

**`def qvantum.gate.Phase.get_matrix()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_matrix()
    matrix([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]])

**`def qvantum.gate.Phase.get_name()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

**`def qvantum.gate.Phase.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

**`def qvantum.gate.Phase.power()`**

Method to raise the unitary matrix of the gate to the given power and overwrites the 
original matrix of the gate with the results matrix.

**Arguments:**
    power {int} -- The power which the gate is raised on

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> t = qvantum.Toffoli()
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]])
    >>> t.power(2)
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])

**`def qvantum.gate.Phase.set_matrix()`**

Setter of matrix of Phase gate. Always raises BaseException.

**Raises:**
    BaseException

**`def qvantum.gate.Phase.set_name()`**

Setter of name of Phase gate. Always raises BaseException.

**Raises:**
    BaseException

**`class qvantum.gate.Pi8`**

This class is an inherited class from the Gate class. It’s the implementation of the 
    Pi/8 gate. Its unitary matrix:
    
    
**`def qvantum.gate.Pi8.__call__()`**

Method which makes possible to call a gate on a qubit or a register. The only 
restriction is that the size of the gate and the size of the qubit or regsiter must be 
equal to each other.

**Arguments:**
    qr {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

**`def qvantum.gate.Pi8.__init__()`**

Method to initialize Pi/8 gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.Pi8()

**`def qvantum.gate.Pi8.get_matrix()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_matrix()
    matrix([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]])

**`def qvantum.gate.Pi8.get_name()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

**`def qvantum.gate.Pi8.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

**`def qvantum.gate.Pi8.power()`**

Method to raise the unitary matrix of the gate to the given power and overwrites the 
original matrix of the gate with the results matrix.

**Arguments:**
    power {int} -- The power which the gate is raised on

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> t = qvantum.Toffoli()
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]])
    >>> t.power(2)
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])

**`def qvantum.gate.Pi8.set_matrix()`**

Setter of matrix of Pi/8 gate. Always raises BaseException.

**Raises:**
    BaseException

**`def qvantum.gate.Pi8.set_name()`**

Setter of name of Pi/8 gate. Always raises BaseException.

**Raises:**
    BaseException

**`class qvantum.gate.SquareNot`**

This class is an inherited class from the Gate class. It’s the implementation of the 
    Square-Not gate. Its unitary matrix:
    
    
**`def qvantum.gate.SquareNot.__call__()`**

Method which makes possible to call a gate on a qubit or a register. The only 
restriction is that the size of the gate and the size of the qubit or regsiter must be 
equal to each other.

**Arguments:**
    qr {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

**`def qvantum.gate.SquareNot.__init__()`**

Method to initialize Square-Not gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.SquareNot()

**`def qvantum.gate.SquareNot.get_matrix()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_matrix()
    matrix([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]])

**`def qvantum.gate.SquareNot.get_name()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

**`def qvantum.gate.SquareNot.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

**`def qvantum.gate.SquareNot.power()`**

Method to raise the unitary matrix of the gate to the given power and overwrites the 
original matrix of the gate with the results matrix.

**Arguments:**
    power {int} -- The power which the gate is raised on

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> t = qvantum.Toffoli()
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]])
    >>> t.power(2)
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])

**`def qvantum.gate.SquareNot.set_matrix()`**

Setter of matrix of Square-Not gate. Always raises BaseException.

**Raises:**
    BaseException

**`def qvantum.gate.SquareNot.set_name()`**

Setter of name of Square-Not gate. Always raises BaseException.

**Raises:**
    BaseException

**`class qvantum.gate.SquareSwap`**

This class is an inherited class from the Gate class. It’s the implementation of the 
    Square-Swap gate. Its unitary matrix:
    
    
**`def qvantum.gate.SquareSwap.__call__()`**

Method which makes possible to call a gate on a qubit or a register. The only 
restriction is that the size of the gate and the size of the qubit or regsiter must be 
equal to each other.

**Arguments:**
    qr {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

**`def qvantum.gate.SquareSwap.__init__()`**

Method to initialize Square-Swap gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.SquareSwap()

**`def qvantum.gate.SquareSwap.get_matrix()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_matrix()
    matrix([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]])

**`def qvantum.gate.SquareSwap.get_name()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

**`def qvantum.gate.SquareSwap.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

**`def qvantum.gate.SquareSwap.power()`**

Method to raise the unitary matrix of the gate to the given power and overwrites the 
original matrix of the gate with the results matrix.

**Arguments:**
    power {int} -- The power which the gate is raised on

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> t = qvantum.Toffoli()
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]])
    >>> t.power(2)
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])

**`def qvantum.gate.SquareSwap.set_matrix()`**

Setter of matrix of Square-Swap gate. Always raises BaseException.

**Raises:**
    BaseException

**`def qvantum.gate.SquareSwap.set_name()`**

Setter of name of Square-Swap gate. Always raises BaseException.

**Raises:**
    BaseException

**`class qvantum.gate.Swap`**

This class is an inherited class from the Gate class. It’s the implementation of the 
    Swap gate. Its unitary matrix:
    
    
**`def qvantum.gate.Swap.__call__()`**

Method which makes possible to call a gate on a qubit or a register. The only 
restriction is that the size of the gate and the size of the qubit or regsiter must be 
equal to each other.

**Arguments:**
    qr {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

**`def qvantum.gate.Swap.__init__()`**

Method to initialize Swap gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.Swap()

**`def qvantum.gate.Swap.get_matrix()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_matrix()
    matrix([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]])

**`def qvantum.gate.Swap.get_name()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

**`def qvantum.gate.Swap.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

**`def qvantum.gate.Swap.power()`**

Method to raise the unitary matrix of the gate to the given power and overwrites the 
original matrix of the gate with the results matrix.

**Arguments:**
    power {int} -- The power which the gate is raised on

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> t = qvantum.Toffoli()
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]])
    >>> t.power(2)
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])

**`def qvantum.gate.Swap.set_matrix()`**

Setter of matrix of Swap gate. Always raises BaseException.

**Raises:**
    BaseException

**`def qvantum.gate.Swap.set_name()`**

Setter of name of Swap gate. Always raises BaseException.

**Raises:**
    BaseException

**`class qvantum.gate.Toffoli`**

This class is an inherited class from the Gate class. It’s the implementation of the 
    Toffoli gate. It’s called on 3 qubits. The parameters determine which one is the target 
    qubit – 0, 1 or 2.Its unitary matrix:
    
    
**`def qvantum.gate.Toffoli.__call__()`**

Method which makes possible to call a gate on a qubit or a register. The only 
restriction is that the size of the gate and the size of the qubit or regsiter must be 
equal to each other.

**Arguments:**
    qr {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

**`def qvantum.gate.Toffoli.__init__()`**

Method to initialize Toffoli gate.

**Arguments:**
    target_qubit {Qubit} -- Possible values: 0, 1 or 2

**Raises:**
    ValueError

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.Toffoli(0)

**`def qvantum.gate.Toffoli.get_matrix()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_matrix()
    matrix([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]])

**`def qvantum.gate.Toffoli.get_name()`**

Method to return the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

**`def qvantum.gate.Toffoli.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

**`def qvantum.gate.Toffoli.power()`**

Method to raise the unitary matrix of the gate to the given power and overwrites the 
original matrix of the gate with the results matrix.

**Arguments:**
    power {int} -- The power which the gate is raised on

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> t = qvantum.Toffoli()
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]])
    >>> t.power(2)
    >>> t.get_matrix()
    matrix([[1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]])

**`def qvantum.gate.Toffoli.set_matrix()`**

Setter of matrix of Toffoli gate. Always raises BaseException.

**Raises:**
    BaseException

**`def qvantum.gate.Toffoli.set_name()`**

Setter of name of Toffoli gate. Always raises BaseException.

**Raises:**
    BaseException

# qvantum.layer module

**`def qvantum.layer.__init__()`**

Initialize self.  See help(type(self)) for accurate signature.
**`class qvantum.layer.Layer`**

layer class

    An instance of layer class represents one stage in a given quantum computional process. The 
    layer is created by defining the gates which are contained by the given layer. The order of 
    gates refers to that qubit which is affected by the given gate. Using the instances of layer 
    class the user can build an instance of circuit class.

    The instances of layer class have the following methods:

    - __init__() - initialization method
    - get_gate_list()    - getter of gates in gate list
    - get_gate_number()  - getter of number of gates
    - get_nth_gate()     - getter of n-th gate
    - get_layer_matrix() - getter of result of Kronecker product of matrices in gate list
    - get_matrix_size()  - getter of size of layer matrix (equals to the size of states on 
which the layer is usable)
    - get_layer_size()   - getter of size of layer (equals to the size of register on 
which the layer is usable)
    - delete_gate()      - delete gate from layer
    - insert_gate()      - insert gate into layer
    
**`def qvantum.layer.Layer.__call__()`**

Call self as a function.
**`def qvantum.layer.Layer.__init__()`**

Method to initialize an instance of the Layer class. The argument must be a list of 
objects in the Gate class or in an inherited class such as: Hadamard, SquareNot, PauliX, 
PauliY, PauliZ, Phase, Pi8, Swap, SquareSwap, CNOT, ControlledZ, ControlledPhase, Ising, 
Toffoli, Fredkin.

**Arguments:**
    gate_list {list} -- List of objects from Gate class

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> l1 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l1.get_gate_list()
    OrderedDict([(0, <qvantum.gate.Hadamard at 0x1ae588c2d68>), (1, <qvantum.gate.Gate at 0x1ae56a08a20>)])
    >>> l2 = qvantum.Layer([qvantum.PauliX()])
    >>> l2.get_layer_matrix()
    matrix([[0., 1.],
    [1., 0.]])

**`def qvantum.layer.Layer.delete_gate()`**

Method to delete the n-th gate from the current Layer object. The parameter must be 
equal to or bigger than 0 and less than the actual size of the Layer.

**Arguments:**
    nth {int} -- Number of n-th possible gate

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate(), qvantum.PauliX()])
    >>> l.get_gate_list()
    OrderedDict([(0, <qvantum.gate.Hadamard at 0x1ae59262ba8>), (1, <qvantum.gate.Gate at 0x1ae58146ba8>), (2, <qvantum.gate.PauliX at 0x1ae59262d30>)])
    >>> l.delete_gate(3)
    ---------------------------------------------------------------------------
    ValueErrorTraceback (most recent call last)
    <ipython-input-24-9e9f639d1d88> in <module>
    ----> 1 l.delete_gate(3)

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_layer.py in wrapper(self, nth)
41 
42 if isinstance(nth, int):
    ---> 43     return function(self, nth)
44 
45 else:

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\layer.py in delete_gate(self, nth)
98 else:
99     raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +    --> 100 'less or equal to ' + str(len(self.__gate_list) - 1) + '.')
101 
102     @check_layer.insert_gate_check

    ValueError: Invalid input! Argument must be greater or equal to 0 and less or equal to 2.
    >>> l.delete_gate(0)
    >>> l.get_gate_list()
    OrderedDict([(0, <qvantum.gate.Gate at 0x1cff211fda0>), (1, <qvantum.gate.PauliX at 0x1cff3f5f4a8>)])

**`def qvantum.layer.Layer.get_gate_list()`**

Method to return the gates which are contained by the current Layer object.

**Examples:**

    >>> import qvantum
    >>>
    >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l.get_gate_list()
    OrderedDict([(0, <qvantum.gate.Hadamard at 0x1ae588c2d68>), (1, <qvantum.gate.Gate at 0x1ae56a08a20>)])

**`def qvantum.layer.Layer.get_gate_number()`**

Method to return the number of the gates which are contained by the current Layer object.

**Examples:**

    >>> import qvantum
    >>>
    >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l.get_gate_number()
    2

**`def qvantum.layer.Layer.get_layer_matrix()`**

Method to return the result of the Kronecker multiplication of the gates’ matrices 
which are contained by the current Layer object. When the Layer is applied on a Register 
during one step of a calculation the state vector of the Register is multiplied by this 
matrix.

**Examples:**

    >>> import qvantum
    >>>
    >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l.get_layer_matrix()
    matrix([[ 0.70710678,  0.,  0.70710678,  0.],
    [ 0.,  0.70710678,  0.,  0.70710678],
    [ 0.70710678,  0., -0.70710678, -0.],
    [ 0.,  0.70710678, -0., -0.70710678]])

**`def qvantum.layer.Layer.get_layer_size()`**

Method to return the size of the current Layer object. Remember, it’s not the size 
of the matrix of the current Layer object but the size of a Register object which the 
Layer can be applied on.

**Examples:**

    >>> import qvantum
    >>>
    >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l.get_layer_matrix()
    matrix([[ 0.70710678,  0.,  0.70710678,  0.],
    [ 0.,  0.70710678,  0.,  0.70710678],
    [ 0.70710678,  0., -0.70710678, -0.],
    [ 0.,  0.70710678, -0., -0.70710678]])
    >>> l.get_matrix_size()
    4
    >>> l.get_layer_size()
    2

**`def qvantum.layer.Layer.get_matrix_size()`**

Method to return the size of the matrix of the current Layer object.

**Examples:**

    >>> import qvantum
    >>>
    >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l.get_layer_matrix()
    matrix([[ 0.70710678,  0.,  0.70710678,  0.],
    [ 0.,  0.70710678,  0.,  0.70710678],
    [ 0.70710678,  0., -0.70710678, -0.],
    [ 0.,  0.70710678, -0., -0.70710678]])
    >>> l.get_matrix_size()
    4

**`def qvantum.layer.Layer.get_nth_gate()`**

Method to return the n-th gate in the current Layer object. The parameter must be 
between 0 and the actual number of the gates.

**Arguments:**
    nth {int} -- Number of n-th possible gate

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l.get_nth_gate(0)
    <qvantum.gate.Hadamard at 0x1ae588c2d68>
    >>> l.get_nth_gate(1)
    <qvantum.gate.Gate at 0x1ae56a08a20>
    >>> l.get_nth_gate(2)
    ---------------------------------------------------------------------------
    KeyError  Traceback (most recent call last)
    <ipython-input-18-5075d5884ea2> in <module>
    ----> 1 l1.get_nth_gate(2)

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_layer.py in wrapper(self, nth)
27 
28 if isinstance(nth, int):
    ---> 29     return function(self, nth)
30 
31 else:

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\layer.py in get_nth_gate(self, nth)
53 ''' getter of n-th gate '''
54 
    ---> 55 return self.__gate_list[nth]
56 
57     def get_layer_matrix(self):

    KeyError: 2

**`def qvantum.layer.Layer.insert_gate()`**

Method to insert a Gate object into the n-th place in the current Layer object. The 
first parameter must be a Gate object or an object in an inherited class such as: 
Hadamard, SquareNot, PauliX, PauliY, PauliZ, Phase, Pi8, Swap, SquareSwap, CNOT, 
ControlledZ, ControlledPhase, Ising, Toffoli, Fredkin. The second parameter must be equal 
to or bigger than 0 and equal to or less than the actual size of the Layer.

**Arguments:**
    g {gate} -- The gate to be inserted
    nth {int} -- The index where the gate is inserted

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate(), qvantum.PauliX()])
    >>> l.get_gate_list()
    OrderedDict([(0, <qvantum.gate.Hadamard at 0x1ae59262ba8>), (1, <qvantum.gate.Gate at 0x1ae58146ba8>), (2, <qvantum.gate.PauliX at 0x1ae59262d30>)])
    >>> l.insert_gate(qvantum.PauliY(), 4)
    ---------------------------------------------------------------------------
    ValueErrorTraceback (most recent call last)
    <ipython-input-32-16da0a14a92d> in <module>
    ----> 1 l.insert_gate(qvantum.PauliY(), 4)

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_layer.py in wrapper(self, g, nth)
57     gate.ControlledZ, gate.ControlledPhase, gate.Ising, gate.Toffoli, gate.Fredkin)) 58     and isinstance(nth, int):
    ---> 59     return function(self, g, nth)
60 
61 else:

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\layer.py in insert_gate(self, g, nth)
123 else:
124     raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +    --> 125 'less or equal to ' + str(len(self.__gate_list)) + '.')

    ValueError: Invalid input! Argument must be greater or equal to 0 and less or equal to 2.
    >>> l.insert_gate(qvantum.PauliY(), 1)
    >>> l.get_gate_list()
    OrderedDict([(0, <qvantum.gate.Hadamard at 0x1ae59266470>),
 (1, <qvantum.gate.PauliY at 0x1ae5923d400>),
 (2, <qvantum.gate.Gate at 0x1ae59266438>),
 (3, <qvantum.gate.PauliX at 0x1ae59266390>)])
    >>> l.insert_gate(qvantum.PauliY(), 4)
    >>> l.get_gate_list()
    OrderedDict([(0, <qvantum.gate.Hadamard at 0x1ae59266470>),
 (1, <qvantum.gate.PauliY at 0x1ae5923d400>),
 (2, <qvantum.gate.Gate at 0x1ae59266438>),
 (3, <qvantum.gate.PauliX at 0x1ae59266390>),
 (4, <qvantum.gate.PauliY at 0x1ae59266400>)])

# qvantum.qubit module

**`def qvantum.qubit.__init__()`**

Initialize self.  See help(type(self)) for accurate signature.
**`class qvantum.qubit.Qubit`**

qubit class

    In quantum computing a qubit or quantum bit is the basic unit of quantum information. Every 
    qubit has two clear states such as 0 and 1 but unlike a classical bit a qubit can be in 
    superposition which is a special  mixture of these clear states. Using qubit class, the user 
    can create qubit objects. When creating a qubit object, the amplitudes must satisfy that 
    |alpha|^2 + |beta|^2 = 1.

    Instances of qubit class have the following methods:

    - __init__()       - initialize qubit
    - get_alpha()      - getter of alpha
    - get_beta()       - getter of beta
    - set_amplitudes() - setter of alpha, beta
    - show()   - qubit representation
    - measure()- measure qubit
    - ket()    - return the ket vector of qubit
    - bra()    - return the bra vector of qubit

    The random_qubit class is the same as qubit class the only difference that an instance of the
    class is created with random amplitudes (alpha, beta). They share the same methods.
    
**`def qvantum.qubit.Qubit.__call__()`**

Call self as a function.
**`def qvantum.qubit.Qubit.__init__()`**

Method to initialize an instance of the qubit class. The squared sum of alpha and beta 
must be equal to zero otherwise a ValueError will be thrown.

**Arguments:**
    alpha {int, float, complex} -- Amplitude or probability of being in state 0
    beta {int, float, complex} -- Amplitude or probability of being in state 1

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import math
    >>> import qvantum
    >>>
    >>> q = qvantum.Qubit(1, 0)
    >>> q.show()
    '|Ψ> = (1.0000+0.0000i)|0> + (0.0000+0.0000i)|1>'
    >>> qvantum.Qubit(1 / math.sqrt(2), 1 / math.sqrt(2)).show()
    '|Ψ> = (0.7071+0.0000i)|0> + (0.7071+0.0000i)|1>'
    >>> q = qvantum.Qubit(5, 2)
    ---------------------------------------------------------------------------
    ValueErrorTraceback (most recent call last)
    <ipython-input-5-9536e50fb31e> in <module>
    ----> 1 q = qvantum.Qubit(5, 2)

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_qubit.py in wrapper(self, alpha, beta)
14     else:
15 raise ValueError('Invalid input! Alpha and beta must statisfy: ' +    ---> 16     '|alpha|² + |beta|² = 1.')
17 
18 else:

    ValueError: Invalid input! Alpha and beta must statisfy: |alpha|² + |beta|² = 1.
    >>> q = qvantum.Qubit(1, ’shoe’)
      File "<ipython-input-6-7c844cc7dd1e>", line 1
    q = qvantum.Qubit(1, ’shoe’)
     ^
    SyntaxError: invalid character in identifier

**`def qvantum.qubit.Qubit.bra()`**

Method to return with the bra vector representation of the qubit.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.bra()
    array([[-0.76536276+0.20163924j, -0.39225178-0.46872167j]])

**`def qvantum.qubit.Qubit.get_alpha()`**

Getter method of alpha.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Qubit(1, 0)
    >>> q.get_alpha()
    1

**`def qvantum.qubit.Qubit.get_beta()`**

Getter method of beta.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Qubit(1, 0)
    >>> q.get_beta()
    0

**`def qvantum.qubit.Qubit.ket()`**

Method to return with the ket vector representation of the qubit.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.ket()
    array([[-0.76536276+0.20163924j],
   [-0.39225178-0.46872167j]])

**`def qvantum.qubit.Qubit.measure()`**

Method to perform a measurement on the qubit and return with one clear state by the 
distribtion according to the coefficients.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (-0.2867+0.5283i)|0> + (-0.2608+0.7555i)|1>'
    >>> q.measure()
    1
    >>> q.show()
    '|Ψ> = (0.0000+0.0000i)|0> + (1.0000+0.0000i)|1>'

**`def qvantum.qubit.Qubit.set_amplitudes()`**

Setter method to replace the old coefficients to new ones. The squared sum of alpha and 
beta must be equal to zero otherwise a ValueError will be thrown.

**Arguments:**
    alpha {int, float, complex} -- Amplitude or probability of being in state 0
    beta {int, float, complex} -- Amplitude or probability of being in state 1

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import math
    >>> import qvantum
    >>>
    >>> q = qvantum.Qubit(1, 0)
    >>> q.show()
    '|Ψ> = (1.0000+0.0000i)|0> + (0.0000+0.0000i)|1>'
    >>> q.set_amplitudes(0, 1)
    >>> q.show()
    '|Ψ> = (0.0000+0.0000i)|0> + (1.0000+0.0000i)|1>'

**`def qvantum.qubit.Qubit.show()`**

Method to show the state function of the qubit object.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Qubit(1, 0)
    >>> q.show()
    '|Ψ> = (1.0000+0.0000i)|0> + (0.0000+0.0000i)|1>'

**`class qvantum.qubit.Random_Qubit`**

This is an inhereted class from the Qubit class. They share the same methods but when an 
    instance of the Random_Qubit class is created the coefficients are randomly choosen.
    
**Arguments:**
Qubit {qubit} -- qubit class
    
**`def qvantum.qubit.Random_Qubit.__call__()`**

Call self as a function.
**`def qvantum.qubit.Random_Qubit.__init__()`**

Method to initialize an instance of the qubit class with randomized amplitudes.

**Examples:**

    >>> import qvantum
    >>>
    >>> rq = qvantum.Random_Qubit()
    >>> rq.show()
    '|Ψ> = (-0.5736+0.2506i)|0> + (0.5223-0.5791i)|1>'
    >>> qvantum.Random_Qubit().show()
    '|Ψ> = (-0.1949+0.9475i)|0> + (0.1028+0.2318i)|1>'

**`def qvantum.qubit.Random_Qubit.bra()`**

Method to return with the bra vector representation of the qubit.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.bra()
    array([[-0.76536276+0.20163924j, -0.39225178-0.46872167j]])

**`def qvantum.qubit.Random_Qubit.get_alpha()`**

Getter method of alpha.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Qubit(1, 0)
    >>> q.get_alpha()
    1

**`def qvantum.qubit.Random_Qubit.get_beta()`**

Getter method of beta.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Qubit(1, 0)
    >>> q.get_beta()
    0

**`def qvantum.qubit.Random_Qubit.ket()`**

Method to return with the ket vector representation of the qubit.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.ket()
    array([[-0.76536276+0.20163924j],
   [-0.39225178-0.46872167j]])

**`def qvantum.qubit.Random_Qubit.measure()`**

Method to perform a measurement on the qubit and return with one clear state by the 
distribtion according to the coefficients.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (-0.2867+0.5283i)|0> + (-0.2608+0.7555i)|1>'
    >>> q.measure()
    1
    >>> q.show()
    '|Ψ> = (0.0000+0.0000i)|0> + (1.0000+0.0000i)|1>'

**`def qvantum.qubit.Random_Qubit.set_amplitudes()`**

Setter method to replace the old coefficients to new ones. The squared sum of alpha and 
beta must be equal to zero otherwise a ValueError will be thrown.

**Arguments:**
    alpha {int, float, complex} -- Amplitude or probability of being in state 0
    beta {int, float, complex} -- Amplitude or probability of being in state 1

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import math
    >>> import qvantum
    >>>
    >>> q = qvantum.Qubit(1, 0)
    >>> q.show()
    '|Ψ> = (1.0000+0.0000i)|0> + (0.0000+0.0000i)|1>'
    >>> q.set_amplitudes(0, 1)
    >>> q.show()
    '|Ψ> = (0.0000+0.0000i)|0> + (1.0000+0.0000i)|1>'

**`def qvantum.qubit.Random_Qubit.show()`**

Method to show the state function of the qubit object.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Qubit(1, 0)
    >>> q.show()
    '|Ψ> = (1.0000+0.0000i)|0> + (0.0000+0.0000i)|1>'

# qvantum.register module

**`def qvantum.register.__init__()`**

Initialize self.  See help(type(self)) for accurate signature.
**`class qvantum.register.Register`**

register class
   
    A system containing more than one qubit is called a register. The state function of a 
    register is the superposition of the allowed states of the qubits. The number of possible 
    states is increasing exponentially with every new qubit is added to the system.

    "A quantum register is a system comprising multiple qubits and is the quantum analog of the 
    classical processor register. An n size quantum register is a quantum system comprising n qubits.
    The Hilbert space, H, in which the data stored in a quantum register is:

H = H(n-1) × H(n-2) × ... × H(0)."

    via Wikipedia: https://en.wikipedia.org/wiki/Quantum_register

    The instances of the register class have the following methods:

    - __init__()  - initialize register
    - get_coeff_list()    - getter of coefficients of qubits
    - get_state_number()  - getter of number of possible states
    - get_qubit_number()  - getter of number of qubits in the register
    - get_states()- getter of states
    - get_amplitudes()    - getter of amplitudes
    - set_amplitudes()    - setter of amplitudes
    - show()      - register representation
    - measure_register()  - measure the whole register
    - measure_nth_qubit() - measure the n-th qubit
    - ket()       - return the ket vector of register
    - bra()       - return the bra vector of register
    - delete_qubit()      - delete qubit from register
    - insert_qubit()      - insert qubit into register
    
**`def qvantum.register.Register.__call__()`**

Call self as a function.
**`def qvantum.register.Register.__init__()`**

Method to initialize an instance of the register class. The input is a list of elements 
in Qubit or Random_Qubit class. Also this list must contain at least 2 elements.

**Arguments:**
    qubit_list {list} -- List of objects from Qubit or Random_Qubit class

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q2 = qvantum.Random_Qubit()
    >>>
    >>> r1 = qvantum.Register([q1])
    ---------------------------------------------------------------------------
    ValueErrorTraceback (most recent call last)
    <ipython-input-28-3c854882d136> in <module>
    ----> 1 r1 = qvantum.Register([q1])

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, qubit_list)
18     else:
19 raise ValueError('Invalid input! Qubit list must contain at least 2 qubit ' +    ---> 20     'object.')
21 
22 else:

    ValueError: Invalid input! Qubit list must contain at least 2 qubit object.
    >>> r1 = qvantum.Register([q1, ’shoe’])
      File "<ipython-input-29-5fa49e76c5fb>", line 1
r1 = qvantum.Register([q1, ’shoe’])
^
    SyntaxError: invalid character in identifier
    >>> r1 = qvantum.Register({q1, q2})
    ---------------------------------------------------------------------------
    TypeError Traceback (most recent call last)
    <ipython-input-30-ac8d1c1cef5d> in <module>
    ----> 1 r1 = qvantum.Register({q1, q2})

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, qubit_list)
21 
22 else:
    ---> 23     raise TypeError('Invalid input! Argument must be a list of qubit objects.')
24 
25     return wrapper

    TypeError: Invalid input! Argument must be a list of qubit objects.
    >>> r2 = qvantum.Register([q1, q2])
    >>> r2.show()
    '|Ψ> = (-0.4171-0.2953i)|00> + (-0.4106-0.7059i)|01> + (-0.1120-0.0875i)|10> + (-0.1049-0.2015i)|11>'

**`def qvantum.register.Register.bra()`**

Method to return with the bra vector representation of the register.

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q2 = qvantum.Random_Qubit()
    >>>
    >>> r = qvantum.Register([q1, q2])
    >>> r.show()
    '|Ψ> = (-0.0257-0.2734i)|00> + (-0.2956-0.0263i)|01> + (0.0982+0.6134i)|10> + (0.6711+0.0160i)|11>'
    >>> r.bra()
    array([[-0.02572105-0.27339407j, -0.29557738-0.02631109j, 0.09820458+0.61339158j,  0.67110846+0.01599728j]])

**`def qvantum.register.Register.delete_qubit()`**

Method to delete the n-th qubit from the regsiter. This method has some drawback which 
is discussed later. The input parameter must be an integer corresponding to the number of 
qubits in the register.

**Arguments:**
    nth {int} -- Number of n-th possible qubit

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q2 = qvantum.Random_Qubit()
    >>> q3 = qvantum.Random_Qubit()
    >>>
    >>> r = qvantum.Register([q1, q2, q3])
    >>> r.show()
    '|Ψ> = (-0.0414-0.7876i)|000> + (-0.3986-0.4355i)|001> + (-0.0142+0.0084i)|010> + (-0.0042+0.0116i)|011> + (0.1003-0.0924i)|100> + (0.0140-0.1011i)|101> + (-0.0027-0.0010i)|110> + (-0.0020+0.0007i)|111>'
    >>> r.delete_qubit(3)
    ---------------------------------------------------------------------------
    ValueErrorTraceback (most recent call last)
    <ipython-input-96-60bd02f79762> in <module>
    ----> 1 r.delete_qubit(3)

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, nth)
90 
91 if isinstance(nth, int):
    ---> 92     return function(self, nth)
93 
94 else:

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum
egister.py in delete_qubit(self, nth)
219 else:
220     raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +    --> 221 'less or equal to ' + str(self.get_qubit_number() - 1) + '.')
222 
223     @check_register.insert_qubit_check

    ValueError: Invalid input! Argument must be greater or equal to 0 and less or equal to 2.
    >>> r.delete_qubit()
    ---------------------------------------------------------------------------
    TypeError Traceback (most recent call last)
    <ipython-input-97-82d89a96f88c> in <module>
    ----> 1 r.delete_qubit()

    TypeError: wrapper() missing 1 required positional argument: 'nth'
    >>> r.delete_qubit()
    >>> r.show()
    '|Ψ> = (0.4927-0.6160i)|00> + (-0.0083-0.5904i)|01> + (0.1364-0.0024i)|10> + (0.0777-0.0663i)|11>'

**`def qvantum.register.Register.get_amplitudes()`**

Method to return with the coefficient of the n-th possible state for the regsiter 
if the parameter is definit. If it isn’t, then the return value is the list of the 
coefficients of all possible states.

**Keyword Arguments:**
    nth {int, None} -- Number of n-th possible amplitude (default: {None})

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q2 = qvantum.Random_Qubit()
    >>>
    >>> r = qvantum.Register([q1, q2])
    >>> r.show()
    '|Ψ> = (0.1075+0.7037i)|00> + (0.6331-0.0247i)|01> + (0.2171-0.0638i)|10> + (-0.0347-0.1983i)|11>'
    >>> r.get_amplitudes(2)
    (-0.10034614628094177-0.1325886060571926j)
    >>> r.get_amplitudes(6)
    ---------------------------------------------------------------------------
    IndexErrorTraceback (most recent call last)
    <ipython-input-60-102f3b99b88f> in <module>
    ----> 1 r.get_amplitudes(6)

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, nth)
44 
45 if isinstance(nth, int) or nth is None:
    ---> 46     return function(self, nth)
47 
48 else:

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum
egister.py in get_amplitudes(self, nth)
97 
98 else:
    ---> 99     return list(self.__state_vector.values())[nth]
100 
101     @check_register.set_amplitudes_check

    IndexError: list index out of range
    >>> r.get_amplitudes('shoe')
    ---------------------------------------------------------------------------
    TypeError Traceback (most recent call last)
    <ipython-input-61-7cf70dfde286> in <module>
    ----> 1 r.get_amplitudes('shoe')

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, nth)
47 
48 else:
    ---> 49     raise TypeError('Invalid input! Argument must be integer or None type.')
50 
51     return wrapper

    TypeError: Invalid input! Argument must be integer or None type.

**`def qvantum.register.Register.get_coeff_list()`**

Method to return the coefficients of the qubits in the regsiter.

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q2 = qvantum.Random_Qubit()
    >>>
    >>> r = qvantum.Register([q1, q2])
    >>> r.show()
    '|Ψ> = (0.1096+0.0234i)|00> + (0.0122-0.3006i)|01> + (-0.3031-0.1320i)|10> + (-0.2118+0.8619i)|11>'
    >>> r.get_coeff_list()
    [[(-0.2655665168302703+0.18036065646408225j),
      (0.873769688896956-0.3653368165178533j)],
     [(-0.24150232744743877-0.25201257747977823j),
      (-0.5574180512412585+0.7532937028675246j)]]

**`def qvantum.register.Register.get_qubit_number()`**

Method to return the number of the qubits in the register.

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q2 = qvantum.Random_Qubit()
    >>>
    >>> r = qvantum.Register([q1, q2])
    >>> r.show()
    '|Ψ> = (0.0512+0.2330i)|00> + (0.9621+0.0483i)|01> + (0.0054+0.0291i)|10> + (0.1193+0.0100i)|11>'
    >>> r.get_state_number()
    2

**`def qvantum.register.Register.get_state_number()`**

Method to return the number of the possible clear states for the register.

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q2 = qvantum.Random_Qubit()
    >>>
    >>> r = qvantum.Register([q1, q2])
    >>> r.show()
    '|Ψ> = (0.1887+0.2917i)|00> + (-0.5572-0.5995i)|01> + (-0.0366-0.1750i)|10> + (0.1566+0.3910i)|11>'
    >>> r.get_state_number()
    4

**`def qvantum.register.Register.get_states()`**

Method to return with the n-th possible state for the regsiter if the parameter is 
definit. If it isn’t then the return value is the list of all possible states.

**Keyword Arguments:**
    nth {int, None} -- Number of n-th possible state (default: {None})

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q2 = qvantum.Random_Qubit()
    >>>
    >>> r = qvantum.Register([q1, q2])
    >>> r.show()
    '|Ψ> = (0.0184-0.0130i)|00> + (0.0597+0.1181i)|01> + (-0.1003-0.1326i)|10> + (0.8560-0.4708i)|11>'
    >>> r.get_states()
    ['00', '01', '10', '11']
    >>> r.get_states(2)
    '10'
    >>> r.get_states(6)
    ---------------------------------------------------------------------------
    IndexErrorTraceback (most recent call last)
    <ipython-input-54-96382c883aac> in <module>
    ----> 1 r.get_states(6)

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, nth)
31 
32 if isinstance(nth, int) or nth is None:
    ---> 33     return function(self, nth)
34 
35 else:

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum
egister.py in get_states(self, nth)
87 
88 else:
    ---> 89     return list(self.__state_vector.keys())[nth]
90 
91     @check_register.get_amplitudes_check

    IndexError: list index out of range
    >>> r.get_states('shoe')
    ---------------------------------------------------------------------------
    TypeError Traceback (most recent call last)
    <ipython-input-55-613fb9d4ee8b> in <module>
    ----> 1 r.get_states('shoe')

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, nth)
34 
35 else:
    ---> 36     raise TypeError('Invalid input! Argument must be integer.')
37 
38     return wrapper

    TypeError: Invalid input! Argument must be integer.

**`def qvantum.register.Register.insert_qubit()`**

Method to insert a given qubit into a register. The input parameter must be an integer 
corresponding to the number of qubits in the register.

**Arguments:**
    q {qubit} -- The qubit to be inserted
    nth {int} -- The index where the qubit is inserted

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q2 = qvantum.Random_Qubit()
    >>>
    >>> r = qvantum.Register([q1, q2])
    >>> r.show()
    '|Ψ> = (0.2206+0.0465i)|00> + (0.1222-0.4511i)|01> + (0.1796+0.3251i)|10> + (0.6939-0.3335i)|11>'
    >>> q3 = qvantum.Random_Qubit()
    >>> r.insert_qubit(q3, 3)
    ---------------------------------------------------------------------------
    ValueErrorTraceback (most recent call last)
    <ipython-input-103-9f4b9a58253e> in <module>
    ----> 1 r.insert_qubit(q3, 3)

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, q, nth)
103 
104 if isinstance(q, (qubit.Qubit, qubit.Random_Qubit)) and isinstance(nth, int):
    --> 105     return function(self, q, nth)
106 
107 else:

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum
egister.py in insert_qubit(self, q, nth)
241 else:
242     raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +    --> 243 'less or equal to ' + str(self.get_qubit_number()) + '.')

    ValueError: Invalid input! Argument must be greater or equal to 0 and less or equal to 2.
    >>> r.insert_qubit(q3, 2)
    >>> r.show()
    '|Ψ> = (-0.0764+0.1775i)|000> + (-0.0002-0.1162i)|001> + (0.3584+0.1790i)|010> + (-0.2404-0.0133i)|011> + (-0.3035+0.0960i)|100> + (0.1446-0.1253i)|101> + (0.1629+0.6394i)|110> + (-0.2424-0.3140i)|111>'
    >>> r.insert_qubit(q3, 2)
    >>> r.show()
    '|Ψ> = (-0.1362-0.0942i)|0000> + (0.0976+0.0195i)|0001> + (0.0976+0.0195i)|0010> + (-0.0585+0.0125i)|0011> + (-0.2109+0.2709i)|0100> + (0.0518-0.1998i)|0101> + (0.0518-0.1998i)|0110> + (0.0190+0.1226i)|0111> + (-0.0293-0.2712i)|1000> + (0.0809+0.1427i)|1001> + (0.0809+0.1427i)|1010> + (-0.0786-0.0595i)|1011> + (-0.5648+0.0288i)|1100> + (0.3048-0.1506i)|1101> + (0.3048-0.1506i)|1110> + (-0.1323+0.1558i)|1111>'

**`def qvantum.register.Register.ket()`**

Method to return with the ket vector representation of the register.

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q2 = qvantum.Random_Qubit()
    >>>
    >>> r = qvantum.Register([q1, q2])
    >>> r.show()
    '|Ψ> = (0.0384+0.3328i)|00> + (0.1544+0.2240i)|01> + (0.6986+0.0481i)|10> + (0.5193-0.2317i)|11>'
    >>> r.ket()
    array([[0.03841413+0.33279281j],
   [0.15435432+0.22402411j],
   [0.69860685+0.04814138j],
   [0.51934712-0.23166933j]])

**`def qvantum.register.Register.measure_nth_qubit()`**

Method to perform a measurement on the n-th qubit in the register and return the final 
state of the register after the process. This final state is randomized regarding to the 
amplitudes of the register. The input parameter must be an integer corresponding to the 
number of qubits in the register.

**Arguments:**
    nth {int} -- Number of n-th possible qubit

**Raises:**
    TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q2 = qvantum.Random_Qubit()
    >>> q3 = qvantum.Random_Qubit()
    >>>
    >>> r = qvantum.Register([q1, q2, q3])
    >>> r.show()
    '|Ψ> = (-0.5585-0.0451i)|000> + (0.2304+0.3353i)|001> + (0.0120+0.0257i)|010> + (0.0090-0.0185i)|011> + (-0.3614+0.4567i)|100> + (0.4228-0.0056i)|101> + (0.0291+0.0045i)|110> + (-0.0108-0.0185i)|111>'
    >>> r.measure_nth_qubit(3)
    ---------------------------------------------------------------------------
    IndexErrorTraceback (most recent call last)
    <ipython-input-81-3e4cf8e71cdd> in <module>
    ----> 1 r.measure_nth_qubit(3)

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, nth)
77 
78 if isinstance(nth, int):
    ---> 79     return function(self, nth)
80 
81 else:

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum
egister.py in measure_nth_qubit(self, nth)
152 for key in self.__state_vector:
153 
    --> 154     if key[nth] == '0':
155 result0.append(self.__state_vector[key])
156 

    IndexError: string index out of range
    >>> r.measure_nth_qubit('shoe')
    ---------------------------------------------------------------------------
    TypeError Traceback (most recent call last)
    <ipython-input-82-72a46a88351a> in <module>
    ----> 1 r.measure_nth_qubit('shoe')

    c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, nth)
80 
81 else:
    ---> 82     raise TypeError('Invalid input! Argument must be integer.')
83 
84     return wrapper

    TypeError: Invalid input! Argument must be integer.
    >>> r.measure_nth_qubit(2)
    1
    >>> r.show()
    '|Ψ> = (0.0000+0.0000i)|000> + (0.3921+0.5707i)|001> + (0.0000+0.0000i)|010> + (0.0153-0.0315i)|011> + (0.0000+0.0000i)|100> + (0.7196-0.0095i)|101> + (0.0000+0.0000i)|110> + (-0.0184-0.0314i)|111>'

**`def qvantum.register.Register.measure_register()`**

Method to perform a measurement on the whole register and return the final state of the 
register after the process. This final state is randomized regarding to the amplitudes of 
the register.

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q2 = qvantum.Random_Qubit()
    >>> q3 = qvantum.Random_Qubit()
    >>>
    >>> r = qvantum.Register([q1, q2, q3])
    >>> r.show()
    '|Ψ> = (-0.0588-0.1859i)|000> + (-0.2113-0.3657i)|001> + (0.1644-0.0125i)|010> + (0.3420-0.1032i)|011> + (0.1755+0.1832i)|100> + (0.4569+0.3056i)|101> + (-0.1849+0.1090i)|110> + (-0.3401+0.3171i)|111>'
    >>> r.measure_register()
    '010'
    >>> r.show()
    '|Ψ> = (0.0000+0.0000i)|000> + (0.0000+0.0000i)|001> + (1.0000+0.0000i)|010> + (0.0000+0.0000i)|011> + (0.0000+0.0000i)|100> + (0.0000+0.0000i)|101> + (0.0000+0.0000i)|110> + (0.0000+0.0000i)|111>'

**`def qvantum.register.Register.set_amplitudes()`**

Method to set new coefficients for the possible states of the register. The input 
parameter is a list of real or complex number and their squared sum must be equal to 1. 
Number of elements in the least must be equal with the number of possible states.

**Arguments:**
    amp_list {list} -- List of int, float or complex objects

**Raises:**
    ValueError, TypeError

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q2 = qvantum.Random_Qubit()
    >>> q3 = qvantum.Random_Qubit()
    >>>
    >>> r = qvantum.Register([q1, q2, q3])
    >>> r.show()
    '|Ψ> = (0.0385+0.1339i)|000> + (0.3000+0.0702i)|001> + (0.1090+0.3519i)|010> + (0.7969+0.1696i)|011> + (-0.0195-0.0380i)|100> + (-0.0945-0.0033i)|101> + (-0.0537-0.0995i)|110> + (-0.2500-0.0038i)|111>'
    >>> r.set_amplitudes([0, 0, 1, 0, 0, 0, 0, 0])
    '|Ψ> = (0.0000+0.0000i)|000> + (0.0000+0.0000i)|001> + (1.0000+0.0000i)|010> + (0.0000+0.0000i)|011> + (0.0000+0.0000i)|100> + (0.0000+0.0000i)|101> + (0.0000+0.0000i)|110> + (0.0000+0.0000i)|111>'

**`def qvantum.register.Register.show()`**

Method to show the state function of the register object.

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q2 = qvantum.Random_Qubit()
    >>> q3 = qvantum.Random_Qubit()
    >>>
    >>> r = qvantum.Register([q1, q2, q3])
    >>> r.show()
    '|Ψ> = (0.3299-0.0125i)|000> + (-0.2215-0.2264i)|001> + (-0.4390+0.3714i)|010> + (0.5469+0.0726i)|011> + (0.1145-0.0835i)|100> + (-0.1332-0.0276i)|101> + (-0.0674+0.2375i)|110> + (0.2123-0.1052i)|111>'
