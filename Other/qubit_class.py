''' qubit class '''

# pylint: disable=E1601
import math
import random
import types
import unicodedata

class Qubit(object):
    ''' qubit class '''
    def __init__(self, alfa=None, beta=None):
        ''' initialize qubit '''
        if isinstance(alfa, (int, float, complex)) \
        and isinstance(beta, (int, float, complex)) \
        and round(abs(alfa) ** 2 + abs(beta) ** 2, 15) == 1:
            self.alfa = alfa
            self.beta = beta
        else:
            # print 'Wrong arguments. State is generated randomly.'

            abs_alfa_2 = random.uniform(0, 1)
            alfa1_2 = random.uniform(0, abs_alfa_2)
            alfa2_2 = abs_alfa_2 - alfa1_2
            alfa1 = math.sqrt(alfa1_2)
            alfa2 = math.sqrt(alfa2_2)

            if random.randint(0, 1) == 0:
                c1 = 1
            else:
                c1 = -1
            if random.randint(0, 1) == 0:
                c2 = 1
            else:
                c2 = -1

            self.alfa = complex(c1 * alfa1, c2 * alfa2)

            abs_beta_2 = 1 - abs_alfa_2
            beta1_2 = random.uniform(0, abs_beta_2)
            beta2_2 = abs_beta_2 - beta1_2
            beta1 = math.sqrt(beta1_2)
            beta2 = math.sqrt(beta2_2)

            if random.randint(0, 1) == 0:
                C1 = 1
            else:
                C1 = -1
            if random.randint(0, 1) == 0:
                C2 = 1
            else:
                C2 = -1

            self.beta = complex(C1 * beta1, C2 * beta2)

    def show(self):
        ''' qubit representation '''
        a1 = round(self.alfa.real, 4)
        a2 = round(self.alfa.imag, 4)

        if a2 == 0:
            A = a1
        else:
            A = complex(a1, a2)

        b1 = round(self.beta.real, 4)
        b2 = round(self.beta.imag, 4)

        if b2 == 0:
            B = b1
        else:
            B = complex(b1, b2)

        return '|' + unicodedata.lookup('GREEK CAPITAL LETTER PSI') + '> = ' + \
        str(A) + '|0> + ' + str(B) + '|1>'

    def check(self):
        ''' check the sum of alfa ** 2 and beta ** 2 '''
        return round(abs(self.alfa) ** 2 + abs(self.beta) ** 2, 10)

    def measure(self):
        ''' measure the qubit '''
        treshold = random.uniform(0, 1)
        if self.alfa == 1 and self.beta == 0:
            # print '|0>'
            return 0
        elif self.alfa == 0 and self.beta == 1:
            # print '|1>'
            return 1
        elif treshold <= abs(self.alfa) ** 2:
            # print '|0>'
            self.alfa = 1
            self.beta = 0
            return 0
        else:
            # print '|1>'
            self.alfa = 0
            self.beta = 1
            return 1

q1 = Qubit()
print(q1.alfa, q1.beta)
print(q1.check())
print(q1.show(), '\n')

# q2 =Qubit(math.sqrt(0.5), math.sqrt(0.5))
# print q2.alfa, q2.beta
# print q2.check()
# print q2.show(), '\n'

# q3 =Qubit(math.sqrt(0.5), 3 * math.sqrt(0.5))
# print q3.alfa, q3.beta
# print q3.check()
# print q3.show(), '\n'

# q4 =Qubit('test')
# print q4.alfa, q4.beta
# print q4.check()
# print q4.show(), '\n'
