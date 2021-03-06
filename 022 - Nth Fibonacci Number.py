# Finding Nth fibonacci number using recursion

def fibonacci(n):
    if n < 1:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


while True:
    n = int(input("Which fibonacci no: "))
    f = fibonacci(n)
    print(f"{n}th Fibonacci no = {f}\n")
    


# Thank You !!!
