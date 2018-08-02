''' register class '''

# pylint: disable=E1601, W0612
import itertools
import math
import random
import unicodedata
import qubit_class as qubit

class Register(object):
    ''' register class '''
    def __init__(self, nr=None):
        ''' initialize register '''
        self.register = []
        self.coeffs_list = []
        if isinstance(nr, int) and nr == 0:
            pass
        elif isinstance(nr, int) and nr > 0 and nr <= 5:
            for i in range(nr):
                self.register.append(qubit.Qubit())
        else:
            for i in range(random.randint(1, 5)):
                self.register.append(qubit.Qubit())

    def coeffs(self):
        ''' create coefficients '''
        self.coeffs_list = []
        states = list(itertools.product(range(2), repeat=len(self.register)))
        for state in states:
            product = 1            
            for i in range(len(state)):
                if state[i] == 0:
                    product = product * self.register[i].alfa
                else:
                    product = product * self.register[i].beta

            self.coeffs_list.append(product)

        return self.coeffs_list

    def check(self):
        ''' check the 2nd power sum of coefficients '''
        if len(self.coeffs_list) != 2 ** len(self.register):
            self.coeffs()
        else:
            pass

        coeffs_list_abs2 = []
        for coeff in self.coeffs_list:
            coeffs_list_abs2.append(abs(coeff) ** 2)

        return round(sum(coeffs_list_abs2), 10)

    def replace_coeff(self, COEFF, index):
        ''' replace coefficient by index '''
        if len(self.coeffs_list) != 2 ** len(self.register):
            self.coeffs()
        else:
            pass

        if isinstance(COEFF, (int, long, float, complex)):
            try:
                self.coeffs_list[index - 1] = COEFF
                return None
            except BaseException:
                return 'Wrong index!'
        else:
            return 'Wrong COEFF argument'

    def show(self):
        ''' qubit representation '''
        if len(self.coeffs_list) != 2 ** len(self.register):
            self.coeffs()
        else:
            pass

        states = list(itertools.product(range(2), repeat = len(self.register)))
        pszi = '|' + unicodedata.lookup('GREEK CAPITAL LETTER PSI') + '> = '
        for i in range(len(states)):
            if self.coeffs_list[i].imag == 0:
                coeff = round(self.coeffs_list[i].real, 4)
            else:
                coeff = complex(round(self.coeffs_list[i].real, 4), \
                        round(self.coeffs_list[i].imag, 4))

            stt = '|'
            for j in range(len(states[i])):
                stt = stt + str(states[i][j])

            stt = stt + '> + '
            pszi = pszi + str(coeff) + stt

        pszi = pszi[:-3]
        return pszi

    def qubit_numbers(self):
        ''' length of register '''
        return len(self.register)

    def add_qubit(self, QUBIT):
        ''' add qubit to register '''
        if isinstance(QUBIT, qubit.Qubit):
            self.register.append(QUBIT)
            return None
        else:
            return 'Wrong argument: not in qubit class!'

    def remove_qubit(self, index):
        ''' remove qubit by index '''
        try:
            self.register.pop(index - 1)
            return None
        except BaseException:
            self.register.pop()
            return 'Wrong index. Last element is removed.'

    def replace_qubit(self, QUBIT, index):
        ''' replace qubit by index '''
        if isinstance(QUBIT, qubit.Qubit):
            try:
                self.register[index - 1] = QUBIT
                return None
            except BaseException:
                return 'Wrong index!'
        else:
            return 'Wrong argument: not in qubit class!'

    def show_qubit(self, index):
        ''' show i-th qubit '''
        try:
            return self.register[index - 1].show()
        except BaseException:
            return 'Wrong index!'

# r = Register(2)

# print r.show()
# print r.check()
# print r.qubit_numbers()
# print r.show_qubit(1), r.show_qubit(2), '\n'

# r.add_qubit(qubit.Qubit())

# print r.show()
# print r.check()
# print r.qubit_numbers()
# print r.show_qubit(1), r.show_qubit(2), r.show_qubit(3), '\n'

# r.remove_qubit(2)
# r.replace_qubit(qubit.Qubit(), 1)

# print r.show()
# print r.check()
# print r.qubit_numbers()
# print r.show_qubit(1), r.show_qubit(2), '\n'

# r.replace_coeff(1 / math.sqrt(2), 1)
# r.replace_coeff(0, 2)
# r.replace_coeff(0, 3)
# r.replace_coeff(1 / math.sqrt(2), 4)

# print r.show()
# print r.check()
# print r.qubit_numbers()
# print r.show_qubit(1), r.show_qubit(2), '\n'

# r = Register(4)

# print r.show()
# print r.check()
# print r.qubit_numbers(), '\n'

# r = Register()

# print r.show()
# print r.check()
# print r.qubit_numbers(), '\n'
