# Ignoring a particular iteration in a loop using 'continue' method

# Whatever is written after continue in a iteration, is ignored by
# the compiler

for i in range(6):
    print("printing ", i)
    if i == 3:
        continue
    print(i)    # will not run for i = 3


# Thank You !!!
