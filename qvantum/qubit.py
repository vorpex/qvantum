'''
qubit class

Using qubit class, the user can create qubit objects. When creating a qubit object, the amplitudes
must satisfy that |alpha|^2 + |beta|^2 = 1.

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
'''

# pylint: disable=E1101

import check_qubit
import numpy
import unicodedata

class Qubit(object):
    ''' qubit class '''

    @check_qubit.qubit_init_check
    def __init__(self, alpha, beta):
        ''' initialize qubit '''

        self.__alpha = alpha
        self.__beta = beta

    def get_alpha(self):
        ''' getter of alpha '''

        return self.__alpha

    def get_beta(self):
        ''' getter of beta '''

        return self.__beta

    @check_qubit.set_amplitudes_check
    def set_amplitudes(self, alpha, beta):
        ''' setter of alpha, beta '''

        self.__alpha = alpha
        self.__beta = beta

    def show(self):
        ''' qubit representation '''

        return '|' + unicodedata.lookup('GREEK CAPITAL LETTER PSI') + '> = ' +\
            '({0:.4f}{1}{2:.4f}i)'.format(self.__alpha.real, '+-'[self.__alpha.imag < 0], \
            abs(self.__alpha.imag)) + '|0> + ' + '({0:.4f}{1}{2:.4f}i)'.format(self.__beta.real, \
            '+-'[self.__beta.imag < 0], abs(self.__beta.imag)) + '|1>'

    def measure(self):
        ''' measure the qubit '''

        result = numpy.random.choice([0, 1], p=[abs(self.__alpha) ** 2, abs(self.__beta) ** 2])
        if result == 0:
            self.__alpha = 1
            self.__beta = 0

        else:
            self.__alpha = 0
            self.__beta = 1
        
        return int(result)

    def ket(self):
        ''' return the ket vector of the qubit '''

        ket = numpy.array([self.__alpha, self.__beta])
        ket.shape = (2, 1)
        return ket

    def bra(self):
        ''' return the bra vector of the qubit '''

        bra = self.ket().transpose()
        return bra

class Random_Qubit(Qubit):
    ''' random qubit class '''

    def __init__(self):
        ''' initialize random qubit '''

        Qubit.__init__(self, 1, 0)

        alpha = numpy.random.uniform(0, 1)
        alpha1 = numpy.random.choice([-1, 1]) * numpy.sqrt(numpy.random.uniform(0, alpha))
        alpha2 = numpy.random.choice([-1, 1]) * numpy.sqrt(alpha - alpha1 ** 2)

        beta1 = numpy.random.choice([-1, 1]) * numpy.sqrt(numpy.random.uniform(0, 1 - alpha))
        beta2 = numpy.random.choice([-1, 1]) * numpy.sqrt(1 - alpha - beta1 ** 2)

        # super().set_amplitudes(complex(alpha1, alpha2), complex(beta1, beta2))
        super(Random_Qubit, self).set_amplitudes(complex(alpha1, alpha2), complex(beta1, beta2))
