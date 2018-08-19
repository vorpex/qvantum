'''
Qubit class

Using Qubit class, the user can create qubit objects. When creating a qubit object, the amplitudes
must satisfy that |alpha|^2 + |beta|^2 = 1.

The instances of the Qubit class have the following methods:

- __init__()       - initialize qubit
- get_alpha()      - getter of alpha
- get_beta()       - getter of beta
- set_amplitudes() - setter of alpha, beta
- check()          - check that |alpha|^2 + |beta|^2 = 1
- show()           - qubit representation
- measure()        - measure the qubit
- ket()            - return the ket vector of the qubit
- bra()            - return the bra vector of the qubit

The Random_Qubit class is the same like the Qubit class the only difference that an instance of the
class is created with random amplitudes (alpha, beta). They share the same methods.
'''

# pylint: disable=E1101

import math
import numpy
import random
import unicodedata

class Qubit(object):
    ''' qubit class '''

    def __init__(self, alpha, beta):
        ''' initialize qubit '''

        if round(abs(alpha) ** 2 + abs(beta) ** 2 - 1, 10) == 0:
            self.__alpha = alpha
            self.__beta = beta
        
        else:
            raise ValueError('Invalid input! Alpha and beta must statisfy: ' +\
            '|alpha|\u00b2 + |beta|\u00b2 = 1')

    def get_alpha(self):
        ''' getter of alpha '''

        return self.__alpha

    def get_beta(self):
        ''' getter of beta '''

        return self.__beta

    def set_amplitudes(self, alpha, beta):
        ''' setter of alpha, beta '''

        if round(abs(alpha) ** 2 + abs(beta) ** 2 - 1, 10) == 0:
            self.__alpha = alpha
            self.__beta = beta
        
        else:
            raise ValueError('Invalid input! Alpha and beta must statisfy: ' +\
            '|alpha|\u00b2 + |beta|\u00b2 = 1')

    def check(self):
        ''' check that |alpha|^2 + |beta|^2 = 1 '''

        if round(abs(self.__alpha) ** 2 + abs(self.__beta) ** 2 - 1, 10) == 0:
            return 1

        else:
            return 0

    def show(self):
        ''' qubit representation '''

        return '|' + unicodedata.lookup('GREEK CAPITAL LETTER PSI') + '> = ' +\
        '({0:.4f}{1}{2:.4f}i)'.format(self.__alpha.real, '+-'[self.__alpha.imag < 0], \
        abs(self.__alpha.imag)) + '|0> + ' + '({0:.4f}{1}{2:.4f}i)'.format(self.__beta.real, \
        '+-'[self.__beta.imag < 0], abs(self.__beta.imag)) + '|1>'

    def measure(self):
        ''' measure the qubit '''

        RESULT = numpy.random.choice([0, 1], p=[abs(self.__alpha) ** 2, abs(self.__beta) ** 2])
        if RESULT == 0:
            self.__alpha = 1
            self.__beta = 0

        else:
            self.__alpha = 0
            self.__beta = 1
        
        # print('|' + str(RESULT) + '>')
        return int(RESULT)

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

        ALPHA = random.uniform(0, 1)
        alpha1 = random.choice([-1, 1]) * math.sqrt(random.uniform(0, ALPHA))
        alpha2 = random.choice([-1, 1]) * math.sqrt(ALPHA - alpha1 ** 2)

        beta1 = random.choice([-1, 1]) * math.sqrt(random.uniform(0, 1 - ALPHA))
        beta2 = random.choice([-1, 1]) * math.sqrt(1 - ALPHA - beta1 ** 2)

        # super().set_amplitudes(complex(alpha1, alpha2), complex(beta1, beta2))
        super(Random_Qubit, self).set_amplitudes(complex(alpha1, alpha2), complex(beta1, beta2))
