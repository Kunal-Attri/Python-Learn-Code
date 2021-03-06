# Sequences in Python

# Basic sequences in python are Strings, List, Tuple, Set,
# Frozenset, Dictionaries, Arrays, etc

# Strings are immutable group of characters, they are generally
# written between single or double quotes. Multiple line strings
# can be written between three single or double quotes. eg.

string1 = 'Hi, my name is Joker'
string2 = "Yes, my name is not Joker"
string3 = '''But I feel good being called Joker,
So i decided to be called Joker'''
string4 = """So, you should call me joker and not joke.
But i prefer being called by my name and not joker"""

# Here, all of the above are acceptable strings. If you want to
# quote something else in a string, you should use other type of
# quotes. eg.
string5 = 'He is not "joke"'
string6 = "He is not 'joke'"
# Either of these are acceptable, while in case of multi-line
# strings with triple quotes, any of these can be used.
print(string1, "\n", string2, '\n', string3, '\n', string4,
      '\n', string5, '\n', string6)


# Lists are mutable group of items, they are written inside
# square brackets - [...]. eg.
list1 = [1, 2, 3]
list2 = ["Rahul", 'Joker', "Kunal", "Dehradun"]
list3 = [True, False, True, True, True, False]
list4 = [1,2, "Height", True, 'Yo', 3.215]
# A list can contain any datatype.
print(list1, '\n', list2, '\n', list3, '\n', list4)


# Tuples are similar to lists, but they are not mutable, i.e.
# they can't be modified. Tuples are enclosed between curved
# brackets - (...). eg.
tuple1 = (1, 2, 3)
tuple2 = ("Rahul", 'Joker', "Kunal", "Dehradun")
tuple3 = (True, False, True, True, True, False)
tuple4 = (1,2, "Height", True, 'Yo', 3.215)
print(tuple1, '\n', tuple2, '\n', tuple3, '\n', tuple4)


# Sets are similar to lists, they are mutable, but *they do not
# contain duplicate items*. They are enclosed between curly
# brackets - {...}. eg.
set1 = {1, 2, 3, 4, 4, 4, 5}
# Although i have put dupliacte numbers, but the set wouldn't be
# having duplicate items when we print it
set2 = {"Rahul", 'Joker', "Kunal", "Dehradun"}
set3 = {True, False, True, True, True, False}
set4 = {1,2, "Height", True, 'Yo', 3.215}
print(set1, '\n', set2, '\n', set3, '\n', set4)

# Frozensets are similar to sets, but they are not mutable. They
# can be made using frozenset method. eg.
frzset1 = frozenset(set1)
frzset2 = frozenset(set2)
frzset3 = frozenset(set3)
frzset4 = frozenset(set4)
print(frzset1, '\n', frzset2, '\n', frzset3, '\n', frzset4)


# Python also supports to create arrays, which contain only a
# specific datatype, like integer, only, string only, etc. They
# can be made using array module. eg
from array import *
array1 = array("i", [1, 2, 3, 4, 5])
# Here, "i" defines that this array will only contain integers
print(array1)

print()
print()
print()
print("Thank you")
