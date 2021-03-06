# Reversing a string, list, array, tuple, etc.
# All three methods can be used on any ordered sequence.

price = [11, 22, 33, 44, 55]
# Method 1 using built in reverse method
print("Before reversing: ", price)
price.reverse()
print("Method 1: ", price)
print()

# Method 2 using list slicing
price = [11, 22, 33, 44, 55]
price1 = price[::-1]
print("Before reversing: ", price)
print("Method 2: ", price1)
print()

# Method 3 using user defined reverse function
def reverse(arr):
    newarr = []
    for i in range(len(arr) - 1, -1, -1):
        newarr.append(arr[i])
    return newarr

price = [11, 22, 33, 44, 55]
price2 = reverse(price)
print("Before reversing: ", price)
print("Method 3: ", price2)
print()


# Thank You !!!
