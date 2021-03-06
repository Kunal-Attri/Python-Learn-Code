# Writing 'for' loop in a single line

x = [1, 2, 3, 4, 5, 6, 7]

# Normal method
sq = []
for i in x:
    sq.append(i**2)    # square of numbers in x


# Single line for loop, same as above

sq2 = [i**2 for i in x]


print(sq)
print(sq2)



# Thank You  !!!
