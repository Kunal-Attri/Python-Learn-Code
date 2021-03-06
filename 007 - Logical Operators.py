# Logical Operators
# There are three types of logical operators - and, or,
# not

# All of them return either True or False

# 'and' operator returns True if both the conditions on
# either side of it are True, otherwise it returns False

a = True
b = True
c = False
d = False

print("a and b is ", a and b)
print("b and c is ", b and c)
print("a and c is ", a and c)

# 'or' operator returns True if either of the conditions
# on either side of it is True, only if both are False,
# it will return False

print("a or b is ", a or b)
print("b or c is ", b or c)
print("d or b is ", d or b)
print("c or d is ", c or d)

# not operator inverses the output of the condition, if
# the condition gives True, with not operator, it will
# give False, and vice versa
print("a is ", a)
print("not a is ", not a)
print("c is ", c)
print("not c is ", not c)
