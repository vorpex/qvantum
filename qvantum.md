# qvantum - python module documentation

## Contents

 1. Introduction
 2. Installation
	 2.1 pip install
	 2.2 wheel install
	 2.3 setup file
3. Module classes
	3.1 Qubit class
	3.2 Register class
	3.3 Gate class
	3.4 Layer class
	3.5 Circuit class
	3.6 Bloch sphere functions
4. Examples
	4.1 Quantum teleportation
	4.2 Grover's algorithm
5. Notes
	5.1 Module reading error
	5.2 Deleting qubit from register
	5.3 Ѱ sign in python2

## 1. Introduction

qvantum is a python module with the goal to ensure an easy use library for understanding quantum computing better or designing new quantum algorithms. Working with this module helps you to get more familiar with the basic concepts such as qubit, register or quantum gate, meanwhile the tool has the power for deeper analysis and development.

The module is in beta release phase: tested but it might contain bugs, therefore every constructive note is highly welcomed. Also If you would like to collaborate in the developing process then do not hesitate and contact us.

## 2. Installation

qvantum module can be easily installed using three different approach below.

### 2.1 pip install

The latest version of the module can be installed online from the PyPi page using pip in command line:

    pip install qvantum

or alternatively

    python –m pip install qvantum
    python -m pip install --index-url https://test.pypi.org/simple qvantum

### 2.2 wheel install

The latest version of the module can be downloaded from the PyPi page in .whl format which can be used for installation:

    pip install qvantum-x.xx-py2.py3-none-any.whl

or alternatively

    python –m pip install qvantum-x.xx-py2.py3-none-any.whl

### 2.3 setup file

A setup.py file is also available on PyPi page. Download the file then run the command in the folder where the setup.py file was downloaded. Use –e if you want the module be immediately available for every user in your system:

    pip install . //(pip install –e .)

or alternatively

    python –m pip install . //(python –m pip install –e .)

## 3. Module classes

In qvantum module there are some classes which represents the basic objects in quantum computing such as: a qubit, a register, a gate, a layer and a circuit. These objects (and therefore the classes which represents them) are built on each other. Due to this concept a register is built on qubits, layers are formed by gates and circuits are created out of gates.
There is a sixth class, the bloch class which is used for teh Bloch representation and visualisation of a qubit.

## 3.1 Qubit class

In quantum computing a qubit or quantum bit is the basic unit of quantum information. Every qubit has two clear states such as 0 and 1 but unlike a classical bit a qubit can be in superposition which is a special  mixture of these clear states.

**qvantum.Qubit.__init__(alpha, beta)**

Method to initialize an instance of the qubit class. The squared sum of alpha and beta bust be equal to zero otherwise a ValueError will be thrown.

*Parameters:*

 - alpha: int, float or complex
 - beta: int, float or complex

*Examples:*

![](Pic/311_Qubit_init.png?raw=true "Qubit.__init__()")

> Written with [StackEdit](https://stackedit.io/).
