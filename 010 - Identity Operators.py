# Identity operators in python

# In python, when we create a variable, it stores that
# variable in memory. So, generally(in most datatypes),
# if two variables have same value, then it doesnt
# allocate different memory spaces for two values of two
# variables, rather it allocates memory space once, and
# put same memory address in both variables. eg.
a = 5
b = 5
# Here, python will store 5 only once, and it will put
# the same address of 5 in both variables a and b.

# Identity operators are used to check if two variables
# locate to same memory address or not.

# They are of two types - 'is', 'is not'

# Note:- *Python allocates same memory space if the
# values are same for datatypes which are "not mutable",
# while it allocates different memory space for datatypes
# which are mutable(like  Lists, Sets, Dictionaries)

# 'is' operator returns True if the location of value of
# variable on left of operator is same as the location
# of variable on right of operator. eg.
print(a is b)    # True
c = 6
d = 6
print(b is c)    # False as the values are different...
print(c is d)    # True as the values are same, so the memory location

# lists are mutable, so they will be in diff location,
# although same. eg
list1 = [1, 2]
list2 = [1, 2]
print(list1 is list2)    # False as lists are mutable


# 'is not' operator is just inverse of 'is' operator, it
# returns True if the locations are different. eg.

print(c is not b)    #* True as locations are different
print(c is not d)    # False as locations are same


print()
print()
print("Thank you")
