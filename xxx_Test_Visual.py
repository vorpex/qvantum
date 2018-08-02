''' test visual '''

# import numpy
# import plotly.plotly as py
# import plotly.graph_objs as go

# #just a sphere
# theta = numpy.linspace(0, 2 * numpy.pi, 100)
# phi = numpy.linspace(0, numpy.pi, 100)
# x = numpy.outer(numpy.cos(theta), numpy.sin(phi))
# y = numpy.outer(numpy.sin(theta), numpy.sin(phi))
# z = numpy.outer(numpy.ones(100), numpy.cos(phi))  # note this is 2d now

# data = go.Data([go.Surface(x=x, y=y, z=z)])
# layout = go.Layout(title='Bloch sphere', autosize=False, width=500, height=500, margin=go.Margin(l=65, r=50, b=65, t=90))
# fig = go.Figure(data=data, layout=layout)
# py.plot(fig, filename='bloch-sphere-surface')

####################

# pylint: disable=E1127

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.patches import Circle
import numpy

fig = plt.figure(figsize=(15, 7.5), frameon=False, tight_layout=True) # figsize, frameon, tight_layout?
plt.style.use('dark_background') # background?

ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('equal')
ax.set_axis_off()

a, b = numpy.mgrid[0:2 * numpy.pi:50j, 0:numpy.pi:50j]
x = numpy.cos(a) * numpy.sin(b)
y = numpy.sin(a) * numpy.sin(b)
z = numpy.cos(b)

# surface or wire_frame?
ax.plot_surface(x, y, z, cmap='Blues_r', alpha=0.3) # cmap, color, alpha?
ax.plot_wireframe(x, y, z, color='#d3d3d3', linewidth=0.075) # color, linewidth?

# ax.scatter([0], [0], [0], color='#ff0000', s=10) # color, size?
ax.quiver(0, 0, 0, 0.5, 0.4, 0.3, color='#ffffff', linewidth=1.5, arrow_length_ratio=0.1) # color, linewidth, arrow_length_ratio?

ax.plot([1, -1], [0, 0], [0, 0], color='#d3d3d3', linewidth=0.3) # color, linewidth?
ax.plot([0, 0], [1, -1], [0, 0], color='#d3d3d3', linewidth=0.3) # color, linewidth?
ax.plot([0, 0], [0, 0], [-1, 1], color='#d3d3d3', linewidth=0.3) # color, linewidth?

circle1 = Circle((0, 0), 1, edgecolor='#d3d3d3', facecolor='none', linewidth=0.3) # edgecolor, linewidth?
ax.add_patch(circle1)
art3d.pathpatch_2d_to_3d(circle1, z=0, zdir='x')
circle2 = Circle((0, 0), 1, edgecolor='#d3d3d3', facecolor='none', linewidth=0.3) # edgecolor, linewidth?
ax.add_patch(circle2)
art3d.pathpatch_2d_to_3d(circle2, z=0, zdir='z')

# is circle3 needed?
circle3 = Circle((0, 0), 1, edgecolor='#d3d3d3', facecolor='none', linewidth=0.3) # edgecolor, linewidth?
ax.add_patch(circle3)
art3d.pathpatch_2d_to_3d(circle3, z=0, zdir='y')

plt.show()
# print(plt.style.available)
