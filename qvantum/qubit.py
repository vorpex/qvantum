'''qubit class'''

# pylint: disable=E1101, W1401

from . import check_qubit
import numpy
import unicodedata

class Qubit(object):
    """qubit class

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
    - show()           - qubit representation
    - measure()        - measure qubit
    - ket()            - return the ket vector of qubit
    - bra()            - return the bra vector of qubit

    The random_qubit class is the same as qubit class the only difference that an instance of the
    class is created with random amplitudes (alpha, beta). They share the same methods.
    """
 
    @check_qubit.qubit_init_check
    def __init__(self, alpha, beta):
        """Method to initialize an instance of the qubit class. The squared sum of alpha and beta 
        must be equal to zero otherwise a ValueError will be thrown.
        
        Arguments:
            alpha {int, float, complex} -- Amplitude or probability of being in state 0
            beta {int, float, complex} -- Amplitude or probability of being in state 1
        
        Raises:
            ValueError, TypeError
        
        Examples:
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
            ValueError                                Traceback (most recent call last)
            <ipython-input-5-9536e50fb31e> in <module>
            ----> 1 q = qvantum.Qubit(5, 2)

            c:\ProgramData\Anaconda3\Lib\site-packages\qvantum\check_qubit.py in wrapper(self, alpha, beta)
                14             else:
                15                 raise ValueError('Invalid input! Alpha and beta must statisfy: ' +\
            ---> 16                     '|alpha|\u00b2 + |beta|\u00b2 = 1.')
                17 
                18         else:

            ValueError: Invalid input! Alpha and beta must statisfy: |alpha|² + |beta|² = 1.
            >>> q = qvantum.Qubit(1, ’shoe’)
              File "<ipython-input-6-7c844cc7dd1e>", line 1
            q = qvantum.Qubit(1, ’shoe’)
                             ^
            SyntaxError: invalid character in identifier
        """

        self.__alpha = alpha
        self.__beta = beta

    def get_alpha(self):
        """Getter method of alpha.

        Examples:
            >>> import qvantum
            >>>
            >>> q = qvantum.Qubit(1, 0)
            >>> q.get_alpha()
            1
        """

        return self.__alpha

    def get_beta(self):
        """Getter method of beta.

        Examples:
            >>> import qvantum
            >>>
            >>> q = qvantum.Qubit(1, 0)
            >>> q.get_beta()
            0
        """

        return self.__beta

    @check_qubit.set_amplitudes_check
    def set_amplitudes(self, alpha, beta):
        """Setter method to replace the old coefficients to new ones. The squared sum of alpha and 
        beta must be equal to zero otherwise a ValueError will be thrown.
        
        Arguments:
            alpha {int, float, complex} -- Amplitude or probability of being in state 0
            beta {int, float, complex} -- Amplitude or probability of being in state 1
        
        Raises:
            ValueError, TypeError
        
        Examples:
            >>> import math
            >>> import qvantum
            >>>
            >>> q = qvantum.Qubit(1, 0)
            >>> q.show()
            '|Ψ> = (1.0000+0.0000i)|0> + (0.0000+0.0000i)|1>'
            >>> q.set_amplitudes(0, 1)
            >>> q.show()
            '|Ψ> = (0.0000+0.0000i)|0> + (1.0000+0.0000i)|1>'
        """

        self.__alpha = alpha
        self.__beta = beta

    def show(self):
        """Method to show the state function of the qubit object.

        Examples:
            >>> import qvantum
            >>>
            >>> q = qvantum.Qubit(1, 0)
            >>> q.show()
            '|Ψ> = (1.0000+0.0000i)|0> + (0.0000+0.0000i)|1>'
        """

        return '|' + unicodedata.lookup('GREEK CAPITAL LETTER PSI') + '> = ' +\
            '({0:.4f}{1}{2:.4f}i)'.format(self.__alpha.real, '+-'[self.__alpha.imag < 0], \
            abs(self.__alpha.imag)) + '|0> + ' + '({0:.4f}{1}{2:.4f}i)'.format(self.__beta.real, \
            '+-'[self.__beta.imag < 0], abs(self.__beta.imag)) + '|1>'

    def measure(self):
        """Method to perform a measurement on the qubit and return with one clear state by the 
        distribtion according to the coefficients.

        Examples:
            >>> import qvantum
            >>>
            >>> q = qvantum.Random_Qubit()
            >>> q.show()
            '|Ψ> = (-0.2867+0.5283i)|0> + (-0.2608+0.7555i)|1>'
            >>> q.measure()
            1
            >>> q.show()
            '|Ψ> = (0.0000+0.0000i)|0> + (1.0000+0.0000i)|1>'
        """

        result = numpy.random.choice([0, 1], p=[abs(self.__alpha) ** 2, abs(self.__beta) ** 2])
        if result == 0:
            self.__alpha = 1
            self.__beta = 0

        else:
            self.__alpha = 0
            self.__beta = 1
        
        return int(result)

    def ket(self):
        """Method to return with the ket vector representation of the qubit.

        Examples:
            >>> import qvantum
            >>>
            >>> q = qvantum.Random_Qubit()
            >>> q.ket()
            array([[-0.76536276+0.20163924j],
                   [-0.39225178-0.46872167j]])
        """

        ket = numpy.array([self.__alpha, self.__beta])
        ket.shape = (2, 1)
        return ket

    def bra(self):
        """Method to return with the bra vector representation of the qubit.

        Examples:
            >>> import qvantum
            >>>
            >>> q = qvantum.Random_Qubit()
            >>> q.bra()
            array([[-0.76536276+0.20163924j, -0.39225178-0.46872167j]])
        """

        bra = self.ket().transpose()
        return bra

class Random_Qubit(Qubit):
    """This is an inhereted class from the Qubit class. They share the same methods but when an 
    instance of the Random_Qubit class is created the coefficients are randomly choosen.
    
    Arguments:
        Qubit {qubit} -- qubit class
    """

    def __init__(self):
        """Method to initialize an instance of the qubit class with randomized amplitudes.

        Examples:
            >>> import qvantum
            >>>
            >>> rq = qvantum.Random_Qubit()
            >>> rq.show()
            '|Ψ> = (-0.5736+0.2506i)|0> + (0.5223-0.5791i)|1>'
            >>> qvantum.Random_Qubit().show()
            '|Ψ> = (-0.1949+0.9475i)|0> + (0.1028+0.2318i)|1>'
        """

        Qubit.__init__(self, 1, 0)

        alpha = numpy.random.uniform(0, 1)
        alpha1 = numpy.random.choice([-1, 1]) * numpy.sqrt(numpy.random.uniform(0, alpha))
        alpha2 = numpy.random.choice([-1, 1]) * numpy.sqrt(alpha - alpha1 ** 2)

        beta1 = numpy.random.choice([-1, 1]) * numpy.sqrt(numpy.random.uniform(0, 1 - alpha))
        beta2 = numpy.random.choice([-1, 1]) * numpy.sqrt(1 - alpha - beta1 ** 2)

        # super().set_amplitudes(complex(alpha1, alpha2), complex(beta1, beta2))
        super(Random_Qubit, self).set_amplitudes(complex(alpha1, alpha2), complex(beta1, beta2))
