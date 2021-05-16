# Sine graph using Matplotlib Animations

import matplotlib.pyplot as plt
import matplotlib.animation as ani
from math import pi
import numpy as np

fig = plt.figure()
a = pi / 360    # resolution of points

ax = plt.axes(ylim=(-1.3, 1.3))
line, = ax.plot([], [], lw=3)    # lw is linewidth
ax.grid(True)

# x axis points
x = [0]
# y axis points
y = np.sin(np.array(x))

# function to initialize graph
def init():
    line.set_data(x, y)
    return line, 

# function for animation
def animate(i):
    x.append(x[-1] + a)
    # to move graph forward
    if x[-1] > 2 * pi:    # adjust as what you like
        x.pop(0)
    y = np.sin(np.array(x))
    ax.set_xlim(x[0], x[-1])
    line.set_data(x, y)
    return line, 


anim = ani.FuncAnimation(fig, animate, init_func=init, frames=360, interval=1)
plt.show()

# Thank You!!!
