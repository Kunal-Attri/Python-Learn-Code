# Membership Operators in Python

# There are two membership operators - 'in', 'not in'
# Both of them return either True or False

# 'in' operator returns True if operand or item on the left
# of operator is found in the sequence given on the right
# of operator. eg.

name = "Kunal"
print("K" in name)    # return True as K is in name
print("p" in name)    # return False as p is not in name

list1 = [1,2,3,56,85,97,45,65,12,32,54,65,98,87]
print(2 in list1)    # True
print(60 in list1)    # False
print(45 in list1)    # True
print(100 in list1)    # False

# 'not in' operator returns True if the operand or item
# given on the left of operator is *not* found in the
# sequence given on the right of operator.
# It is just inverse of 'in' operator eg.

print("K" not in name)    # return False as K is in name
print("p" not in name)    # return True as p is not in name

print(2 not in list1)    # False
print(60 not in list1)    # True
print(45 not in list1)    # False
print(100 not in list1)    # True
print('\n', '\n', '\n', "Thank you")
