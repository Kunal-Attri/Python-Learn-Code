# Simplest Recursive Function

# Let's create a recursive function to print numbers from
# n to 0

def printN(n):
    # Lets put a condition
    if n >= 0:
        print(n)
        printN(n-1)
    
printN(10)


# Thank You !!!
