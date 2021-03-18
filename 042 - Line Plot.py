# Simple line plot in matplotlib

import matplotlib.pyplot as plt
from random import randint

# 100 random point on x axis
x = [randint(0, 100) for i in range(100)]
# corresponding 100 random points on y axis
y = [randint(0, 100) for i in range(100)]

plt.plot(x, y)
plt.grid(True)
plt.title("Line plot")
plt.show()


# Thank You !!!
