'''
Bloch Sphere

"In quantum mechanics, the Bloch sphere is a geometrical representation of the pure state space of 
a two-level quantum mechanical system (qubit), named after the physicist Felix Bloch.

Quantum mechanics is mathematically formulated in Hilbert space or projective Hilbert space. The 
space of pure states of a quantum system is given by the one-dimensional subspaces of the 
corresponding Hilbert space (or the "points" of the projective Hilbert space).

The Bloch sphere is a unit 2-sphere, with antipodal points corresponding to a pair of mutually 
orthogonal state vectors. The north and south poles of the Bloch sphere are typically chosen to 
correspond to the standard basis vectors |0> and |1>, respectively, which in turn might correspond 
e.g. to the spin-up and spin-down states of an electron. This choice is arbitrary, however. The 
points on the surface of the sphere correspond to the pure states of the system, whereas the 
interior points correspond to the mixed states."

via Wikipedia: https://en.wikipedia.org/wiki/Bloch_sphere

The following functions are the Bloch Sphere related functions in the package:

- bloch_sphere()      - calculate bloch coordinates from qubit
- bloch_qubit()       - calculate qubit from bloch coordinates
- phase_test()        - compute phase between two complex number
- bloch_coords_plot() - plot bloch representation

bloch_coords_plot(): function uses MATPLOTLIB for ploting purpose and has some parameters to
personalize the user's own graphs. These parameters can be found below with their default value:

- xfigsize = 15
- yfigsize = 7.5
- frame_on = False
- tight_layout_on = True
- style = 'dark_background'
- surface_on = True
- wireframe_on = True
- surface_cmap = 'Blues_r'
- surface_alpha = 0.3
- wireframe_color = '#d3d3d3'
- wireframe_linewidth = 0.075
- quiver_color = '#ffffff'
- quiver_linewidth = 1.5
- quiver_ratio = 0.1
- line_color = '#d3d3d3'
- line_linewidth = 0.3
- circle_edgecolor = '#d3d3d3'
- circle_facecolor = 'none'
- circle_linewidth = 0.3
'''

# pylint: disable=E1127

import logging
import math
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
import numpy
import Qubit

def bloch_sphere(qubit):
    ''' calculate bloch coordinates from qubit '''

    if isinstance(qubit, Qubit.Qubit):
        P00 = complex(qubit.get_alpha().real ** 2 + qubit.get_alpha().imag ** 2, 0)
            
        P01 = complex(qubit.get_alpha().real * qubit.get_beta().real + \
            qubit.get_alpha().imag * qubit.get_beta().imag, \
            qubit.get_alpha().imag * qubit.get_beta().real - \
            qubit.get_alpha().real * qubit.get_beta().imag)
            
        P10 = complex(qubit.get_alpha().real * qubit.get_beta().real + \
            qubit.get_alpha().imag * qubit.get_beta().imag, \
            qubit.get_alpha().real * qubit.get_beta().imag - \
            qubit.get_alpha().imag * qubit.get_beta().real)

        P11 = complex(qubit.get_beta().real ** 2 + qubit.get_beta().imag ** 2, 0)

        u = P10 + P01
        u = u.real
        v = (P01 - P10) * complex(0, 1)
        v = v.real
        w = P00 - P11
        w = w.real

        return u, v, w

    else:
        logging.warning('Invalid input! Not in Qubit class. Please use instance of Qubit class.')

def bloch_qubit(u, v, w):
    ''' calculate qubit from bloch coordinates '''

    if isinstance(u, (int, float)) and isinstance(v, (int, float)) and isinstance(w, (int, float)):
        if round(u ** 2 + v ** 2 + w ** 2 - 1, 10) == 0:
            alpha = complex(math.cos(math.acos(w) / 2), 0)
            
            beta = complex(math.sin(math.acos(w) / 2) * u / math.sin(math.acos(w)), \
                math.sin(math.acos(w) / 2) * v / math.sin(math.acos(w)))

            return Qubit.Qubit(alpha, beta)

        else:
            logging.warning('Invalid input! Use proper coordinates. Make sure that u\u00b2 + ' +\
            'v\u00b2 + w\u00b2 = 1.')

    else:
        logging.warning('Invalid input! Please use the following types: int, float for u, v, w.')

def phase_test(c1, c2):
    ''' compute phase between two complex number '''

    if isinstance(c1, (int, float, complex)) and isinstance(c2, (int, float, complex)):
        phase = (c1.real * c2.real + c1.imag * c2.imag) / \
        (math.sqrt(c1.real ** 2 + c1.imag ** 2) * math.sqrt(c2.real ** 2 + c2.imag ** 2))

        return phase
    
    else:
        logging.warning('Invalid input! Please use the following types: int, float or complex ' +\
        'for c1 and c2.')

def bloch_coords_plot(u, v, w, xfigsize=None, yfigsize=None, frame_on=None, tight_layout_on=None, \
    style=None, surface_on=None, wireframe_on=None, surface_cmap=None, surface_alpha=None, \
    wireframe_color=None, wireframe_linewidth=None, quiver_color=None, quiver_linewidth=None, \
    quiver_ratio=None, line_color=None, line_linewidth=None, circle_edgecolor=None, \
    circle_facecolor=None, circle_linewidth=None):
    ''' plot bloch representation '''

    if isinstance(u, (int, float)) and isinstance(v, (int, float)) and isinstance(w, (int, float)):
        if round(u ** 2 + v ** 2 + w ** 2 - 1, 10) == 0:
            
            if xfigsize is None:
                xfigsize = 15
            
            if yfigsize is None:
                yfigsize = 7.5

            if frame_on is None:
                frame_on = False
            
            if tight_layout_on is None:
                tight_layout_on = True
            
            if style is None:
                style = 'dark_background'
            
            if surface_on is None:
                surface_on = True
            
            if wireframe_on is None:
                wireframe_on = True
            
            if surface_cmap is None:
                surface_cmap = 'Blues_r'

            if surface_alpha is None:
                surface_alpha = 0.3
            
            if wireframe_color is None:
                wireframe_color = '#d3d3d3'

            if wireframe_linewidth is None:
                wireframe_linewidth = 0.075
            
            if quiver_color is None:
                quiver_color = '#ffffff'
            
            if quiver_linewidth is None:
                quiver_linewidth = 1.5
            
            if quiver_ratio is None:
                quiver_ratio = 0.1
            
            if line_color is None:
                line_color = '#d3d3d3'
            
            if line_linewidth is None:
                line_linewidth = 0.3
            
            if circle_edgecolor is None:
                circle_edgecolor = '#d3d3d3'
            
            if circle_facecolor is None:
                circle_facecolor = 'none'
            
            if circle_linewidth is None:
                circle_linewidth = 0.3

            fig = plt.figure(figsize=(xfigsize, yfigsize), frameon=frame_on, \
                tight_layout=tight_layout_on)
            plt.style.use(style)

            ax = fig.add_subplot(111, projection='3d')
            ax.set_aspect('equal')
            ax.set_axis_off()

            a, b = numpy.mgrid[0:2 * numpy.pi:50j, 0:numpy.pi:50j]
            x = numpy.cos(a) * numpy.sin(b)
            y = numpy.sin(a) * numpy.sin(b)
            z = numpy.cos(b)

            if surface_on is True:
                ax.plot_surface(x, y, z, cmap=surface_cmap, alpha=surface_alpha)
            if wireframe_on is True:
                ax.plot_wireframe(x, y, z, color=wireframe_color, linewidth=wireframe_linewidth)
            
            ax.quiver(0, 0, 0, u, v, w, color=quiver_color, linewidth=quiver_linewidth, \
                arrow_length_ratio=quiver_ratio)

            ax.plot([1, -1], [0, 0], [0, 0], color=line_color, linewidth=line_linewidth)
            ax.plot([0, 0], [1, -1], [0, 0], color=line_color, linewidth=line_linewidth)
            ax.plot([0, 0], [0, 0], [-1, 1], color=line_color, linewidth=line_linewidth)

            circle1 = Circle((0, 0), 1, edgecolor=circle_edgecolor, facecolor=circle_facecolor, \
                linewidth=circle_linewidth)
            ax.add_patch(circle1)
            art3d.pathpatch_2d_to_3d(circle1, z=0, zdir='x')
            
            circle2 = Circle((0, 0), 1, edgecolor=circle_edgecolor, facecolor=circle_facecolor, \
                linewidth=circle_linewidth)
            ax.add_patch(circle2)
            art3d.pathpatch_2d_to_3d(circle2, z=0, zdir='z')

            circle3 = Circle((0, 0), 1, edgecolor=circle_edgecolor, facecolor=circle_facecolor, \
                linewidth=circle_linewidth)
            ax.add_patch(circle3)
            art3d.pathpatch_2d_to_3d(circle3, z=0, zdir='y')

            plt.show()
            return None

        else:
            logging.warning('Invalid input! Use proper coordinates. Make sure that u\u00b2 + ' +\
            'v\u00b2 + w\u00b2 = 1.')

    else:
        logging.warning('Invalid input! Please use the following types: int, float for u, v, w.')
