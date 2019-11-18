'''checking functions for circuit class'''

# pylint: disable=E1101, W1401

from . import layer
from . import register

def circuit_init_check(function):
    """Decorator to check the arguments of initialization function in circuit class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, layer_list):
        """Method to initialize an instance of the Circuit class. The argument must be a list 
        of objects in the Layer class with the same size.
        
        Arguments:
            layer_list {list} -- List of objects from Layer class
        
        Raises:
            ValueError, TypeError
        
        Examples:
            >>> import qvantum
            >>>
            >>> l1 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
            >>> l2 = qvantum.Layer([qvantum.PauliY(), qvantum.PauliX()])
            >>> c = qvantum.Circuit([l1, l2])
            >>> c.get_layer_list()
            OrderedDict([(0, <qvantum.layer.Layer at 0x27b474c2cf8>), (1, <qvantum.layer.Layer at 0x27b47bf2198>)])
            >>> c.get_nth_layer(0)
            <qvantum.layer.Layer at 0x27b474c2cf8>
        """

        if isinstance(layer_list, list) \
            and all(isinstance(elem, layer.Layer) for elem in layer_list):
            return function(self, layer_list)
        
        else:
            raise TypeError('Invalid input! Argument must be a list of layer objects.')
    
    return wrapper

def get_nth_layer_check(function):
    """Decorator to check the arguments of getting nth layer function.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, nth):
        """Method to return the n-th layer in the current Circuit object. The parameter must be 
        between 0 and the actual number of the layers.
        
        Arguments:
            nth {int} -- Number of nth possible layer
        
        Raises:
            TypeError
        
        Examples:
            >>> import qvantum
            >>>
            >>> l1 = qvantum.Layer([qvantum.Hadamard(), qvantum.Gate()])
            >>> l2 = qvantum.Layer([qvantum.PauliY(), qvantum.PauliX()])
            >>> c = qvantum.Circuit([l1, l2])
            >>> c.get_layer_list()
            OrderedDict([(0, <qvantum.layer.Layer at 0x27b474c2cf8>), (1, <qvantum.layer.Layer at 0x27b47bf2198>)])
            >>> c.get_nth_layer(1)
            <qvantum.layer.Layer at 0x27b47bf2198>
        """

        if isinstance(nth, int):
            return function(self, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be integer.')
    
    return wrapper

def delete_layer_check(function):
    """Decorator to check the arguments of deleting layer function.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, nth):
        """Method to delete the n-th layer from the current Circuit object. The parameter must 
        be equal to or bigger than 0 and less than the actual number of the layers in the Circuit.
        
        Arguments:
            nth {int} -- Number of layer to be deleted
        
        Raises:
            ValueError, TypeError
        
        Examples:
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
        """

        if isinstance(nth, int):
            return function(self, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be integer.')
    
    return wrapper

def insert_layer_check(function):
    """Decorator to check the arguments of inserting layer function.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, l, nth):
        """Method to insert a Layer object into the n-th place in the current Circuit object. The 
        first parameter must be a Layer object while the second parameter must be equal to or 
        bigger than 0 and equal to or less than the actual size of the layers in the Circuit. The 
        size of the Layer object must be equal to the size of the already used Layers in the 
        Circuit.
        
        Arguments:
            l {layer} -- Layer to be inserted
            nth {int} -- Index where the layer to be inserted
        
        Raises:
            ValueError, TypeError
        
        Examples:
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
        """

        if isinstance(l, layer.Layer) and isinstance(nth, int):
            return function(self, l, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be a pair of layer object and integer.')
    
    return wrapper

def run_check(function):
    """Decorator to check the arguments of running circuit function.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, r):
        """Method to perform the computational process on a Register object as input and returns 
        the result. The size of the Register object and the size of the Circuit object must be 
        equal.
        
        Arguments:
            r {register} -- Register which the circuit is applied on
        
        Raises:
            ValueError, TypeError
        
        Examples:
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
        """

        if isinstance(r, register.Register):
            return function(self, r)
        
        else:
            raise TypeError('Invalid input! Argument must be a register object.')
    
    return wrapper
