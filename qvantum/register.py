'''register class'''

# pylint: disable=E1101, W1401

from . import check_register
import collections
import itertools
import numpy
import unicodedata

class Register(object):
    """register class
   
    A system containing more than one qubit is called a register. The state function of a 
    register is the superposition of the allowed states of the qubits. The number of possible 
    states is increasing exponentially with every new qubit is added to the system.

    "A quantum register is a system comprising multiple qubits and is the quantum analog of the 
    classical processor register. An n size quantum register is a quantum system comprising n qubits.
    The Hilbert space, H, in which the data stored in a quantum register is:
        
        H = H(n-1) × H(n-2) × ... × H(0)."

    via Wikipedia: https://en.wikipedia.org/wiki/Quantum_register

    The instances of the register class have the following methods:

    - __init__()          - initialize register
    - get_coeff_list()    - getter of coefficients of qubits
    - get_state_number()  - getter of number of possible states
    - get_qubit_number()  - getter of number of qubits in the register
    - get_states()        - getter of states
    - get_amplitudes()    - getter of amplitudes
    - set_amplitudes()    - setter of amplitudes
    - show()              - register representation
    - measure_register()  - measure the whole register
    - measure_nth_qubit() - measure the n-th qubit
    - ket()               - return the ket vector of register
    - bra()               - return the bra vector of register
    - delete_qubit()      - delete qubit from register
    - insert_qubit()      - insert qubit into register
    """

    @check_register.register_init_check
    def __init__(self, qubit_list):
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
            >>> r = qvantum.Register([q1, q2])
            >>> r.show()
            '|Ψ> = (-0.4171-0.2953i)|00> + (-0.4106-0.7059i)|01> + (-0.1120-0.0875i)|10> + (-0.1049-0.2015i)|11>'
        """

        self.__coeff_list = [[q.get_alpha(), q.get_beta()] for q in qubit_list]

        states_list = list(itertools.product(range(2), repeat=len(qubit_list)))
        states = [''.join(map(str, states_list[i])) for i in range(len(states_list))]
        states.sort()
        coeffs = []
        for state in states:

            product = 1
            for i in range(len(state)):
                
                if state[i] == '0':
                    product = product * qubit_list[i].get_alpha()

                else:
                    product = product * qubit_list[i].get_beta()

            coeffs.append(product)

        self.__state_vector = collections.OrderedDict(zip(states, coeffs))

    def get_coeff_list(self):
        """Method to return the coefficients of the qubits in the regsiter.

        Examples:
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
        """

        return self.__coeff_list
    
    def get_state_number(self):
        """Method to return the number of the possible clear states for the register.

        Examples:
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
        """

        return int(len(self.__state_vector))
    
    def get_qubit_number(self):
        """Method to return the number of the qubits in the register.

        Examples:
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
        """

        return int(numpy.log2(self.get_state_number()))

    @check_register.get_states_check
    def get_states(self, nth=None):
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
        """

        if nth is None:
            return list(self.__state_vector.keys())
        
        else:
            return list(self.__state_vector.keys())[nth]

    @check_register.get_amplitudes_check
    def get_amplitudes(self, nth=None):
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
        """

        if nth is None:
            return list(self.__state_vector.values())

        else:
            return list(self.__state_vector.values())[nth]
    
    @check_register.set_amplitudes_check
    def set_amplitudes(self, amp_list):
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

        if len(amp_list) == self.get_state_number():
            i = 0
            for key in self.__state_vector:

                self.__state_vector[key] = amp_list[i]
                i = i + 1

        else:
            raise ValueError('Invalid input! The amplitudes list must be the same size as the ' +\
                'number of possible states.')

    def show(self):
        """Method to show the state function of the register object.

        Examples:
            >>> import qvantum
            >>>
            >>> q1 = qvantum.Random_Qubit()
            >>> q2 = qvantum.Random_Qubit()
            >>> q3 = qvantum.Random_Qubit()
            >>>
            >>> r = qvantum.Register([q1, q2, q3])
            >>> r.show()
            '|Ψ> = (0.3299-0.0125i)|000> + (-0.2215-0.2264i)|001> + (-0.4390+0.3714i)|010> + (0.5469+0.0726i)|011> + (0.1145-0.0835i)|100> + (-0.1332-0.0276i)|101> + (-0.0674+0.2375i)|110> + (0.2123-0.1052i)|111>'
        """

        keys = list(self.__state_vector.keys())
        values = list(self.__state_vector.values())
        state_string = '|' + unicodedata.lookup('GREEK CAPITAL LETTER PSI') + '> ='
        
        for i in range(len(keys)):

            state_string = state_string + ' ' + '({0:.4f}{1}{2:.4f}i)'.format(values[i].real, \
                '+-'[values[i].imag < 0], abs(values[i].imag)) + '|' + keys[i] + '> +'
        
        state_string = state_string[:-2]

        return state_string

    def measure_register(self):
        """Method to perform a measurement on the whole register and return the final state of the 
        register after the process. This final state is randomized regarding to the amplitudes of 
        the register.

        Examples:
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
        """

        result = numpy.random.choice(list(self.__state_vector.keys()), \
            p=list(numpy.square(numpy.absolute(numpy.array(list(self.__state_vector.values()))))))
        for key in self.__state_vector:

            if key == result:
                self.__state_vector[key] = 1

            else:
                self.__state_vector[key] = 0

        return result
    
    @check_register.measure_nth_qubit_check
    def measure_nth_qubit(self, nth):
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
            >>> r.measure_nth_qubit(2)
            1
            >>> r.show()
            '|Ψ> = (0.0000+0.0000i)|000> + (0.3921+0.5707i)|001> + (0.0000+0.0000i)|010> + (0.0153-0.0315i)|011> + (0.0000+0.0000i)|100> + (0.7196-0.0095i)|101> + (0.0000+0.0000i)|110> + (-0.0184-0.0314i)|111>'
        """

        result0 = []
        for key in self.__state_vector:

            if key[nth] == '0':
                result0.append(self.__state_vector[key])
        
        prob0 = numpy.sum(numpy.square(numpy.absolute(numpy.array(result0))))
        result = numpy.random.choice([0, 1], p=[prob0, 1 - prob0])
        
        for key in self.__state_vector:

            if key[nth] != str(result):
                self.__state_vector[key] = 0
        
        renorm = numpy.sum(numpy.square(numpy.absolute(numpy.array( \
            list(self.__state_vector.values())))))
    
        for key in self.__state_vector:

            self.__state_vector[key] = self.__state_vector[key] / numpy.sqrt(renorm)

        return int(result)
    
    def ket(self):
        """Method to return with the ket vector representation of the register.

        Examples:
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
        """

        ket = numpy.array(list(self.__state_vector.values()))
        ket.shape = (len(ket), 1)
        return ket

    def bra(self):
        """Method to return with the bra vector representation of the register.

        Examples:
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
        """

        bra = self.ket().transpose()
        return bra

    @check_register.delete_qubit_check
    def delete_qubit(self, nth):
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
            >>> r.delete_qubit(2)
            >>> r.show()
            '|Ψ> = (0.4927-0.6160i)|00> + (-0.0083-0.5904i)|01> + (0.1364-0.0024i)|10> + (0.0777-0.0663i)|11>'            
        """

        if nth >= 0 and nth <= self.get_qubit_number() - 1:
            keys =[]
            for key in self.__state_vector:

                list_key = list(key)
                list_key.pop(nth)
                keys.append(''.join(list_key))
            
            values = list(self.__state_vector.values())
            
            self.__state_vector = collections.OrderedDict()
            for i in range(len(keys)):

                if keys[i] not in list(self.__state_vector.keys()):
                    self.__state_vector[keys[i]] = values[i]

                else:
                    self.__state_vector[keys[i]] = self.__state_vector[keys[i]] + values[i]

            for key in self.__state_vector:

                if self.__coeff_list[nth][0] == -1 * self.__coeff_list[nth][1]:
                    self.__state_vector[key] = 1
                # qubit.Qubit(-1 / numpy.sqrt(2), 1 / numpy.sqrt(2)) causes problem
                else:
                    self.__state_vector[key] = self.__state_vector[key] / \
                        (self.__coeff_list[nth][0] + self.__coeff_list[nth][1])

        else:
            raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +\
                'less or equal to ' + str(self.get_qubit_number() - 1) + '.')
    
    @check_register.insert_qubit_check
    def insert_qubit(self, q, nth):
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
            >>> r.insert_qubit(q3, 2)
            >>> r.show()
            '|Ψ> = (-0.0764+0.1775i)|000> + (-0.0002-0.1162i)|001> + (0.3584+0.1790i)|010> + (-0.2404-0.0133i)|011> + (-0.3035+0.0960i)|100> + (0.1446-0.1253i)|101> + (0.1629+0.6394i)|110> + (-0.2424-0.3140i)|111>'
            >>> r.insert_qubit(q3, 2)
            >>> r.show()
            '|Ψ> = (-0.1362-0.0942i)|0000> + (0.0976+0.0195i)|0001> + (0.0976+0.0195i)|0010> + (-0.0585+0.0125i)|0011> + (-0.2109+0.2709i)|0100> + (0.0518-0.1998i)|0101> + (0.0518-0.1998i)|0110> + (0.0190+0.1226i)|0111> + (-0.0293-0.2712i)|1000> + (0.0809+0.1427i)|1001> + (0.0809+0.1427i)|1010> + (-0.0786-0.0595i)|1011> + (-0.5648+0.0288i)|1100> + (0.3048-0.1506i)|1101> + (0.3048-0.1506i)|1110> + (-0.1323+0.1558i)|1111>'
        """

        if nth >= 0 and nth <= self.get_qubit_number():
            qubit_keys = ['0', '1']
            qubit_values = [q.get_alpha(), q.get_beta()]
            keys = list(self.__state_vector.keys())
            values = list(self.__state_vector.values())
            state_dict = collections.OrderedDict()
            for i in range(self.get_state_number()):
                for j in range(2):

                    state_dict[keys[i][:nth] + qubit_keys[j] + keys[i][nth:]] = \
                        values[i] * qubit_values[j]

            self.__state_vector = collections.OrderedDict(sorted(state_dict.items()))

        else:
            raise ValueError('Invalid input! Argument must be greater or equal to 0 and ' +\
                'less or equal to ' + str(self.get_qubit_number()) + '.')
