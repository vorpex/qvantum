'''Bloch sphere

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

- bloch_coords()      - calculate bloch coordinates from qubit
- bloch_qubit()       - calculate qubit from bloch coordinates
- bloch_sphere_plot() - plot bloch representation
- phase_test()        - compute phase between two complex numbers
'''

# pylint: disable=E1127, W1401

from . import check_bloch
from matplotlib.patches import Circle, PathPatch
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
import numpy
from . import qubit

@check_bloch.bloch_coords_check
def bloch_coords(q):
    """This function calculates the coordinates of the Bloch representation from the state vector 
    of a Qubit object.
    
    Arguments:
        q {qubit} -- Instance of Qubit class or Random_Qubit class
    
    Raises:
        TypeError
    
    Examples:
        >>> import qvantum
        >>>
        >>> q = qvantum.Random_Qubit()
        >>> q.show()
        '|Ψ> = (-0.5879-0.7251i)|0> + (0.3522-0.0674i)|1>'
        >>> qvantum.bloch_coords(q)
        (-0.31632342351128423, 0.5899599386821074, 0.7428908146479567)
    """

    p00 = complex(q.get_alpha().real ** 2 + q.get_alpha().imag ** 2, 0)
        
    p01 = complex(q.get_alpha().real * q.get_beta().real + \
        q.get_alpha().imag * q.get_beta().imag, \
        q.get_alpha().imag * q.get_beta().real - \
        q.get_alpha().real * q.get_beta().imag)
        
    p10 = complex(q.get_alpha().real * q.get_beta().real + \
        q.get_alpha().imag * q.get_beta().imag, \
        q.get_alpha().real * q.get_beta().imag - \
        q.get_alpha().imag * q.get_beta().real)

    p11 = complex(q.get_beta().real ** 2 + q.get_beta().imag ** 2, 0)

    u = p10 + p01
    u = u.real
    v = (p01 - p10) * complex(0, 1)
    v = v.real
    w = p00 - p11
    w = w.real

    return u, v, w

@check_bloch.bloch_qubit_check
def bloch_qubit(u, v, w):
    """This function calculates the state vector of a Qubit object from the given Bloch 
    coordinates.
    
    Arguments:
        u {int, float} -- 1st coordinate of Bloch representation
        v {int, float} -- 2nd coordinate of Bloch representation
        w {int, float} -- 3rd coordinate of Bloch representation
    
    Raises:
        ValueError, TypeError
    
    Examples:
        >>> import math
        >>> import qvantum
        >>>
        >>> u = 0
        >>> v = 1 / math.sqrt(2)
        >>> w = 1 / math.sqrt(2)
        >>> qvantum.bloch_qubit(u, v, w).show()
        '|Ψ> = (0.9239+0.0000i)|0> + (0.0000+0.3827i)|1>'
    """

    alpha = complex(numpy.cos(numpy.arccos(w) / 2), 0)
    
    beta = complex(numpy.sin(numpy.arccos(w) / 2) * u / numpy.sin(numpy.arccos(w)), \
        numpy.sin(numpy.arccos(w) / 2) * v / numpy.sin(numpy.arccos(w)))

    return qubit.Qubit(alpha, beta)

@check_bloch.bloch_sphere_plot_check
def bloch_sphere_plot(u, v, w, xfigsize=15, yfigsize=7.5, frame_on=False, tight_layout_on=False, \
        style='dark_background', surface_on=True, wireframe_on=True, surface_cmap='Blues_r', \
        surface_alpha=0.3, wireframe_color='#d3d3d3', wireframe_linewidth=0.075, \
        quiver_color='#ffffff', quiver_linewidth=1.5, quiver_ratio=0.1, line_color='#d3d3d3', \
        line_linewidth=0.3, circle_edgecolor='#d3d3d3', circle_facecolor='none', \
        circle_linewidth=0.3):
    """This function visualizes the qubit using its bloch coordinates and the matplotlib module.
    
    Arguments:
        u {int, float} -- 1st coordinate of Bloch representation
        v {int, float} -- 2nd coordinate of Bloch representation
        w {int, float} -- 3rd coordinate of Bloch representation
    
    Keyword Arguments:
        Keyword Arguments:
        xfigsize {int, float} -- X size of figure (default: {15})
        yfigsize {int, float} -- Y size of figure (default: {7.5})
        frame_on {bool} -- Frame (default: {False})
        tight_layout_on {bool} -- Tight layout (default: {False})
        style {str} -- Style (default: {'dark_background'})
        surface_on {bool} -- Surface (default: {True})
        wireframe_on {bool} -- Wireframe (default: {True})
        surface_cmap {str} -- Surface cmap (default: {'Blues_r'})
        surface_alpha {int, float} -- Surface alpha (default: {0.3})
        wireframe_color {str} -- Wireframe color (default: {'#d3d3d3'})
        wireframe_linewidth {int, float} -- Width of wireframe line (default: {0.075})
        quiver_color {str} -- Quiver color (default: {'#ffffff'})
        quiver_linewidth {int, float} -- Width of quiver line (default: {1.5})
        quiver_ratio {int, float} -- Quiver ratio (default: {0.1})
        line_color {str} -- Line color (default: {'#d3d3d3'})
        line_linewidth {int, float} -- Width of line (default: {0.3})
        circle_edgecolor {str} -- Edge color of circle (default: {'#d3d3d3'})
        circle_facecolor {str} -- Face color of circle (default: {'none'})
        circle_linewidth {int, float} -- Width of circle line (default: {0.3})
    
    Raises:
        ValueError, TypeError
    
    Examples:
        >>> import qvantum
        >>>
        >>> q = qvantum.Random_Qubit()
        >>> q.show()
        '|Ψ> = (0.6257-0.4027i)|0> + (-0.5114+0.4299i)|1>'
        >>> u = qvantum.bloch_coords(q)[0]
        >>> v = qvantum.bloch_coords(q)[1]
        >>> w = qvantum.bloch_coords(q)[2]
        >>> qvantum.bloch_sphere_plot(u, v, w)
    """

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

@check_bloch.phase_test_check
def phase_test(c1, c2):
    """Computes the phase between two complex number.
    
    Arguments:
        c1 {complex} -- 1st complex number
        c2 {complex} -- 2nd complex number
    
    Raises:
        TypeError
    
    Examples:
        >>> import qvantum
        >>>
        >>> q1 = qvantum.Random_Qubit()
        >>> q1.show()
        '|Ψ> = (0.6615-0.4616i)|0> + (0.5513-0.2132i)|1>'
        >>> q2 = qvantum.Random_Qubit()
        >>> q2.show()
        '|Ψ> = (-0.2091-0.3620i)|0> + (-0.3893+0.8208i)|1>'
        >>> qvantum.phase_test(q1.get_alpha(), q2.get_alpha())
        0.08522011231864535
        >>> qvantum.phase_test(q1.get_beta(), q2.get_beta())
        -0.7255489587145547
    """

    phase = (c1.real * c2.real + c1.imag * c2.imag) / \
        (numpy.sqrt(c1.real ** 2 + c1.imag ** 2) * numpy.sqrt(c2.real ** 2 + c2.imag ** 2))

    return phase
