# Function Overloading in Python

# By default, python does not supprt function overloading
# If we define a function multiple times in python, then
# python only considers the latest declaration

# Function overloading a property of a programming language
# in which we can declare a function multiple times but with
# different parameters, and then when calling the function,
# only that declaration is called, which has the given arguments

# In python, we can achieve that using multipledispatch module
# Lets first pip install it

from multipledispatch import dispatch

# Lets create an add fucntion with different parameters
@dispatch(int)
def add(a):
    print("F1 called")

@dispatch(int, int)
def add(a, b):
    print("F2 called")

@dispatch(int, int, int)
def add(a, b, c):
    print("F3 called")

@dispatch(int, float)
def add(a, b):
    print("F4 called")

@dispatch(float, int)
def add(a, b):
    print("F5 called")

@dispatch(float, float)
def add(a, b):
    print("F6 called")

@dispatch(float, float, float)
def add(a, b, c):
    print("F7 called")


# Lets call them and see if it works or not

add(1)
add(1, 2)
add(1, 3.2)
add(1.2, 2.3)
add(1, 5, 6)
add(1.2, 6)
add(1.2, 20.6, 100.9)
add(100)
add(100, 1000.3)


# Thank You !!!
