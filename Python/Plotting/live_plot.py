import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import time


fig = plt.figure()
ax = fig.add_subplot(111)
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.ion()
line_plot, = ax.plot(x, y)
plt.show()
for i in range(100):
    x += 0.1
    y = np.roll(y, -1)
    y[-1] = np.sin(x[-1])
    line_plot.set_ydata(y)
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.1)