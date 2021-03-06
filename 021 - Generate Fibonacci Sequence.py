# Program to generate fibonacci sequence

terms = int(input("No of terms: "))

a = 0    # first term
b = 1    # second term

if terms > 0:
    print(a)
if terms > 1:
    print(b)

while terms > 2:
    new = a + b
    a = b
    b = new
    print(new)
    terms -= 1



# Thank You !!!
