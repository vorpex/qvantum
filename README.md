﻿# qvantum - module documentation

## Contents

 1. Introduction
 2. Installation  
	 2.1 pip install  
	 2.2 wheel install  
	 2.3 setup file  
3. Modules  
	3.1 qvantum.qubit module  
	3.2 qvantum.register module  
	3.3 qvantum.gate module  
	3.4 qvantum.layer module  
	3.5 qvantum.circuit module  
	3.6 qvantum.bloch module  
4. Examples  
	4.1 Quantum teleportation  
	4.2 Grover's algorithm  
5. Notes  
	5.1 Module reading error  
	5.2 Deleting qubit from register  
	5.3 Ѱ sign in python2  

## 1. Introduction

qvantum is a python module, and it's goal is to ensure an easy use library for understanding quantum computing better or designing new quantum algorithms. Working with this module helps you to get more familiar with the basic concepts such as qubit, register or quantum gate, meanwhile the tool has the power for deeper analysis and development.

The module is in beta release phase: tested but it might contain bugs, therefore every constructive note is highly appreciated. Also if you would like to collaborate in the developing process do not hesitate to contact us.

## 2. Installation

qvantum module can be easily installed using three different approach below (you could extend the commands below like "/path/to/python.exe -m pip install ...", if python wasn't in your PATH)

### 2.1 pip install

The latest version of the module can be installed online from the PyPi page using pip in command line:

    pip install qvantum

or

    pip install --index-url https://test.pypi.org/simple qvantum

### 2.2 wheel install

The latest version of the module can be downloaded from the PyPi page in .whl format which can be used for installation:

    pip install qvantum-x.xx-py2.py3-none-any.whl

### 2.3 setup file

A setup.py file is also available on PyPi page. Download the file and the folder called "qvantum" then run the command in the folder where all the files were downloaded. Use –e if you want the module be immediately available for every user in your system:

    pip install .

or

	pip install –e .

## 3. Modules

In qvantum module there are some classes which represents the basic objects in quantum computing such as: qubit, register, gate, layer and circuit. These objects (and therefore the classes which represents them) are built on each other. Due to this concept a register is built on qubits, layers are formed by gates and circuits are created out of gates.
There is a sixth module, the bloch module which is used for the Bloch representation and visualization of a qubit.

### 3.1 qvantum.qubit module

### **`class qvantum.qubit.Qubit`**

In quantum computing a qubit or quantum bit is the basic unit of quantum information. Every qubit has two clear states such as 0 and 1 but unlike a classical bit a qubit can be in superposition which is a special  mixture of these clear states. Using qubit class, the user can create qubit objects. When creating a qubit object, the amplitudes must satisfy that |alpha|^2 + |beta|^2 = 1.

Instances of qubit class have the following methods:

	- __init__()		- initialize qubit
	- get_alpha()		- getter of alpha
    - get_beta()		- getter of beta
    - set_amplitudes()	- setter of alpha, beta
    - show()		- qubit representation
    - measure()		- measure qubit
    - ket()			- return the ket vector of qubit
    - bra()			- return the bra vector of qubit

The Random_Qubit class is the same as qubit class the only difference that an instance of the class is created with random amplitudes (alpha, beta). They share the same methods.
   
### **`def qvantum.qubit.Qubit.__init__(alpha, beta)`**

Method to initialize an instance of the qubit class. The squared sum of alpha and beta must be equal to zero otherwise a ValueError will be thrown.

**Arguments:**  
	*alpha* {int, float, complex} -- Amplitude or probability of being in state 0  
	*beta* {int, float, complex} -- Amplitude or probability of being in state 1  

**Raises:**  
    *ValueError, TypeError*

**Examples:**

    >>> import math
    >>> import qvantum
    >>>
    >>> q = qvantum.Qubit(1, 0)
    >>> q.show()
    '|Ψ> = (1.0000+0.0000i)|0> + (0.0000+0.0000i)|1>'
    >>> qvantum.Qubit(1 / math.sqrt(2), 1 / math.sqrt(2)).show()
    '|Ψ> = (0.7071+0.0000i)|0> + (0.7071+0.0000i)|1>'

### **`def qvantum.qubit.Qubit.bra()`**

Method to return with the bra vector representation of the qubit.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.bra()
    array([[-0.76536276+0.20163924j, -0.39225178-0.46872167j]])

### **`def qvantum.qubit.Qubit.get_alpha()`**

Getter method of alpha.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Qubit(1, 0)
    >>> q.get_alpha()
    1

### **`def qvantum.qubit.Qubit.get_beta()`**

Getter method of beta.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Qubit(1, 0)
    >>> q.get_beta()
    0

### **`def qvantum.qubit.Qubit.ket()`**

Method to return with the ket vector representation of the qubit.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.ket()
    array([[-0.76536276+0.20163924j],[-0.39225178-0.46872167j]])

### **`def qvantum.qubit.Qubit.measure()`**

Method to perform a measurement on the qubit and return with one clear state by the distribution according to the coefficients.

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

### **`def qvantum.qubit.Qubit.set_amplitudes(alpha, beta)`**

Setter method to replace the old coefficients to new ones. The squared sum of alpha and beta must be equal to zero otherwise a ValueError will be thrown.

**Arguments:**  
    *alpha* {int, float, complex} -- Amplitude or probability of being in state 0  
    *beta* {int, float, complex} -- Amplitude or probability of being in state 1  

**Raises:**  
    *ValueError, TypeError*

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

### **`def qvantum.qubit.Qubit.show()`**

Method to show the state function of the qubit object.

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Qubit(1, 0)
    >>> q.show()
    '|Ψ> = (1.0000+0.0000i)|0> + (0.0000+0.0000i)|1>'

### **`class qvantum.qubit.Random_Qubit(Qubit)`**

This is an inherited class from the Qubit class. They share the same methods but when an instance of the Random_Qubit class is created the coefficients are randomly chosen.
    
**Arguments:**  
	*Qubit* {qubit} -- qubit class

### **`def qvantum.qubit.Random_Qubit.__init__()`**

Method to initialize an instance of the qubit class with randomized amplitudes.

**Examples:**

    >>> import qvantum
    >>>
    >>> rq = qvantum.Random_Qubit()
    >>> rq.show()
    '|Ψ> = (-0.5736+0.2506i)|0> + (0.5223-0.5791i)|1>'
    >>> qvantum.Random_Qubit().show()
    '|Ψ> = (-0.1949+0.9475i)|0> + (0.1028+0.2318i)|1>'

### 3.2 qvantum.register module

### **`class qvantum.register.Register`**

A system containing more than one qubit is called a register. The state function of a register is the superposition of the allowed states of the qubits. The number of possible states are increasing exponentially with every new qubit added to the system.

> A quantum register is a system comprising multiple qubits and is the quantum analog of the classical processor register. An n size quantum register is a quantum system comprising n qubits. The Hilbert space, H, in which the data stored in a quantum register is:
> 
> H = H(n-1) × H(n-2) × ... × H(0).
> 
> via Wikipedia: https://en.wikipedia.org/wiki/Quantum_register

The instances of the register class have the following methods:

    - __init__()		- initialize register
    - get_coeff_list()	- getter of coefficients of qubits
    - get_state_number()	- getter of number of possible states
    - get_qubit_number()	- getter of number of qubits in the register
    - get_states()		- getter of states
    - get_amplitudes()	- getter of amplitudes
    - set_amplitudes()	- setter of amplitudes
    - show()		- register representation
    - measure_register()	- measure the whole register
    - measure_nth_qubit()	- measure the n-th qubit
    - ket()			- return the ket vector of register
    - bra()			- return the bra vector of register
    - delete_qubit()	- delete qubit from register
    - insert_qubit()	- insert qubit into register
    
### **`def qvantum.register.Register.__init__(qubit_list)`**

Method to initialize an instance of the register class. The input is a list of elements in Qubit or Random_Qubit class. Also this list must contain at least 2 elements.

**Arguments:**  
    *qubit_list* {list} -- List of objects from Qubit or Random_Qubit class

**Raises:**  
    *ValueError, TypeError*

**Examples:**

    >>> import qvantum
    >>>
    >>> q1 = qvantum.Random_Qubit()
    >>> q2 = qvantum.Random_Qubit()
    >>>
    >>> r = qvantum.Register([q1, q2])
    >>> r.show()
    '|Ψ> = (-0.4171-0.2953i)|00> + (-0.4106-0.7059i)|01> + (-0.1120-0.0875i)|10> + (-0.1049-0.2015i)|11>'

### **`def qvantum.register.Register.bra()`**

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

### **`def qvantum.register.Register.delete_qubit(nth)`**

Method to delete the n-th qubit from the register. This method has some drawback which is discussed later. The input parameter must be an integer corresponding to the number of qubits in the register.

**Arguments:**  
    *nth* {int} -- Number of n-th possible qubit

**Raises:**  
    *ValueError, TypeError*

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
    >>> r.delete_qubit(2)
    >>> r.show()
    '|Ψ> = (0.4927-0.6160i)|00> + (-0.0083-0.5904i)|01> + (0.1364-0.0024i)|10> + (0.0777-0.0663i)|11>'

### **`def qvantum.register.Register.get_amplitudes(nth=None)`**

Method to return with the coefficient of the n-th possible state for the register if the parameter is definite. If it isn’t, then the return value is the list of the coefficients of all possible states.

**Keyword Arguments:**  
    *nth* {int, None} -- Number of n-th possible amplitude (default: {None})

**Raises:**  
    *TypeError*

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

### **`def qvantum.register.Register.get_coeff_list()`**

Method to return the coefficients of the qubits in the register.

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

### **`def qvantum.register.Register.get_qubit_number()`**

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

### **`def qvantum.register.Register.get_state_number()`**

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

### **`def qvantum.register.Register.get_states(nth=None)`**

Method to return with the n-th possible state for the register if the parameter is definite. If it isn’t then the return value is the list of all possible states.

**Keyword Arguments:**  
    *nth* {int, None} -- Number of n-th possible state (default: {None})

**Raises:**  
    *TypeError*

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

### **`def qvantum.register.Register.insert_qubit(q, nth)`**

Method to insert a given qubit into a register. The input parameter must be an integer corresponding to the number of qubits in the register.

**Arguments:**  
    *q* {qubit} -- The qubit to be inserted  
    *nth* {int} -- The index where the qubit is inserted

**Raises:**  
    *ValueError, TypeError*

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
    >>> r.insert_qubit(q3, 2)
    >>> r.show()
    '|Ψ> = (-0.0764+0.1775i)|000> + (-0.0002-0.1162i)|001> + (0.3584+0.1790i)|010> + (-0.2404-0.0133i)|011> + (-0.3035+0.0960i)|100> + (0.1446-0.1253i)|101> + (0.1629+0.6394i)|110> + (-0.2424-0.3140i)|111>'
    >>> r.insert_qubit(q3, 2)
    >>> r.show()
    '|Ψ> = (-0.1362-0.0942i)|0000> + (0.0976+0.0195i)|0001> + (0.0976+0.0195i)|0010> + (-0.0585+0.0125i)|0011> + (-0.2109+0.2709i)|0100> + (0.0518-0.1998i)|0101> + (0.0518-0.1998i)|0110> + (0.0190+0.1226i)|0111> + (-0.0293-0.2712i)|1000> + (0.0809+0.1427i)|1001> + (0.0809+0.1427i)|1010> + (-0.0786-0.0595i)|1011> + (-0.5648+0.0288i)|1100> + (0.3048-0.1506i)|1101> + (0.3048-0.1506i)|1110> + (-0.1323+0.1558i)|1111>'

### **`def qvantum.register.Register.ket()`**

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

### **`def qvantum.register.Register.measure_nth_qubit(nth)`**

Method to perform a measurement on the n-th qubit in the register and return the final state of the register after the process. This final state is randomized regarding to the amplitudes of the register. The input parameter must be an integer corresponding to the number of qubits in the register.

**Arguments:**  
    *nth* {int} -- Number of n-th possible qubit

**Raises:**  
    *TypeError*

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
    >>> r.measure_nth_qubit(2)
    1
    >>> r.show()
    '|Ψ> = (0.0000+0.0000i)|000> + (0.3921+0.5707i)|001> + (0.0000+0.0000i)|010> + (0.0153-0.0315i)|011> + (0.0000+0.0000i)|100> + (0.7196-0.0095i)|101> + (0.0000+0.0000i)|110> + (-0.0184-0.0314i)|111>'

### **`def qvantum.register.Register.measure_register()`**

Method to perform a measurement on the whole register and return the final state of the register after the process. This final state is randomized regarding to the amplitudes of the register.

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

### **`def qvantum.register.Register.set_amplitudes(amp_list)`**

Method to set new coefficients for the possible states of the register. The input parameter is a list of real or complex number and their squared sum must be equal to 1. Number of elements in the least must be equal with the number of possible states.

**Arguments:**  
    *amp_list* {list} -- List of int, float or complex objects

**Raises:**  
    *ValueError, TypeError*

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

### **`def qvantum.register.Register.show()`**

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

### 3.3 qvantum.gate module

### **`class qvantum.gate.Gate`**

> "In quantum computing and specifically the quantum circuit model of computation, a quantum logic gate is a basic quantum circuit operating on a small number of qubits. They are the building blocks of quantum circuits, like classical logic gates are for conventional digital circuits.
> 
> Quantum logic gates are represented by unitary matrices. The most common quantum gates operate on spaces of one or two qubits, just like the common classical logic gates operate on one or two bits. As matrices, quantum gates can be described by 2^n x 2^n sized unitary matrices, where n is the number of qubits that the gate act on. The variables that the gates act upon, the quantum states, are vectors in 2^n complex dimensions, where n again is the number of qubits of variable:
> - The base vectors are the possible outcomes if measured, and a quantum state is a linear combination of outcomes."
> 
> via Wikipedia: https://en.wikipedia.org/wiki/Quantum_logic_gate

The instances of gate class have the following methods:

    - __init__()	- initialization method
    - __call__()	- call method
    - get_name()	- getter of name of gate
    - get_matrix()	- getter of matrix of gate
    - get_size()	- getter of size of matrix of gate
    - set_name()	- setter of name of gate
    - set_matrix()	- setter of matrix of gate
    - power()	- raise the matrix of gate to the given power
    
### **`def qvantum.gate.Gate.__call__(qr)`**

Method which makes possible to call a gate on a qubit or a register. The only restriction is that the size of the gate and the size of the qubit or register must be equal to each other.

**Arguments:**  
    *qr* {Qubit, Register} -- The qubit or register which the gate is called on

**Raises:**  
    *ValueError, TypeError*

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (0.6542+0.3385i)|0> + (-0.5226-0.4293i)|1>'
    >>> qvantum.Hadamard()(q)
    >>> q.show()
    '|Ψ> = (0.0930-0.0642i)|0> + (0.8321+0.5429i)|1>'

### **`def qvantum.gate.Gate.__init__()`**

Method to initialize a 2x2 sized identity matrix. Every identity matrix is a unitary matrix as well.

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

### **`def qvantum.gate.Gate.get_matrix()`**

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

### **`def qvantum.gate.Gate.get_name()`**

Method to return the name of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_name()
    'Controlled-Not'

### **`def qvantum.gate.Gate.get_size()`**

Method to retun the size of the unitary matrix of the gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> c = qvantum.CNOT(0, 1)
    >>> c.get_size()
    4

### **`def qvantum.gate.Gate.power(power)`**

Method to raise the unitary matrix of the gate to the given power and overwrite the original matrix of the gate with the result's matrix.

**Arguments:**  
    *power* {int} -- The power which the gate is raised on

**Raises:**  
    *TypeError*

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

### **`def qvantum.gate.Gate.set_matrix(matrix)`**

Method to set a new unitary matrix for the gate. If matrix is not unitary then an error is raised.

**Arguments:**  
    *matrix* {numpy.ndarray} -- Matrix of the gate to be set

**Raises:**  
    *ValueError, TypeError*

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

### **`def qvantum.gate.Gate.set_name(name)`**

Method to set a new name for the gate.

**Arguments:**  
    *name* {str} -- Name of the gate to be set

**Raises:**  
    *TypeError*

**Examples:**

    >>> import qvantum
    >>> g = qvantum.Gate()
    >>> g.get_name()
    'Identity'
    >>> g.set_name('shoe')
    >>> g.get_name()
    'shoe'

### **`class qvantum.gate.CNOT`**

This class is an inherited class from the Gate class. It’s the implementation of the Controlled-Not gate. It’s called on 2 qubits. The parameters determine which one is the control and the target – (0, 1) or (1, 0). Its unitary matrix:

<p align="center"><img src="/tex/f0268d81e824bf4ab71e107f0ea79296.svg?invert_in_darkmode&sanitize=true" align=middle width=229.53983909999997pt height=78.9048876pt/></p>

### **`def qvantum.gate.CNOT.__init__(control_qubit, target_qubit)`**

Method to initialize Controlled-Not gate.

**Arguments:**  
    *control_qubit* {int} -- Possible values: 0 or 1  
    *target_qubit* {int} -- Possible values: 0 or 1

**Raises:**  
    *ValueError*

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.CNOT(1, 0)

### **`def qvantum.gate.CNOT.set_matrix()`**

Setter of matrix of Controlled-Not gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`def qvantum.gate.CNOT.set_name()`**

Setter of name of Controlled-Not gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`class qvantum.gate.ControlledPhase`**

This class is an inherited class from the Gate class. It’s the implementation of the Controlled-Phase gate. Its unitary matrix:

<p align="center"><img src="/tex/80eaa43c84a5dd97612398f7c333ed6d.svg?invert_in_darkmode&sanitize=true" align=middle width=104.10975959999999pt height=78.9048876pt/></p>
    
### **`def qvantum.gate.ControlledPhase.__init__()`**

Method to initialize Controlled-Phase gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.ControlledPhase()

### **`def qvantum.gate.ControlledPhase.set_matrix()`**

Setter of matrix of Controlled-Phase gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`def qvantum.gate.ControlledPhase.set_name()`**

Setter of name of Controlled-Phase gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`class qvantum.gate.ControlledZ`**

This class is an inherited class from the Gate class. It’s the implementation of the Controlled-Z gate. Its unitary matrix:

<p align="center"><img src="/tex/b4b2643cd082a5fdcfb14c880b2370ac.svg?invert_in_darkmode&sanitize=true" align=middle width=116.8951872pt height=78.9048876pt/></p>

### **`def qvantum.gate.ControlledZ.__init__()`**

Method to initialize Controlled-Z gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.ControlledZ()

### **`def qvantum.gate.ControlledZ.set_matrix()`**

Setter of matrix of Controlled-Z gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`def qvantum.gate.ControlledZ.set_name()`**

Setter of name of Controlled-Z gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`class qvantum.gate.Fredkin`**

This class is an inherited class from the Gate class. It’s the implementation of the Fredkin gate. It’s called on 3 qubits. The parameters determine which one is the control qubit – 0, 1 or 2. Its  unitary matrix:

<p align="center"><img src="/tex/275f0ebef0f6edc1738dd7cfb7ac8857.svg?invert_in_darkmode&sanitize=true" align=middle width=650.8606318499999pt height=157.80979994999998pt/></p>

### **`def qvantum.gate.Fredkin.__init__(control_qubit)`**

Method to initialize Fredkin gate.

**Arguments:**  
    *control_qubit* {Qubit} -- Possible values: 0, 1 or 2

**Raises:**  
    *ValueError*

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.Fredkin(2)

### **`def qvantum.gate.Fredkin.set_matrix()`**

Setter of matrix of Fredkin gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`def qvantum.gate.Fredkin.set_name()`**

Setter of name of Fredkin gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`class qvantum.gate.Hadamard`**

This class is an inherited class from the Gate class. It’s the implementation of the Hadamard gate. Its unitary matrix:

<p align="center"><img src="/tex/fbdffe1a35fef45958e21f6c41477e99.svg?invert_in_darkmode&sanitize=true" align=middle width=78.21026565pt height=49.315569599999996pt/></p>

### **`def qvantum.gate.Hadamard.__init__()`**

Method to initialize Hadamard gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.Hadamard()

### **`def qvantum.gate.Hadamard.set_matrix()`**

Setter of matrix of Hadamard gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`def qvantum.gate.Hadamard.set_name()`**

Setter of name of Hadamard gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`class qvantum.gate.Ising`**

This class is an inherited class from the Gate class. It’s the implementation of the Ising gate. Its unitary matrix:

<p align="center"><img src="/tex/30a7661452606fce00430aa87b38e096.svg?invert_in_darkmode&sanitize=true" align=middle width=433.87934699999994pt height=78.9048876pt/></p>

### **`def qvantum.gate.Ising.__init__(phi)`**

Method to initialize Ising gate.

**Arguments:**  
    *phi* {int, float} -- The used angle

**Raises:**  
    *TypeError*

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.Ising(1)

### **`def qvantum.gate.Ising.set_matrix()`**

Setter of matrix of Ising gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`def qvantum.gate.Ising.set_name()`**

Setter of name of Ising gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`class qvantum.gate.PauliX`**

This class is an inherited class from the Gate class. It’s the implementation of the Pauli-X gate. Its unitary matrix:

<p align="center"><img src="/tex/cb1d8591b83600d4a7a0b69d2e05e205.svg?invert_in_darkmode&sanitize=true" align=middle width=50.2284453pt height=39.452455349999994pt/></p>
    
### **`def qvantum.gate.PauliX.__init__()`**

Method to initialize Pauli-X gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.PauliX()

### **`def qvantum.gate.PauliX.set_matrix()`**

Setter of matrix of Pauli-X gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`def qvantum.gate.PauliX.set_name()`**

Setter of name of Pauli-X gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`class qvantum.gate.PauliY`**

This class is an inherited class from the Gate class. It’s the implementation of the Pauli-Y gate. Its unitary matrix:

<p align="center"><img src="/tex/65b7d579ddbee867531d64ec3e42bebb.svg?invert_in_darkmode&sanitize=true" align=middle width=60.45789584999999pt height=39.452455349999994pt/></p>
    
### **`def qvantum.gate.PauliY.__init__()`**

Method to initialize Pauli-Y gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.PauliY()

### **`def qvantum.gate.PauliY.set_matrix()`**

Setter of matrix of Pauli-Y gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`def qvantum.gate.PauliY.set_name()`**

Setter of name of Pauli-Y gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`class qvantum.gate.PauliZ`**

This class is an inherited class from the Gate class. It’s the implementation of the Pauli-Z gate. Its unitary matrix:

<p align="center"><img src="/tex/1be182f72cdd82702c1beb7ea0970958.svg?invert_in_darkmode&sanitize=true" align=middle width=63.0138729pt height=39.452455349999994pt/></p>
    
### **`def qvantum.gate.PauliZ.__init__()`**

Method to initialize Pauli-Z gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.PauliZ()

### **`def qvantum.gate.PauliZ.set_matrix()`**

Setter of matrix of Pauli-Z gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`def qvantum.gate.PauliZ.set_name()`**

Setter of name of Pauli-Z gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`class qvantum.gate.Phase`**

This class is an inherited class from the Gate class. It’s the implementation of the Phase gate. Its unitary matrix:

<p align="center"><img src="/tex/33e237af55add78cdfd704292f7b004b.svg?invert_in_darkmode&sanitize=true" align=middle width=50.2284453pt height=39.452455349999994pt/></p>
    
### **`def qvantum.gate.Phase.__init__()`**

Method to initialize Phase gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.Phase()

### **`def qvantum.gate.Phase.set_matrix()`**

Setter of matrix of Phase gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`def qvantum.gate.Phase.set_name()`**

Setter of name of Phase gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`class qvantum.gate.Pi8`**

This class is an inherited class from the Gate class. It’s the implementation of the Pi/8 gate. Its unitary matrix:

<p align="center"><img src="/tex/3e8ee7c3be16e9416b938ebbbb95c863.svg?invert_in_darkmode&sanitize=true" align=middle width=150.95453835pt height=41.004310049999994pt/></p>
    
### **`def qvantum.gate.Pi8.__init__()`**

Method to initialize Pi/8 gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.Pi8()

### **`def qvantum.gate.Pi8.set_matrix()`**

Setter of matrix of Pi/8 gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`def qvantum.gate.Pi8.set_name()`**

Setter of name of Pi/8 gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`class qvantum.gate.SquareNot`**

This class is an inherited class from the Gate class. It’s the implementation of the Square-Not gate. Its unitary matrix:

<p align="center"><img src="/tex/a5d2af8d0f35e65bfc49fae795e34fe2.svg?invert_in_darkmode&sanitize=true" align=middle width=101.73726749999999pt height=39.452455349999994pt/></p>
    
### **`def qvantum.gate.SquareNot.__init__()`**

Method to initialize Square-Not gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.SquareNot()

### **`def qvantum.gate.SquareNot.set_matrix()`**

Setter of matrix of Square-Not gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`def qvantum.gate.SquareNot.set_name()`**

Setter of name of Square-Not gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`class qvantum.gate.SquareSwap`**

This class is an inherited class from the Gate class. It’s the implementation of the Square-Swap gate. Its unitary matrix:

<p align="center"><img src="/tex/a09e9af305230f07c7b55ffd2f28b323.svg?invert_in_darkmode&sanitize=true" align=middle width=138.51658095pt height=78.9048876pt/></p>
    
### **`def qvantum.gate.SquareSwap.__init__()`**

Method to initialize Square-Swap gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.SquareSwap()

### **`def qvantum.gate.SquareSwap.set_matrix()`**

Setter of matrix of Square-Swap gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`def qvantum.gate.SquareSwap.set_name()`**

Setter of name of Square-Swap gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`class qvantum.gate.Swap`**

This class is an inherited class from the Gate class. It’s the implementation of the Swap gate. Its unitary matrix:

<p align="center"><img src="/tex/f76361edbba0f0bf33790f8c8209d6b6.svg?invert_in_darkmode&sanitize=true" align=middle width=104.10975959999999pt height=78.9048876pt/></p>
    
### **`def qvantum.gate.Swap.__init__()`**

Method to initialize Swap gate.

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.Swap()

### **`def qvantum.gate.Swap.set_matrix()`**

Setter of matrix of Swap gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`def qvantum.gate.Swap.set_name()`**

Setter of name of Swap gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`class qvantum.gate.Toffoli`**

This class is an inherited class from the Gate class. It’s the implementation of the Toffoli gate. It’s called on 3 qubits. The parameters determine which one is the target qubit – 0, 1 or 2. Its  unitary matrix:

<p align="center"><img src="/tex/64183c5c95d641197230fbe0abe8683f.svg?invert_in_darkmode&sanitize=true" align=middle width=650.8606318499999pt height=157.80979994999998pt/></p>
    
### **`def qvantum.gate.Toffoli.__init__(target_qubit)`**

Method to initialize Toffoli gate.

**Arguments:**  
    *target_qubit* {Qubit} -- Possible values: 0, 1 or 2

**Raises:**  
    *ValueError*

**Examples:**

    >>> import qvantum
    >>>
    >>> h = qvantum.Toffoli(0)

### **`def qvantum.gate.Toffoli.set_matrix()`**

Setter of matrix of Toffoli gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### **`def qvantum.gate.Toffoli.set_name()`**

Setter of name of Toffoli gate. Always raises BaseException.

**Raises:**  
    *BaseException*

### 3.4 qvantum.layer module

### **`class qvantum.layer.Layer`**

An instance of layer class represents one stage in a given quantum computational process. The layer is created by defining the gates which are contained by the given layer. The order of gates refer to that qubit which is affected by the given gate. Using the instances of layer class the user can build an instance of circuit class.

The instances of layer class have the following methods:

    - __init__()		- initialization method
    - get_gate_list()	- getter of gates in gate list
    - get_gate_number()	- getter of number of gates
    - get_nth_gate()	- getter of n-th gate
    - get_layer_matrix()	- getter of result of Kronecker product of matrices in gate list
    - get_matrix_size()	- getter of size of layer matrix (equals to the size of states on which the layer is usable)
    - get_layer_size()	- getter of size of layer (equals to the size of register on which the layer is usable)
    - delete_gate()		- delete gate from layer
    - insert_gate()		- insert gate into layer

### **`def qvantum.layer.Layer.__init__(gate_list)`**

Method to initialize an instance of the Layer class. The argument must be a list of objects in the Gate class or in an inherited class such as: Hadamard, SquareNot, PauliX, PauliY, PauliZ, Phase, Pi8, Swap, SquareSwap, CNOT, ControlledZ, ControlledPhase, Ising, Toffoli, Fredkin.

**Arguments:**  
    *gate_list* {list} -- List of objects from Gate class

**Raises:**  
    *TypeError*

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

### **`def qvantum.layer.Layer.delete_gate(nth)`**

Method to delete the n-th gate from the current Layer object. The parameter must be equal to or greater than 0 and less than the actual size of the Layer.

**Arguments:**  
    *nth* {int} -- Number of n-th possible gate

**Raises:**  
    *ValueError, TypeError*

**Examples:**

    >>> import qvantum
    >>>
    >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate(), qvantum.PauliX()])
    >>> l.get_gate_list()
    OrderedDict([(0, <qvantum.gate.Hadamard at 0x1ae59262ba8>), (1, <qvantum.gate.Gate at 0x1ae58146ba8>), (2, <qvantum.gate.PauliX at 0x1ae59262d30>)])
    >>> l.delete_gate(0)
    >>> l.get_gate_list()
    OrderedDict([(0, <qvantum.gate.Gate at 0x1cff211fda0>), (1, <qvantum.gate.PauliX at 0x1cff3f5f4a8>)])

### **`def qvantum.layer.Layer.get_gate_list()`**

Method to return the gates which are contained by the current Layer object.

**Examples:**

    >>> import qvantum
    >>>
    >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l.get_gate_list()
    OrderedDict([(0, <qvantum.gate.Hadamard at 0x1ae588c2d68>), (1, <qvantum.gate.Gate at 0x1ae56a08a20>)])

### **`def qvantum.layer.Layer.get_gate_number()`**

Method to return the number of the gates which are contained by the current Layer object.

**Examples:**

    >>> import qvantum
    >>>
    >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l.get_gate_number()
    2

### **`def qvantum.layer.Layer.get_layer_matrix()`**

Method to return the result of the Kronecker multiplication of the gates’ matrices which are contained by the current Layer object. When the Layer is applied on a Register during one step of a calculation the state vector of the Register is multiplied by this 
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

### **`def qvantum.layer.Layer.get_layer_size()`**

Method to return the size of the current Layer object. Remember, it’s not the size of the matrix of the current Layer object but the size of a Register object which the Layer can be applied on.

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

### **`def qvantum.layer.Layer.get_matrix_size()`**

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

### **`def qvantum.layer.Layer.get_nth_gate(nth)`**

Method to return the n-th gate in the current Layer object. The parameter must be between 0 and the actual number of the gates.

**Arguments:**  
    *nth* {int} -- Number of n-th possible gate

**Raises:**  
    *TypeError*

**Examples:**

    >>> import qvantum
    >>>
    >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l.get_nth_gate(0)
    <qvantum.gate.Hadamard at 0x1ae588c2d68>
    >>> l.get_nth_gate(1)
    <qvantum.gate.Gate at 0x1ae56a08a20>

### **`def qvantum.layer.Layer.insert_gate(g, nth)`**

Method to insert a Gate object into the n-th place in the current Layer object. The first parameter must be a Gate object or an object in an inherited class such as: 
Hadamard, SquareNot, PauliX, PauliY, PauliZ, Phase, Pi8, Swap, SquareSwap, CNOT, ControlledZ, ControlledPhase, Ising, Toffoli, Fredkin. The second parameter must be equal to or greater than 0 and equal to or less than the actual size of the Layer.

**Arguments:**  
    *g* {gate} -- The gate to be inserted  
    *nth* {int} -- The index where the gate is inserted

**Raises:**  
    *ValueError, TypeError*

**Examples:**

    >>> import qvantum
    >>>
    >>> l = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate(), qvantum.PauliX()])
    >>> l.get_gate_list()
    OrderedDict([(0, <qvantum.gate.Hadamard at 0x1ae59262ba8>), (1, <qvantum.gate.Gate at 0x1ae58146ba8>), (2, <qvantum.gate.PauliX at 0x1ae59262d30>)])
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

### 3.5 qvantum.circuit module

### **`class qvantum.circuit.Circuit`**

An instance of circuit class represents a whole quantum computational process. The circuit is created by defining the layers which are contained by the given circuit. The order of layers refers to that stage which is ran by the given layer. Using the instances of circuit class the user can build a quantum algorithm.

The instances of circuit class have the following methods:

    - __init__()		- initialization method
    - get_layer_list()	- getter of layers in layer list
    - get_layer_number()	- getter of number of layers
    - get_nth_layer()	- getter of n-th layer
    - get_circuit_size()	- getter of size of circuit (equals to the size of register on which the layer is usable)
    - delete_layer()	- delete layer from circuit
    - insert_layer()	- insert layer into circuit
    - run()			- run circuit on starting register

### **`def qvantum.circuit.Circuit.__init__(layer_list)`**

Method to initialize an instance of the Circuit class. The argument must be a list of objects in the Layer class with the same size.

**Arguments:**  
    *layer_list* {list} -- List of objects from Layer class

**Raises:**  
    *ValueError, TypeError*

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

### **`def qvantum.circuit.Circuit.delete_layer(nth)`**

Method to delete the n-th layer from the current Circuit object. The parameter must be equal to or greater than 0 and less than the actual number of the layers in the Circuit.

**Arguments:**  
    *nth* {int} -- Number of layer to be deleted

**Raises:**  
    *ValueError, TypeError*

**Examples:**

    >>> import qvantum
    >>>
    >>> l1 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l2 = qvantum.Layer([qvantum.CNOT(1, 0)])
    >>> c = qvantum.Circuit([l1, l2])
    >>> c.get_layer_list()
    OrderedDict([(0, <qvantum.layer.Layer at 0x27b47e65630>), (1, <qvantum.layer.Layer at 0x27b47e65cc0>)])
    >>> c.delete_layer(0)
    >>> c.get_layer_list()
    OrderedDict([(0, <qvantum.layer.Layer at 0x27b47e65cc0>)])

### **`def qvantum.circuit.Circuit.get_circuit_size()`**

Method to return the size of the current Circuit object. It’s the size of the Register object which the Circuit can be applied on.

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

### **`def qvantum.circuit.Circuit.get_layer_list()`**

Method to return the layers which are contained by the current Circuit object.

**Examples:**

    >>> import qvantum
    >>>
    >>> l1 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l2 = qvantum.Layer([qvantum.PauliY(), qvantum.PauliX()])
    >>> c = qvantum.Circuit([l1, l2])
    >>> c.get_layer_list()
    OrderedDict([(0, <qvantum.layer.Layer at 0x27b474c2cf8>), (1, <qvantum.layer.Layer at 0x27b47bf2198>)])

### **`def qvantum.circuit.Circuit.get_layer_number()`**

Method to return the number of the layers which are contained by the current Circuit object.

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

### **`def qvantum.circuit.Circuit.get_nth_layer(nth)`**

Method to return the n-th layer in the current Circuit object. The parameter must be between 0 and the actual number of the layers.

**Arguments:**  
    *nth* {int} -- Number of nth possible layer

**Raises:**  
    *TypeError*

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

### **`def qvantum.circuit.Circuit.insert_layer(l, nth)`**

Method to insert a Layer object into the n-th place in the current Circuit object. The first parameter must be a Layer object while the second parameter must be equal to or greater than 0 and equal to or less than the actual size of the layers in the Circuit. The size of the Layer object must be equal to the size of the already used Layers in the Circuit.

**Arguments:**  
    *l* {layer} -- Layer to be inserted  
    *nth* {int} -- Index where the layer to be inserted

**Raises:**  
    *ValueError, TypeError*

**Examples:**

    >>> import qvantum
    >>>
    >>> l1 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
    >>> l2 = qvantum.Layer([qvantum.CNOT(1, 0)])
    >>> c = qvantum.Circuit([l1, l2])
    >>> c.get_layer_list()
    OrderedDict([(0, <qvantum.layer.Layer at 0x27b47de9898>), (1, <qvantum.layer.Layer at 0x27b47de9550>)])
    >>> l3 = qvantum.Layer([qvantum.Swap()])
    >>> c.insert_layer(l3, 1)
    >>> c.get_layer_list()
    OrderedDict([(0, <qvantum.layer.Layer at 0x27b47de9898>), (1, <qvantum.layer.Layer at 0x27b47e5dc50>), (2, <qvantum.layer.Layer at 0x27b47de9550>)])

### **`def qvantum.circuit.Circuit.run(r)`**

Method to perform the computational process on a Register object as input and returns the result. The size of the Register object and the size of the Circuit object must be equal.

**Arguments:**  
    *r* {register} -- Register which the circuit is applied on

**Raises:**  
    *ValueError, TypeError*

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

### 3.6 qvantum.bloch module

> "In quantum mechanics, the Bloch sphere is a geometrical representation of the pure state space of a two-level quantum mechanical system (qubit), named after the physicist Felix Bloch. Quantum mechanics is mathematically formulated in Hilbert space or projective Hilbert space. The space of pure states of a quantum system is given by the one-dimensional subspaces of the corresponding Hilbert space (or the "points" of the projective Hilbert space).
> 
> The Bloch sphere is a unit 2-sphere, with antipodal points corresponding to a pair of mutually orthogonal state vectors. The north and south poles of the Bloch sphere are typically chosen to correspond to the standard basis vectors |0> and |1>, respectively, which in turn might correspond e.g. to the spin-up and spin-down states of an electron. This choice is arbitrary, however. The points on the surface of the sphere correspond to the pure states of the system, whereas the interior points correspond to the mixed states."
> 
> via Wikipedia: https://en.wikipedia.org/wiki/Bloch_sphere

The following functions are the Bloch Sphere related functions in the package: 

	- bloch_coords()	- calculate bloch coordinates from qubit
	- bloch_qubit()		- calculate qubit from bloch coordinates
	- bloch_sphere_plot()	- plot bloch representation
	- phase_test()		- compute phase between two complex numbers

### **`def qvantum.bloch.bloch_coords(q)`**

This function calculates the coordinates of the Bloch representation from the state vector of a Qubit object.
    
**Arguments:**  
    *q* {qubit} -- Instance of Qubit class or Random_Qubit class

**Raises:**  
    *TypeError*

**Examples:**

    >>> import qvantum
    >>>
    >>> q = qvantum.Random_Qubit()
    >>> q.show()
    '|Ψ> = (-0.5879-0.7251i)|0> + (0.3522-0.0674i)|1>'
    >>> qvantum.bloch_coords(q)
    (-0.31632342351128423, 0.5899599386821074, 0.7428908146479567)

### **`def qvantum.bloch.bloch_qubit(u, v, w)`**

This function calculates the state vector of a Qubit object from the given Bloch coordinates.

**Arguments:**  
    *u* {int, float} -- 1st coordinate of Bloch representation  
    *v* {int, float} -- 2nd coordinate of Bloch representation  
    *w* {int, float} -- 3rd coordinate of Bloch representation  

**Raises:**  
    *ValueError, TypeError*

**Examples:**

    >>> import math
    >>> import qvantum
    >>>
    >>> u = 0
    >>> v = 1 / math.sqrt(2)
    >>> w = 1 / math.sqrt(2)
    >>> qvantum.bloch_qubit(u, v, w).show()
    '|Ψ> = (0.9239+0.0000i)|0> + (0.0000+0.3827i)|1>'

### **`def qvantum.bloch.bloch_sphere_plot(u, v, w, xfigsize=15, yfigsize=7.5, frame_on=False, tight_layout_on=False, style='dark_background', surface_on=True, wireframe_on=True, surface_cmap='Blues_r', surface_alpha=0.3, wireframe_color='#d3d3d3', wireframe_linewidth=0.075, quiver_color='#ffffff', quiver_linewidth=1.5, quiver_ratio=0.1, line_color='#d3d3d3', line_linewidth=0.3, circle_edgecolor='#d3d3d3', circle_facecolor='none', circle_linewidth=0.3)`**

This function visualizes the qubit using its bloch coordinates and the matplotlib module.
    
**Arguments:**  
    *u* {int, float} -- 1st coordinate of Bloch representation  
    *v* {int, float} -- 2nd coordinate of Bloch representation  
    *w* {int, float} -- 3rd coordinate of Bloch representation  

**Keyword Arguments:**  
    *xfigsize* {int, float} -- X size of figure (default: {15})  
    *yfigsize* {int, float} -- Y size of figure (default: {7.5})  
    *frame_on* {bool} -- Frame (default: {False})  
    *tight_layout_on* {bool} -- Tight layout (default: {False})  
    *style* {str} -- Style (default: {'dark_background'})  
    *surface_on* {bool} -- Surface (default: {True})  
    *wireframe_on* {bool} -- Wireframe (default: {True})  
    *surface_cmap* {str} -- Surface cmap (default: {'Blues_r'})  
    *surface_alpha* {int, float} -- Surface alpha (default: {0.3})  
    *wireframe_color* {str} -- Wireframe color (default: {'#d3d3d3'})  
    *wireframe_linewidth* {int, float} -- Width of wireframe line (default: {0.075})  
    *quiver_color* {str} -- Quiver color (default: {'#ffffff'})  
    *quiver_linewidth* {int, float} -- Width of quiver line (default: {1.5})  
    *quiver_ratio* {int, float} -- Quiver ratio (default: {0.1})  
    *line_color* {str} -- Line color (default: {'#d3d3d3'})  
    *line_linewidth* {int, float} -- Width of line (default: {0.3})  
    *circle_edgecolor* {str} -- Edge color of circle (default: {'#d3d3d3'})  
    *circle_facecolor* {str} -- Face color of circle (default: {'none'})  
    *circle_linewidth* {int, float} -- Width of circle line (default: {0.3})

**Raises:**  
    *ValueError, TypeError*

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

### **`def qvantum.bloch.phase_test(c1, c2)`**

Computes the phase between two complex number.
    
**Arguments:**  
    *c1* {complex} -- 1st complex number  
    *c2* {complex} -- 2nd complex number

**Raises:**  
    *TypeError*

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

## 4. Examples

The examples in this section show the way how to interpret the already known quantum circuits or develop new ones using the qvantum module.

### 4.1 Quantum teleportation

The quantum circuit of teleportation looks like this below:
<p align="center"><img src="/pics/Quantum_Teleportation.jpg?invert_in_darkmode&sanitize=true" align=middle/></p>

> Michael A. Nielsen & Isaac L. Chuang - Quantum Computation and Quantum Information

And the same circuit can be represented this way by using qvantum module:

	>>> import qvantum
	>>>
	>>> q = qvantum.Random_Qubit()
	>>> q1 = qvantum.Qubit(1, 0)
	>>> q2 = qvantum.Qubit(1, 0)
	>>>
	>>> r = qvantum.Register([q1, q2])
	>>>
	>>> l0 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
	>>> l1 = qvantum.Layer([qvantum.CNOT(0, 1)])
	>>>
	>>> c0 = qvantum.Circuit([l0, l1])
	>>> c0.run(r)
	>>>
	>>> r.insert_qubit(q, 0)
	>>>
	>>> l2 = qvantum.Layer([qvantum.CNOT(0, 1), qvantum.Gate()])
	>>> l3 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate(), qvantum.Gate()])
	>>>
	>>> c1 = qvantum.Circuit([l2, l3])
	>>> c1.run(r)
	>>>
	>>> m0 = r.measure_nth_qubit(0)
	>>> m1 = r.measure_nth_qubit(1)
	>>>
	>>> # print(r.show())
	>>>
	>>> XM2 = qvantum.PauliX()
	>>> XM2.power(m1)
	>>> ZM1 = qvantum.PauliZ()
	>>> ZM1.power(m0)
	>>>
	>>> l4 = qvantum.Layer([qvantum.Gate(), qvantum.Gate(), XM2])
	>>> l5 = qvantum.Layer([qvantum.Gate(), qvantum.Gate(), ZM1])
	>>>
	>>> c2 = qvantum.Circuit([l4, l5])
	>>> c2.run(r)
	>>>
	>>> r.delete_qubit(0)
	>>> r.delete_qubit(0)
	>>>
	>>> q.show()
	'|Ψ> = (0.0495+0.6502i)|0> + (0.3629-0.6657i)|1>'
	>>> r.show()
	'|Ψ> = (0.0495+0.6502i)|0> + (0.3629-0.6657i)|1>'

<p align="center"><img src="/pics/Quantum_Teleportation_qvantum.jpg?invert_in_darkmode&sanitize=true" align=middle/></p>

### 4.2 Grover’s algorithm

The quantum circuit of teleportation looks like this below:
<p align="center"><img src="/pics/Quantum_Grover5.jpg?invert_in_darkmode&sanitize=true" align=middle/></p>

> http://demonstrations.wolfram.com/QuantumCircuitImplementingGroversSearchAlgorithm/

And the same circuit can be represented this way by using qvantum module:

	>>> import numpy
	>>> import qvantum
	>>>
	>>> q0 = qvantum.Qubit(1, 0)
	>>> q1 = qvantum.Qubit(1, 0)
	>>> q2 = qvantum.Qubit(1, 0)
	>>> q3 = qvantum.Qubit(0, 1)
	>>>
	>>> r = qvantum.Register([q0, q1, q2, q3])
	>>> r.show()
	'|Ψ> = (0.0000+0.0000i)|0000> + (1.0000+0.0000i)|0001> + 			(0.0000+0.0000i)|0010> + (0.0000+0.0000i)|0011> + (0.0000+0.0000i)|0100> + (0.0000+0.0000i)|0101> + (0.0000+0.0000i)|0110> + (0.0000+0.0000i)|0111> + (0.0000+0.0000i)|1000> + (0.0000+0.0000i)|1001> + (0.0000+0.0000i)|1010> + (0.0000+0.0000i)|1011> + (0.0000+0.0000i)|1100> + (0.0000+0.0000i)|1101> + (0.0000+0.0000i)|1110> + (0.0000+0.0000i)|1111>'
	>>> l0 = qvantum.Layer([qvantum.Hadamard(), qvantum.Hadamard(), qvantum.Hadamard(), qvantum.Hadamard()])
	>>> l1 = qvantum.Layer([qvantum.Gate(), qvantum.PauliX(), qvantum.Gate(), qvantum.Gate()])
	>>>
	>>> g2 = qvantum.Gate()
	>>> g2.set_matrix(numpy.matrix([
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
	>>>
	>>> l2 = qvantum.Layer([g2])
	>>> l3 = qvantum.Layer([qvantum.Gate(), qvantum.PauliX(), qvantum.Gate(), qvantum.Gate()])
	>>> l4 = qvantum.Layer([qvantum.Hadamard(), qvantum.Hadamard(), qvantum.Hadamard(), qvantum.Gate()])
	>>> l5 = qvantum.Layer([qvantum.PauliX(), qvantum.PauliX(), qvantum.PauliX(), qvantum.Gate()])
	>>>
	>>> g6 = qvantum.Gate()
	>>> g6.set_matrix(numpy.matrix([
		[1, 0, 0, 0, 0, 0, 0, 0],
		[0, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0, 0, 0, 0],
		[0, 0, 0, 1, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 0, 0, 0],
		[0, 0, 0, 0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0, 0, 1, 0],
		[0, 0, 0, 0, 0, 0, 0, -1]
		]))
	>>>
	>>> l6 = qvantum.Layer([g6, qvantum.Gate()])
	>>> l7 = qvantum.Layer([qvantum.PauliX(), qvantum.PauliX(), qvantum.PauliX(), qvantum.Gate()])
	>>> l8 = qvantum.Layer([qvantum.Hadamard(), qvantum.Hadamard(), qvantum.Hadamard(), qvantum.Gate()])
	>>>
	>>> c = qvantum.Circuit([l0, l1, l2, l3, l4, l5, l6, l7, l8])
	>>> c.run(r)
	>>>
	>>> r.show()
	'|Ψ> = (-0.1250+0.0000i)|0000> + (0.1250+0.0000i)|0001> + (-0.1250+0.0000i)|0010> + (0.1250+0.0000i)|0011> + (-0.1250+0.0000i)|0100> + (0.1250+0.0000i)|0101> + (-0.1250+0.0000i)|0110> + (0.1250+0.0000i)|0111> + (-0.1250+0.0000i)|1000> + (0.1250+0.0000i)|1001> + (-0.6250+0.0000i)|1010> + (0.6250+0.0000i)|1011> + (-0.1250+0.0000i)|1100> + (0.1250+0.0000i)|1101> + (-0.1250+0.0000i)|1110> + (0.1250+0.0000i)|1111>'
	>>> r.measure_nth_qubit(3)
	0
	>>> r.delete_qubit(3)
	>>> r.show()
	'|Ψ> = (-0.1768+0.0000i)|000> + (-0.1768+0.0000i)|001> + (-0.1768+0.0000i)|010> + (-0.1768+0.0000i)|011> + (-0.1768+0.0000i)|100> + (-0.8839+0.0000i)|101> + (-0.1768+0.0000i)|110> + (-0.1768+0.0000i)|111>'

<p align="center"><img src="/pics/Quantum_Grover5_qvantum.jpg?invert_in_darkmode&sanitize=true" align=middle/></p>

## 5. Notes

### 5.1 Module reading error

If there is some error after the installation of the module then it’s possible that there is some misconfiguration in the local variable parameters. In that case try to load the module using the actual path in the local system

	>>> import sys
	>>> sys.path.append(’path\to\your\module’)
	>>> import qvantum

### 5.2 Deleting a qubit from register

It is possible when using the delete method of an object of the Register class the result is not what was expected. It’s because in quantum mechanics there are states which are not possible to be described by the product of two different quantum states. These states are called quantum entanglement. Please be careful during using this method. Developing alternative ways to come over this problem are in progress.

### 5.3 Ѱ sign in python2

Using python2, the state symbol Ѱ may not be displayed correctly. Unfortunately this problem cannot be solved on just the code level, the display also depends on the current local system parameters. Try to modify that if you face this problem.
