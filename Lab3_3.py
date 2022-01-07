import matplotlib.pyplot as pl
import numpy as np

x = np.linspace(1, 2, 3)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

pl.plot(x, y1)
pl.plot(x, y2)
pl.plot(x, y3)


pl.show()

