# Basic methods in matplotlib

# importing matplotlib
import matplotlib.pyplot as plt
# this is for plotting graphs and visuals

plt.grid(True)    # to show the grid in graph
plt.xlim(0, 5)    # setting the x limits in graph
plt.ylim(-5, 5)    # setting the y limits in graph
plt.title("Learning matplotlib basic method")    # title of graph
plt.xlabel("x - axis label")    # x axis label
plt.ylabel("y - axis label")    # y axis label

# Lets plot points (0, 0), (1, 0), (0, 1), (2.5, -3), (3, -2)
x = [0, 1, 0, 2.5, 3]    # x axis point
y = [0, 0, 1, -3, -2]    # y axis point

# plt.scatter(x, y)    # To simply plot discrete points
plt.plot(x, y)    # To plot a line connecting all the given points


plt.show()    # to show graph after plotting

# These are the basic ones, there are many many advanced ones also
# We will see them later



# Thank You !!!
