# Function to take only integer input by Recursion

def get_integer(msg = "Enter Integer: "):
    # msg is set to a default string so that if we want this
    # message to be displayed then we need not put any argument
    # while calling function
    try:
        inp = int(input(msg))
        # Here, if the input is not integer, then ValueError
        # will be raised, so, lets put an exception
    except ValueError:
        print("Invalid Input, enter an integer...")
        inp = get_integer(msg)
        # Here, if there is an error, we again need to take input
    return inp    # returning the input integer value

# Lets try it out

age = get_integer("Enter age: ")
height = get_integer("Enter height: ")
integr = get_integer()

print(age)
print(height)
print(integr)


# Thank you...
