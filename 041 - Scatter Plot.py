# Scatter plots in Matplotlib

import matplotlib.pyplot as plt
from random import randint

# 100 random points on x axis
x = [randint(0, 100) for i in range(100)]
# corresponding 100 random points on y axis
y = [randint(0, 100) for i in range(100)]

# scatter plot
plt.scatter(x, y)
plt.grid(True)
plt.title("Scatter plot")
plt.show()



# Thank You !!!
