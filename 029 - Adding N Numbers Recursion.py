# Adding first N numbers from 0 using recursion

def add(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + add(n - 1)

print(add(1))
print(add(2))
print(add(3))
print(add(5))
print(add(10))
print(add(100))


# Thank you !!!
