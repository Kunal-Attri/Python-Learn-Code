# Color naming and types in Matplotlib

# There are about 6 types of color naming in matplotlib:
# 1. FIrst one is by simple letters - b, g, r, c, m, y, k, w
# b - blue, g - green, r - red, c - cyan, m - magenta, y - yellow,
# k - black, w - white

import matplotlib.pyplot as plt

x = [0, 1, 2, 3]
y = []
for i in range(11):
    y.append([j+i for j in x])

singleNames = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
for i in range(8):
    plt.plot(x, y[i], color = singleNames[i])

# 2. Second is by simple Color codes with C before them
# C1, C2, C3, C4, C5, C6, C7, C8, C9
# dark blue, orange, green, red, purple, brown, pink, gray, yellow,
# light blue

colorCodes = ['C1', 'C2', 'C3', 'C4', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9']

x = [4, 5, 6, 7]
for i in range(10):
    plt.plot(x, y[i], color = colorCodes[i])


# 3. Third is grayscale, i.e. shades between white and black via decimal
# These lies between 0.0 and 1.0, where, 0.0 - black and 1.0 is white

gray = ['0.0', '0.1' ,'0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']

x = [8, 9, 10, 11]
for i in range(11):
    plt.plot(x, y[i], color = gray[i])


# 4. Fourth way is via pre defined names, there is a very big list of
# those,I will give a link in description to see all those with colors
# Here, i am showing a few of those
x = [12, 13, 14, 15]

colorNames = ['DarkRed', 'Firebrick', 'Crimson', 'IndianRed', 'Salmon']
for i in range(5):
    plt.plot(x, y[i], color = colorNames[i])


# 5. Fifth method is by giving RGB values in between 0 and 1, where 0 means
# least color and 1 means max
# It can be written as (R, G, B)
# Optionally, you can also define the opacity or alpha value
# (R, G, B, A), A is alpha value

rgb = [(1, 0, 0), (0, 1, 1), (0, 1, 1, 0.5), (1, 0, 0, 0.25)]
x = [16, 17, 18, 19]
for i in range(4):
    plt.plot(x, y[i], rgb[i])

# 6. Last method is also via RGB values but in hexadecimal form, Here
# also you can optionally define alpha or opacity

rgbs = ['#ff0000', '#00ffff', '#00ffffb8', '#ff000064']
x = [20, 21, 22, 23]

for i in range(4):
    plt.plot(x, y[i], color = rgbs[i])

plt.grid(True)
plt.show()


# Thank You !!!
