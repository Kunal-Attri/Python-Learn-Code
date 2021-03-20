# Graph styles available in matplotlib

import matplotlib.pyplot as plt

# There are many styles available in matplotlib, you can see them
# using the following command
print(plt.style.available)


# Let us look at a few of them
plt.style.use("fivethirtyeight")

x = [0, 2, 4]
y = [0, 2, 0]

plt.plot(x, y)
plt.title("fivethirtyeight")
plt.show()


# So, we looked at default, classic, grayscale, bmh, ggplot, seaborn
# fast, Solarize_Light2, seaborn-pastel, seaborn-notebook, seaborn-dark
# You can try others from available list


# Thank you!!!
