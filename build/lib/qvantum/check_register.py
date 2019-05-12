'''checking functions for register class'''

# pylint: disable=E1101, W1401

import numpy
from . import qubit

def register_init_check(function):
    """Decorator to check the arguments of initialization function in register class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, qubit_list):
        """Method to initialize an instance of the register class. The input is a list of elements 
        in Qubit or Random_Qubit class. Also this list must contain at least 2 elements.
        
        Arguments:
            qubit_list {list} -- List of objects from Qubit or Random_Qubit class
        
        Raises:
            ValueError, TypeError
        
        Examples:
            >>> import qvantum
            >>>
            >>> q1 = qvantum.Random_Qubit()
            >>> q2 = qvantum.Random_Qubit()
            >>>
            >>> r1 = qvantum.Register([q1])
            ---------------------------------------------------------------------------
            ValueError                                Traceback (most recent call last)
            <ipython-input-28-3c854882d136> in <module>
            ----> 1 r1 = qvantum.Register([q1])

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, qubit_list)
                18             else:
                19                 raise ValueError('Invalid input! Qubit list must contain at least 2 qubit ' +\
            ---> 20                     'object.')
                21 
                22         else:

            ValueError: Invalid input! Qubit list must contain at least 2 qubit object.
            >>> r1 = qvantum.Register([q1, ’shoe’])
              File "<ipython-input-29-5fa49e76c5fb>", line 1
                r1 = qvantum.Register([q1, ’shoe’])
                                                ^
            SyntaxError: invalid character in identifier
            >>> r1 = qvantum.Register({q1, q2})
            ---------------------------------------------------------------------------
            TypeError                                 Traceback (most recent call last)
            <ipython-input-30-ac8d1c1cef5d> in <module>
            ----> 1 r1 = qvantum.Register({q1, q2})

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, qubit_list)
                21 
                22         else:
            ---> 23             raise TypeError('Invalid input! Argument must be a list of qubit objects.')
                24 
                25     return wrapper

            TypeError: Invalid input! Argument must be a list of qubit objects.
            >>> r2 = qvantum.Register([q1, q2])
            >>> r2.show()
            '|Ψ> = (-0.4171-0.2953i)|00> + (-0.4106-0.7059i)|01> + (-0.1120-0.0875i)|10> + (-0.1049-0.2015i)|11>'
        """

        if isinstance(qubit_list, list) \
            and all(isinstance(elem, (qubit.Qubit, qubit.Random_Qubit)) for elem in qubit_list):
            if len(qubit_list) >= 2:
                return function(self, qubit_list)
            
            else:
                raise ValueError('Invalid input! Qubit list must contain at least 2 qubit ' +\
                    'object.')
        
        else:
            raise TypeError('Invalid input! Argument must be a list of qubit objects.')
    
    return wrapper

def get_states_check(function):
    """Decorator to check the arguments of getting states function in register class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, nth=None):
        """Method to return with the n-th possible state for the regsiter if the parameter is 
        definit. If it isn’t then the return value is the list of all possible states.
        
        Keyword Arguments:
            nth {int, None} -- Number of n-th possible state (default: {None})
        
        Raises:
            TypeError
        
        Examples:
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
            IndexError                                Traceback (most recent call last)
            <ipython-input-54-96382c883aac> in <module>
            ----> 1 r.get_states(6)

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, nth)
                31 
                32         if isinstance(nth, int) or nth is None:
            ---> 33             return function(self, nth)
                34 
                35         else:

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\register.py in get_states(self, nth)
                87 
                88         else:
            ---> 89             return list(self.__state_vector.keys())[nth]
                90 
                91     @check_register.get_amplitudes_check

            IndexError: list index out of range
            >>> r.get_states('shoe')
            ---------------------------------------------------------------------------
            TypeError                                 Traceback (most recent call last)
            <ipython-input-55-613fb9d4ee8b> in <module>
            ----> 1 r.get_states('shoe')

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, nth)
                34 
                35         else:
            ---> 36             raise TypeError('Invalid input! Argument must be integer.')
                37 
                38     return wrapper

            TypeError: Invalid input! Argument must be integer.
        """

        if isinstance(nth, int) or nth is None:
            return function(self, nth)

        else:
            raise TypeError('Invalid input! Argument must be integer.')

    return wrapper

def get_amplitudes_check(function):
    """Decorator to check the arguments of getting amplitudes function in register class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, nth=None):
        """Method to return with the coefficient of the n-th possible state for the regsiter 
        if the parameter is definit. If it isn’t, then the return value is the list of the 
        coefficients of all possible states.
        
        Keyword Arguments:
            nth {int, None} -- Number of n-th possible amplitude (default: {None})
        
        Raises:
            TypeError
        
        Examples:
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
            IndexError                                Traceback (most recent call last)
            <ipython-input-60-102f3b99b88f> in <module>
            ----> 1 r.get_amplitudes(6)

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, nth)
                44 
                45         if isinstance(nth, int) or nth is None:
            ---> 46             return function(self, nth)
                47 
                48         else:

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\register.py in get_amplitudes(self, nth)
                97 
                98         else:
            ---> 99             return list(self.__state_vector.values())[nth]
                100 
                101     @check_register.set_amplitudes_check

            IndexError: list index out of range
            >>> r.get_amplitudes('shoe')
            ---------------------------------------------------------------------------
            TypeError                                 Traceback (most recent call last)
            <ipython-input-61-7cf70dfde286> in <module>
            ----> 1 r.get_amplitudes('shoe')

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, nth)
                47 
                48         else:
            ---> 49             raise TypeError('Invalid input! Argument must be integer or None type.')
                50 
                51     return wrapper

            TypeError: Invalid input! Argument must be integer or None type.
        """

        if isinstance(nth, int) or nth is None:
            return function(self, nth)

        else:
            raise TypeError('Invalid input! Argument must be integer or None type.')

    return wrapper

def set_amplitudes_check(function):
    """Decorator to check the arguments of setting amplitudes function in register class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, amp_list):
        """Method to set new coefficients for the possible states of the register. The input 
        parameter is a list of real or complex number and their squared sum must be equal to 1. 
        Number of elements in the least must be equal with the number of possible states.
        
        Arguments:
            amp_list {list} -- List of int, float or complex objects
        
        Raises:
            ValueError, TypeError
        
        Examples:
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
        """

        if isinstance(amp_list, list) \
            and all(isinstance(elem, (int, float, complex)) for elem in amp_list):
            if round(numpy.sum(numpy.square(numpy.absolute(amp_list))) - 1, 10) == 0:
                return function(self, amp_list)

            else:
                raise ValueError('Invalid input! The square sum of absolute value of ' +\
                    'amplitudes must be equal to 1.')
        
        else:
            raise TypeError('Invalid input! Argument must be a list of integer, float or ' +\
                'complex numbers.')
    
    return wrapper

def measure_nth_qubit_check(function):
    """Decorator to check the arguments of measuring qubit function in register class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, nth):
        """Method to perform a measurement on the n-th qubit in the register and return the final 
        state of the register after the process. This final state is randomized regarding to the 
        amplitudes of the register. The input parameter must be an integer corresponding to the 
        number of qubits in the register.
        
        Arguments:
            nth {int} -- Number of n-th possible qubit
        
        Raises:
            TypeError
        
        Examples:
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
            IndexError                                Traceback (most recent call last)
            <ipython-input-81-3e4cf8e71cdd> in <module>
            ----> 1 r.measure_nth_qubit(3)

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, nth)
                77 
                78         if isinstance(nth, int):
            ---> 79             return function(self, nth)
                80 
                81         else:

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\register.py in measure_nth_qubit(self, nth)
                152         for key in self.__state_vector:
                153 
            --> 154             if key[nth] == '0':
                155                 result0.append(self.__state_vector[key])
                156 

            IndexError: string index out of range
            >>> r.measure_nth_qubit('shoe')
            ---------------------------------------------------------------------------
            TypeError                                 Traceback (most recent call last)
            <ipython-input-82-72a46a88351a> in <module>
            ----> 1 r.measure_nth_qubit('shoe')

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, nth)
                80 
                81         else:
            ---> 82             raise TypeError('Invalid input! Argument must be integer.')
                83 
                84     return wrapper

            TypeError: Invalid input! Argument must be integer.
            >>> r.measure_nth_qubit(2)
            1
            >>> r.show()
            '|Ψ> = (0.0000+0.0000i)|000> + (0.3921+0.5707i)|001> + (0.0000+0.0000i)|010> + (0.0153-0.0315i)|011> + (0.0000+0.0000i)|100> + (0.7196-0.0095i)|101> + (0.0000+0.0000i)|110> + (-0.0184-0.0314i)|111>'
        """

        if isinstance(nth, int):
            return function(self, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be integer.')
    
    return wrapper

def delete_qubit_check(function):
    """Decorator to check the arguments of deleting qubit function in register class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, nth):
        """Method to delete the n-th qubit from the regsiter. This method has some drawback which 
        is discussed later. The input parameter must be an integer corresponding to the number of 
        qubits in the register.
        
        Arguments:
            nth {int} -- Number of n-th possible qubit
        
        Raises:
            ValueError, TypeError
        
        Examples:
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
            ValueError                                Traceback (most recent call last)
            <ipython-input-96-60bd02f79762> in <module>
            ----> 1 r.delete_qubit(3)

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, nth)
                90 
                91         if isinstance(nth, int):
            ---> 92             return function(self, nth)
                93 
                94         else:

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\register.py in delete_qubit(self, nth)
                219         else:
                220             raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +\
            --> 221                 'less or equal to ' + str(self.get_qubit_number() - 1) + '.')
                222 
                223     @check_register.insert_qubit_check

            ValueError: Invalid input! Argument must be greater or equal to 0 and less or equal to 2.
            >>> r.delete_qubit()
            ---------------------------------------------------------------------------
            TypeError                                 Traceback (most recent call last)
            <ipython-input-97-82d89a96f88c> in <module>
            ----> 1 r.delete_qubit()

            TypeError: wrapper() missing 1 required positional argument: 'nth'
            >>> r.delete_qubit()
            >>> r.show()
            '|Ψ> = (0.4927-0.6160i)|00> + (-0.0083-0.5904i)|01> + (0.1364-0.0024i)|10> + (0.0777-0.0663i)|11>'
        """
    
        if isinstance(nth, int):
            return function(self, nth)
        
        else:
            raise TypeError('Invalid input! Argument must be integer.')
    
    return wrapper

def insert_qubit_check(function):
    """Decorator to check the arguments of inserting qubit function in register class.
    
    Arguments:
        function {} -- The tested function
    """

    def wrapper(self, q, nth):
        """Method to insert a given qubit into a register. The input parameter must be an integer 
        corresponding to the number of qubits in the register.
        
        Arguments:
            q {qubit} -- The qubit to be inserted
            nth {int} -- The index where the qubit is inserted
        
        Raises:
            ValueError, TypeError
        
        Examples:
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
            ValueError                                Traceback (most recent call last)
            <ipython-input-103-9f4b9a58253e> in <module>
            ----> 1 r.insert_qubit(q3, 3)

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_register.py in wrapper(self, q, nth)
                103 
                104         if isinstance(q, (qubit.Qubit, qubit.Random_Qubit)) and isinstance(nth, int):
            --> 105             return function(self, q, nth)
                106 
                107         else:

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\register.py in insert_qubit(self, q, nth)
                241         else:
                242             raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +\
            --> 243                 'less or equal to ' + str(self.get_qubit_number()) + '.')

            ValueError: Invalid input! Argument must be greater or equal to 0 and less or equal to 2.
            >>> r.insert_qubit(q3, 2)
            >>> r.show()
            '|Ψ> = (-0.0764+0.1775i)|000> + (-0.0002-0.1162i)|001> + (0.3584+0.1790i)|010> + (-0.2404-0.0133i)|011> + (-0.3035+0.0960i)|100> + (0.1446-0.1253i)|101> + (0.1629+0.6394i)|110> + (-0.2424-0.3140i)|111>'
            >>> r.insert_qubit(q3, 2)
            >>> r.show()
            '|Ψ> = (-0.1362-0.0942i)|0000> + (0.0976+0.0195i)|0001> + (0.0976+0.0195i)|0010> + (-0.0585+0.0125i)|0011> + (-0.2109+0.2709i)|0100> + (0.0518-0.1998i)|0101> + (0.0518-0.1998i)|0110> + (0.0190+0.1226i)|0111> + (-0.0293-0.2712i)|1000> + (0.0809+0.1427i)|1001> + (0.0809+0.1427i)|1010> + (-0.0786-0.0595i)|1011> + (-0.5648+0.0288i)|1100> + (0.3048-0.1506i)|1101> + (0.3048-0.1506i)|1110> + (-0.1323+0.1558i)|1111>'
        """

        if isinstance(q, (qubit.Qubit, qubit.Random_Qubit)) and isinstance(nth, int):
            return function(self, q, nth)

        else:
            raise TypeError('Invalid input! Argument must a pair of qubit object and integer.')
    
    return wrapper
