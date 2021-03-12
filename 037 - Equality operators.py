# '==' vs 'is'

# '==' operator is used to check if the values are same or not
# 'is' operator is used to check if the memory locations of values
# are same or not

a = 1
b = 1

print(a is b)
print(a == b)

a = 1
b = 2

print(a is b)
print(a == b)

# For non mutable datatypes, if values are same, then the value
# is stored only once, and same memory location is referred in
# all variables

# For mutableble datatypes, i.e. lists, sets, dictionaries, values
# are always stored in different locations, even if same

a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)


# Thank You !!!
