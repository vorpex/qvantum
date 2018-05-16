''' bloch sphere '''

# pylint: disable=E1127, E1601
from itertools import product, combinations
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import qubit_class as qubit

def bloch_sphr(qubit):
    ''' calculate bloch coordinates from qubit '''
    if isinstance(qubit, qubit.qubit):
        if qubit.check() == 1:
            P00 = qubit.alfa.real ** 2 + qubit.alfa.imag ** 2
            P01 = complex(\
                qubit.alfa.real * qubit.beta.real + qubit.alfa.imag * qubit.beta.imag,\
                qubit.alfa.imag * qubit.beta.real - qubit.alfa.real * qubit.beta.imag)
            P10 = complex(\
                qubit.alfa.real * qubit.beta.real + qubit.alfa.imag * qubit.beta.imag,\
                qubit.alfa.real * qubit.beta.imag - qubit.alfa.imag * qubit.beta.real)
            P11 = qubit.beta.real ** 2 + qubit.beta.imag ** 2

            u = P10.real + P01.real
            v = (P01.imag - P10.imag) * -1
            w = P00 - P11

            if round(u ** 2 + v ** 2 + w ** 2, 10) == 1:
                # print 'qubit REPRESENTATION:' + \
                # '\n' + 'alfa = ' + str(complex(round(qubit.alfa.real, 4), round(qubit.alfa.imag, 4))) + \
                # '\n' + 'beta = ' + str(complex(round(qubit.beta.real, 4), round(qubit.beta.imag, 4))) + \
                # '\n\n' + 'BLOCH COORDS REPRESENTATION:' + \
                # '\n' + 'u = ' + str(round(u, 4)) + '\n' + 'v = ' + str(round(v, 4)) +\
                # '\n' + 'w = ' + str(round(w, 4))
                return qubit.alfa, qubit.beta, u, v, w
            else:
                return 'Error: u^2 + v^2 + w^2 != 1'
        else:
            return 'abs(alfa)^2 + abs(beta)^2 != 1. Use proper qubit!'
    else:
        return 'Wrong argument: not in qubit class!'

def bloch_qubit(u, v, w):
    ''' calculate qubit from bloch coordinates '''
    if isinstance(u, (int, float)) and \
    isinstance(v, (int, float)) and \
    isinstance(w, (int, float)):
        if round(u ** 2 + v ** 2 + w ** 2, 10) == 1:
            alfa = math.cos(math.acos(w) / 2)
            beta1 = math.sin(math.acos(w) / 2) * u / math.sin(math.acos(w))
            beta2 = math.sin(math.acos(w) / 2) * v / math.sin(math.acos(w))
            beta = complex(beta1, beta2)

            if round(abs(alfa) ** 2 + abs(beta) ** 2, 10) == 1:
                # print 'BLOCH COORDS REPRESENTATION:' + \
                # '\n' + 'u = ' + str(round(u, 4)) + '\n' + 'v = ' + str(round(v, 4)) +\
                # '\n' + 'w = ' + str(round(w, 4)) + \
                # '\n\n' + 'qubit REPRESENTATION:' + \
                # '\n' + 'alfa = ' + str(round(alfa, 4)) + \
                # '\n' + 'beta = ' + str(complex(round(beta1, 4), round(beta2, 4)))
                return u, v, w, alfa, beta
            else:
                return 'Error: abs(alfa)^2 + abs(beta)^2 != 1'
        else:
            return 'u^2 + v^2 + w^2 != 1. Use proper coordinates!'
    else:
        return 'Wrong arguments: use integer, long or float numbers!'

def phase_test(c1, c2):
    ''' compute phase between two complex number '''
    if isinstance(c1, (int, float, complex)) and \
    isinstance(c2, (int, float, complex)):
        phase = (c1.real * c2.real + c1.imag * c2.imag) / \
        (math.sqrt(c1.real ** 2 + c1.imag ** 2) * math.sqrt(c2.real ** 2 + c2.imag ** 2))

        # print 'Phase between ' + str(complex(round(c1.real, 4), round(c1.imag, 4))) + ' and ' + \
        # str(complex(round(c2.real, 4), round(c2.imag, 4))) + ': ' + str(round(phase, 4))
        return phase
    else:
        return 'Wrong arguments: use integer, long or float numbers!'

def bloch_coords_plot(U, V, W):
    ''' plot bloch representation '''
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect('equal')

    u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
    x = np.cos(u) * np.sin(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(v)
    ax.plot_wireframe(x, y, z, color='r')

    ax.scatter([0], [0], [0], color='g', s=100)
    ax.quiver(0, 0, 0, U, V, W)

    plt.show()
    return None

q = qubit.Qubit()
print(bloch_sphr(q))
u = bloch_sphr(q)[2]
v = bloch_sphr(q)[3]
w = bloch_sphr(q)[4]
print(bloch_qubit(u, v, w))
alfa = bloch_qubit(u, v, w)[3]
beta = bloch_qubit(u, v, w)[4]
print(phase_test(q.alfa, alfa))
print(phase_test(q.beta, beta))
bloch_coords_plot(-0.8154, 0.4743, 0.3320)
bloch_coords_plot(0, 0, 1)
bloch_coords_plot(0, 0, -1)
