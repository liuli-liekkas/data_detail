import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update_points(num):
    point_ani.set_data(x[num], y[num])
    return point_ani,


x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

fig = plt.figure(tight_layout=True)
plt.plot(x, y)
point_ani, = plt.plot(x[0], y[0], "ro")
plt.grid(ls="--")

ani = animation.FuncAnimation(fig, update_points, frames=np.arange(0, 100), interval=100, blit=True)

plt.show()
