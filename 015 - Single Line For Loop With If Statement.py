# Writing a 'for' loop with an 'if' statement

x = [1, 2, 3, 4, 5, 6, 10, 56, 85, 98, 74, 35, 26, 91, 100]

# Code to bring out numbers greater than 10

# Normal method
y = []
for i in x:
    if i > 10:
        y.append(i)

# Single line method, same as above:

y1 = [i for i in x if i > 10]

# i will be appended
# i comes from a for loop looping over x
# i will be appended if i is greater than 10

# Let's see

print(y)
print(y1)



# Thank You !!!
