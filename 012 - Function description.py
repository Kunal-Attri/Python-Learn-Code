# Adding a simple documentation to a function

# Documentation can be written between triple quotes
# Can be written on just the starting of function...
def add(a, b):
    """This function can be used to add two numbers"""
    return a + b

# __doc__ is used to print documentation of a function

print(add.__doc__)
