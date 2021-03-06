# Writing an 'if-else' statement in a single line

x = 45
y = 77

# Normal method
if x > y:
    greater = x
else:
    greater = y

# Single line method, this is same as above

greater2 = x if x > y else y


print(greater)
print(greater2)


# Thank you !!!
