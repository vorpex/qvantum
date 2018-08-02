'''
Qubit class

Using Qubit class, the user can create qubit objects. When creating a qubit object, the parameters
must satisfy that |alpha|^2 + |beta|^2 = 1. Parameters can have the following types:

- None
- int
- long
- float
- complex

If the specified parameters are of the wrong types or do not meet the above criterion or
the type of both of the parameters is None, then the qubit object is randomly generated.

The instances of the Qubit class have the following methods:

- __init__()       - initialize qubit
- get_alpha()      - getter of alpha
- get_beta()       - getter of beta
- set_parameters() - setter of alpha, beta
- check()     	   - check that |alpha|^2 + |beta|^2 = 1
- show()      	   - qubit representation
- measure()   	   - measure the qubit
- ket()       	   - return the ket vector of the qubit
- bra()       	   - return the bra vector of the qubit
'''

# pylint: disable=E1101

import logging
import math
import numpy
import random
import unicodedata

class Qubit(object):
    ''' qubit class '''

    def __init__(self, alpha=None, beta=None):
        ''' initialize qubit '''

        if isinstance(alpha, (int, long, float, complex)) \
        and isinstance(beta, (int, long, float, complex)) \
        and round(abs(alpha) ** 2 + abs(beta) ** 2 - 1, 10) == 0:
             self.__alpha = complex(alpha.real, alpha.imag)
             self.__beta = complex(beta.real, beta.imag)

        elif isinstance(alpha, (int, long, float, complex)) \
        and beta is None \
        and abs(alpha) ** 2 <= 1:
             self.__alpha = alpha
             self.__beta = math.sqrt(1 - abs(alpha) ** 2)

        elif alpha is None \
        and isinstance(beta, (int, long, float, complex)) \
        and abs(beta) ** 2 <= 1:
             self.__alpha = math.sqrt(1 - abs(beta) ** 2)
             self.__beta = beta

        else:
            if alpha is not None or beta is not None:
                logging.warning('Invalid input! Please use the following types: None, int, long' +\
                ', float or complex. Make sure that |alpha|\u00b2 + |beta|\u00b2 = 1. Qubit is ' +\
                'randomly generated.')
            
            ALPHA = random.uniform(0, 1)

            alpha1 = random.choice([-1, 1]) * math.sqrt(random.uniform(0, ALPHA))
            alpha2 = random.choice([-1, 1]) * math.sqrt(ALPHA - alpha1 ** 2)
            self.__alpha = complex(alpha1, alpha2)

            beta1 = random.choice([-1, 1]) * math.sqrt(random.uniform(0, 1 - ALPHA))
            beta2 = random.choice([-1, 1]) * math.sqrt(1 - ALPHA - beta1 ** 2)
            self.__beta = complex(beta1, beta2)

    def get_alpha(self):
        ''' getter of alpha '''

        return self.__alpha

    def get_beta(self):
        ''' getter of beta '''

        return self.__beta

    def set_parameters(self, alpha_value, beta_value):
        ''' setter of alpha, beta '''

        if isinstance(alpha_value, (int, long, float, complex)) \
        and isinstance(beta_value, (int, long, float, complex)) \
        and round(abs(alpha_value) ** 2 + abs(beta_value) ** 2 - 1, 10) == 0:
            self.__alpha = alpha_value
            self.__beta = beta_value
        
        else:
            logging.warning('Invalid input! Please use the following types: None, int, ' +\
            'float or complex. Make sure that |alpha|\u00b2 + |beta|\u00b2 = 1. Qubit ' +\
            'remained the same.')

    def check(self):
        ''' check that |alpha|^2 + |beta|^2 = 1 '''

        if round(abs(self.__alpha) ** 2 + abs(self.__beta) ** 2 - 1, 10) == 0:
            return 1

        else:
            return round(abs(self.__alpha) ** 2 + abs(self.__beta) ** 2, 10)

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
        return RESULT

    def ket(self):
        ''' return the ket vector of the qubit '''

        ket = numpy.array([self.__alpha, self.__beta])
        ket.shape = (2, 1)
        return ket

    def bra(self):
        ''' return the bra vector of the qubit '''

        bra = self.ket().transpose()
        return bra
