# Line Styling in Python
import matplotlib.pyplot as plt
# There are basically two types of linestyling - linestyle or ls
# and dash_capstyle, which is basically cap styling, i will show, wait

# linestyle or ls
# It has basically 4 types - "-", ":", "--", "-."
x = [0, 1, 2, 3]
y1 = [i for i in x]
y2 = [i+1 for i in x]
y3 = [i+2 for i in x]
y4 = [i+3 for i in x]

plt.plot(x, y1, linestyle = "-")    # this is also the default
plt.plot(x, y2, linestyle = ":")
plt.plot(x, y3, linestyle = "--")
plt.plot(x, y4, linestyle = "-.")
# you can also write ls in place of linestyle, its the same


# dash_capstyle
# It has basically 3 types = "butt", "round", "projecting"
# butt has larger gap than projecting
x = [4, 5, 6, 7]
y1 = [i for i in x]
y2 = [i+1 for i in x]
y3 = [i+2 for i in x]
# You can also always change the line width
plt.plot(x, y1, ls = "--", dash_capstyle = "butt", linewidth = 3)
plt.plot(x, y2, ls = "--", dash_capstyle = "round", linewidth = 3)
plt.plot(x, y3, ls = "--", dash_capstyle = "projecting", linewidth = 3)

# Lets see the output
plt.show()


# Thank You !!!
